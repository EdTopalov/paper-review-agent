"""Offline checks of comparative selection, separate from single-paper quality."""

from copy import deepcopy
import json

import pytest

from paper_review.runner import Config
from paper_review.selection import run_selection, validate_selection
from paper_review.trace import read_events
from test_harness import Client, FIXTURE, OPENING_REVIEW, Response, finish


CHOICE = {"selected_id": "a", "reason": "A clearer test of the club's question.",
          "comparisons": [{"candidate_id": "b", "trade_off": "B leaves more design uncertainty."}],
          "tied_alternatives": [], "uncertainties": ["These are synthetic inputs."]}


def candidates(tmp_path, count=2):
    paths = []
    for name in "abc"[:count]:
        path = tmp_path / f"{name}.json"
        snapshot = json.loads(FIXTURE.read_text(encoding="utf-8"))
        snapshot["title"] = name
        path.write_text(json.dumps(snapshot), encoding="utf-8")
        paths.append(path)
    return paths


def test_pilot_reviews_each_candidate_then_accounts_for_choice(tmp_path):
    client = Client([finish(), finish(), Response(text=json.dumps(CHOICE))])
    result = run_selection(candidates(tmp_path), tmp_path / "pilot", Config(),
                           variant="evidence_memory", brief="Discuss experimental design.", client=client)
    assert result["status"] == "ok" and result["choice"]["selected_id"] == "a"
    assert result["total_api_calls"] == 3
    assert result["selection_usage"]["api_calls"] == 1
    assert result["selection_usage"]["decision_steps"] == 1
    assert result["total_input_tokens"] == 300 and result["total_output_tokens"] == 60
    assert result["candidate_count"] == result["completed_candidates"] == 2
    assert result["total_estimated_cost_usd"] == pytest.approx(3 * (100 * .1 + 20 * .5) / 1e6)
    comparison = json.loads(client.requests[-1]["input"][0]["content"])
    assert [row["id"] for row in comparison["candidates"]] == ["a", "b"]
    assert all(row["review"] == OPENING_REVIEW for row in comparison["candidates"])
    assert all(row["citation_checks"] for row in comparison["candidates"])
    assert "tools" not in client.requests[-1]
    assert (tmp_path / "pilot/README.md").is_file()
    events = read_events(tmp_path / "pilot/selection-trace.jsonl")
    assert events[-1]["event"] == "selection_end"
    assert all(row["variant"] == "evidence_memory" for row in events)


def test_unavailable_candidates_stay_visible_and_costed(tmp_path):
    def reviews(path, out, config, task_id, **kwargs):
        return {"task_id": task_id, "status": "error" if task_id == "c" else "ok",
                "review": None if task_id == "c" else OPENING_REVIEW,
                "error": {"code": "fixture_failure"} if task_id == "c" else None,
                "api_calls": 2, "estimated_cost_usd": .001, "billing_uncertain": False}
    client = Client([Response(text=json.dumps(CHOICE))])
    result = run_selection(candidates(tmp_path, 3), tmp_path / "pilot", Config(),
                           brief="Discuss limitations.", client=client, review_runner=reviews)
    assert result["status"] == "ok" and result["total_api_calls"] == 7
    assert result["total_estimated_cost_usd"] > .003
    assert result["candidate_results"][-1]["status"] == "error"
    supplied = json.loads(client.requests[0]["input"][0]["content"])
    assert supplied["candidates"][-1]["status"] == "error"


def test_no_comparative_call_when_fewer_than_two_reviews_complete(tmp_path):
    def failed(path, out, config, task_id, **kwargs):
        return {"task_id": task_id, "status": "error", "review": None,
                "api_calls": 1, "estimated_cost_usd": None, "billing_uncertain": True}
    client = Client([])
    result = run_selection(candidates(tmp_path), tmp_path / "pilot", Config(),
                           brief="Discuss limitations.", client=client, review_runner=failed)
    assert result["status"] == "error" and result["choice"] is None
    assert result["error"]["code"] == "insufficient_completed_candidates"
    assert result["total_api_calls"] == 2 and result["total_estimated_cost_usd"] is None
    assert result["billing_uncertain"] and not client.requests


@pytest.mark.parametrize("change", [
    {"selected_id": "unknown"}, {"selected_id": "b"},
    {"comparisons": []}, {"tied_alternatives": ["a"]},
    {"tied_alternatives": ["b", "b"]}, {"reason": " "},
])
def test_choice_cannot_select_missing_candidate_or_skip_tradeoff(change):
    choice = deepcopy(CHOICE)
    choice.update(change)
    with pytest.raises(ValueError):
        validate_selection(choice, {"a", "b"})


def test_duplicate_candidates_rejected_before_output_or_api_calls(tmp_path):
    paths = candidates(tmp_path)
    paths[1].write_bytes(paths[0].read_bytes())
    with pytest.raises(ValueError, match="distinct paper inputs"):
        run_selection(paths, tmp_path / "pilot", Config(), brief="Discuss evidence.", client=Client([]))
    assert not (tmp_path / "pilot").exists()
