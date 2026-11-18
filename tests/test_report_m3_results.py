"""Offline checks for report selection, exact correctness, costs, and intervals."""

from copy import deepcopy
import importlib.util
import json
from pathlib import Path

import pytest


pytest.importorskip("scipy")
SCRIPT = Path(__file__).resolve().parents[1] / "scripts/report_m3_results.py"
SPEC = importlib.util.spec_from_file_location("report_m3_results", SCRIPT)
reporter = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(reporter)


def tasks():
    result = []
    for task_id, kind, track in [("Q", "qa", "qasper"), ("R", "critique", "reviewcritique"),
                                 ("C1", "claim", "controlled"), ("C2", "claim", "controlled"),
                                 ("S", "selection", "selection")]:
        reference = {"qa": {"answers": [{"answer": "Alpha beta", "answer_type": "extractive", "evidence": []}]},
                     "critique": {"verdict": "reliable", "error_types": []},
                     "claim": {"verdict": "supported" if task_id == "C1" else "contradicted",
                               "pair_id": "pair", "family": "fixture", "evidence": []},
                     "selection": {"acceptable_ids": ["P1"], "eligible_ids": ["P1"],
                                   "base_set_id": "set", "order_id": 0}}[kind]
        result.append({"id": task_id, "kind": kind, "track": track, "group_id": track,
                       "input": {"id": task_id, "kind": kind, "instructions": "Use supplied evidence.",
                                 "documents": [{"id": "P1", "title": "Fixture", "blocks": [
                                     {"id": "b1", "text": "Alpha beta."}]}]}, "reference": reference})
    return result


def prediction(task):
    output = {"explanation": "The fixture supplies the stated result.", "evidence": []}
    output.update({"qa": {"answer": "Alpha beta"},
                   "critique": {"verdict": "reliable", "error_types": []},
                   "claim": {"verdict": task["reference"].get("verdict")},
                   "selection": {"selected_id": "P1", "tied_ids": []}}[task["kind"]])
    return output


def write_stage(root, fixture_tasks, stage, number, *, model="fixture-model", variants=("agent", "baseline"),
                omit=(), updates=None, manifest="fixture-manifest"):
    selected = [task for task in fixture_tasks if (task["track"] == "selection") == (stage == "selection")]
    directory = root / f"r{number}" / stage
    directory.mkdir(parents=True)
    plan = {"manifest_sha256": manifest, "split": "test", "task_ids": [task["id"] for task in selected],
            "repeats": 1, "variants": list(variants), "source_sha256": "fixture-source", "workers": 2,
            "seed": number, "config": {"model": model, "max_reads": 20 if stage == "selection" else 5}}
    (directory / "plan.json").write_text(json.dumps(plan), encoding="utf-8")
    rows = []
    for variant in variants:
        for task in selected:
            if (variant, task["id"]) in omit:
                continue
            row = {"id": task["id"], "variant": variant, "repeat": 1, "model": model,
                   "status": "ok", "prediction": prediction(task), "estimated_cost_usd": .01,
                   "latency_seconds": 1.0, "api_calls": 1}
            row.update((updates or {}).get((variant, task["id"]), {}))
            rows.append(row)
    (directory / "records.jsonl").write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
    return directory


def experiment(tmp_path, name="experiment", *, model="fixture-model", variants=("agent", "baseline")):
    root = tmp_path / name
    root.mkdir()
    (root / "experiment.json").write_text(json.dumps({"model": model, "variants": list(variants)}), encoding="utf-8")
    return root


def test_student_t_intervals_use_repetition_means_and_preserve_unknowns():
    assert reporter.mean_interval([2])["ci95"] is None
    result = reporter.mean_interval([1, 3])
    assert result["mean"] == 2
    assert result["ci95"] == pytest.approx([-10.7062047364, 14.7062047364])
    assert reporter.mean_interval([.01, None])["mean"] is None
    with pytest.raises(ValueError):
        reporter.mean_interval([float("nan")])


def test_live_reader_ignores_only_unfinished_final_line(tmp_path):
    path = tmp_path / "records.jsonl"
    path.write_bytes(b'{"id":"done"}\n{"id":')
    assert reporter.read_live_records(path) == ([{"id": "done"}], True)
    path.write_bytes(b'{broken}\n{"id":"done"}\n')
    with pytest.raises(ValueError, match="Malformed"):
        reporter.read_live_records(path)


def test_pooled_report_waits_for_complete_shared_76_case_rounds(tmp_path):
    fixture = tasks()
    root = experiment(tmp_path)
    for number in (1, 2):
        write_stage(root, fixture, "core", number)
    write_stage(root, fixture, "selection", 1)
    write_stage(root, fixture, "selection", 2, omit=[("baseline", "S")])
    collected = reporter.collect([root], fixture, "fixture-manifest")
    assert collected["common_rounds"] == {"core": [1, 2], "selection": [1]}
    assert reporter.summarize_pooled(fixture, collected)["rounds"] == [1]
    assert reporter.summarize_stage(fixture, collected, "core")["rounds"] == [1, 2]
    assert any("incomplete selection round 2" in note for note in collected["notes"])


def test_failures_are_zero_and_partial_qa_f1_is_not_exact_accuracy(tmp_path):
    fixture = tasks()
    root = experiment(tmp_path)
    for number in (1, 2):
        updates = {("agent", "C2"): {"status": "error", "prediction": None, "estimated_cost_usd": .11}}
        if number == 1:
            partial = prediction(fixture[0])
            partial["answer"] = "Alpha"
            updates["agent", "Q"] = {"prediction": partial}
        write_stage(root, fixture, "core", number, updates=updates)
        write_stage(root, fixture, "selection", number)
    collected = reporter.collect([root], fixture, "fixture-manifest")
    pooled = reporter.summarize_pooled(fixture, collected)
    assert pooled["methods"]["agent"]["attempts"] == 10
    assert pooled["methods"]["agent"]["correct"] == 7
    assert pooled["methods"]["agent"]["accuracy_percent"]["mean"] == pytest.approx(70)
    assert pooled["methods"]["agent"]["usd_per_attempt"]["mean"] == pytest.approx(.03)
    assert pooled["methods"]["baseline"]["accuracy_percent"]["mean"] == 100
    core = reporter.summarize_stage(fixture, collected, "core")
    assert core["methods"]["agent"]["qasper"]["primary_percent"]["mean"] == pytest.approx(100 * (2 / 3 + 1) / 2)
    assert core["methods"]["agent"]["controlled"]["primary_percent"]["mean"] == 0


@pytest.mark.parametrize("problem", ["model", "manifest", "duplicate"])
def test_mismatched_or_duplicate_sources_are_rejected(tmp_path, problem):
    fixture = tasks()
    root = experiment(tmp_path)
    directory = write_stage(root, fixture, "core", 1, manifest="wrong" if problem == "manifest" else "fixture-manifest")
    if problem == "model":
        plan = reporter.read_json(directory / "plan.json")
        plan["config"]["model"] = "other"
        (directory / "plan.json").write_text(json.dumps(plan), encoding="utf-8")
    if problem == "duplicate":
        with (directory / "records.jsonl").open("a", encoding="utf-8") as stream:
            stream.write((directory / "records.jsonl").read_text(encoding="utf-8").splitlines()[0] + "\n")
    with pytest.raises(ValueError):
        reporter.collect([root], fixture, "fixture-manifest")


def test_unknown_cost_is_not_silently_zero(tmp_path):
    fixture = tasks()
    root = experiment(tmp_path)
    write_stage(root, fixture, "core", 1, updates={("agent", "Q"): {"estimated_cost_usd": None}})
    write_stage(root, fixture, "selection", 1)
    pooled = reporter.summarize_pooled(fixture, reporter.collect([root], fixture, "fixture-manifest"))
    assert pooled["methods"]["agent"]["usd_per_attempt"]["mean"] is None
    assert pooled["methods"]["agent"]["unknown_cost_attempts"] == 1


def test_source_is_stable_per_method_but_can_differ_between_methods(tmp_path):
    fixture = tasks()
    roots = []
    for variant in ("agent", "baseline"):
        root = experiment(tmp_path, variant, variants=[variant])
        roots.append(root)
        for number in (1, 2):
            for stage in ("core", "selection"):
                directory = write_stage(root, fixture, stage, number, variants=[variant])
                plan = reporter.read_json(directory / "plan.json")
                plan["source_sha256"] = variant + "-source"
                (directory / "plan.json").write_text(json.dumps(plan), encoding="utf-8")
    collected = reporter.collect(roots, fixture, "fixture-manifest")
    assert collected["source_sha256_by_method"] == {"agent": "agent-source", "baseline": "baseline-source"}
    path = roots[0] / "r2/core/plan.json"
    plan = reporter.read_json(path)
    plan["source_sha256"] = "changed-source"
    path.write_text(json.dumps(plan), encoding="utf-8")
    with pytest.raises(ValueError, match="changes frozen source"):
        reporter.collect(roots, fixture, "fixture-manifest")


def test_one_plot_distinguishes_models_without_pooling_them(tmp_path):
    pytest.importorskip("matplotlib")
    fixture = tasks()
    models = {}
    for index, model in enumerate(("model-one", "model-two")):
        root = experiment(tmp_path, f"experiment-{index}", model=model)
        for number in (1, 2):
            for stage in ("core", "selection"):
                write_stage(root, fixture, stage, number, model=model)
        collected = reporter.collect([root], fixture, "fixture-manifest")
        models[model] = {"pooled": reporter.summarize_pooled(fixture, collected)}
    report = {"variants": ["agent", "baseline"], "models": models}
    out = tmp_path / "report"
    out.mkdir()
    reporter.draw_plot(report, out)
    reporter.write_markdown(report, out)
    assert (out / "accuracy-cost.svg").read_text(encoding="utf-8").count("<svg") == 1
    assert (out / "accuracy-cost.png").read_bytes().startswith(b"\x89PNG")
    markdown = (out / "README.md").read_text(encoding="utf-8")
    assert markdown.count("![") == 1
    assert "model-one" in markdown and "model-two" in markdown
    assert "descriptive aggregate" in markdown
