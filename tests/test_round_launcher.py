"""Exercise offset round scheduling without model clients or API requests."""

import importlib.util
import json
from pathlib import Path

import pytest


@pytest.fixture
def launcher(monkeypatch, tmp_path):
    spec = importlib.util.spec_from_file_location(
        "round_launcher", Path(__file__).parents[1] / "scripts/run_existing_benchmark.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    tasks = [{"id": f"{track}-{i}", "track": track}
             for track, count in (("qasper", 20), ("reviewcritique", 20),
                                  ("controlled", 24), ("selection", 12))
             for i in range(count)]
    observations = {"plans": [], "validations": [], "executions": [], "m2": [], "scores": []}

    def make_plan(root, split, *, tracks, variants, repeats, config, workers, seed):
        selected = [task for task in tasks if task["track"] in tracks]
        plan = {"tasks": selected, "variants": variants, "planned_runs": len(selected) * len(variants),
                "config": {"max_reads": config.max_reads}, "seed": seed}
        observations["plans"].append(plan)
        return plan

    def run_plan(plan, out, execute=False):
        observations["executions" if execute else "validations"].append(Path(out))
        if execute:
            out.mkdir(parents=True)
            records = [{"id": task["id"], "variant": variant, "repeat": 1,
                        "status": "ok", "trace_path": f"{variant}/{task['id']}/trace.jsonl"}
                       for task in plan["tasks"] for variant in plan["variants"]]
            (out / "records.jsonl").write_text(
                "".join(json.dumps(record) + "\n" for record in records), encoding="utf-8")
        return {"model_calls": 0}

    def evaluate(sample, out, config, **kwargs):
        observations["m2"].append((out, kwargs))
        return {variant: {"runs": 20, "completed": 20, "all_citations_verified": 20,
                          "mean_cost_usd": 0} for variant in kwargs["variants"]}

    def score_predictions(tasks, records, *, variants, repeats):
        observations["scores"].append((list(records), repeats))
        return {"variants": {variant: {"tracks": {}} for variant in variants}}

    monkeypatch.setattr(module, "make_plan", make_plan)
    monkeypatch.setattr(module, "run_plan", run_plan)
    monkeypatch.setattr(module, "evaluate", evaluate)
    monkeypatch.setattr(module, "score_predictions", score_predictions)
    monkeypatch.setattr(module, "load_benchmark", lambda *args: tasks)
    monkeypatch.setattr(module, "load_sample", lambda *args: [{}] * 20)
    sample = tmp_path / "sample.jsonl"
    sample.write_text("frozen sample", encoding="utf-8")
    return module, observations, sample


@pytest.mark.parametrize("start", [1, 4, 5])
def test_one_round_uses_global_ids_and_counted_completion(launcher, tmp_path, start):
    module, observed, sample = launcher
    out = tmp_path / "experiment"
    result = module.run(tmp_path, out, repeats=1, start_round=start, workers=8,
                        variants=list(module.AVAILABLE_VARIANTS), m2_sample=sample, execute=True)
    assert result["rounds"] == 1 and result["attempts"] == 384
    assert [path.relative_to(out).as_posix() for path in observed["executions"]] == [
        f"r{start}/core", f"r{start}/selection"]
    assert all(plan["seed"] == 20261118 + start for plan in observed["plans"])
    assert observed["m2"][0][0] == out / f"r{start}/m2"
    assert observed["m2"][0][1]["order_seed"] == 20261118 + start
    records, repeat_ids = observed["scores"][0]
    assert repeat_ids == [start] and len(records) == 304
    assert all(record["repeat"] == record["source_round"] == start for record in records)
    assert all(record["source_repeat"] == 1 and record["trace_path"].startswith(f"r{start}/")
               for record in records)
    settings = json.loads((out / "experiment.json").read_text())
    assert settings["start_round"] == start and settings["rounds"] == 1
    assert settings["planned_attempts"] == 384
    assert {stage["round"] for stage in settings["stages"]} == {start}
    progress = json.loads((out / "progress.json").read_text())
    assert progress["completed_rounds"] == 1 and progress["global_round"] == start


def test_offset_dry_run_only_validates_without_output_or_execution(launcher, tmp_path):
    module, observed, sample = launcher
    out = tmp_path / "dry"
    result = module.run(tmp_path, out, repeats=1, start_round=4,
                        variants=list(module.AVAILABLE_VARIANTS), m2_sample=sample)
    assert result["model_calls"] == 0 and result["planned_attempts"] == 384
    assert result["start_round"] == 4 and result["rounds"] == 1
    assert len(observed["validations"]) == 2
    assert not observed["executions"] and not observed["m2"] and not observed["scores"]
    assert not out.exists()


@pytest.mark.parametrize("start", [0, -1, True, 1.5])
def test_invalid_start_round_is_rejected_before_planning(launcher, tmp_path, start):
    module, observed, sample = launcher
    with pytest.raises(ValueError, match="Start round"):
        module.run(tmp_path, tmp_path / "invalid", repeats=1, start_round=start, m2_sample=sample)
    assert not observed["plans"]
