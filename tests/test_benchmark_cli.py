"""Offline CLI paths must work without credentials or constructing model clients."""

import json
import sys

import openai
import pytest

from paper_review import benchmark_runner, cli, runner
from test_benchmark_data import fixture_benchmark


@pytest.fixture
def offline_cli(tmp_path, monkeypatch, capsys):
    # Use an empty working directory so the user's ignored .env cannot supply a
    # credential and accidentally conceal an API-key requirement.
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("OPENAI_MODEL", raising=False)

    def forbidden(*args, **kwargs):
        pytest.fail("Offline benchmark commands must not construct or invoke a model")

    monkeypatch.setattr(openai, "OpenAI", forbidden)
    monkeypatch.setattr(runner, "OpenAI", forbidden)
    monkeypatch.setattr(benchmark_runner, "OpenAI", forbidden)
    monkeypatch.setattr(benchmark_runner, "ModelCalls", forbidden)
    for name in ("run_review", "run_selection", "evaluate", "audit_experiment"):
        monkeypatch.setattr(cli, name, forbidden)

    def invoke(*arguments):
        monkeypatch.setattr(sys, "argv", ["paper-review", *map(str, arguments)])
        assert cli.main() == 0
        captured = capsys.readouterr()
        assert captured.err == ""
        return json.loads(captured.out)

    return invoke


def test_benchmark_verify_needs_no_api_key_or_model(tmp_path, offline_cli):
    root = fixture_benchmark(tmp_path)
    result = offline_cli("benchmark-verify", "--root", root)
    assert result["tasks"] == 5 and result["model_calls"] == 0
    assert not list(tmp_path.glob("**/trace.jsonl"))


def test_benchmark_export_is_public_and_needs_no_api_key_or_model(tmp_path, offline_cli):
    root = fixture_benchmark(tmp_path)
    out = tmp_path / "export"
    result = offline_cli("benchmark-export", "--root", root, "--split", "dev",
                         "--tracks", "qasper", "--out", out)
    assert result["tasks"] == 1 and result["reference_files_exported"] == 0
    assert {path.name for path in out.iterdir()} == {"inputs.jsonl", "qasper-0.json"}
    public = json.loads((out / "qasper-0.json").read_text(encoding="utf-8"))
    assert "reference" not in public and "answers" not in public
    assert "scripted_test_fixture" not in (out / "qasper-0.json").read_text(encoding="utf-8")


def test_benchmark_plan_writes_only_a_plan_without_api_key_or_model(tmp_path, offline_cli):
    root = fixture_benchmark(tmp_path)
    out = tmp_path / "plans" / "comparison.json"
    result = offline_cli("benchmark-plan", "--root", root, "--split", "dev",
                         "--tracks", "qasper", "--variants", "agent", "baseline",
                         "--repeats", "2", "--model", "scripted-model-name", "--out", out)
    assert result["tasks"] == 1 and result["planned_jobs"] == 4 and result["model_calls"] == 0
    plan = json.loads(out.read_text(encoding="utf-8"))
    assert plan["config"]["model"] == "scripted-model-name"
    assert plan["status"] == "planned_not_executed"
    assert plan["task_ids"] == ["qasper-0"]
    assert list(out.parent.iterdir()) == [out]
    assert not list(tmp_path.glob("**/trace.jsonl"))


def test_benchmark_run_defaults_to_validation_without_api_key_or_model(tmp_path, offline_cli):
    root = fixture_benchmark(tmp_path)
    plan_path = tmp_path / "plan.json"
    offline_cli("benchmark-plan", "--root", root, "--split", "dev", "--tracks", "qasper",
                "--variants", "agent", "baseline", "--repeats", "2", "--out", plan_path)
    out = tmp_path / "must-not-be-created"
    result = offline_cli("benchmark-run", "--plan", plan_path, "--out", out)
    assert result["status"] == "dry_run"
    assert result["execution_enabled"] is False and result["model_calls"] == 0
    assert result["tasks"] == 1 and result["planned_runs"] == 4
    assert not out.exists()
    assert not list(tmp_path.glob("**/trace.jsonl"))
