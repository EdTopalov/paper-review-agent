"""Exercise the real PyAgent loop with scripted provider responses, offline."""

import asyncio
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
import json
import sys
from zipfile import ZipFile

import httpx
from openai import APIStatusError
import pytest

pytest.importorskip("pyagent_patterns")

from paper_review.evaluation import check_experiment, evaluate, summarize
from paper_review.paper import file_hash
from paper_review.pyagent_runner import ENGINE_FINISH_TOKEN, PaperReviewReAct
from paper_review.runner import Config, run_review
from paper_review.trace import read_events
from test_harness import Client, FIXTURE, OPENING_REVIEW, REVIEW, Response, finish


def action(name, arguments):
    return Response(text=f"Action: {name}({json.dumps(arguments, ensure_ascii=False)})")


def submit(review=None):
    return action("submit_review", {"reason": "Evidence inspected; submit the assessment.",
                                     "review": review or OPENING_REVIEW})


def run(tmp_path, responses, config=None, task_id="dev"):
    client = Client(responses)
    folder = tmp_path / task_id
    result = run_review(FIXTURE, folder, config or Config(), task_id,
                        variant="pyagent_react", client=client)
    return result, client, read_events(folder / "trace.jsonl")


def test_real_harness_accepts_without_an_extra_provider_call(tmp_path, monkeypatch):
    from pyagent_patterns.advanced import ReAct

    entered = []
    execute = ReAct._execute
    assert PaperReviewReAct._execute is execute

    async def observe(self, context):
        entered.append(isinstance(self, ReAct))
        return await execute(self, context)

    monkeypatch.setattr(ReAct, "_execute", observe)
    result, client, events = run(tmp_path, [submit()])
    assert entered == [True]
    assert result["status"] == "ok"
    assert result["api_calls"] == result["decision_steps"] == result["tool_calls"] == 1
    assert result["reading_actions"] == 0
    assert result["harness"]["harness_version"] == "0.3.0"
    assert result["prompt_version"] == "m3-v2-pyagent-react-v2"
    assert result["harness"]["protocol"] == "pyagent-text-action-v2"
    assert all(e["variant"] == "pyagent_react" and e["task_id"] == "dev" for e in events)
    assert len(client.requests) == 1 and client.requests[0]["store"] is False
    assert "tools" not in client.requests[0]
    assert "Available tool contracts" in client.requests[0]["instructions"]
    assert not any("You are a ReAct agent" in str(m) for m in client.requests[0]["input"])
    assert result["input_tokens"] == 100 and result["output_tokens"] == 20
    assert result["estimated_cost_usd"] == pytest.approx((100 * .1 + 20 * .5) / 1e6)
    assert next(e for e in events if e["event"] == "harness_stop")["accepted"]
    assert check_experiment(tmp_path / "dev")["passed"] == 1


def test_page_tools_keep_observed_evidence_and_identity(tmp_path):
    result, client, events = run(tmp_path, [
        action("read_pages", {"start": 2, "end": 3, "reason": "Inspect evidence."}),
        submit(REVIEW),
    ])
    assert result["status"] == "ok" and result["evidence_observed"] == [True, True]
    assert result["reading_actions"] == 1 and result["decision_steps"] == 2
    assert "PDF PAGE" not in client.requests[0]["input"][0]["content"]
    pages = next(e["observation"]["pages"] for e in events if e["event"] == "tool_observation")
    assert [p["page"] for p in pages] == [2, 3]
    assert "Observation:" in client.requests[1]["input"][-1]["content"]
    assert check_experiment(tmp_path / "dev")["passed"] == 1


@pytest.mark.parametrize("template", [
    "We need use tools only action.Action: read_pages({payload})",
    "```json\nAction: read_pages(\n{payload}\n)\n```",
    "  action: read_pages ( {payload} )  ",
])
def test_text_action_wrappers_and_multiline_json_keep_exact_arguments(tmp_path, template):
    arguments = {"start": 2, "end": 3,
                 "reason": 'Inspect (results), "quotes", and Action: strings.\nKeep page identity.'}
    content = template.format(payload=json.dumps(arguments, indent=2))
    result, client, events = run(tmp_path, [Response(text=content), submit(REVIEW)])
    assert result["status"] == "ok" and result["reading_actions"] == 1
    assert result["api_calls"] == result["decision_steps"] == 2
    call = next(e for e in events if e["event"] == "tool_call")
    assert call["name"] == "read_pages" and call["arguments"] == arguments
    # The adapter parses the response; it does not rewrite provider output or
    # replace PyAgent's conversation history with a fabricated action.
    assert client.requests[1]["input"][-2]["content"] == content
    assert check_experiment(tmp_path / "dev")["passed"] == 1


@pytest.mark.parametrize("separator", ["", "\n", "\n\n"])
def test_concatenated_actions_execute_only_the_first_and_wait_for_observation(tmp_path, separator):
    first = action("read_pages", {"start": 2, "end": 3, "reason": "Inspect evidence."}).output_text
    extra = action("read_pages", {"start": 1, "end": 1, "reason": "Duplicate read."}).output_text
    content = separator.join([first, extra, submit().output_text])
    result, client, events = run(tmp_path, [Response(text=content), submit(REVIEW)])
    assert result["status"] == "ok"
    assert result["api_calls"] == result["decision_steps"] == result["tool_calls"] == 2
    assert result["reading_actions"] == result["submission_attempts"] == 1
    calls = [e for e in events if e["event"] == "tool_call"]
    assert [(e["name"], e["step"]) for e in calls] == [("read_pages", 1), ("submit_review", 2)]
    assert result["review"] == REVIEW
    assert "Observation:" in client.requests[1]["input"][-1]["content"]
    assert check_experiment(tmp_path / "dev")["passed"] == 1


def test_multiline_review_is_validated_without_stripping_json_string_content(tmp_path):
    arguments = {"reason": "Submit inspected evidence.", "review": OPENING_REVIEW}
    result, _, events = run(tmp_path, [Response(text="Action: submit_review(\n"
                                               + json.dumps(arguments, indent=2) + "\n)")])
    assert result["status"] == "ok" and result["review"] == OPENING_REVIEW
    assert result["api_calls"] == result["submission_attempts"] == 1
    assert next(e for e in events if e["event"] == "tool_call")["arguments"] == arguments


@pytest.mark.parametrize("first,expected_error", [
    ('Action: read_pages({"start":": 2, "end": 4, "reason":"Inspect evidence."})', "invalid_arguments"),
    ('Action: read_pages({"start":2,"end":3,"reason":"Missing closing parenthesis."}', "invalid_arguments"),
    ('Action: missing_tool({})', "unknown_tool"),
])
def test_invalid_first_action_is_not_skipped_or_repaired_to_execute_a_later_action(tmp_path, first, expected_error):
    result, client, events = run(tmp_path, [Response(text=first + submit().output_text), submit()])
    assert result["status"] == "ok" and result["reading_actions"] == 0
    assert result["api_calls"] == result["decision_steps"] == 2
    feedback = "Unknown tool:" if expected_error == "unknown_tool" else expected_error
    assert feedback in client.requests[1]["input"][-1]["content"]
    assert next(e for e in events if e["event"] == "tool_observation")["observation"]["error"] == expected_error
    assert [(e["step"], e["name"]) for e in events if e["event"] == "tool_call"] == [(2, "submit_review")]


def test_search_fragments_can_be_used_as_evidence(tmp_path):
    review = deepcopy(OPENING_REVIEW)
    review["observations"][1] = deepcopy(REVIEW["observations"][0])
    result, _, _ = run(tmp_path, [
        action("search_paper", {"query": "English questions only", "reason": "Find scope."}),
        submit(review),
    ])
    assert result["status"] == "ok" and result["evidence_observed"] == [True, True]


def test_rejected_citation_is_returned_and_repaired(tmp_path):
    bad = deepcopy(OPENING_REVIEW)
    bad["observations"][0]["quote"] = "Invented quotation."
    result, client, _ = run(tmp_path, [submit(bad), submit()])
    assert result["status"] == "ok" and result["rejected_submissions"] == 1
    assert result["first_submission_checks"][0]["status"] == "not_found"
    assert "citation_validation_failed" in client.requests[1]["input"][-1]["content"]
    assert result["submission_attempts"] == 2


def test_real_but_unobserved_quote_requires_reading(tmp_path):
    result, client, _ = run(tmp_path, [
        submit(REVIEW),
        action("read_pages", {"start": 2, "end": 3, "reason": "Read the cited source."}),
        submit(REVIEW),
    ])
    assert result["status"] == "ok" and result["rejected_submissions"] == 1
    assert all(c["citation_verified"] and not c["observed"] for c in result["first_submission_checks"])
    assert "citation_validation_failed" in client.requests[1]["input"][-1]["content"]
    assert result["reading_actions"] == 1


@pytest.mark.parametrize("payload", ["{", "[]", "null", "1", '"text"'])
def test_bad_json_arguments_are_recoverable(tmp_path, payload):
    result, client, _ = run(tmp_path, [Response(text=f"Action: read_pages({payload})"), submit()])
    assert result["status"] == "ok" and result["reading_actions"] == 0
    assert "invalid_arguments" in client.requests[1]["input"][-1]["content"]
    assert result["tool_calls"] == 2


@pytest.mark.parametrize("response,expected", [
    (action("read_pages", {"start": 99, "end": 99, "reason": "Check appendix."}), "invalid_page_range"),
    (action("search_paper", {"query": "absent-phrase", "reason": "Find evidence."}), "matches"),
])
def test_read_errors_and_empty_searches_consume_budget(tmp_path, response, expected):
    result, client, _ = run(tmp_path, [response, submit()])
    assert result["status"] == "ok" and result["reading_actions"] == 1
    assert expected in client.requests[1]["input"][-1]["content"]


def test_reading_budget_is_enforced_even_if_the_model_ignores_it(tmp_path):
    read = action("read_pages", {"start": 1, "end": 1, "reason": "Read opening."})
    result, client, events = run(tmp_path, [read, read, submit()], Config(max_reads=1))
    assert result["status"] == "ok" and result["reading_actions"] == 1
    assert len([e for e in events if e["event"] == "tool_call" and e["name"] == "read_pages"]) == 1
    assert "reading_budget_exhausted" in client.requests[2]["input"][-1]["content"]
    assert '"name": "read_pages"' not in client.requests[1]["instructions"]
    assert '"name": "submit_review"' in client.requests[1]["instructions"]
    assert check_experiment(tmp_path / "dev")["passed"] == 1


def test_acceptance_on_the_last_step_does_not_require_a_finish_turn(tmp_path):
    bad = deepcopy(OPENING_REVIEW)
    bad["observations"][0]["quote"] = "Invented quotation."
    result, _, events = run(tmp_path, [submit(bad), submit(bad), submit()], Config(max_reads=0))
    assert result["status"] == "ok" and result["api_calls"] == 3
    assert next(e for e in events if e["event"] == "harness_stop")["reason"] == "accepted_on_last_step"


def test_harness_step_exhaustion_is_not_a_success(tmp_path):
    bad = deepcopy(OPENING_REVIEW)
    bad["observations"][0]["quote"] = "Invented quotation."
    result, _, _ = run(tmp_path, [submit(bad)] * 8)
    assert result["status"] == "error" and result["review"] is None
    assert result["error"]["code"] == "model_decision_budget_exhausted"
    assert result["api_calls"] == result["rejected_submissions"] == 8
    assert check_experiment(tmp_path / "dev")["passed"] == 1


def test_engine_finish_marker_cannot_bypass_submit_review(tmp_path):
    result, _, _ = run(tmp_path, [Response(text=ENGINE_FINISH_TOKEN + json.dumps(OPENING_REVIEW))])
    assert result["status"] == "error" and result["review"] is None
    assert result["error"]["code"] == "pyagent_finished_without_accepted_review"
    assert result["submission_attempts"] == 0


@pytest.mark.parametrize("content", ["FINISH: a review", "Here is my answer", "Action: missing_tool({})"])
def test_missing_or_unknown_action_is_observed_and_can_be_repaired(tmp_path, content):
    result, client, _ = run(tmp_path, [Response(text=content), submit()])
    assert result["status"] == "ok" and result["api_calls"] == 2
    assert "Unknown tool:" in client.requests[1]["input"][-1]["content"]


def test_api_retry_counts_requests_but_not_extra_decisions(tmp_path, monkeypatch):
    monkeypatch.setattr("paper_review.runner.time.sleep", lambda _: None)
    error = APIStatusError("temporary", response=httpx.Response(503, request=httpx.Request("POST", "https://example.invalid")), body=None)
    result, _, events = run(tmp_path, [error, submit()])
    assert result["status"] == "ok" and result["api_calls"] == 2
    assert result["decision_steps"] == result["successful_model_calls"] == 1
    assert any(e["event"] == "retry" for e in events)
    assert check_experiment(tmp_path / "dev")["passed"] == 1


def test_permanent_api_error_is_logged_without_credential_fragments(tmp_path):
    error = APIStatusError("secret credential fragment", response=httpx.Response(403, request=httpx.Request("POST", "https://example.invalid")), body=None)
    result, _, _ = run(tmp_path, [error])
    assert result["status"] == "error" and result["error"]["status_code"] == 403
    assert "secret credential" not in (tmp_path / "dev" / "trace.jsonl").read_text()


def test_sync_entry_point_also_works_inside_a_notebook_event_loop(tmp_path):
    async def notebook():
        return run(tmp_path, [submit()])[0]

    assert asyncio.run(notebook())["status"] == "ok"


def test_concurrent_tasks_do_not_share_observed_evidence(tmp_path):
    clients = [Client([submit()]), Client([submit(REVIEW)] * 8)]
    with ThreadPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(run_review, FIXTURE, tmp_path / f"run-{i}",
                               Config(), f"dev-{i}", "pyagent_react", client)
                   for i, client in enumerate(clients)]
        results = [future.result() for future in futures]
    assert results[0]["status"] == "ok"
    assert results[1]["status"] == "error"
    assert results[1]["error"]["code"] == "model_decision_budget_exhausted"
    assert all(not c["observed"] for c in results[1]["first_submission_checks"])


def test_three_variant_evaluation_archive_reports_and_resume(tmp_path, monkeypatch):
    paper = json.loads(FIXTURE.read_text())
    paper["arxiv_id"] = "synthetic-dev-v1"
    snapshot = tmp_path / "paper.json"
    snapshot.write_text(json.dumps(paper))
    sample = tmp_path / "tasks.jsonl"
    sample.write_text(json.dumps({"id": "dev", "arxiv_id": paper["arxiv_id"],
                                  "paper_path": "paper.json", "snapshot_sha256": file_hash(snapshot),
                                  "instructions_version": "m2-v1"}))
    clients = iter([Client([finish()]), Client([submit()]),
                    Client([Response(text=json.dumps(OPENING_REVIEW))])])
    monkeypatch.setattr("paper_review.runner.OpenAI", lambda **_: next(clients))
    out = tmp_path / "comparison"
    variants = ["agent", "pyagent_react", "baseline"]
    summary = evaluate(sample, out, Config(), workers=1, variants=variants)
    assert set(summary) == set(variants)
    assert all(r["completed"] == 1 and r["mean_input_tokens"] == 100 for r in summary.values())
    assert summarize(out) == summary
    assert evaluate(sample, out, Config(), workers=1, variants=variants) == summary
    assert check_experiment(out) == {"runs": 3, "passed": 3, "failures": []}
    settings = json.loads((out / "experiment.json").read_text())
    assert settings["variant_metadata"]["pyagent_react"]["harness_version"] == "0.3.0"
    assert "Tokens (in/out)" in (out / "README.md").read_text()
    with ZipFile(out / "source.zip") as archive:
        assert {"src/paper_review/pyagent_runner.py", "requirements-m3.txt",
                "variants/pyagent_react/README.md"} <= set(archive.namelist())
        assert ".env" not in archive.namelist()


def test_checker_detects_a_result_not_matching_the_accepted_submission(tmp_path):
    run(tmp_path, [submit()])
    path = tmp_path / "dev" / "trace.jsonl"
    rows = [json.loads(line) for line in path.read_text().splitlines()]
    rows[-1]["result"]["review"]["summary"] = "Tampered summary."
    path.write_text("\n".join(json.dumps(row) for row in rows) + "\n")
    result = check_experiment(path.parent)
    assert result["passed"] == 0
    assert not result["failures"][0]["checks"]["pyagent_accepted_review"]


def test_audit_appends_variant_labels_and_preserves_the_review(tmp_path, monkeypatch):
    from paper_review.audit import audit_one

    run(tmp_path, [submit()])
    path = tmp_path / "dev" / "trace.jsonl"
    verdicts = {"observations": [{"index": i, "verdict": "supported", "explanation": "Fixture."}
                                 for i in range(2)]}
    monkeypatch.setattr("paper_review.audit.OpenAI", lambda **_: Client([Response(text=json.dumps(verdicts))]))
    task = {"id": "dev", "paper_path": "toy.json", "snapshot_sha256": file_hash(FIXTURE)}
    result = audit_one(path, task, FIXTURE.parent / "tasks.jsonl", Config())
    assert result["status"] == "ok" and result["variant"] == "pyagent_react"
    assert all(e["variant"] == "pyagent_react" for e in read_events(path))
    assert check_experiment(path.parent)["passed"] == 1


@pytest.mark.parametrize("variants", [["missing"], ["agent", "agent"], []])
def test_invalid_variant_selection_creates_no_experiment(tmp_path, variants):
    with pytest.raises(ValueError):
        evaluate("data/eval/tasks.jsonl", tmp_path / "out", Config(), variants=variants)
    assert not (tmp_path / "out").exists()


def test_unknown_single_variant_is_not_silently_run_as_baseline(tmp_path):
    with pytest.raises(ValueError, match="Unknown variant"):
        run_review(FIXTURE, tmp_path / "out", Config(), "dev", "missing")
    assert not (tmp_path / "out").exists()


def test_cli_selects_v2_and_an_explicit_comparison(tmp_path, monkeypatch):
    from paper_review import cli

    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("OPENAI_API_KEY", "offline-placeholder")
    calls = []
    monkeypatch.setattr(cli, "run_review", lambda *args: calls.append(args) or {"status": "ok"})
    monkeypatch.setattr(sys, "argv", ["paper-review", "review", "toy.json", "--variant",
                                     "pyagent_react", "--out", "review-out"])
    assert cli.main() == 0 and calls[0][4] == "pyagent_react"
    monkeypatch.setattr(cli, "evaluate", lambda *args, **kw: calls.append(kw))
    monkeypatch.setattr(sys, "argv", ["paper-review", "eval", "--variants", "agent",
                                     "pyagent_react", "baseline", "--out", "eval-out"])
    assert cli.main() == 0
    assert calls[-1]["variants"] == ["agent", "pyagent_react", "baseline"]
