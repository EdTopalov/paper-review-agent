"""Offline checks for ReviewCritique source preservation and split integrity."""

from collections import Counter
import importlib.util
import json
from pathlib import Path

import pytest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/prepare_reviewcritique.py"
SPEC = importlib.util.spec_from_file_location("prepare_reviewcritique", SCRIPT)
prepare = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prepare)
FROZEN = SCRIPT.parent.parent / "data/benchmark/v1/reviewcritique"


def segment(text, reliability="Yes", **updates):
    row = {"segment_text": text, "reliability": reliability,
           "topic_class_1": "Weakness", "topic_class_2": "Experiments",
           "error_type": float("nan"), "explanation": float("nan")}
    row.update(updates)
    return row


def test_title_partition_is_canonical_and_deterministic():
    assert prepare.paper_identity("  A Study: OF Models!") == prepare.paper_identity("a study of models")
    group, split = prepare.paper_identity("A Study of Models")
    assert group.startswith("paper-") and split in {"dev", "test"}


def test_filter_discards_headings_context_dependent_labels_and_bad_values():
    text = "The experiment reports several conditions but it is unclear which independent examples were used in evaluation."
    rows = [segment(text), segment(17), segment("Summary:", topic_class_2="Section title"),
            segment(text + " Other.", "No", error_type="Contradiction", explanation="Contradicts another review paragraph."),
            segment(text + " Again.", "No", error_type="Misunderstanding", explanation=float("nan")),
            segment(text + " Context.", "No", error_type="Neglect", explanation="This is stated in the other comments."),
            segment(text + " Source.", "No", error_type="Neglect", explanation="Section 4 lists the independent test examples.")]
    counters = Counter()
    result = prepare.substantive_segments({"review#1": {"review": rows}}, counters)
    assert len(result) == 2
    assert [row["verdict"] for row in result] == ["reliable", "deficient"]
    assert counters["outside_factual_slice"] == counters["missing_expert_explanation"] == 1
    assert counters["external_or_review_context"] == 1


def test_conflicting_repeated_annotations_are_excluded():
    text = "The experiment does not state how many examples are used for independent evaluation on the target task."
    paper = {"review#1": {"review": [segment(text)]},
             "review#2": {"review": [segment(text, "No", error_type="Neglect", explanation="Section 4 gives this count.")]}}
    counters = Counter()
    assert prepare.substantive_segments(paper, counters) == []
    assert counters["conflicting_repeated_segment"] == 2


def test_document_blocks_preserve_order_and_source_text_without_labels():
    text = "  First paragraph.\n\n" + "x" * 8001 + "\n\nLast paragraph.  "
    blocks = prepare.paper_blocks(text)
    assert [row["id"] for row in blocks] == ["b0001", "b0002", "b0003", "b0004"]
    assert [len(row["text"]) for row in blocks] == [16, 8000, 1, 15]
    assert all(row["text"] in text for row in blocks)


def test_frozen_dataset_is_balanced_hash_bound_and_label_free():
    manifests = [json.loads(line) for line in (FROZEN / "manifest.jsonl").read_text(encoding="utf-8").splitlines()]
    assert Counter(row["split"] for row in manifests) == {"dev": 6, "test": 20}
    groups, verdicts = {}, Counter()
    for row in manifests:
        source = FROZEN / "inputs" / Path(row["input_path"]).name
        target = FROZEN / "references" / Path(row["reference_path"]).name
        assert prepare.digest_bytes(source.read_bytes()) == row["input_sha256"]
        assert prepare.digest_bytes(target.read_bytes()) == row["reference_sha256"]
        item = json.loads(source.read_text(encoding="utf-8"))
        reference = json.loads(target.read_text(encoding="utf-8"))
        assert item["id"] == reference["id"] == row["id"]
        assert set(item) == {"id", "kind", "instructions", "comment", "comment_context", "documents"}
        assert item["comment"] in item["comment_context"]
        assert all(isinstance(text, str) for text in item["comment_context"])
        assert "expert_explanation" not in item and "verdict" not in item
        assert len(item["documents"]) == 1 and item["documents"][0]["blocks"]
        assert reference["label_origin"] == "reviewcritique_expert"
        assert (reference["expert_explanation"] is not None) == (reference["verdict"] == "deficient")
        group, split = prepare.paper_identity(item["documents"][0]["title"])
        assert row["group_id"] == group and row["split"] == split
        groups.setdefault(group, set()).add(split)
        verdicts[row["split"], reference["verdict"]] += 1
    assert len(groups) == 13 and all(len(splits) == 1 for splits in groups.values())
    assert verdicts == {("dev", "reliable"): 3, ("dev", "deficient"): 3,
                        ("test", "reliable"): 10, ("test", "deficient"): 10}


def test_missing_balanced_papers_raise_instead_of_fabricating_data():
    with pytest.raises(ValueError, match="balanced"):
        prepare.select_papers([], test_papers=1, dev_papers=0)


def test_freezer_writes_lf_manifest_and_preserves_upstream_notice_bytes(tmp_path, monkeypatch):
    title = "A Study of Models"
    paper = {"title": title, "body_text": "The evaluation uses independent held-out examples. " * 100,
             "review#1": {"review": [
                 segment("The paper does not make clear whether its independent evaluation includes enough examples to support its reported conclusion."),
                 segment("The paper does not state any information about the size of the held-out evaluation sample used for this experiment.",
                         "No", error_type="Misunderstanding", explanation="Section 4 states the held-out sample size.")]}}
    source = tmp_path / "source.jsonl"
    source.write_text(json.dumps(paper) + "\n", encoding="utf-8", newline="\n")
    notice = tmp_path / "notice"
    notice.write_bytes(b"Pinned upstream notice\r\n")
    sources = {name: {"path": source if name.startswith("data/") else notice,
                      "url": "https://example.invalid/source", "sha256": "fixture", "bytes": 1}
               for name in prepare.SOURCE_FILES}
    monkeypatch.setattr(prepare, "fetch_sources", lambda cache: sources)
    split = prepare.paper_identity(title)[1]
    out = tmp_path / "frozen"
    prepare.freeze(out, tmp_path / "unused-cache", test_papers=int(split == "test"), dev_papers=int(split == "dev"))
    assert b"\r\n" not in (out / "manifest.jsonl").read_bytes()
    assert (out / "LICENSE").read_bytes() == notice.read_bytes()
    assert (out / "UPSTREAM_README.md").read_bytes() == notice.read_bytes()
