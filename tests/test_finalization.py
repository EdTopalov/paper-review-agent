"""Scripted checks for the one-request, observed-evidence final answer."""

from copy import deepcopy
import json

import httpx
from openai import APIStatusError
import pytest

from paper_review.agent_tools import PaperEvidence
from paper_review.benchmark_tasks import AssessmentContract, BenchmarkPaper
from paper_review.finalization import BUDGET_POLICY, decision_cap, force_submit
from paper_review.paper import Paper
from paper_review.runner import Config, ModelCalls, run_review, variant_metadata
from paper_review.trace import Trace, read_events
from test_harness import Client, FIXTURE, OPENING_REVIEW, Response, finish


@pytest.mark.parametrize("reads,cap", [(0, 6), (5, 16), (20, 46)])
def test_doubled_decision_cap(reads, cap):
    assert decision_cap(Config(max_reads=reads)) == cap


def test_native_forces_one_final_answer_and_retains_bad_citation(tmp_path):
    bad = deepcopy(OPENING_REVIEW)
    bad["observations"][0]["quote"] = "Not in the supplied source."
    config = Config(max_reads=0)
    client = Client([finish(bad) for _ in range(decision_cap(config))] + [
        Response(text=json.dumps({"answer": bad}))])
    out = tmp_path / "run"
    result = run_review(FIXTURE, out, config, "dev", client=client)
    assert result["status"] == "ok"
    assert result["review"] == bad
    assert result["forced_final_submission"] is True
    assert result["api_calls"] == result["decision_steps"] == decision_cap(config) + 1
    assert result["rejected_submissions"] == decision_cap(config)
    assert result["citation_checks"][0]["citation_verified"] is False
    assert result["evidence_observed"][0] is False
    request = client.requests[-1]
    assert "tools" not in request and "tool_choice" not in request
    assert "retries" not in request
    assert request["text"]["format"]["schema"]["properties"]["answer"]["anyOf"][1] == {"type": "null"}
    events = read_events(out / "trace.jsonl")
    assert sum(e["event"] == "forced_finalization" for e in events) == 1
    assert any(
        e["event"] == "decision" and e["action"] == "final_answer" for e in events)


def test_native_null_final_answer_is_a_recorded_failure(tmp_path):
    config = Config(max_reads=0)
    client = Client([Response() for _ in range(decision_cap(config))] + [
        Response(text='{"answer": null}')])
    result = run_review(FIXTURE, tmp_path / "run", config, "dev", client=client)
    assert result["status"] == "error"
    assert result["error"]["code"] == "final_answer_none"
    assert result["review"] is None
    assert result["api_calls"] == decision_cap(config) + 1
    assert len(client.requests) == decision_cap(config) + 1


def test_finalizer_uses_only_observed_fragments_and_global_block_mapping(tmp_path):
    public = {"id": "QA-1", "kind": "qa", "instructions": "Answer the question.",
              "question": "What was measured?", "documents": [
                  {"id": "P1", "title": "First", "blocks": [
                      {"id": "a", "text": "Initially observed."},
                      {"id": "b", "text": "UNREAD_FIRST_DOCUMENT"}]},
                  {"id": "P2", "title": "Second", "blocks": [
                      {"id": "a", "text": "Search fragment. UNREAD_FRAGMENT_SUFFIX"},
                      {"id": "b", "text": "UNREAD_SECOND_DOCUMENT"}]}]}
    paper = BenchmarkPaper(public)
    evidence = PaperEvidence(paper)
    evidence.remember("search_paper", {"matches": [{"page": 3, "snippet": "Search fragment."}]})
    prediction = {"answer": "7", "explanation": "A best effort from observed evidence.",
                  "evidence": [{"document_id": "P2", "block_id": "a", "quote": "Wrong quotation."}]}
    config = Config()
    client = Client([Response(text=json.dumps({"answer": prediction}))])
    trace = Trace(tmp_path / "trace.jsonl")
    try:
        calls = ModelCalls(client, config, trace)
        calls.stats["decision_steps"] = decision_cap(config)
        answer, trajectory = force_submit(paper, calls, config, trace, evidence,
                                          contract=AssessmentContract(paper, config))
    finally:
        trace.close()
    payload = json.loads(client.requests[0]["input"][0]["content"])
    assert not any(secret in json.dumps(payload) for secret in (
        "UNREAD_FIRST_DOCUMENT", "UNREAD_FRAGMENT_SUFFIX", "UNREAD_SECOND_DOCUMENT"))
    assert payload["observed_fragments"] == [
        {"index": 1, "text": "Initially observed.", "document_id": "P1", "block_id": "a"},
        {"index": 3, "text": "Search fragment.", "document_id": "P2", "block_id": "a"}]
    assert answer == prediction and trajectory["evidence_observed"] == [False]
    assert calls.stats["first_submission_checks"][0]["citation_verified"] is False


def test_final_request_disables_configured_transport_retries(tmp_path):
    error = APIStatusError("temporary", response=httpx.Response(
        503, request=httpx.Request("POST", "https://example.invalid")), body=None)
    client = Client([error, Response(text='{"answer": null}')])
    config = Config(retries=3)
    paper = Paper.load(FIXTURE)
    trace = Trace(tmp_path / "trace.jsonl")
    calls = ModelCalls(client, config, trace)
    try:
        with pytest.raises(APIStatusError):
            force_submit(paper, calls, config, trace, PaperEvidence(paper))
    finally:
        trace.close()
    assert calls.stats["api_calls"] == len(client.requests) == 1
    assert not any(e["event"] == "retry" for e in read_events(tmp_path / "trace.jsonl"))


def test_reading_variant_metadata_records_budget_policy():
    assert variant_metadata("agent")["prompt_version"] == "m3-native-forced-final-v1"
    assert variant_metadata("agent")["budget_policy"] == BUDGET_POLICY
    assert "budget_policy" not in variant_metadata("baseline")
