"""Offline M2 appendices preserve shared grids, failures, and trace identities."""

import importlib.util
import json
from pathlib import Path

import pytest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/report_m3_m2_results.py"
SPEC = importlib.util.spec_from_file_location("report_m3_m2_results", SCRIPT)
reporter = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(reporter)
TASKS = [f"T{index:02}" for index in range(1, 21)]


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


def experiment(tmp_path, name, variants, *, model="fixture-model"):
    root = tmp_path / name
    write_json(root / "experiment.json", {"model": model, "variants": list(variants),
                                         "m2_sample_sha256": "sample-hash"})
    return root


def stage(root, number, *, missing=(), updates=None, source=None):
    settings = reporter.read_json(root / "experiment.json")
    directory = root / f"r{number}/m2"
    config = {"model": settings["model"], "max_reads": 5}
    plan = {"sample_sha256": "sample-hash", "task_ids": TASKS, "config": config,
            "variants": settings["variants"], "repeats": 1,
            "source_sha256": source or root.name, "rubric_version": "rubric",
            "checker_version": "checker", "workers": 2, "order_seed": 10 + number}
    write_json(directory / "experiment.json", plan)
    for variant in settings["variants"]:
        for task in TASKS:
            path = directory / f"{variant}-r1" / task / "trace.jsonl"
            result = {"task_id": task, "variant": variant, "model": settings["model"],
                "status": "ok", "checker_version": "checker", "rubric_version": "rubric",
                "review": {"score": .5},
                "citation_checks": [{"quote_matches": True, "citation_verified": True}],
                "decision_steps": 2, "reading_actions": 1, "tool_calls": 2,
                "api_calls": 2, "input_tokens": 100, "output_tokens": 30,
                "estimated_cost_usd": .01, "latency_seconds": 1.0}
            result.update((updates or {}).get((variant, task), {}))
            events = [{"event": "run_start", "task_id": task, "variant": variant, "config": config,
                       "metadata": {"source_sha256": plan["source_sha256"], "sample_sha256": "sample-hash"}},
                      {"event": "note", "text": "Source paragraph\u2028contains a Unicode separator."}]
            if (variant, task) not in missing:
                events.append({"event": "run_end", "result": result})
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("".join(json.dumps(event, ensure_ascii=False) + "\n" for event in events),
                            encoding="utf-8")
    return directory


def test_common_complete_rounds_read_traces_and_preserve_failures(tmp_path, monkeypatch):
    first = experiment(tmp_path, "existing", ("agent", "pyagent_react", "baseline"))
    second = experiment(tmp_path, "deliberative", ("deliberative_review",))
    for number in (1, 2, 3):
        updates = {("baseline", "T01"): {"citation_checks": [
            {"quote_matches": False, "citation_verified": False}]}}
        if number == 1:
            updates["agent", "T01"] = {"status": "error", "review": None,
                                        "estimated_cost_usd": .03}
        if number == 3:
            updates["pyagent_react", "T02"] = {"estimated_cost_usd": None}
        stage(first, number, updates=updates)
        stage(second, number, missing=(("deliberative_review", "T20"),) if number == 2 else ())
    before = {path: path.read_bytes() for path in tmp_path.rglob("trace.jsonl")}
    collected = reporter.collect_model([first, second], TASKS, "sample-hash")
    assert collected["common_rounds"] == [1, 3]
    assert collected["complete_rounds_by_method"]["agent"] == [1, 2, 3]
    assert any("19/20" in note for note in collected["notes"])
    calls = []
    original = reporter.repetition_statistics

    def counted(records):
        calls.append(len(records))
        return original(records)

    monkeypatch.setattr(reporter, "repetition_statistics", counted)
    block = reporter.summarize_model(collected, TASKS, tmp_path / "out")
    assert calls == [160]
    assert block["analysis_repeat_to_global_round"] == {1: 1, 2: 3}
    agent = block["methods"]["agent"]
    assert agent["attempts"] == 40 and agent["completed"] == agent["verified_successes"] == 39
    assert agent["mean_cost_usd"] == pytest.approx(.0105)
    assert agent["mean_input_tokens"] == 100
    assert agent["repetition_statistics"]["pass_power_k"] == pytest.approx({"1": .975, "2": .95})
    paired = agent["repetition_statistics"]["paired_comparisons"]["baseline"]["verified_success_rate"]
    assert paired["tasks"] == 20 and paired["mean_difference"] == pytest.approx(.025)
    assert len(paired["ci95"]) == 2
    assert block["methods"]["baseline"]["completed"] == 40
    assert block["methods"]["baseline"]["verified_successes"] == 38
    assert block["methods"]["pyagent_react"]["mean_cost_usd"] is None
    assert block["methods"]["pyagent_react"]["unknown_cost_attempts"] == 1
    assert len(block["attempts"]) == 160
    assert all(Path(row["trace_path"]).is_file() and len(row["trace_sha256"]) == 64
               for row in block["attempts"])
    assert all(path.read_bytes() == contents for path, contents in before.items())
    report = {"models": {"fixture-model": block}, "experiments": [str(first), str(second)]}
    out = tmp_path / "out"
    out.mkdir()
    reporter.render_markdown(report, out)
    markdown = (out / "M2.md").read_text(encoding="utf-8")
    assert "20 × 2 = 40" in markdown and "95% paper bootstrap interval" in markdown
    assert "k=2" in markdown and "unknown" in markdown


@pytest.mark.parametrize("problem", ["sample", "model", "duplicate", "source", "trace_identity"])
def test_incompatible_or_ambiguous_evidence_is_rejected(tmp_path, problem):
    root = experiment(tmp_path, "suite", reporter.VARIANTS)
    directory = stage(root, 1)
    if problem in ("sample", "model"):
        path = directory / "experiment.json"
        plan = reporter.read_json(path)
        if problem == "sample":
            plan["sample_sha256"] = "other"
        else:
            plan["config"]["model"] = "other-model"
        write_json(path, plan)
    elif problem == "source":
        stage(root, 2, source="changed-source")
    elif problem == "trace_identity":
        path = directory / "agent-r1/T01/trace.jsonl"
        text = path.read_text(encoding="utf-8").replace('"task_id": "T01"', '"task_id": "T02"')
        path.write_text(text, encoding="utf-8")
    roots = [root, root] if problem == "duplicate" else [root]
    with pytest.raises(ValueError):
        reporter.collect_model(roots, TASKS, "sample-hash")


def test_unfinished_final_trace_is_excluded_but_persisted_corruption_fails(tmp_path):
    root = experiment(tmp_path, "suite", reporter.VARIANTS)
    directory = stage(root, 1)
    path = directory / "agent-r1/T01/trace.jsonl"
    with path.open("ab") as stream:
        stream.write(b'{"event":')
    assert reporter.collect_model([root], TASKS, "sample-hash")["common_rounds"] == []
    with path.open("ab") as stream:
        stream.write(b"\n")
    with pytest.raises(ValueError, match="Malformed persisted trace"):
        reporter.collect_model([root], TASKS, "sample-hash")


def test_generate_keeps_models_separate_and_constructs_no_client(tmp_path, monkeypatch):
    roots = []
    for name in ("model-one", "model-two"):
        root = experiment(tmp_path, name, reporter.VARIANTS, model=name)
        stage(root, 1)
        roots.append(root)
    sample = tmp_path / "sample.jsonl"
    sample.write_text("fixture", encoding="utf-8")
    monkeypatch.setattr(reporter, "load_sample", lambda _: [{"id": task} for task in TASKS])
    monkeypatch.setattr(reporter, "file_hash", lambda _: "sample-hash")

    def forbidden(*args, **kwargs):
        raise AssertionError("Offline report constructed a model client")

    monkeypatch.setattr("paper_review.runner.OpenAI", forbidden)
    out = tmp_path / "report"
    report = reporter.generate(roots, out, sample=sample)
    assert set(report["models"]) == {"model-one", "model-two"}
    assert all(block["methods"]["agent"]["attempts"] == 20 for block in report["models"].values())
    assert (out / "m2-results.json").is_file() and (out / "M2.md").is_file()
    assert json.loads((out / "m2-results.json").read_text())["schema_version"] == "m3-original-m2-results-v1"
