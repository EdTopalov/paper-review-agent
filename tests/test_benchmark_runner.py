"""Runner checks use scripted clients only; no live benchmark is executed."""

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace
from zipfile import ZipFile

import pytest

from paper_review.benchmark_data import BENCHMARK_VERSION
from paper_review.benchmark_runner import check_runs, make_plan, run_one, run_plan, write_progress
from paper_review.runner import Config
from paper_review.trace import read_events
from test_harness import Action, Client, Response


PREDICTION = {"answer": "7", "evidence": [
    {"document_id": "P1", "block_id": "b1", "quote": "The measured result is 7."}],
    "explanation": "The supplied result states the value."}


def frozen_fixture(tmp_path):
    root = tmp_path / "benchmark"
    root.mkdir()
    public = {"id": "QA-01", "kind": "qa", "instructions": "Answer using the supplied paper.",
              "question": "What is the measured result?", "documents": [
                  {"id": "P1", "title": "Runner fixture", "blocks": [
                      {"id": "b1", "text": "The measured result is 7."},
                      {"id": "b2", "text": "A second paragraph reports the study scope."}]}]}
    reference = {"id": "QA-01", "answers": [{"answer_type": "extractive", "answer": "7",
                  "evidence": [{"document_id": "P1", "block_id": "b1"}]}],
                 "label_origin": "scripted_test_fixture", "private_marker": "PRIVATE_GOLD_EXPLANATION"}
    paths = {"input": root / "input.json", "reference": root / "reference.json"}
    for kind, value in [("input", public), ("reference", reference)]:
        paths[kind].write_text(json.dumps(value) + "\n", encoding="utf-8")
    row = {"id": "QA-01", "track": "qasper", "kind": "qa", "split": "dev", "group_id": "fixture-paper"}
    for kind, path in paths.items():
        row.update({f"{kind}_path": path.name, f"{kind}_sha256": sha256(path.read_bytes()).hexdigest()})
    manifest = root / "manifest.jsonl"
    manifest.write_text(json.dumps(row) + "\n", encoding="utf-8")
    (root / "benchmark.json").write_text(json.dumps({"version": BENCHMARK_VERSION, "tasks": 1,
        "manifest_sha256": sha256(manifest.read_bytes()).hexdigest(), "source_files": {}}), encoding="utf-8")
    return root, public


def native_finish():
    return Response([Action("submit_review", {"reason": "Evidence is sufficient.", "review": PREDICTION}, "finish")])


def test_plan_and_dry_run_never_construct_a_model_client_or_create_output(tmp_path, monkeypatch):
    root, _ = frozen_fixture(tmp_path)
    monkeypatch.setattr("paper_review.benchmark_runner.OpenAI", lambda **kwargs: pytest.fail("Live client forbidden"))
    plan = make_plan(root, "dev", variants=["agent", "baseline"], repeats=3, workers=1)
    assert plan == make_plan(root, "dev", variants=["agent", "baseline"], repeats=3, workers=1)
    assert plan["tasks"] == 1 and plan["planned_runs"] == 6
    assert len({job["job_id"] for job in plan["jobs"]}) == 6
    out = tmp_path / "not-created"
    result = run_plan(plan, out, client_factory=lambda: pytest.fail("No client factory in dry run"))
    assert result["model_calls"] == 0 and result["execution_enabled"] is False
    assert not out.exists()


@pytest.mark.parametrize("field,value", [("source_sha256", "changed"), ("manifest_sha256", "changed"),
                                          ("task_ids", ["unknown"]), ("jobs", [])])
def test_changed_plan_rejected_before_output_or_client(tmp_path, field, value):
    root, _ = frozen_fixture(tmp_path)
    plan = make_plan(root, "dev", variants=["baseline"], repeats=1)
    plan[field] = value
    out = tmp_path / "not-created"
    with pytest.raises(ValueError):
        run_plan(plan, out, execute=True, client_factory=lambda: pytest.fail("Client forbidden"))
    assert not out.exists()


def test_changed_dataset_rejected_before_output_or_client(tmp_path):
    root, _ = frozen_fixture(tmp_path)
    plan = make_plan(root, "dev", variants=["baseline"], repeats=1)
    (root / "input.json").write_text("{}\n", encoding="utf-8")
    with pytest.raises(ValueError, match="hash mismatch"):
        run_plan(plan, tmp_path / "not-created", execute=True,
                 client_factory=lambda: pytest.fail("Client forbidden"))
    assert not (tmp_path / "not-created").exists()


def test_explicit_mock_execution_scores_and_archives_without_reference_leak(tmp_path, monkeypatch):
    root, _ = frozen_fixture(tmp_path)
    monkeypatch.setattr("paper_review.benchmark_runner.OpenAI", lambda **kwargs: pytest.fail("Live client forbidden"))
    plan = make_plan(root, "dev", variants=["baseline"], repeats=2, workers=1)
    out = tmp_path / "scripted-only"
    created = []

    def factory():
        client = Client([Response(text=json.dumps(PREDICTION))])
        created.append(client)
        return client

    result = run_plan(plan, out, execute=True, client_factory=factory)
    assert result["runs"] == result["completed"] == 2
    assert len(created) == 2
    assert check_runs(out) == {"runs": 2, "passed": 2, "failures": []}
    assert (out / "scores.json").is_file() and (out / "README.md").is_file()
    report = (out / "README.md").read_text(encoding="utf-8")
    assert "Content by track" in report and "Answer F1" in report
    assert "r1: 1.000; r2: 1.000" in report
    for client in created:
        assert "PRIVATE_GOLD_EXPLANATION" not in json.dumps(client.requests)
        assert "scripted_test_fixture" not in json.dumps(client.requests)
    for trace in out.glob("*/*/trace.jsonl"):
        assert "PRIVATE_GOLD_EXPLANATION" not in trace.read_text(encoding="utf-8")
    with ZipFile(out / "source.zip") as archive:
        assert "src/paper_review/benchmark_runner.py" in archive.namelist()
        assert not any(name.endswith(".env") or name.endswith("AGENTS.md") for name in archive.namelist())
    with pytest.raises(FileExistsError):
        run_plan(plan, out, execute=True, client_factory=lambda: pytest.fail("Do not overwrite"))


@pytest.mark.parametrize("variant", ["agent", "pyagent_react"])
def test_shared_agent_controllers_accept_scripted_predictions(tmp_path, variant):
    if variant == "pyagent_react":
        pytest.importorskip("pyagent_patterns")
    _, public = frozen_fixture(tmp_path)
    response = (Response(text="Action: submit_review(" + json.dumps({
        "reason": "Evidence is sufficient.", "review": PREDICTION}) + ")")
        if variant == "pyagent_react" else native_finish())
    result = run_one(public, tmp_path / variant, Config(), public["id"], variant,
                     client=Client([response]), metadata={"repeat": 2})
    assert result["status"] == "ok", result.get("error")
    assert result["prediction"] == PREDICTION
    assert result["api_calls"] == 1 and result["repeat"] == 2
    assert all(check["citation_verified"] for check in result["citation_checks"])
    events = read_events(tmp_path / variant / "trace.jsonl")
    assert all(event["variant"] == variant and event["repeat"] == 2 for event in events)


def test_failed_model_attempts_are_retained_and_costed(tmp_path):
    root, _ = frozen_fixture(tmp_path)
    plan = make_plan(root, "dev", variants=["agent"], repeats=1, config=Config(max_reads=0), workers=1)
    out = tmp_path / "scripted-failure"
    result = run_plan(plan, out, execute=True,
                      client_factory=lambda: Client([Response() for _ in range(6)]
                                                    + [Response(text='{"answer": null}')]))
    assert result["runs"] == 1 and result["completed"] == 0
    record = json.loads((out / "records.jsonl").read_text(encoding="utf-8"))
    assert record["error"]["code"] == "final_answer_none"
    assert record["api_calls"] == 7 and record["estimated_cost_usd"] > 0
    progress = json.loads((out / "progress.json").read_text(encoding="utf-8"))
    assert progress["status"] == "finished"
    assert progress["total"] == progress["completed"] == progress["failed"] == 1
    assert progress["succeeded"] == progress["remaining"] == 0
    assert check_runs(out)["passed"] == 1
    record["status"] = "ok"
    (out / "records.jsonl").write_text(json.dumps(record) + "\n", encoding="utf-8")
    assert check_runs(out)["passed"] == 0


@pytest.mark.parametrize("ids", [[], ["unknown"], ["QA-01", "QA-01"]])
def test_task_selection_requires_known_distinct_ids(tmp_path, ids):
    root, _ = frozen_fixture(tmp_path)
    with pytest.raises(ValueError, match="distinct task IDs"):
        make_plan(root, "dev", task_ids=ids)


def test_execution_opt_in_must_be_boolean(tmp_path):
    root, _ = frozen_fixture(tmp_path)
    plan = make_plan(root, "dev", variants=["baseline"], repeats=1)
    with pytest.raises(ValueError, match="explicit boolean"):
        run_plan(plan, tmp_path / "not-created", execute="false")


def test_subset_plan_executes_and_scores_only_selected_tasks(tmp_path):
    root, public = frozen_fixture(tmp_path)
    second_public = {**public, "id": "QA-02"}
    second_reference = {**json.loads((root / "reference.json").read_text()), "id": "QA-02"}
    second_row = {**json.loads((root / "manifest.jsonl").read_text()), "id": "QA-02"}
    for kind, value in [("input", second_public), ("reference", second_reference)]:
        path = root / f"second-{kind}.json"
        path.write_text(json.dumps(value) + "\n", encoding="utf-8")
        second_row.update({f"{kind}_path": path.name, f"{kind}_sha256": sha256(path.read_bytes()).hexdigest()})
    manifest = root / "manifest.jsonl"
    with manifest.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(second_row) + "\n")
    (root / "benchmark.json").write_text(json.dumps({"version": BENCHMARK_VERSION, "tasks": 2,
        "manifest_sha256": sha256(manifest.read_bytes()).hexdigest(), "source_files": {}}), encoding="utf-8")

    plan = make_plan(root, "dev", variants=["baseline"], repeats=1, task_ids=["QA-02"])
    result = run_plan(plan, tmp_path / "subset", execute=True,
                      client_factory=lambda: Client([Response(text=json.dumps(PREDICTION))]))
    assert result["runs"] == result["completed"] == result["scores"]["task_count"] == 1
    assert [row["id"] for row in result["scores"]["items"]] == ["QA-02"]
    assert check_runs(tmp_path / "subset")["passed"] == 1


def test_client_creation_failure_remains_a_traceable_failed_attempt(tmp_path):
    root, _ = frozen_fixture(tmp_path)
    plan = make_plan(root, "dev", variants=["baseline"], repeats=1)

    def unavailable_client():
        raise RuntimeError("Private client setup details")

    out = tmp_path / "client-failure"
    result = run_plan(plan, out, execute=True, client_factory=unavailable_client)
    assert result["runs"] == 1 and result["completed"] == 0
    record = json.loads((out / "records.jsonl").read_text(encoding="utf-8"))
    assert record["status"] == "error" and record["api_calls"] == 0
    assert record["error"]["type"] == "RuntimeError"
    assert "Private client setup details" not in (out / record["trace_path"]).read_text(encoding="utf-8")
    assert check_runs(out)["passed"] == 1


def test_input_limit_failure_precedes_client_creation(tmp_path):
    _, public = frozen_fixture(tmp_path)
    result = run_one(public, tmp_path / "over-limit", Config(max_paper_chars=1), public["id"], "agent",
                     client_factory=lambda: pytest.fail("No client for rejected input"))
    assert result["status"] == "error" and result["api_calls"] == 0
    assert result["error"]["code"] == "paper_exceeds_documented_input_limit"


def test_deliberative_variant_dispatches_to_its_controller(tmp_path, monkeypatch):
    from paper_review.deliberative_runner import DELIBERATIVE_POLICY, DELIBERATIVE_PROMPT_VERSION

    _, public = frozen_fixture(tmp_path)
    received = []

    def deliberate(paper, calls, config, trace, *, contract=None):
        received.append((paper, calls, config, trace, contract))
        return PREDICTION, {"reading_actions": 0, "tool_calls": 0, "decision_steps": 0}

    monkeypatch.setitem(sys.modules, "paper_review.deliberative_runner", SimpleNamespace(
        run_deliberative=deliberate, DELIBERATIVE_POLICY=DELIBERATIVE_POLICY,
        DELIBERATIVE_PROMPT_VERSION=DELIBERATIVE_PROMPT_VERSION))
    result = run_one(public, tmp_path / "deliberative", Config(), public["id"], "deliberative_review", client=Client([]))
    assert result["status"] == "ok" and result["api_calls"] == 0
    assert len(received) == 1 and received[0][-1].output_schema["properties"]["answer"]
    assert received[0][0].public == public


def test_progress_is_published_before_clients_and_after_each_persisted_attempt(tmp_path, monkeypatch):
    from paper_review import benchmark_runner

    root, _ = frozen_fixture(tmp_path)
    plan = make_plan(root, "dev", variants=["baseline"], repeats=2, workers=1)
    out = tmp_path / "with-progress"
    snapshots = []
    original = write_progress

    def observe(*args, **kwargs):
        original(*args, **kwargs)
        snapshot = json.loads((out / "progress.json").read_text(encoding="utf-8"))
        if (out / "records.jsonl").exists():
            assert snapshot["completed"] == len((out / "records.jsonl").read_text(encoding="utf-8").splitlines())
        snapshots.append(snapshot)

    def client():
        assert json.loads((out / "progress.json").read_text(encoding="utf-8"))["status"] == "running"
        assert (out / "source.zip").is_file() and (out / "plan.json").is_file()
        return Client([Response(text=json.dumps(PREDICTION))])

    monkeypatch.setattr(benchmark_runner, "write_progress", observe)
    run_plan(plan, out, execute=True, client_factory=client)
    assert [(row["status"], row["completed"]) for row in snapshots] == [
        ("running", 0), ("running", 1), ("running", 2), ("finished", 2)]
    final = snapshots[-1]
    assert final["total"] == final["completed"] == final["succeeded"] == 2
    assert final["failed"] == final["remaining"] == final["infrastructure_errors"] == 0
    assert final["eta_remaining_seconds"] == 0
    assert final["recent_mean_attempt_seconds"] >= 0 and final["recent_p50_attempt_seconds"] >= 0
    assert final["wall_throughput_attempts_per_second"] > 0
    assert final["model"] == plan["config"]["model"] and final["variants"] == ["baseline"]
    assert final["source_sha256"] == plan["source_sha256"]
    assert not (out / "progress.json.tmp").exists()


def test_unhandled_worker_error_keeps_other_attempts_and_reports_incomplete_progress(tmp_path, monkeypatch):
    from paper_review import benchmark_runner

    root, _ = frozen_fixture(tmp_path)
    plan = make_plan(root, "dev", variants=["baseline"], repeats=2, workers=1)
    original = run_one

    def one(*args, **kwargs):
        if kwargs["metadata"]["repeat"] == 1:
            raise RuntimeError("Private infrastructure details")
        return original(*args, **kwargs)

    monkeypatch.setattr(benchmark_runner, "run_one", one)
    out = tmp_path / "incomplete"
    with pytest.raises(RuntimeError, match="benchmark_worker_failed"):
        run_plan(plan, out, execute=True, client_factory=lambda: Client([Response(text=json.dumps(PREDICTION))]))
    progress = json.loads((out / "progress.json").read_text(encoding="utf-8"))
    assert progress["status"] == "error" and progress["total"] == 2
    assert progress["completed"] == progress["succeeded"] == progress["remaining"] == 1
    assert progress["failed"] == 0 and progress["infrastructure_errors"] == 1
    assert progress["latest_runner_error"]["repeat"] == 1
    failure = json.loads((out / "runner_errors.jsonl").read_text(encoding="utf-8"))
    assert failure["error"]["type"] == "RuntimeError" and failure["repeat"] == 1
    record = json.loads((out / "records.jsonl").read_text(encoding="utf-8"))
    assert record["repeat"] == 2 and record["status"] == "ok"
    assert (out / record["trace_path"]).is_file() and not (out / "scores.json").exists()
    assert "Private infrastructure details" not in (out / "progress.json").read_text(encoding="utf-8")
    assert "Private infrastructure details" not in (out / "runner_errors.jsonl").read_text(encoding="utf-8")


def test_scoring_error_preserves_completed_records_and_marks_progress(tmp_path, monkeypatch):
    root, _ = frozen_fixture(tmp_path)
    plan = make_plan(root, "dev", variants=["baseline"], repeats=1)

    def fail_score(*args, **kwargs):
        raise ValueError("Private scoring details")

    monkeypatch.setattr("paper_review.benchmark_scoring.score_predictions", fail_score)
    out = tmp_path / "scoring-error"
    with pytest.raises(ValueError, match="Private scoring details"):
        run_plan(plan, out, execute=True, client_factory=lambda: Client([Response(text=json.dumps(PREDICTION))]))
    progress = json.loads((out / "progress.json").read_text(encoding="utf-8"))
    assert progress["status"] == "error" and progress["completed"] == progress["total"] == 1
    assert progress["error"]["type"] == "ValueError"
    assert "Private scoring details" not in (out / "progress.json").read_text(encoding="utf-8")
    assert check_runs(out)["passed"] == 1


def test_public_progress_helper_uses_recent_timings_and_needs_no_benchmark_manifest(tmp_path):
    plan = {"planned_runs": 30, "config": {"model": "scripted-model"}, "variants": ["agent"]}
    records = [{"status": "ok" if index % 2 else "error", "latency_seconds": index}
               for index in range(25)]
    write_progress(tmp_path, plan, records, time.perf_counter() - 10, "running")
    progress = json.loads((tmp_path / "progress.json").read_text(encoding="utf-8"))
    assert progress["total"] == 30 and progress["completed"] == 25 and progress["remaining"] == 5
    assert progress["succeeded"] == 12 and progress["failed"] == 13
    assert progress["recent_attempts"] == 20
    assert progress["recent_mean_attempt_seconds"] == progress["recent_p50_attempt_seconds"] == 14.5
    assert progress["elapsed_seconds"] >= 10
    assert progress["eta_remaining_seconds"] == pytest.approx(
        progress["remaining"] / progress["wall_throughput_attempts_per_second"])
    assert progress["source_sha256"] is None and progress["manifest_sha256"] is None
