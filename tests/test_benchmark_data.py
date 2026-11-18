"""Frozen data, split boundaries, references, and public exports are independent of models."""

from copy import deepcopy
import json
from pathlib import Path

import pytest

from paper_review.benchmark_data import (benchmark_summary, export_inputs, freeze_catalog,
                                         load_benchmark, read_jsonl, write_jsonl)
from paper_review.paper import file_hash


def fixture_benchmark(tmp_path):
    root = tmp_path / "benchmark"
    for track, kind in (("qasper", "qa"), ("reviewcritique", "critique"),
                        ("controlled", "claim"), ("selection", "selection")):
        folder = root / track
        (folder / "inputs").mkdir(parents=True)
        (folder / "references").mkdir()
        (folder / "source.json").write_text('{"fixture":true}', encoding="utf-8")
        manifest = []
        for index in range(2 if kind == "claim" else 1):
            task_id = f"{track}-{index}"
            public = {"id": task_id, "kind": kind, "instructions": "Assess the supplied evidence.",
                      "documents": [{"id": "P1", "title": track,
                                     "blocks": [{"id": "b1", "text": "The effect is positive."}]}]}
            evidence = [{"document_id": "P1", "block_id": "b1"}]
            reference = {"id": task_id, "label_origin": "scripted_test_fixture"}
            if kind == "qa":
                public["question"] = "What is the effect?"
                reference["answers"] = [{"answer_type": "extractive", "answer": "positive", "evidence": evidence}]
            elif kind == "critique":
                public["comment"] = "The effect is positive."
                reference["verdict"] = "reliable"
            elif kind == "claim":
                public["statement"] = "The effect is positive."
                reference.update(verdict="supported" if index == 0 else "contradicted",
                                 evidence=evidence, pair_id="pair", family="fixture")
                if index:
                    public["documents"][0]["blocks"][0]["text"] = "The effect is negative."
            else:
                public["brief"] = "Choose the supplied candidate."
                reference.update(eligible_ids=["P1"], acceptable_ids=["P1"])
            paths = {}
            for name, value in (("input", public), ("reference", reference)):
                relative = f"{track}/{name}s/{task_id}.json"
                path = root / relative
                path.write_text(json.dumps(value), encoding="utf-8")
                paths[f"{name}_path"] = relative
                paths[f"{name}_sha256"] = file_hash(path)
            manifest.append({"id": task_id, "track": track, "kind": kind, "split": "dev",
                             "group_id": track, **paths})
        write_jsonl(folder / "manifest.jsonl", manifest)
    freeze_catalog(root)
    return root


def change_input(root, task_id, mutate):
    rows = read_jsonl(root / "manifest.jsonl")
    row = next(row for row in rows if row["id"] == task_id)
    path = root / row["input_path"]
    public = json.loads(path.read_text(encoding="utf-8"))
    mutate(public)
    path.write_text(json.dumps(public), encoding="utf-8")
    track_rows = read_jsonl(root / row["track"] / "manifest.jsonl")
    next(item for item in track_rows if item["id"] == task_id)["input_sha256"] = file_hash(path)
    write_jsonl(root / row["track"] / "manifest.jsonl", track_rows)


def test_committed_dataset_integrity_and_expected_prepared_counts():
    root = Path(__file__).resolve().parents[1] / "data/benchmark/v1"
    summary = benchmark_summary(root)
    assert summary["tasks"] == 102 and summary["model_calls"] == 0
    tasks = load_benchmark(root)
    assert len([task for task in tasks if task["split"] == "test"]) == 76
    assert all("reference" not in task["input"] for task in tasks)


@pytest.mark.parametrize("field", ["input", "reference"])
def test_changed_frozen_payload_rejected(tmp_path, field):
    root = fixture_benchmark(tmp_path)
    row = read_jsonl(root / "manifest.jsonl")[0]
    (root / row[f"{field}_path"]).write_text("{}", encoding="utf-8")
    with pytest.raises(ValueError, match="hash mismatch"):
        load_benchmark(root)


def test_source_notices_and_track_manifests_are_hash_bound(tmp_path):
    root = fixture_benchmark(tmp_path)
    with (root / "qasper/manifest.jsonl").open("a", encoding="utf-8") as stream:
        stream.write("\n")
    with pytest.raises(ValueError, match="notice hash"):
        load_benchmark(root)


def test_export_contains_public_inputs_only_and_refuses_overwrite(tmp_path):
    root = fixture_benchmark(tmp_path)
    out = tmp_path / "public"
    result = export_inputs(root, out, split="dev")
    assert result["reference_files_exported"] == 0
    assert {path.name for path in out.iterdir()} == {"inputs.jsonl", *[f"{task['id']}.json" for task in load_benchmark(root)]}
    assert all(set(row) == {"id", "kind", "input_path", "input_sha256"}
               for row in read_jsonl(out / "inputs.jsonl"))
    with pytest.raises(FileExistsError):
        export_inputs(root, out, split="dev")


def test_source_group_cannot_cross_splits(tmp_path):
    root = fixture_benchmark(tmp_path)
    path = root / "controlled/manifest.jsonl"
    rows = read_jsonl(path)
    rows[1]["split"] = "test"
    write_jsonl(path, rows)
    with pytest.raises(ValueError, match="crosses"):
        freeze_catalog(root)


def test_controlled_pair_requires_both_conditions(tmp_path):
    root = fixture_benchmark(tmp_path)
    path = root / "controlled/manifest.jsonl"
    write_jsonl(path, read_jsonl(path)[:1])
    with pytest.raises(ValueError, match="incomplete"):
        freeze_catalog(root)


def test_public_reference_fields_and_wrong_gold_locations_rejected(tmp_path):
    root = fixture_benchmark(tmp_path)
    change_input(root, "qasper-0", lambda public: public.update(answers=["leaked"]))
    with pytest.raises(ValueError, match="Reference-only"):
        freeze_catalog(root)


def test_manifest_paths_cannot_escape_dataset(tmp_path):
    root = fixture_benchmark(tmp_path)
    path = root / "qasper/manifest.jsonl"
    rows = read_jsonl(path)
    rows[0]["input_path"] = "../outside.json"
    write_jsonl(path, rows)
    with pytest.raises(ValueError, match="leaves its root"):
        freeze_catalog(root)
