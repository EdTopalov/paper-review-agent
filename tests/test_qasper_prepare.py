"""Offline checks for QASPER provenance, exclusion rules, and label isolation."""

from collections import Counter
from copy import deepcopy
from hashlib import sha256
import importlib.util
import io
import json
from pathlib import Path
import tarfile

import pytest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/prepare_qasper.py"
SPEC = importlib.util.spec_from_file_location("prepare_qasper", SCRIPT)
qasper = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(qasper)


def paper_fixture():
    paragraph = "The experiment uses 120 held-out examples and three independent runs."
    answer = {"unanswerable": False, "yes_no": None,
              "extractive_spans": ["120 held-out examples"], "free_form_answer": "",
              "evidence": [paragraph], "highlighted_evidence": [paragraph]}
    question = {"question": "How many held-out examples were used?", "question_id": "abcdefghijklmno",
                "answers": [{"answer": answer, "annotation_id": "source-annotation"}]}
    paper = {"title": "A small source paper", "abstract": "A controlled empirical study.",
             "full_text": [{"section_name": "Methods", "paragraphs": [paragraph]}],
             "figures_and_tables": [{"caption": "Figure 1. Schematic overview."}], "qas": [question]}
    return paper, question


def test_conversion_preserves_source_text_and_keeps_reference_out_of_input():
    paper, question = paper_fixture()
    document = qasper.paper_document("0000.00000", paper)
    row = qasper.convert_question("0000.00000", paper, question, document)
    assert [block["text"] for block in document["blocks"]] == [
        paper["abstract"], paper["full_text"][0]["paragraphs"][0], paper["figures_and_tables"][0]["caption"]]
    assert row["reference"]["answers"][0]["evidence"] == [{"document_id": "P1", "block_id": "b0002"}]
    assert row["reference"]["answers"][0]["answer"] == "120 held-out examples"
    assert "answers" not in row["input"] and "reference" not in row["input"]
    assert "source-annotation" not in json.dumps(row["input"])
    assert row["input"]["documents"][0]["source_url"] == "https://arxiv.org/abs/0000.00000"


@pytest.mark.parametrize("change,reason", [
    ({"evidence": ["FLOAT SELECTED: result table"]}, "nontext_evidence"),
    ({"evidence": ["This paragraph is absent."]}, "unmatched_evidence"),
    ({"evidence": []}, "missing_evidence"),
    ({"extractive_spans": ["BIBREF19"]}, "placeholder_answer"),
])
def test_unsuitable_gold_is_excluded_without_inventing_a_mapping(change, reason):
    paper, question = paper_fixture()
    question["answers"][0]["answer"].update(change)
    with pytest.raises(ValueError, match=reason):
        qasper.convert_question("fixture", paper, question, qasper.paper_document("fixture", paper))


def test_multi_reference_answers_preserved_and_conflicting_boolean_labels_rejected():
    paper, question = paper_fixture()
    second = deepcopy(question["answers"][0])
    second["annotation_id"] = "second-source-annotation"
    second["answer"]["extractive_spans"] = ["120"]
    question["answers"].append(second)
    row = qasper.convert_question("fixture", paper, question, qasper.paper_document("fixture", paper))
    assert len(row["reference"]["answers"]) == 2
    assert row["reference"]["source_annotation_ids"] == ["source-annotation", "second-source-annotation"]
    for index, annotation in enumerate(question["answers"]):
        annotation["answer"].update(extractive_spans=[], yes_no=bool(index))
    with pytest.raises(ValueError, match="boolean_disagreement"):
        qasper.convert_question("fixture", paper, question, qasper.paper_document("fixture", paper))


def test_duplicate_text_mapping_is_not_guessed_and_unanswerable_can_have_no_evidence():
    paper, question = paper_fixture()
    paper["full_text"][0]["paragraphs"] *= 2
    with pytest.raises(ValueError, match="ambiguous_evidence"):
        qasper.convert_question("fixture", paper, question, qasper.paper_document("fixture", paper))
    question["answers"][0]["answer"].update(unanswerable=True, extractive_spans=[], evidence=[])
    row = qasper.convert_question("fixture", paper, question, qasper.paper_document("fixture", paper))
    assert row["reference"]["answers"] == [{"answer_type": "unanswerable", "answer": "Unanswerable", "evidence": []}]


def test_unanswerable_reference_evidence_is_empty_as_in_official_evaluator():
    paper, question = paper_fixture()
    question["answers"][0]["answer"].update(unanswerable=True, extractive_spans=[])
    row = qasper.convert_question("fixture", paper, question, qasper.paper_document("fixture", paper))
    assert row["reference"]["answers"][0]["evidence"] == []


def test_selection_is_order_independent_and_limits_contributions_per_paper():
    candidates = [{"id": f"Q{i}-{j}", "split": "test", "group_id": f"paper-{i}",
                   "answer_type": "extractive"} for i in range(3) for j in range(4)]
    quotas = {"test": {"extractive": 6}}
    selected = qasper.select_candidates(candidates, quotas)
    assert selected == qasper.select_candidates(list(reversed(candidates)), quotas)
    assert Counter(row["group_id"] for row in selected) == {"paper-0": 2, "paper-1": 2, "paper-2": 2}
    with pytest.raises(ValueError, match="Insufficient"):
        qasper.select_candidates(candidates, {"test": {"extractive": 7}})
    assert qasper.paper_identity("A Source: PAPER!") == qasper.paper_identity("a source paper")


def test_pinned_download_rejects_cache_drift_without_network(tmp_path, monkeypatch):
    cached = tmp_path / "source.bin"
    cached.write_bytes(b"changed")
    monkeypatch.setattr(qasper.requests, "get", lambda *a, **k: pytest.fail("No network expected"))
    with pytest.raises(ValueError, match="hash mismatch"):
        qasper.download_checked("https://example.invalid", cached, sha256(b"original").hexdigest())


def test_freezer_is_reproducible_from_verified_cache_and_refuses_overwrite(tmp_path, monkeypatch):
    paper, question = paper_fixture()
    candidates, _ = qasper.build_candidates({"fixture": paper})
    split = candidates[0]["split"]
    monkeypatch.setattr(qasper, "TYPE_QUOTAS", {split: {"extractive": 1}})
    # Default arguments intentionally capture the released quotas; override the
    # selector for this tiny archive while retaining its actual selection logic.
    select = qasper.select_candidates
    monkeypatch.setattr(qasper, "select_candidates", lambda rows: select(rows, {split: {"extractive": 1}}))
    cache = tmp_path / "cache"
    cache.mkdir()
    archive_path = cache / "qasper-train-dev-v0.3.tgz"
    with tarfile.open(archive_path, "w:gz") as archive:
        for name, value in [(qasper.MEMBER, json.dumps({"fixture": paper}).encode()),
                            ("README.md", b"Upstream description")]:
            info = tarfile.TarInfo(name)
            info.size = len(value)
            archive.addfile(info, io.BytesIO(value))
    monkeypatch.setattr(qasper, "ARCHIVE_SHA256", sha256(archive_path.read_bytes()).hexdigest())
    card = cache / f"qasper-card-{qasper.HF_REVISION}.md"
    card.write_bytes(b"CC BY 4.0")
    monkeypatch.setattr(qasper, "CARD_SHA256", sha256(card.read_bytes()).hexdigest())
    monkeypatch.setattr(qasper.requests, "get", lambda *a, **k: pytest.fail("No network expected"))
    first, second = tmp_path / "first", tmp_path / "second"
    qasper.freeze(first, cache)
    qasper.freeze(second, cache)
    for name in ("README.md", "LICENSE.md", "manifest.jsonl", "source.json"):
        assert b"\r\n" not in (first / name).read_bytes()
    assert {p.relative_to(first): p.read_bytes() for p in first.rglob("*") if p.is_file()} == {
        p.relative_to(second): p.read_bytes() for p in second.rglob("*") if p.is_file()}
    manifest = json.loads((first / "manifest.jsonl").read_text())
    input_path = first / manifest["input_path"].removeprefix("qasper/")
    assert sha256(input_path.read_bytes()).hexdigest() == manifest["input_sha256"]
    with pytest.raises(FileExistsError):
        qasper.freeze(first, cache)


def test_committed_slice_has_exact_quotas_valid_evidence_and_disjoint_paper_splits():
    root = SCRIPT.parents[1] / "data/benchmark/v1/qasper"
    rows = [json.loads(line) for line in (root / "manifest.jsonl").read_text(encoding="utf-8").splitlines()]
    assert Counter(row["split"] for row in rows) == {"dev": 6, "test": 20}
    groups = {}
    per_split_types = {"dev": Counter(), "test": Counter()}
    for row in rows:
        assert groups.setdefault(row["group_id"], row["split"]) == row["split"]
        task = json.loads((root / row["input_path"].removeprefix("qasper/")).read_text(encoding="utf-8"))
        reference = json.loads((root / row["reference_path"].removeprefix("qasper/")).read_text(encoding="utf-8"))
        block_ids = {block["id"] for block in task["documents"][0]["blocks"]}
        assert len(block_ids) == len(task["documents"][0]["blocks"])
        per_split_types[row["split"]][reference["answers"][0]["answer_type"]] += 1
        for answer in reference["answers"]:
            assert all(evidence["document_id"] == "P1" and evidence["block_id"] in block_ids
                       for evidence in answer["evidence"])
    assert per_split_types == qasper.TYPE_QUOTAS
    assert len(groups) == 26
