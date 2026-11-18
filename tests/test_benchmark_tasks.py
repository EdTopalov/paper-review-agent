"""Exercise benchmark task contracts through actual loops with scripted outputs.

These are offline software fixtures, not benchmark predictions or model runs.
"""

from copy import deepcopy
import importlib.util
import json

import pytest
import jsonschema

from paper_review.agent_tools import PaperEvidence
from paper_review.benchmark_tasks import AssessmentContract, BenchmarkPaper, prediction_schema
from paper_review.runner import Config, ModelCalls, agent, baseline
from paper_review.trace import Trace, read_events
from test_harness import Action, Client, Response, finish


PUBLIC = {
    "id": "fixture-qa", "kind": "qa",
    "instructions": "Answer using the supplied source blocks.",
    "question": "How many independent repetitions were performed?",
    "documents": [{"id": "DOC-A", "title": "A hypothetical study", "blocks": [
        {"id": "intro", "text": "A retrieval procedure is evaluated under a fixed experimental protocol."},
        {"id": "repetitions", "text": "We conducted five independent repetitions and report every result."},
    ]}, {"id": "DOC-B", "title": "A supplementary note", "blocks": [
        {"id": "repetitions", "text": "The supplementary note discusses limitations, not additional trials."},
    ]}],
}
PREDICTION = {
    "answer": "Five", "explanation": "The methods explicitly state the repetition count.",
    "evidence": [{"document_id": "DOC-A", "block_id": "repetitions",
                  "quote": "We conducted five independent repetitions"}],
}


def native_read():
    return Response([Action("read_pages", {"start": 2, "end": 2, "reason": "Inspect the repetition record."}, "read")])


def text_action(name, arguments):
    return Response(text=f"Action: {name}({json.dumps(arguments)})")


def run_contract(tmp_path, variant, responses, *, public=PUBLIC, config=None):
    config = config or Config()
    paper = BenchmarkPaper(public)
    contract = AssessmentContract(paper, config)
    client = Client(responses)
    path = tmp_path / f"{variant}.jsonl"
    trace = Trace(path, context={"task_id": public["id"], "variant": variant})
    calls = ModelCalls(client, config, trace)
    try:
        if variant == "baseline":
            prediction, trajectory = baseline(paper, calls, trace, contract=contract)
        elif variant == "pyagent_react":
            from paper_review.pyagent_runner import run_pyagent
            prediction, trajectory = run_pyagent(paper, calls, config, trace, contract=contract)
        else:
            prediction, trajectory = agent(paper, calls, config, trace, contract=contract)
    finally:
        trace.close()
    return prediction, trajectory, calls.stats, client, read_events(path)


def test_source_blocks_preserve_document_identity_without_pdf_page_claims():
    paper = BenchmarkPaper(PUBLIC)
    assert paper.introduction()["location_unit"] == "source_block"
    catalog = paper.introduction()["block_catalog"]
    assert catalog == [{"index": 1, "document_id": "DOC-A", "block_id": "intro"},
                       {"index": 2, "document_id": "DOC-A", "block_id": "repetitions"},
                       {"index": 3, "document_id": "DOC-B", "block_id": "repetitions"}]
    result = paper.read_pages(2, 3)
    assert result["location_unit"] == "source_block"
    assert [(row["document_id"], row["block_id"]) for row in result["pages"]] == [
        ("DOC-A", "repetitions"), ("DOC-B", "repetitions")]
    assert "SOURCE BLOCK 2: DOC-A/repetitions" in paper.full_text()
    assert "=== PDF PAGE" not in paper.full_text()
    assert "source-block" in paper.read_pages(99, 99)["hint"]


def test_search_returns_citable_block_ids_and_unknown_locations_fail():
    paper = BenchmarkPaper(PUBLIC)
    search = paper.search("independent repetitions")
    assert search["location_unit"] == "source_block"
    assert search["matches"][0]["document_id"] == "DOC-A"
    assert search["matches"][0]["block_id"] == "repetitions"
    assert paper.source_checks(PREDICTION)[0]["citation_verified"] is True
    for location in ({"document_id": "UNKNOWN"}, {"block_id": "UNKNOWN"}):
        prediction = deepcopy(PREDICTION)
        prediction["evidence"][0].update(location)
        check = paper.source_checks(prediction)[0]
        assert check["status"] == "unknown_block" and not check["citation_verified"]
    wrong_document = deepcopy(PREDICTION)
    wrong_document["evidence"][0]["document_id"] = "DOC-B"
    assert not paper.source_checks(wrong_document)[0]["citation_verified"]


def test_task_context_and_selection_brief_are_preserved_for_every_interface():
    public = deepcopy(PUBLIC)
    public.update({"kind": "critique", "comment": "This comparison omits an important cost.",
                   "comment_context": ["The comparison uses total operating cost.",
                                       "This comparison omits an important cost."]})
    paper = BenchmarkPaper(public)
    assert paper.introduction()["task"] == {key: value for key, value in public.items() if key != "documents"}
    assert "The comparison uses total operating cost." in paper.full_text()
    public.update({"kind": "selection", "brief": "Choose a study with at least five independent repetitions."})
    assert BenchmarkPaper(public).introduction()["task"]["brief"] == public["brief"]


def test_observation_gate_uses_both_document_and_block():
    paper = BenchmarkPaper(PUBLIC)
    contract = AssessmentContract(paper, Config())
    observed = PaperEvidence(paper)
    assert contract.check(observed, PREDICTION)[0]["observed"] is False
    observed.remember("read_pages", paper.read_pages(3, 3))
    assert contract.check(observed, PREDICTION)[0]["observed"] is False
    observed.remember("search_paper", paper.search("independent repetitions"))
    assert contract.check(observed, PREDICTION)[0]["observed"] is True


@pytest.mark.parametrize("variant", ["agent", "baseline", "pyagent_react"])
def test_each_existing_architecture_obeys_the_common_task_contract(tmp_path, variant):
    if variant == "pyagent_react":
        if importlib.util.find_spec("pyagent_patterns") is None:
            pytest.skip("Optional PyAgent dependency is unavailable")
        responses = [text_action("read_pages", {"start": 2, "end": 2, "reason": "Inspect evidence."}),
                     text_action("submit_review", {"reason": "Evidence inspected.", "review": PREDICTION})]
    elif variant == "baseline":
        responses = [Response(text=json.dumps(PREDICTION))]
    else:
        responses = [native_read(), finish(PREDICTION)]
    result, trajectory, stats, client, events = run_contract(tmp_path, variant, responses)
    assert result == PREDICTION
    assert stats["api_calls"] == (1 if variant == "baseline" else 2)
    assert trajectory["reading_actions"] == (0 if variant == "baseline" else 1)
    if variant != "baseline":
        assert trajectory["evidence_observed"] == [True]
        assert stats["first_submission_checks"][0]["observed"] is True
    assert "=== PDF PAGE" not in json.dumps(client.requests)
    assert "not PDF pages" in client.requests[0]["instructions"]
    assert all(row["variant"] == variant for row in events)
    schemas = (client.requests[0]["text"]["format"]["schema"] if variant == "baseline" else
               prediction_schema("qa"))
    assert "answer" in schemas["properties"] and "score" not in schemas["properties"]


def test_unobserved_submission_is_rejected_then_read_and_repaired(tmp_path):
    result, _, stats, _, events = run_contract(tmp_path, "agent", [finish(PREDICTION), native_read(), finish(PREDICTION)])
    assert result == PREDICTION and stats["rejected_submissions"] == 1
    observations = [row["observation"] for row in events if row["event"] == "tool_observation"]
    assert observations[0]["error"] == "citation_validation_failed"
    assert observations[0]["citation_checks"][0]["citation_verified"] is True
    assert observations[0]["citation_checks"][0]["observed"] is False
    assert observations[-1]["accepted"] is True


def test_reference_labels_cannot_enter_requests_through_public_contract(tmp_path):
    task = {"input": deepcopy(PUBLIC), "reference": {"answer": "SECRET_REFERENCE_LABEL", "explanation": "SECRET_EXPERT_REASON"}}
    result, _, _, client, _ = run_contract(tmp_path, "agent", [native_read(), finish(PREDICTION)], public=task["input"])
    assert result == PREDICTION
    serialized = json.dumps(client.requests)
    assert "SECRET_REFERENCE_LABEL" not in serialized and "SECRET_EXPERT_REASON" not in serialized
    assert "source_block" in serialized


def test_unanswerable_can_finish_without_fabricated_evidence(tmp_path):
    prediction = {"answer": "Unanswerable", "explanation": "The supplied material does not identify a study location.", "evidence": []}
    public = deepcopy(PUBLIC)
    public["question"] = "In which city was the experiment conducted?"
    result, trajectory, stats, _, _ = run_contract(tmp_path, "agent", [finish(prediction)], public=public)
    assert result == prediction and trajectory["reading_actions"] == 0
    assert stats["api_calls"] == 1


def test_contract_rejects_duplicate_evidence_and_blank_fields():
    contract = AssessmentContract(BenchmarkPaper(PUBLIC), Config())
    duplicate = deepcopy(PREDICTION)
    duplicate["evidence"].append(deepcopy(duplicate["evidence"][0]))
    with pytest.raises(ValueError, match="duplicate_evidence"):
        contract.validate(duplicate)
    for field in ("answer", "explanation"):
        blank = deepcopy(PREDICTION)
        blank[field] = " "
        with pytest.raises(jsonschema.ValidationError):
            contract.validate(blank)


def test_critique_contract_teaches_and_constrains_canonical_error_types():
    public = deepcopy(PUBLIC)
    public.update(kind="critique", comment="The review misstates the reported experiments.")
    contract = AssessmentContract(BenchmarkPaper(public), Config())
    prediction = {"verdict": "deficient", "explanation": "The comment misreads the supplied paper.",
                  "error_types": [], "evidence": []}
    categories = ["misunderstanding", "neglect", "inaccurate_summary", "unstated_statement"]
    for category in categories:
        contract.validate({**prediction, "error_types": [category]})
        assert category + " means " in contract.rubric
    assert "Use [] for error_types when the comment is reliable." in contract.rubric
    contract.validate({**prediction, "verdict": "reliable"})
    with pytest.raises(jsonschema.ValidationError):
        contract.validate({**prediction, "error_types": ["unknown_category"]})
    with pytest.raises(ValueError, match="duplicate_error_types"):
        contract.validate({**prediction, "error_types": ["neglect", "neglect"]})


def test_selection_ties_must_be_consistent_with_the_selected_candidate():
    public = deepcopy(PUBLIC)
    public["kind"] = "selection"
    public["brief"] = "Choose an eligible candidate or abstain."
    contract = AssessmentContract(BenchmarkPaper(public), Config())
    prediction = {"selected_id": None, "tied_ids": [], "explanation": "No candidate qualifies.", "evidence": []}
    contract.validate(prediction)
    for selected, ties in [(None, ["DOC-A"]), ("DOC-A", ["DOC-B"]), ("unknown", [])]:
        invalid = {**prediction, "selected_id": selected, "tied_ids": ties}
        with pytest.raises(ValueError):
            contract.validate(invalid)
