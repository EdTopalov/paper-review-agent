"""Source rebuilding keeps maintained guides and generated catalog bytes stable."""

import importlib.util
import json
from pathlib import Path
import sys

from test_benchmark_data import fixture_benchmark
from paper_review.benchmark_data import freeze_catalog


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/prepare_benchmark.py"
SPEC = importlib.util.spec_from_file_location("prepare_benchmark", SCRIPT)
prepare = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prepare)


def test_source_rebuild_copies_maintained_readmes_without_changing_their_bytes(tmp_path, monkeypatch, capsys):
    source, out = tmp_path / "source", tmp_path / "rebuilt"
    for relative in prepare.MAINTAINED_READMES:
        path = source / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((relative + "\r\nMaintained guide.\n").encode("utf-8"))
    monkeypatch.setattr(prepare, "SOURCE_BENCHMARK", source)
    invoked = []

    def generate(arguments, check):
        assert check is True
        invoked.append(Path(arguments[1]).name)
        for track in ("qasper", "reviewcritique", "controlled", "selection"):
            (out / track).mkdir(parents=True, exist_ok=True)

    def assemble(destination):
        assert destination == out
        for relative in prepare.MAINTAINED_READMES:
            assert (out / relative).read_bytes() == (source / relative).read_bytes()
        return {"status": "prepared_not_evaluated"}

    monkeypatch.setattr(prepare.subprocess, "run", generate)
    monkeypatch.setattr(prepare, "freeze_catalog", assemble)
    monkeypatch.setattr(sys, "argv", [str(SCRIPT), "--out", str(out), "--rebuild-sources"])
    prepare.main()
    assert invoked == ["prepare_qasper.py", "prepare_reviewcritique.py", "prepare_controlled_benchmark.py"]
    assert json.loads(capsys.readouterr().out)["status"] == "prepared_not_evaluated"


def test_catalog_is_lf_and_repeated_freezing_is_byte_identical(tmp_path):
    root = fixture_benchmark(tmp_path)
    before = {name: (root / name).read_bytes() for name in ("manifest.jsonl", "benchmark.json")}
    freeze_catalog(root)
    after = {name: (root / name).read_bytes() for name in before}
    assert before == after
    assert all(b"\r\n" not in content for content in after.values())
