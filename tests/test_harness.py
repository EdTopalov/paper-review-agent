"""Offline checks of recovery, stopping, frozen inputs, accounting, and tracing.

Model outputs in these tests are deliberately scripted fixtures, not evaluation
results. Live evaluations never replace the model or its tool observations.
"""

from copy import deepcopy
import json
from pathlib import Path
from types import SimpleNamespace

import httpx
from openai import APIStatusError
import pytest

from paper_review.evaluation import load_sample
from paper_review.audit import normalize_indices
from paper_review.paper import Paper, file_hash
from paper_review.runner import Config, run_review
from paper_review.trace import read_events, read_result


FIXTURE = Path(__file__).resolve().parents[1] / "data/dev/toy.json"
REVIEW = {
    "score": 0.4, "summary": "Small hypothetical experiment; uncertainty is substantial.",
    "observations": [
        {"kind": "limitation", "claim": "The experiment covers English only.", "page": 3,
         "quote": "The experiment covers English questions only"},
        {"kind": "uncertainty", "claim": "No significance test was conducted.", "page": 2,
         "quote": "We did not conduct a statistical significance test."},
    ], "unresolved_questions": ["Does the small difference persist across runs?"],
}
OPENING_REVIEW = {
    "score": 0.25, "summary": "A clearly labeled synthetic development fixture.",
    "observations": [
        {"kind": "uncertainty", "claim": "This is not a real paper.", "page": 1,
         "quote": "DEVELOPMENT FIXTURE, NOT A REAL PAPER."},
        {"kind": "limitation", "claim": "The fixture reports a small question sample.", "page": 1,
         "quote": "40 English questions."},
    ], "unresolved_questions": [],
}


class Action:
    type = "function_call"

    def __init__(self, name, args, call_id):
        self.name, self.arguments, self.call_id = name, json.dumps(args), call_id

    def model_dump(self, **_):
        return {"type": self.type, "name": self.name, "arguments": self.arguments, "call_id": self.call_id}


class Response:
    status = "completed"

    def __init__(self, actions=(), text="", cached=0, writes=0):
        self.output, self.output_text = list(actions), text
        self.usage = SimpleNamespace(input_tokens=100, output_tokens=20,
                                     input_tokens_details=SimpleNamespace(cached_tokens=cached, cache_write_tokens=writes))

    def model_dump(self, **_):
        return {"status": self.status, "output": [a.model_dump() for a in self.output],
                "output_text": self.output_text}


class Client:
    def __init__(self, responses):
        self.pending = iter(responses)
        self.requests = []
        self.responses = self

    def create(self, **request):
        # Copy the complete request at call time, as a real HTTP client would.
        self.requests.append(deepcopy(request))
        response = next(self.pending)
        if isinstance(response, Exception):
            raise response
        return response


def finish(review=None):
    return Response([Action("submit_review", {"reason": "Enough evidence; remaining questions recorded.",
                                              "review": review or OPENING_REVIEW}, "finish")])


def events(folder):
    with (folder / "trace.jsonl").open(encoding="utf-8") as stream:
        return [json.loads(line) for line in stream]


def test_reading_tools_return_recoverable_results():
    paper = Paper.load(FIXTURE)
    assert paper.search("absent-query")["matches"] == []
    assert "Literal phrase" in paper.search("absent-query")["hint"]
    assert paper.search(" ")["error"] == "empty_query"
    assert paper.read_pages(0, 2)["error"] == "invalid_page_range"
    assert paper.read_pages(1, 4)["error"] == "invalid_page_range"
    assert paper.search("significance test")["matches"][0]["page"] == 2


@pytest.mark.parametrize("action,expected", [
    (Action("read_pages", {"start": 99, "end": 99, "reason": "Check a table."}, "bad-range"), "invalid_page_range"),
    (Action("search_paper", {"query": "not-in-this-paper", "reason": "Check prior work."}, "empty"), "matches"),
    (Action("read_pages", {"start": "two", "end": 2, "reason": "Read methods."}, "bad-type"), "invalid_arguments"),
])
def test_model_can_recover_after_bad_or_empty_observation(tmp_path, action, expected):
    client = Client([Response([action]), finish()])
    folder = tmp_path / "run"
    result = run_review(FIXTURE, folder, Config(), "dev", client=client)
    assert result["status"] == "ok"
    assert result["api_calls"] == 2
    observations = [e["observation"] for e in events(folder) if e["event"] == "tool_observation"]
    assert expected in observations[0] or observations[0].get("error") == expected
    assert expected in json.dumps(client.requests[1]["input"])
    assert all(check["quote_matches"] for check in result["citation_checks"])
    sequence = [e["seq"] for e in events(folder)]
    assert sequence == list(range(1, len(sequence)+1))


def test_model_controls_early_stop(tmp_path):
    client = Client([finish()])
    result = run_review(FIXTURE, tmp_path / "run", Config(), "dev", client=client)
    assert result["status"] == "ok" and result["reading_actions"] == 0
    assert result["api_calls"] == 1


def test_reading_budget_removes_read_tools(tmp_path):
    client = Client([Response([Action("read_pages", {"start": 2, "end": 3, "reason": "Check evidence."}, "read")]), finish()])
    result = run_review(FIXTURE, tmp_path / "run", Config(max_reads=1), "dev", client=client)
    assert result["status"] == "ok" and result["reading_actions"] == 1
    assert [tool["name"] for tool in client.requests[1]["tools"]] == ["submit_review"]


def test_retry_is_traced_and_counted(tmp_path, monkeypatch):
    monkeypatch.setattr("paper_review.runner.time.sleep", lambda _: None)
    error = APIStatusError("temporary", response=httpx.Response(503, request=httpx.Request("POST", "https://example.invalid")), body=None)
    result = run_review(FIXTURE, tmp_path / "run", Config(), "dev", client=Client([error, finish()]))
    assert result["status"] == "ok" and result["api_calls"] == 2
    assert any(e["event"] == "retry" for e in events(tmp_path / "run"))


def test_permanent_api_error_is_saved_without_echoing_message(tmp_path):
    error = APIStatusError("sensitive credential fragment", response=httpx.Response(403, request=httpx.Request("POST", "https://example.invalid")), body=None)
    folder = tmp_path / "run"
    result = run_review(FIXTURE, folder, Config(), "dev", client=Client([error]))
    assert result["status"] == "error" and result["api_calls"] == 1
    assert "sensitive credential" not in (folder / "trace.jsonl").read_text(encoding="utf-8")
    assert read_result(folder / "trace.jsonl")["status"] == "error"
    assert (folder / "README.md").exists()


def test_cost_includes_cache_reads_writes_and_output(tmp_path):
    response = finish()
    response.usage.input_tokens_details.cached_tokens = 20
    response.usage.input_tokens_details.cache_write_tokens = 30
    result = run_review(FIXTURE, tmp_path / "run", Config(), "dev", client=Client([response]))
    expected = (50 * 0.1 + 20 * 0.01 + 30 * 0.125 + 20 * 0.5) / 1e6
    assert result["estimated_cost_usd"] == pytest.approx(expected)


def test_baseline_has_one_model_call_and_no_tools(tmp_path):
    client = Client([Response(text=json.dumps(REVIEW))])
    result = run_review(FIXTURE, tmp_path / "run", Config(), "dev", variant="baseline", client=client)
    assert result["status"] == "ok" and result["api_calls"] == 1
    assert "tools" not in client.requests[0]
    assert "=== PDF PAGE 3 ===" in client.requests[0]["input"][0]["content"]


def test_exact_quotes_are_not_equated_with_semantic_support():
    review = deepcopy(REVIEW)
    review["observations"][0]["claim"] = "The opposite of what this quotation establishes."
    assert Paper.load(FIXTURE).check_citations(review)[0]["quote_matches"] is True


def test_empty_or_invalid_quotes_fail_mechanical_check():
    review = deepcopy(REVIEW)
    review["observations"][0]["quote"] = ""
    review["observations"][1]["page"] = 99
    assert not any(c["quote_matches"] for c in Paper.load(FIXTURE).check_citations(review))


def test_frozen_manifest_detects_changed_input(tmp_path):
    snapshot = tmp_path / "paper.json"
    snapshot.write_text(json.dumps({"arxiv_id": "dev-v1", "pages": ["Original text"]}), encoding="utf-8")
    task = {"id": "dev", "arxiv_id": "dev-v1", "paper_path": "paper.json", "snapshot_sha256": file_hash(snapshot)}
    manifest = tmp_path / "tasks.jsonl"
    manifest.write_text(json.dumps(task), encoding="utf-8")
    assert len(load_sample(manifest)) == 1
    snapshot.write_text("{}", encoding="utf-8")
    with pytest.raises(ValueError, match="hash mismatch"):
        load_sample(manifest)


def test_live_sample_has_twenty_unique_frozen_papers():
    sample = FIXTURE.parents[1] / "eval/tasks.jsonl"
    tasks = load_sample(sample)
    assert len(tasks) == 20
    assert all(task["reference_score"] is None for task in tasks)


def test_audit_accepts_unambiguous_zero_or_one_based_indices():
    zero = {"observations": [{"index": 0, "verdict": "supported"}, {"index": 1, "verdict": "uncertain"}]}
    one = {"observations": [{"index": 1, "verdict": "supported"}, {"index": 2, "verdict": "uncertain"}]}
    assert normalize_indices(zero, 2) == (zero, None)
    normalized, operation = normalize_indices(one, 2)
    assert normalized == zero and operation == "one_based_indices_normalized"
    assert one["observations"][0]["index"] == 1  # Keep the original model output intact.


def test_audit_rejects_missing_or_duplicate_observations():
    with pytest.raises(ValueError):
        normalize_indices({"observations": [{"index": 1}, {"index": 1}]}, 2)


def test_citation_rejection_can_be_repaired_by_model(tmp_path):
    invalid = deepcopy(OPENING_REVIEW)
    invalid["observations"][0]["quote"] = "An invented sentence."
    client = Client([finish(invalid), finish()])
    result = run_review(FIXTURE, tmp_path / "run", Config(), "dev", client=client)
    assert result["status"] == "ok"
    assert result["rejected_submissions"] == 1 and result["submission_attempts"] == 2
    assert result["first_submission_checks"][0]["status"] == "not_found"
    assert "citation_validation_failed" in json.dumps(client.requests[1]["input"])


def test_real_but_unobserved_quote_requires_reading(tmp_path):
    client = Client([finish(REVIEW), Response([Action("read_pages", {
        "start": 2, "end": 3, "reason": "Observe the cited evidence."}, "read")]), finish(REVIEW)])
    result = run_review(FIXTURE, tmp_path / "run", Config(), "dev", client=client)
    assert result["status"] == "ok" and result["rejected_submissions"] == 1
    assert all(result["evidence_observed"])
    assert not any(c["observed"] for c in result["first_submission_checks"])


def test_structured_page_reads_keep_each_page_identity():
    result = Paper.load(FIXTURE).read_pages(2, 3)
    assert [page["page"] for page in result["pages"]] == [2, 3]
    assert "Methods." in result["pages"][0]["text"]
    assert "Limitations." in result["pages"][1]["text"]


def test_repeated_bad_submissions_end_with_recorded_budget_failure(tmp_path):
    bad = deepcopy(OPENING_REVIEW)
    bad["observations"][0]["quote"] = "Invented quotation."
    client = Client([finish(bad) for _ in range(3)])
    result = run_review(FIXTURE, tmp_path / "run", Config(max_reads=0), "dev", client=client)
    assert result["status"] == "error" and result["api_calls"] == 3
    assert result["error"]["code"] == "model_decision_budget_exhausted"
    assert result["rejected_submissions"] == 3


def test_compact_trace_reconstructs_exact_requests_with_retry_and_tool_change(tmp_path, monkeypatch):
    monkeypatch.setattr("paper_review.runner.time.sleep", lambda _: None)
    error = APIStatusError("temporary", response=httpx.Response(503, request=httpx.Request("POST", "https://example.invalid")), body=None)
    client = Client([error, Response([Action("read_pages", {"start": 2, "end": 3, "reason": "Check support."}, "read")]), finish(REVIEW)])
    path = tmp_path / "run" / "trace.jsonl"
    run_review(FIXTURE, path.parent, Config(max_reads=1), "dev", client=client)
    replay = [e["request"] for e in read_events(path) if e["event"] == "model_request"]
    assert replay == client.requests
    raw = [e for e in events(path.parent) if e["event"] == "model_request"]
    assert raw[1]["request"]["input"] == []  # Retry stores no repeated input.
    assert raw[2]["input_prefix"] == 1
    assert not (path.parent / "result.json").exists()


def test_audit_shares_trace_and_preserves_review_and_accounting(tmp_path, monkeypatch):
    from paper_review.audit import audit_one
    from paper_review.evaluation import check_experiment
    path = tmp_path / "run" / "trace.jsonl"
    original = run_review(FIXTURE, path.parent, Config(), "dev", client=Client([finish()]))
    verdicts = {"observations": [{"index": i, "verdict": "supported", "explanation": "Synthetic fixture supports this."} for i in (1, 2)]}
    client = Client([Response(text=json.dumps(verdicts))])
    monkeypatch.setattr("paper_review.audit.OpenAI", lambda **_: client)
    task = {"id": "dev", "paper_path": "toy.json", "snapshot_sha256": file_hash(FIXTURE)}
    record = audit_one(path, task, FIXTURE.parent / "tasks.jsonl", Config())
    assert record["status"] == "ok"
    assert read_result(path) == original
    assert read_result(path, audit=True) == record
    assert check_experiment(path.parent)["passed"] == 1
    count = len(read_events(path))
    assert audit_one(path, task, FIXTURE.parent / "tasks.jsonl", Config()) == record
    assert len(read_events(path)) == count and len(client.requests) == 1
    assert {p.name for p in path.parent.iterdir()} == {"trace.jsonl", "README.md"}


def test_paired_evaluation_and_resume_need_no_duplicate_result_files(tmp_path, monkeypatch):
    from zipfile import ZipFile
    from paper_review.evaluation import evaluate, summarize, check_experiment
    paper = json.loads(FIXTURE.read_text(encoding="utf-8"))
    paper["arxiv_id"] = "synthetic-dev-v1"
    snapshot = tmp_path / "paper.json"
    snapshot.write_text(json.dumps(paper), encoding="utf-8")
    sample = tmp_path / "tasks.jsonl"
    sample.write_text(json.dumps({"id": "dev", "arxiv_id": paper["arxiv_id"], "paper_path": "paper.json",
                                  "snapshot_sha256": file_hash(snapshot), "instructions_version": "m2-v1"}), encoding="utf-8")
    clients = iter([Client([finish()]), Client([Response(text=json.dumps(OPENING_REVIEW))])])
    monkeypatch.setattr("paper_review.runner.OpenAI", lambda **_: next(clients))
    out = tmp_path / "comparison"
    first = evaluate(sample, out, Config(), workers=1)
    assert first["agent"]["completed"] == first["baseline"]["completed"] == 1
    assert summarize(out) == first
    assert evaluate(sample, out, Config(), workers=1) == first
    assert check_experiment(out)["passed"] == 2
    assert {p.name for p in out.iterdir() if p.is_file()} == {"experiment.json", "source.zip", "README.md"}
    assert not list(out.rglob("result.json"))
    with ZipFile(out / "source.zip") as archive:
        assert "src/paper_review/runner.py" in archive.namelist()
        assert "requirements-m2.txt" in archive.namelist()


def test_checker_detects_incomplete_trace(tmp_path):
    from paper_review.evaluation import check_experiment
    folder = tmp_path / "run"
    run_review(FIXTURE, folder, Config(), "dev", client=Client([finish()]))
    with (folder / "trace.jsonl").open(encoding="utf-8") as stream:
        rows = list(stream)
    (folder / "trace.jsonl").write_text("".join(rows[:-1]), encoding="utf-8")
    checked = check_experiment(folder)
    assert checked["passed"] == 0
    assert not checked["failures"][0]["checks"]["terminal_result"]
