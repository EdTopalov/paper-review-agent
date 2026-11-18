"""Repeated-run estimates use papers as units and retain unsuccessful attempts."""

import json
from pathlib import Path
import random

import pytest

from paper_review.evaluation import evaluate, repetition_statistics, summarize
from paper_review.runner import Config, run_review
from test_harness import Client, FIXTURE, OPENING_REVIEW, Response, finish


def record(variant, task, repeat, *, completed=True, verified=True, score=0.5,
           model="test-model", cost=0.01):
    result = {
        "variant": variant, "task_id": task, "status": "ok" if completed else "error",
        "review": {"score": score} if completed else None,
        "model": model, "checker_version": "test-checker",
        "citation_checks": [{"quote_matches": verified, "citation_verified": verified}],
        "api_calls": 2, "input_tokens": 100, "output_tokens": 30,
        "estimated_cost_usd": cost, "latency_seconds": 1.0,
    }
    return Path(f"experiment/{variant}-r{repeat}/{task}/trace.jsonl"), result


def test_pass_power_k_is_all_attempts_success_not_at_least_once():
    records = [record("agent", "T01", repeat, completed=repeat != 3)
               for repeat in range(1, 4)]
    records += [record("agent", "T02", repeat) for repeat in range(1, 4)]
    row = repetition_statistics(records)["agent"]
    assert row["pass_power_k"] == pytest.approx({"1": 5 / 6, "2": 2 / 3, "3": 1 / 2})
    assert [repeat["verified_successes"] for repeat in row["per_repeat"]] == [2, 2, 1]
    assert [repeat["completion_rate"] for repeat in row["per_repeat"]] == [1, 1, 0.5]
    assert row["per_task"]["T01"]["attempts"] == 3
    assert row["per_task"]["T01"]["score_count"] == 2
    assert row["tasks_always_verified"] == row["tasks_sometimes_verified"] == 1
    assert row["tasks_never_verified"] == 0


def test_citation_verified_error_and_unverified_completion_are_not_success():
    records = [record("agent", "T01", 1, completed=False, verified=True),
               record("agent", "T01", 2, completed=True, verified=False)]
    row = repetition_statistics(records)["agent"]
    assert row["pass_power_k"] == {"1": 0, "2": 0}
    assert row["per_task"]["T01"]["completed"] == 1
    assert row["tasks_never_verified"] == 1


@pytest.mark.parametrize("missing", [
    ("agent", "T02", 2),  # A paper omitted from a repetition.
    ("baseline", None, 2),  # A whole repetition omitted from one variant.
    (None, None, 1),  # Repetition numbering does not start at one.
])
def test_incomplete_repetition_groups_are_rejected(missing):
    records = [record(variant, task, repeat)
               for variant in ("agent", "baseline")
               for task in ("T01", "T02") for repeat in (1, 2)]
    variant, task, repeat = missing
    records = [(path, result) for path, result in records
               if not ((variant is None or result["variant"] == variant)
                       and (task is None or result["task_id"] == task)
                       and path.parent.parent.name.endswith(f"-r{repeat}"))]
    with pytest.raises(ValueError, match="[Ii]ncomplete|same repetition"):
        repetition_statistics(records)


def test_models_are_not_pooled_and_unknown_verification_is_not_zero():
    records = [record("agent", "T01", 1), record("baseline", "T01", 1, model="other-model")]
    with pytest.raises(ValueError, match="different models"):
        repetition_statistics(records)
    path, result = record("agent", "T01", 1)
    result.pop("checker_version")
    row = repetition_statistics([(path, result)])["agent"]
    assert row["pass_power_k"] is None
    assert row["per_repeat"][0]["verified_success_rate"] is None
    assert row["per_task"]["T01"]["verified_successes"] is None


def test_paired_statistics_keep_task_clusters_and_separate_score_spread():
    records = []
    for repeat, score in enumerate((0.2, 0.4, 0.6), 1):
        for task in ("T01", "T02"):
            records += [record("agent", task, repeat, score=score, cost=0.02),
                        record("baseline", task, repeat, score=0.3,
                               verified=task == "T02", cost=0.01)]
    first = repetition_statistics(records)
    assert repetition_statistics(records) == first  # The bootstrap seed is fixed.
    agent = first["agent"]
    assert agent["within_task_mean_absolute_score_difference"] == pytest.approx(0.8 / 3)
    assert agent["per_task"]["T01"]["score_sample_sd"] == pytest.approx(0.2)
    comparison = agent["paired_comparisons"]["baseline"]
    assert comparison["verified_success_rate"] == {
        "tasks": 2, "mean_difference": 0.5, "ci95": [0, 1]}
    assert comparison["mean_score"]["mean_difference"] == pytest.approx(0.1)
    assert comparison["mean_cost_usd"]["mean_difference"] == pytest.approx(0.01)
    assert comparison["mean_absolute_task_score_difference"] == pytest.approx(0.1)


def test_single_paper_has_no_bootstrap_interval():
    records = [record("agent", "T01", 1), record("baseline", "T01", 1)]
    comparison = repetition_statistics(records)["agent"]["paired_comparisons"]["baseline"]
    assert comparison["verified_success_rate"]["ci95"] is None
    assert repetition_statistics(records)["agent"]["within_task_mean_absolute_score_difference"] is None


def test_summary_renders_repeats_reliability_and_failed_attempts(tmp_path):
    for repeat in (1, 2):
        for variant in ("agent", "baseline"):
            client = (Client([]) if repeat == 2 and variant == "agent" else
                      Client([finish()]) if variant == "agent" else
                      Client([Response(text=json.dumps(OPENING_REVIEW))]))
            run_review(FIXTURE, tmp_path / f"{variant}-r{repeat}/dev", Config(),
                       "dev", variant, client=client)
    result = summarize(tmp_path)
    assert result["agent"]["runs"] == 2
    assert result["agent"]["completed"] == 1
    assert result["agent"]["repetition_statistics"]["pass_power_k"] == {"1": 0.5, "2": 0}
    report = (tmp_path / "README.md").read_text(encoding="utf-8")
    assert "Repetition variation" in report
    assert "pass^k" in report and "C(s,k)/C(n,k)" in report
    assert "Per-paper consistency" in report and "agent-r2/dev" in report
    assert "do not capture future API model drift" in report


def test_task_selector_keeps_full_frozen_sample_and_seeded_job_order(tmp_path, monkeypatch):
    import paper_review.evaluation as evaluation

    sample = Path(__file__).resolve().parents[1] / "data/eval/tasks.jsonl"
    original_sample = sample.read_bytes()
    jobs = []

    def fake_run(paper, folder, config, task_id, variant, metadata):
        jobs.append((task_id, variant, folder.parent.name))
        assert paper.name == "T17.json"
        return {"status": "ok", "api_calls": 1, "latency_seconds": 0}

    monkeypatch.setattr(evaluation, "run_review", fake_run)
    monkeypatch.setattr(evaluation, "summarize", lambda out: "offline test")
    out = tmp_path / "comparison"
    assert evaluate(sample, out, Config(), workers=1, repeats=3,
                    task_ids=["T17"], variants=["agent", "baseline"], order_seed=42) == "offline test"
    planned = [("T17", variant, f"{variant}-r{repeat}")
               for repeat in (1, 2, 3) for variant in ("agent", "baseline")]
    random.Random(42).shuffle(planned)
    assert jobs == planned
    manifest = json.loads((out / "experiment.json").read_text(encoding="utf-8"))
    assert manifest["task_ids"] == ["T17"]
    assert manifest["order_seed"] == 42
    assert manifest["sample_path"] == str(sample.resolve())
    assert sample.read_bytes() == original_sample
    progress = json.loads((out / "progress.json").read_text(encoding="utf-8"))
    assert progress["status"] == "finished"
    assert progress["total"] == progress["completed"] == progress["succeeded"] == 6
    assert progress["failed"] == progress["remaining"] == 0
    assert progress["model"] == Config.model and progress["variants"] == ["agent", "baseline"]
    assert progress["source_sha256"] == manifest["source_sha256"]


def test_evaluation_progress_includes_retained_results_on_resume(tmp_path, monkeypatch):
    import paper_review.evaluation as evaluation

    sample = Path(__file__).resolve().parents[1] / "data/eval/tasks.jsonl"
    out = tmp_path / "resumed"
    calls = []

    def fake_run(paper, folder, config, task_id, variant, metadata):
        result = {"status": "ok", "api_calls": 1, "latency_seconds": 1.0}
        folder.mkdir(parents=True)
        (folder / "trace.jsonl").write_text(json.dumps({"event": "run_end", "result": result}) + "\n", encoding="utf-8")
        calls.append(task_id)
        return result

    monkeypatch.setattr(evaluation, "run_review", fake_run)
    monkeypatch.setattr(evaluation, "summarize", lambda out: "offline test")
    options = {"workers": 1, "task_ids": ["T17"], "variants": ["agent"], "repeats": 2}
    assert evaluate(sample, out, Config(), **options) == "offline test"
    first = json.loads((out / "progress.json").read_text(encoding="utf-8"))
    assert evaluate(sample, out, Config(), **options) == "offline test"
    second = json.loads((out / "progress.json").read_text(encoding="utf-8"))
    assert len(calls) == 2
    assert second["status"] == "finished" and second["completed"] == second["total"] == 2
    assert second["remaining"] == second["failed"] == 0
    assert second["elapsed_seconds"] >= first["elapsed_seconds"]


def test_evaluation_progress_records_failure_without_raw_exception_text(tmp_path, monkeypatch):
    import paper_review.evaluation as evaluation

    def fail_run(*args, **kwargs):
        raise RuntimeError("Private API setup detail")

    sample = Path(__file__).resolve().parents[1] / "data/eval/tasks.jsonl"
    out = tmp_path / "failed"
    monkeypatch.setattr(evaluation, "run_review", fail_run)
    with pytest.raises(RuntimeError, match="Private API setup detail"):
        evaluate(sample, out, Config(), workers=1, task_ids=["T17"], variants=["agent"])
    progress = json.loads((out / "progress.json").read_text(encoding="utf-8"))
    assert progress["status"] == "error" and progress["total"] == progress["remaining"] == 1
    assert progress["completed"] == 0 and progress["error"]["type"] == "RuntimeError"
    assert "Private API setup detail" not in (out / "progress.json").read_text(encoding="utf-8")


@pytest.mark.parametrize("task_ids,limit,message", [
    (["T99"], None, "Unknown task IDs"),
    (["T17", "T17"], None, "distinct task IDs"),
    ([], None, "nonempty"),
    (["T17"], 1, "task_ids or limit"),
])
def test_invalid_task_selection_fails_before_creating_experiment(tmp_path, task_ids, limit, message):
    sample = Path(__file__).resolve().parents[1] / "data/eval/tasks.jsonl"
    out = tmp_path / "comparison"
    with pytest.raises(ValueError, match=message):
        evaluate(sample, out, Config(), task_ids=task_ids, limit=limit)
    assert not out.exists()
