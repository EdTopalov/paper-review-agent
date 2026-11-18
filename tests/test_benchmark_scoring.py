"""Scripted offline checks for content scoring, missingness, and denominators."""

from copy import deepcopy

import pytest

from paper_review.benchmark_scoring import answer_f1, score_one, score_predictions


def task(task_id="Q1", kind="qa", group="paper-one", reference=None):
    references = {
        "qa": {"answers": [{"answer": "Alpha beta", "answer_type": "extractive",
                             "evidence": [{"document_id": "P1", "block_id": "b1"}]}]},
        "critique": {"verdict": "reliable", "error_types": []},
        "claim": {"verdict": "supported", "pair_id": "pair-one", "family": "cost",
                  "evidence": [{"document_id": "P1", "block_id": "b1"}]},
        "selection": {"acceptable_ids": ["P1"], "eligible_ids": ["P1"],
                      "base_set_id": "set-one", "order_id": 0},
    }
    public = {"id": task_id, "kind": kind, "instructions": "Assess the supplied source.",
              "documents": [{"id": "P1", "title": "Fixture", "blocks": [
                  {"id": "b1", "text": "Alpha beta provides the measured result."},
                  {"id": "b2", "text": "The alternative analysis is described here."}]}]}
    return {"id": task_id, "kind": kind, "track": {"qa": "qasper", "critique": "reviewcritique",
            "claim": "controlled", "selection": "selection"}[kind],
            "group_id": group, "input": public, "reference": deepcopy(reference or references[kind])}


def prediction(kind="qa", *, evidence=True, **updates):
    output = {"explanation": "The supplied source supports this conclusion.",
              "evidence": [{"document_id": "P1", "block_id": "b1", "quote": "Alpha beta"}] if evidence else []}
    output.update({"qa": {"answer": "Alpha beta"}, "critique": {"verdict": "reliable", "error_types": []},
                   "claim": {"verdict": "supported"}, "selection": {"selected_id": "P1", "tied_ids": []}}[kind])
    output.update(updates)
    return output


def record(item, variant="agent", repeat=1, **updates):
    output = {"id": item["id"], "variant": variant, "repeat": repeat, "status": "ok",
              "prediction": prediction(item["kind"]), "model": "scripted-fixture",
              "api_calls": 2, "input_tokens": 100, "output_tokens": 20,
              "cached_input_tokens": 10, "estimated_cost_usd": 0.02, "latency_seconds": 1.0}
    output.update(updates)
    return output


def test_official_answer_f1_and_independent_reference_maxima():
    assert answer_f1("The alpha, beta!", "beta alpha") == 1
    assert answer_f1("alpha", "alpha beta") == pytest.approx(2 / 3)
    assert answer_f1("!", "?") == 0  # QASPER's empty-token convention.
    item = task()
    item["reference"]["answers"].append({"answer": "A different answer", "answer_type": "extractive",
        "evidence": [{"document_id": "P1", "block_id": "b2"}]})
    proposed = prediction(evidence=False)
    proposed["evidence"] = [{"document_id": "P1", "block_id": "b2", "quote": "alternative analysis"}]
    row = score_one(item, proposed)
    assert row["answer_f1"] == row["evidence_f1"] == 1
    assert row["content_correct_with_verified_citation"]


def test_bad_locations_and_wrong_quotes_do_not_become_semantic_truth():
    item = task()
    proposed = prediction()
    proposed["evidence"][0]["block_id"] = "missing"
    row = score_one(item, proposed)
    assert row["content_correct"] and row["completed"]
    assert row["valid_citation_locations"] == row["verified_quotes"] == 0
    assert not row["content_correct_with_verified_citation"]
    wrong = prediction(answer="An incorrect answer")
    row = score_one(item, wrong)
    assert row["all_citations_verified"] and not row["content_correct"]


def test_unanswerable_can_be_correct_without_claiming_verified_evidence():
    item = task(reference={"answers": [{"answer": "Unanswerable", "answer_type": "unanswerable", "evidence": []}]})
    row = score_one(item, prediction(answer="Unanswerable", evidence=False))
    assert row["answer_f1"] == row["evidence_f1"] == 1
    assert row["answerability_correct"] and row["content_correct"]
    assert not row["all_citations_verified"] and not row["content_correct_with_verified_citation"]


def test_invalid_predictions_and_failed_runs_score_zero():
    item = task()
    malformed = prediction()
    malformed.pop("explanation")
    for row in (score_one(item, malformed), score_one(item, prediction(), "error"),
                score_one(item, prediction(explanation="  "))):
        assert not row["completed"] and not row["content_correct"] and row["content_score"] == 0
    duplicated = prediction()
    duplicated["evidence"] *= 2
    assert not score_one(item, duplicated)["prediction_valid"]


def test_fixed_binary_macro_f1_penalizes_majority_label_shortcut():
    first = task("R1", "critique")
    second = task("R2", "critique", group="paper-two", reference={"verdict": "deficient", "error_types": ["neglect"]})
    output = score_predictions([first, second], [record(first), record(second)])
    summary = output["variants"]["agent"]["tracks"]["reviewcritique"]
    assert summary["content_success_rate"] == 0.5
    assert summary["classification"]["macro_f1"] == pytest.approx(1 / 3)
    assert summary["classification"]["error_category_slices"]["neglect"]["content_success_rate"] == 0
    assert summary["mean_evidence_f1"] is None  # No fabricated RC gold spans.


def test_repetitions_include_failure_costs_and_pass_power_k():
    first, second = task("Q1"), task("Q2", group="paper-two")
    rows = [record(item, repeat=repeat) for item in (first, second) for repeat in (1, 2)]
    rows[1].update(status="error", prediction=None, estimated_cost_usd=0.06)
    output = score_predictions([first, second], rows, variants=["agent"], repeats=2)
    summary = output["variants"]["agent"]["tracks"]["qasper"]
    assert summary["attempts"] == 4 and summary["completed"] == 3
    assert summary["mean_content_score"] == .75
    assert summary["pass_power_k"] == {"1": .75, "2": .5}
    assert summary["mean_estimated_cost_usd"] == pytest.approx(.03)
    assert summary["per_repeat"]["2"]["content_success_rate"] == .5
    assert summary["per_group"]["paper-one"]["attempts"] == 2


@pytest.mark.parametrize("problem", ["missing", "duplicate", "unknown", "mixed_models", "repeat_gap", "invalid_repeat"])
def test_incomplete_or_incomparable_prediction_grids_are_rejected(problem):
    item = task()
    rows = [record(item), record(item, repeat=2)]
    kwargs = {"variants": ["agent"], "repeats": 2}
    if problem == "missing":
        rows.pop()
    elif problem == "duplicate":
        rows.append(deepcopy(rows[0]))
    elif problem == "unknown":
        rows[0]["id"] = "UNKNOWN"
    elif problem == "mixed_models":
        rows[1]["model"] = "another-model"
    elif problem == "repeat_gap":
        rows[1]["repeat"] = 3
        kwargs.pop("repeats")
    else:
        rows[1]["repeat"] = True
    with pytest.raises(ValueError):
        score_predictions([item], rows, **kwargs)


@pytest.mark.parametrize("model", [None, "", " \t ", 17, [], {}])
def test_invalid_model_identities_are_rejected(model):
    item = task()
    with pytest.raises(ValueError, match="model identity"):
        score_predictions([item], [record(item, model=model)])


def test_absent_model_identity_is_rejected():
    item = task()
    row = record(item)
    row.pop("model")
    with pytest.raises(ValueError, match="model identity"):
        score_predictions([item], [row])


def test_controlled_pair_accuracy_requires_both_correct():
    tasks = [task(f"C{index}", "claim", group="synthetic-cost", reference={
        "verdict": "supported" if index % 2 else "contradicted", "pair_id": f"pair-{(index - 1) // 2}",
        "family": "cost", "evidence": [{"document_id": "P1", "block_id": "b1"}]}) for index in range(1, 5)]
    rows = [record(item, prediction=prediction("claim", verdict=item["reference"]["verdict"])) for item in tasks]
    rows[-1]["prediction"]["verdict"] = "supported"
    summary = score_predictions(tasks, rows)["variants"]["agent"]["tracks"]["controlled"]
    assert summary["content_success_rate"] == .75
    assert summary["pair_accuracy"] == {"complete_pair_attempts": 2, "incomplete_pair_attempts": 0,
                                         "both_correct": 1, "rate": .5}


def test_selection_ties_abstention_and_order_metrics():
    tasks = [task("S1", "selection"), task("S2", "selection", reference={
        "acceptable_ids": [], "eligible_ids": [], "base_set_id": "set-two", "order_id": 1})]
    rows = [record(tasks[0]), record(tasks[1], prediction=prediction("selection", selected_id=None, evidence=False))]
    summary = score_predictions(tasks, rows)["variants"]["agent"]["tracks"]["selection"]
    assert summary["content_success_rate"] == 1
    assert summary["correct_tie_sets"] == 2
    assert set(summary["per_order"]) == {"0", "1"}
    assert summary["per_candidate_count"]["1"]["attempts"] == 2
    assert not score_one(tasks[0], prediction("selection", selected_id="unknown"))["prediction_valid"]


def test_selection_tie_set_includes_selected_candidate():
    item = task("S1", "selection", reference={"acceptable_ids": ["P1", "P2"],
        "eligible_ids": ["P1", "P2"], "base_set_id": "tied-set", "order_id": 0})
    item["input"]["documents"].append({"id": "P2", "title": "Alternative", "blocks": [
        {"id": "b1", "text": "Both candidates satisfy the same selection profile."}]})
    assert score_one(item, prediction("selection", tied_ids=["P1", "P2"]))["ties_correct"]
    assert not score_one(item, prediction("selection", tied_ids=[]))["ties_correct"]
    unique = task("S2", "selection")
    assert score_one(unique, prediction("selection", tied_ids=[]))["ties_correct"]
    assert score_one(unique, prediction("selection", tied_ids=["P1"]))["ties_correct"]


def test_accounting_unknowns_stay_unknown_and_invalid_values_rejected():
    item = task()
    rows = [record(item)]
    rows[0].pop("estimated_cost_usd")
    summary = score_predictions([item], rows)["variants"]["agent"]["tracks"]["qasper"]
    assert summary["mean_estimated_cost_usd"] is None
    assert summary["unknown_estimated_cost_usd_attempts"] == 1
    rows[0]["estimated_cost_usd"] = -1
    with pytest.raises(ValueError, match="accounting"):
        score_predictions([item], rows)


def test_controller_accounting_includes_failed_attempts():
    item = task()
    rows = [record(item, repeat=1), record(item, repeat=2)]
    rows[0].update(decision_steps=2, reading_actions=1, tool_calls=2)
    rows[1].update(status="error", prediction=None, decision_steps=8,
                   reading_actions=5, tool_calls=7)
    summary = score_predictions([item], rows)["variants"]["agent"]["tracks"]["qasper"]
    assert summary["mean_decision_steps"] == 5
    assert summary["mean_reading_actions"] == 3
    assert summary["mean_tool_calls"] == 4.5
    assert summary["known_total_decision_steps"] == 10


def test_paired_comparisons_use_groups_not_repeated_attempts():
    tasks = [task("Q1"), task("Q2", group="paper-two")]
    rows = [record(item, variant=variant, repeat=repeat) for item in tasks
            for variant in ("agent", "baseline") for repeat in (1, 2)]
    output = score_predictions(tasks, rows)
    comparison = output["paired_comparisons"][0]
    assert comparison["content_success_rate"]["tasks"] == 2
    assert comparison["content_success_rate"]["ci95"] == [0, 0]
    assert "paper" in comparison["unit"]
