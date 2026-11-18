"""Offline checks of synthetic ground truth, source rendering, and split units."""

from collections import Counter, defaultdict
from copy import deepcopy
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import statistics

import pytest


PATH = Path(__file__).resolve().parents[1] / "scripts/prepare_controlled_benchmark.py"
SPEC = importlib.util.spec_from_file_location("prepare_controlled_benchmark", PATH)
generator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(generator)


def test_pairs_have_one_decisive_edit_and_opposite_oracle_answers():
    groups = defaultdict(list)
    for split, group_id, public, reference in generator.controlled_cases():
        groups[reference["pair_id"]].append((split, group_id, public, reference))
    assert len(groups) == 16
    assert Counter(rows[0][0] for rows in groups.values()) == {"dev": 4, "test": 12}
    changed_blocks = {"confidence_interval": "b0004", "total_cost": "b0007",
                      "independent_evaluation": "b0007", "language_scope": "b0004",
                      "seed_aggregation": "b0001", "appendix_comparison": "b0007"}
    for rows in groups.values():
        (split_a, group_a, a, reference_a), (split_b, group_b, b, reference_b) = rows
        assert split_a == split_b and group_a == group_b
        assert a["statement"] == b["statement"]
        assert a["instructions"] == b["instructions"]
        assert reference_a["verdict"] != reference_b["verdict"]
        changed = [left["id"] for left, right in zip(a["documents"][0]["blocks"], b["documents"][0]["blocks"], strict=True)
                   if left != right]
        assert changed == [changed_blocks[reference_a["family"]]]


def test_reference_evidence_exists_and_labels_are_recomputed_from_records():
    labels = Counter()
    families = defaultdict(set)
    for split, group_id, public, reference in generator.controlled_cases():
        assert reference["verdict"] == generator.claim_oracle(reference["family"], reference["facts"])
        locations = {(document["id"], block["id"]) for document in public["documents"] for block in document["blocks"]}
        assert all((item["document_id"], item["block_id"]) in locations for item in reference["evidence"])
        assert reference["evidence"]
        labels[reference["verdict"]] += 1
        families[group_id].add(split)
        assert not {"facts", "verdict", "family", "condition", "pair_id", "label_origin"} & public.keys()
    assert set(labels) == {"supported", "contradicted", "insufficient"}
    assert labels["supported"] == 16  # A blanket criticism strategy cannot pass.
    assert all(len(splits) == 1 for splits in families.values())


def test_oracles_handle_uncertainty_total_expense_and_missing_counterevidence():
    assert generator.claim_oracle("confidence_interval", {"interval95": [-.4, .9]}) == "insufficient"
    assert generator.claim_oracle("confidence_interval", {"interval95": [-1.4, -.1]}) == "contradicted"
    assert generator.claim_oracle("total_cost", {"new_preparation_usd": 200, "new_inference_usd": 5,
                                                  "baseline_preparation_usd": 0, "baseline_inference_usd": 150}) == "contradicted"
    assert generator.claim_oracle("appendix_comparison", {"additional_quantitative_problems": 12}) == "contradicted"
    assert generator.claim_oracle("appendix_comparison", {"additional_quantitative_problems": 0}) == "supported"


def test_language_claim_targets_accuracy_without_equating_missing_tests_with_negative_results():
    cases = [row for row in generator.controlled_cases() if row[3]["family"] == "language_scope"]
    assert len(cases) == 6
    for _, _, public, reference in cases:
        facts = reference["facts"]
        assert "higher accuracy" in public["statement"]
        assert "supplies direct evaluation evidence" not in public["statement"]
        assert facts["new_accuracy"] > facts["baseline_accuracy"]
        results = public["documents"][0]["blocks"][3]["text"]
        assert f"baseline accuracy is {facts['baseline_accuracy']}%" in results
        assert f"new method's accuracy is {facts['new_accuracy']}%" in results
        if reference["verdict"] == "supported":
            assert facts["tested_languages"] == ["English", "German", "Spanish"]
            assert "Evaluation languages are exactly: English, German, Spanish." in results
        else:
            assert reference["verdict"] == "insufficient"
            assert facts["tested_languages"] == ["English"]
            assert "Evaluation languages are exactly: English." in results
            assert "No other language evaluation was conducted." in results


def test_selection_oracle_has_unique_tied_and_empty_choices():
    cases = generator.selection_cases()
    assert len(cases) == 18
    bases = {}
    for split, group, public, reference in cases:
        bases.setdefault(reference["base_set_id"], reference)
        assert reference["acceptable_ids"] == generator.selection_oracle(reference["facts"], reference["profile"])["acceptable_ids"]
        assert reference["eligible_ids"] == generator.selection_oracle(reference["facts"], reference["profile"])["eligible_ids"]
        document_ids = {row["id"] for row in public["documents"]}
        assert set(reference["acceptable_ids"]) <= set(reference["eligible_ids"]) <= document_ids
        assert not {"acceptable_ids", "eligible_ids", "facts", "profile", "family", "order_id", "base_set_id"} & public.keys()
    assert len(bases["equal_candidates"]["acceptable_ids"]) == 2
    assert bases["no_eligible_candidate"]["acceptable_ids"] == []
    assert all(len(row["acceptable_ids"]) == 1 for key, row in bases.items()
               if key not in {"equal_candidates", "no_eligible_candidate"})
    assert set(len(row["facts"]) for row in bases.values()) == {3, 6, 9}


def test_selection_orders_preserve_facts_but_move_the_unique_winner():
    groups = defaultdict(list)
    for split, group_id, public, reference in generator.selection_cases():
        groups[group_id].append((split, public, reference))
    assert len(groups) == 6
    for rows in groups.values():
        assert len(rows) == 3 and len({row[0] for row in rows}) == 1
        assert all(row[2]["facts"] == rows[0][2]["facts"] for row in rows)
        assert all(row[2]["acceptable_ids"] == rows[0][2]["acceptable_ids"] for row in rows)
        assert len({tuple(document["id"] for document in row[1]["documents"]) for row in rows}) == 3
        if len(rows[0][2]["acceptable_ids"]) == 1:
            winner = rows[0][2]["acceptable_ids"][0]
            positions = [next(index for index, document in enumerate(public["documents"]) if document["id"] == winner)
                         for _, public, _ in rows]
            count = len(rows[0][1]["documents"])
            assert positions == [0, count // 2, count - 1]


def test_selection_references_describe_the_rendered_resources_and_seeds():
    for _, _, public, reference in generator.selection_cases():
        source = {row["id"]: row for row in reference["facts"]}
        for document in public["documents"]:
            facts = source[document["id"]]
            blocks = {row["id"]: row["text"] for row in document["blocks"]}
            assert f"{facts['peak_gpu_gb']} GB" in blocks["b0003"]
            assert f"supplies {facts['reported_seeds']}" in blocks["b0004"]
            if reference["profile"] == "critique" and facts["id"] in reference["eligible_ids"]:
                assert facts["headline_accuracy"] > statistics.mean(facts["seed_accuracies"])
                assert str(facts["headline_accuracy"]) in blocks["b0001"]


def test_selection_oracle_never_uses_undisclosed_seed_values():
    candidate = generator.candidate_record("hidden-seeds", 0)
    candidate["reported_seeds"] = 1
    candidate["headline_accuracy"] = max(candidate["seed_accuracies"])
    assert generator.selection_oracle([candidate], "critique")["eligible_ids"] == []
    candidate["reported_seeds"] = 5
    candidate["seed_accuracies"] = [70]
    assert generator.selection_oracle([candidate], "replication")["eligible_ids"] == []


def test_preparation_is_reproducible_hash_bound_and_preserves_existing_artifacts(tmp_path):
    counts = generator.prepare(tmp_path)
    assert counts["controlled"]["cases"] == 32
    assert counts["selection"]["cases"] == 18
    before = {path.relative_to(tmp_path).as_posix(): path.read_bytes() for path in tmp_path.rglob("*") if path.is_file()}
    generator.prepare(tmp_path)
    after = {path.relative_to(tmp_path).as_posix(): path.read_bytes() for path in tmp_path.rglob("*") if path.is_file()}
    assert before == after
    for manifest in tmp_path.glob("*/manifest.jsonl"):
        rows = [json.loads(line) for line in manifest.read_text(encoding="utf-8").splitlines()]
        for row in rows:
            for name in ("input", "reference"):
                assert sha256((tmp_path / row[name + "_path"]).read_bytes()).hexdigest() == row[name + "_sha256"]
    first = next((tmp_path / "controlled/inputs").glob("*.json"))
    first.write_text("tampered", encoding="utf-8")
    with pytest.raises(ValueError, match="Existing frozen artifact differs"):
        generator.prepare(tmp_path)
