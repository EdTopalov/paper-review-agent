"""Scripted tests of phase control and provenance; no model evaluation results."""

from copy import deepcopy
import json

import pytest

from paper_review.benchmark_tasks import AssessmentContract, BenchmarkPaper
from paper_review.deliberative_runner import (
    CRITIC_SCHEMA, DELIBERATIVE_POLICY, PLAN_SCHEMA, DeliberativeSession,
    SourceArchive, run_deliberative,
)
from paper_review.evaluation import check_experiment
from paper_review.paper import Paper
from paper_review.runner import Config, ModelCalls, run_review
from paper_review.trace import Trace, read_events
from test_harness import Action, Client, FIXTURE, OPENING_REVIEW, REVIEW, Response


PLAN = {"checks": ["Do the sources support the conclusion and its stated scope?"]}


def output(value):
    return Response(text=json.dumps(value))


def ledger(*sources, status="supported"):
    return [{"check_id": "C1", "status": status,
             "finding": "The observed material bounds this conclusion.",
             "support": list(sources), "counterevidence": [],
             "unknown": "Generality beyond the supplied source is unknown."}]


def draft(review=None, *, sources=("E1",), changes=""):
    return {"review": deepcopy(OPENING_REVIEW if review is None else review),
            "ledger": ledger(*sources), "changes": changes}


def critic(recommendation="approve", *, sources=("E1",), target=""):
    return {"recommendation": recommendation,
            "issues": [] if recommendation == "approve" else ["Check the uninspected methods evidence."],
            "target": target, "ledger": ledger(*sources)}


def read(name="read_pages", **arguments):
    if not arguments:
        arguments = {"start": 2, "end": 3}
    return Response([Action(name, {**arguments, "reason": "Resolve the evidence obligation."}, "source-read")])


def done_reading():
    return Response([Action("finish_reading", {"reason": "Enough evidence for a provisional draft."}, "stop-reading")])


def run(tmp_path, responses, *, config=None, paper=None, contract=None):
    paper = paper or Paper.load(FIXTURE)
    config = config or Config()
    client = Client(responses)
    path = tmp_path / "trace.jsonl"
    trace = Trace(path, context={"task_id": "fixture", "variant": "deliberative_review"})
    calls = ModelCalls(client, config, trace)
    try:
        result = run_deliberative(paper, calls, config, trace, contract=contract)
    finally:
        trace.close()
    return result, calls.stats, client, read_events(path)


def context(client, index):
    request = client.requests[index]
    assert len(request["input"]) == 1 and request["input"][0]["role"] == "user"
    return json.loads(request["input"][0]["content"])


def phases(events):
    return [event["phase"] for event in events if event["event"] == "deliberative_phase"]


def test_critic_approval_ends_early_without_ceremonial_revision(tmp_path):
    (review, trajectory), stats, client, events = run(tmp_path, [
        output(PLAN), done_reading(), output(draft()), output(critic()),
    ])
    assert review == OPENING_REVIEW
    assert phases(events) == ["plan", "investigate", "draft", "critic"]
    assert stats["api_calls"] == stats["decision_steps"] == trajectory["decision_steps"] == 4
    assert stats["reading_actions"] == trajectory["reading_actions"] == 0
    assert stats["submission_attempts"] == 1 and stats["rejected_submissions"] == 0
    assert trajectory["evidence_observed"] == [True, True]
    assert events[-1]["event"] == "deliberative_stop" and events[-1]["accepted"]
    assert all(request["model"] == Config.model for request in client.requests)
    assert all(event["policy"] == DELIBERATIVE_POLICY
               for event in events if event["event"] == "deliberative_phase")


def test_public_review_entry_point_writes_operationally_valid_traces(tmp_path):
    client = Client([output(PLAN), read(), done_reading(),
                     output(draft(REVIEW, sources=("E2", "E3"))),
                     output(critic(sources=("E2", "E3")))])
    folder = tmp_path / "public-review"
    result = run_review(FIXTURE, folder, Config(), "fixture",
                        variant="deliberative_review", client=client)
    assert result["status"] == "ok" and result["review"] == REVIEW
    assert result["api_calls"] == result["decision_steps"] == 5
    assert result["reading_actions"] == 1
    assert result["harness"]["context_policy"] == DELIBERATIVE_POLICY
    assert all(row["citation_verified"] for row in result["citation_checks"])
    assert (folder / "README.md").is_file()
    report = (folder / "README.md").read_text(encoding="utf-8")
    assert report.index("## Deliberative phases") < report.index("## Decisions")
    assert "| plan |" in report and "| critic |" in report
    assert PLAN["checks"][0] in report and "Recommendation: approve" in report
    assert "Finished exploration:" in report and "trace.jsonl#L" in report
    assert check_experiment(folder) == {"runs": 1, "passed": 1, "failures": []}


def test_source_archive_upgrades_identical_partial_fragment_without_changing_id():
    text = "This entire short source is available after the full read."
    archive = SourceArchive(Paper({"pages": ["Initial page.", text]}))
    archive.remember("search_paper", {"matches": [{"page": 2, "snippet": text}]})
    before = deepcopy(archive.entries[1])
    assert before["truncated"] and archive.coverage()["partial_indices"] == [2]
    archive.remember("read_pages", {"pages": [{"page": 2, "text": text, "truncated": False}]})
    assert len(archive.entries) == 2
    assert archive.entries[1] == {**before, "truncated": False}
    assert archive.entries[1]["source_id"] == "E2"
    assert archive.coverage()["partial_indices"] == []


def test_every_role_context_reports_budget_remaining_after_its_own_decision(tmp_path):
    _, stats, client, _ = run(tmp_path, [output(PLAN), done_reading(), output(draft()), output(critic())])
    budget = Config().max_reads + 3
    assert stats["decision_steps"] == len(client.requests) == 4
    assert [context(client, index)["decisions_remaining"] for index in range(len(client.requests))] == [
        budget - step for step in range(1, len(client.requests) + 1)]


def test_default_schedule_reserves_critic_targeted_read_and_revision(tmp_path):
    responses = [output(PLAN), read(start=2, end=2), read(start=3, end=3),
                 read("search_paper", query="missing-phrase"), output(draft(REVIEW, sources=("E2", "E3"))),
                 output(critic("investigate", sources=("E2", "E3"), target="Inspect the exact methods passage.")),
                 read(start=2, end=2), output(draft(REVIEW, sources=("E2", "E3"), changes="Scope retained after rereading."))]
    (review, trajectory), stats, _, events = run(tmp_path, responses)
    assert review == REVIEW
    assert phases(events) == ["plan", "investigate", "investigate", "investigate", "draft", "critic",
                              "targeted_read", "revise"]
    assert stats["api_calls"] == stats["decision_steps"] == 8
    assert stats["reading_actions"] == trajectory["reading_actions"] == 4
    assert any(event["event"] == "tool_observation" and event["observation"].get("matches") == []
               for event in events)


def test_larger_reading_budget_expands_exploration_and_preserves_reservations(tmp_path):
    config = Config(max_reads=20)
    exploratory = config.max_reads - 2
    responses = [output(PLAN)] + [read(start=2, end=2) for _ in range(exploratory)] + [
        output(draft()), output(critic("investigate", target="Inspect the scope limitation.")),
        read(start=3, end=3), output(draft(changes="Retained the bounded conclusion after investigation.")),
    ]
    (review, trajectory), stats, client, events = run(tmp_path, responses, config=config)
    assert review == OPENING_REVIEW
    assert phases(events).count("investigate") == exploratory == 18
    assert stats["reading_actions"] == trajectory["reading_actions"] == 19 <= config.max_reads
    assert stats["api_calls"] == stats["decision_steps"] == config.max_reads + 3 == 23
    assert phases(events)[-4:] == ["draft", "critic", "targeted_read", "revise"]
    archive = context(client, 22)["observed_sources"]
    assert [(row["source_id"], row["page"]) for row in archive] == [("E1", 1), ("E2", 2), ("E3", 3)]
    assert len(archive) == 3  # Repeated identical reads do not invent new sources.


@pytest.mark.parametrize("tool", ["read_pages", "search_paper"])
def test_critic_can_trigger_targeted_source_action_before_revision(tmp_path, tool):
    revised = deepcopy(OPENING_REVIEW)
    revised["observations"][1] = deepcopy(REVIEW["observations"][1])
    action = read(start=2, end=2) if tool == "read_pages" else read("search_paper", query="significance test")
    (review, _), stats, client, events = run(tmp_path, [
        output(PLAN), output(draft()),
        output(critic("investigate", target="Check the significance-test statement.")),
        action, output(draft(revised, sources=("E1", "E2"), changes="Added the requested methods evidence.")),
    ], config=Config(max_reads=2))
    assert review == revised and stats["api_calls"] == 5
    assert stats["reading_actions"] == 1
    assert phases(events) == ["plan", "draft", "critic", "targeted_read", "revise"]
    final = context(client, 4)
    assert final["coverage"]["observed_indices"] == [1, 2]
    assert final["observed_sources"][1]["page"] == 2
    assert "significance test" in final["observed_sources"][1]["text"]


def test_fresh_critic_sees_sources_and_coverage_without_reader_conversation(tmp_path):
    reader = read(start=2, end=2)
    reader.output[0].arguments = json.dumps({"start": 2, "end": 2, "reason": "READER_TRANSCRIPT_MARKER"})
    _, _, client, _ = run(tmp_path, [output(PLAN), reader, done_reading(),
                                   output(draft()), output(critic())])
    inspection = context(client, 4)
    assert inspection["draft"] == OPENING_REVIEW
    assert inspection["coverage"]["observed_indices"] == [1, 2]
    assert len(inspection["obligations"]) == 1
    assert all("source_id" in source and "text" in source for source in inspection["observed_sources"])
    assert "READER_TRANSCRIPT_MARKER" not in json.dumps(inspection)
    assert "reader_conversation" not in inspection and "history" not in inspection


def test_critic_approval_cannot_bypass_exact_observed_quotation_gate(tmp_path):
    bad = deepcopy(OPENING_REVIEW)
    bad["observations"][0]["quote"] = "THIS_QUOTE_WAS_NEVER_OBSERVED"
    (review, _), stats, client, events = run(tmp_path, [
        output(PLAN), done_reading(), output(draft(bad)), output(critic()),
        output(draft(changes="Replaced the unobserved quote with source text.")),
    ])
    assert review == OPENING_REVIEW
    assert stats["submission_attempts"] == 2 and stats["rejected_submissions"] == 1
    assert stats["first_submission_checks"][0]["observed"] is False
    repaired = context(client, 4)
    assert repaired["latest_feedback"]["error"] == "citation_validation_failed"
    assert any(event["event"] == "tool_observation"
               and event["observation"].get("error") == "citation_validation_failed" for event in events)


@pytest.mark.parametrize("invalid", ["not JSON", {"review": {}},
                                      draft(sources=("INVENTED_SOURCE_ID",))])
def test_invalid_draft_or_ledger_can_be_repaired_without_inventing_sources(tmp_path, invalid):
    bad_response = Response(text=invalid) if isinstance(invalid, str) else output(invalid)
    (review, _), stats, client, events = run(tmp_path, [
        output(PLAN), done_reading(), bad_response, output(critic("revise")),
        output(draft(changes="Rebuilt a valid draft from the observed source.")),
    ])
    assert review == OPENING_REVIEW and stats["api_calls"] == 5
    assert any(event["event"] == "phase_error" and event["phase"] == "draft" for event in events)
    assert [row["source_id"] for row in context(client, 4)["observed_sources"]] == ["E1"]


def test_invalid_critic_forces_revision_with_bounded_diagnostics(tmp_path):
    (review, _), stats, client, events = run(tmp_path, [
        output(PLAN), done_reading(), output(draft()), output({"recommendation": "approve"}),
        output(draft(changes="Rechecked the qualified assessment after invalid critic output.")),
    ])
    assert review == OPENING_REVIEW and stats["api_calls"] == 5
    assert phases(events)[-1] == "revise"
    assert context(client, 4)["latest_feedback"]["phase"] == "critic"
    assert context(client, 4)["critic"] is None


def test_incomplete_json_draft_is_diagnosed_and_repaired_within_budget(tmp_path):
    incomplete = Response(text='{"review":')
    incomplete.status = "incomplete"
    (review, _), stats, client, events = run(tmp_path, [
        output(PLAN), done_reading(), incomplete, output(critic("revise")),
        output(draft(changes="Reconstructed a complete prediction after truncation.")),
    ])
    assert review == OPENING_REVIEW and stats["api_calls"] == 5
    failure = next(row for row in events if row["event"] == "phase_error")
    assert failure["phase"] == "draft" and failure["response_status"] == "incomplete"
    assert failure["type"] == "JSONDecodeError"
    assert context(client, 3)["draft_validation"]["response_status"] == "incomplete"


def test_unknown_critic_ledger_reference_cannot_authorize_early_acceptance(tmp_path):
    (review, _), stats, client, events = run(tmp_path, [
        output(PLAN), done_reading(), output(draft()),
        output(critic(sources=("UNSEEN_CRITIC_SOURCE",))),
        output(draft(changes="Used only observed source IDs after invalid critic feedback.")),
    ])
    assert review == OPENING_REVIEW and stats["api_calls"] == 5
    failure = next(row for row in events if row["event"] == "phase_error")
    assert failure["phase"] == "critic" and failure["code"] == "unobserved_ledger_reference"
    assert context(client, 4)["critic"] is None
    assert [row["source_id"] for row in context(client, 4)["observed_sources"]] == ["E1"]


def test_bad_tool_arguments_and_source_range_errors_preserve_read_accounting(tmp_path):
    malformed = read()
    malformed.output[0].arguments = "{"
    (review, _), stats, client, events = run(tmp_path, [
        output(PLAN), malformed, read(start=99, end=99), done_reading(),
        output(draft()), output(critic()),
    ])
    assert review == OPENING_REVIEW and stats["api_calls"] == 6
    assert stats["reading_actions"] == 1  # Valid request returning a range error counts.
    observations = [row["observation"] for row in events if row["event"] == "tool_observation"]
    assert observations[0]["error"] == "invalid_arguments"
    assert observations[1]["error"] == "invalid_page_range"
    assert context(client, 4)["coverage"]["observed_indices"] == [1]


def test_invalid_plan_uses_disclosed_unknown_check_without_extra_planning_call(tmp_path):
    (review, _), stats, client, events = run(tmp_path, [
        output({"checks": [" "]}), output(draft()), output(critic()),
    ], config=Config(max_reads=2))
    assert review == OPENING_REVIEW and stats["api_calls"] == 3
    assert context(client, 1)["obligations"][0]["check_id"] == "C1"
    assert any(event.get("code") == "invalid_plan_checks" for event in events)


def test_budget_exhaustion_preserves_all_failed_attempts_and_stops(tmp_path):
    bad = deepcopy(OPENING_REVIEW)
    bad["observations"][0]["quote"] = "Not in the fixture"
    paper = Paper.load(FIXTURE)
    config = Config(max_reads=1)
    client = Client([output(PLAN), output(draft(bad)), output(critic()), output(draft(bad))])
    trace = Trace(tmp_path / "trace.jsonl")
    calls = ModelCalls(client, config, trace)
    try:
        with pytest.raises(RuntimeError, match="model_decision_budget_exhausted"):
            run_deliberative(paper, calls, config, trace)
    finally:
        trace.close()
    assert calls.stats["api_calls"] == calls.stats["decision_steps"] == config.max_reads + 3 == 4
    assert calls.stats["rejected_submissions"] == 2
    assert calls.stats["reading_actions"] == 0
    assert read_events(tmp_path / "trace.jsonl")[-1]["accepted"] is False


def test_infeasible_budget_is_rejected_before_provider_calls(tmp_path):
    trace = Trace(tmp_path / "trace.jsonl")
    client = Client([])
    calls = ModelCalls(client, Config(max_reads=0), trace)
    try:
        with pytest.raises(ValueError, match="deliberative_infeasible_budget"):
            run_deliberative(Paper.load(FIXTURE), calls, Config(max_reads=0), trace)
    finally:
        trace.close()
    assert calls.stats["api_calls"] == calls.stats["decision_steps"] == 0


@pytest.mark.parametrize("kind", ["qa", "critique", "claim", "selection"])
def test_every_benchmark_kind_uses_unchanged_contract_and_source_provenance(tmp_path, kind):
    public = {"id": "fixture", "kind": kind, "instructions": "Use only supplied evidence.",
              "question": "How many trials?", "comment": "The study omits independent trials.",
              "claim": "The study reports five independent trials.", "brief": "Choose the study reporting five trials.",
              "documents": [{"id": "DOC-A", "title": "Study", "blocks": [
                  {"id": "intro", "text": "This hypothetical report describes a controlled study."},
                  {"id": "methods", "text": "Five independent trials were conducted."}]},
                  {"id": "DOC-B", "title": "Alternative", "blocks": [
                      {"id": "intro", "text": "This alternative report describes one trial."}]}]}
    key = {"qa": {"answer": "Five"},
           "critique": {"verdict": "deficient", "error_types": ["neglect"]},
           "claim": {"verdict": "supported"},
           "selection": {"selected_id": "DOC-A", "tied_ids": []}}[kind]
    provisional = {**key, "explanation": "Provisional assessment; methods remain uninspected.", "evidence": []}
    final = {**key, "explanation": "The supplied methods explicitly state the trial count.",
             "evidence": [{"document_id": "DOC-A", "block_id": "methods",
                           "quote": "Five independent trials were conducted."}]}
    paper = BenchmarkPaper(public)
    config = Config(max_reads=2)
    contract = AssessmentContract(paper, config)
    private_reference = "SECRET_REFERENCE_LABEL_MUST_NOT_ENTER_ROLE_CONTEXT"
    paper.snapshot["private_reference"] = {"answer": private_reference}
    assert private_reference not in json.dumps(public)
    (prediction, trajectory), stats, client, events = run(tmp_path, [
        output(PLAN), output(draft(provisional)),
        output(critic("investigate", target="Inspect the source's trial-count statement.")),
        read(start=2, end=2), output(draft(final, sources=("E2",), changes="Added inspected methods evidence.")),
    ], paper=paper, config=config, contract=contract)
    assert prediction == final and stats["api_calls"] == 5
    assert trajectory["evidence_observed"] == [True]
    source = context(client, 4)["observed_sources"][1]
    assert source["document_id"] == "DOC-A" and source["block_id"] == "methods"
    assert "page" not in source
    assert private_reference not in json.dumps(client.requests)
    assert all("score" not in request["text"]["format"]["schema"]["properties"]
               for request in client.requests if "text" in request)


def test_internal_object_schemas_are_strict_compatible(tmp_path):
    session = DeliberativeSession(Paper.load(FIXTURE), None, Config(), None, None)

    def inspect(schema):
        if schema.get("type") == "object":
            assert schema["additionalProperties"] is False
            assert set(schema["required"]) == set(schema["properties"])
            for value in schema["properties"].values():
                inspect(value)
        if "items" in schema:
            inspect(schema["items"])
        assert "uniqueItems" not in schema

    for schema in (PLAN_SCHEMA, CRITIC_SCHEMA, session.draft_schema):
        inspect(schema)
