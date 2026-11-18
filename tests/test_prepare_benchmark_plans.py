"""Prepared plans retain four methods and the single primary model, offline."""

import importlib.util
import json
from pathlib import Path

import pytest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/prepare_benchmark_plans.py"
SPEC = importlib.util.spec_from_file_location("prepare_benchmark_plans", SCRIPT)
prepare = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prepare)


def test_prepares_four_primary_model_plans_without_model_clients(tmp_path, monkeypatch):
    monkeypatch.setattr("paper_review.benchmark_runner.OpenAI",
                        lambda **kwargs: pytest.fail("Plan preparation must not construct clients"))
    out = tmp_path / "plans"
    summaries = prepare.prepare(SCRIPT.parent.parent / "data/benchmark/v1", out)
    assert len(summaries) == 4
    expected = {"dev-core-smoke-luna6.json": (5, 20, 5),
                "dev-selection-smoke-luna6.json": (1, 4, 20),
                "test-core-luna6-r3.json": (64, 768, 5),
                "test-selection-luna6-r3.json": (12, 144, 20)}
    assert {path.name for path in out.iterdir()} == set(expected)
    for path in out.glob("*.json"):
        plan = json.loads(path.read_text(encoding="utf-8"))
        assert plan["config"]["model"] == "gpt-6-luna"
        assert set(plan["variants"]) == {"agent", "pyagent_react", "deliberative_review", "baseline"}
        assert (plan["tasks"], plan["planned_runs"], plan["config"]["max_reads"]) == expected[path.name]
        assert plan["workers"] == 6 and plan["status"] == "planned_not_executed"
    assert not (out / "unused-dry-run-output").exists()
