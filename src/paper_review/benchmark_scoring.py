"""Offline content, evidence, and reliability scoring for frozen benchmark tasks.

QASPER answer normalization follows the official SQuAD-style token-F1 convention:
https://github.com/allenai/qasper-led-baseline . This implementation is original.
Reference labels never enter model-facing task inputs through this module.
"""

from collections import Counter, defaultdict
from itertools import combinations
from math import comb, isfinite
import re
import statistics
import string

import jsonschema

from .citations import check_quote
from .evaluation import _paired_interval


def _tokens(text):
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    return re.sub(r"\b(a|an|the)\b", " ", text).split()


def answer_f1(predicted, expected):
    """Bag-of-token F1, maximizing over human references at the call site."""
    predicted, expected = _tokens(predicted), _tokens(expected)
    if not predicted or not expected:
        return 0.0
    overlap = sum((Counter(predicted) & Counter(expected)).values())
    return 2 * overlap / (len(predicted) + len(expected))


def _location(item):
    return item["document_id"], item["block_id"]


def _set_f1(predicted, expected):
    predicted, expected = set(predicted), set(expected)
    if not predicted or not expected:
        return float(predicted == expected)
    return 2 * len(predicted & expected) / (len(predicted) + len(expected))


def _citation_checks(task, evidence):
    blocks = {(document["id"], block["id"]): block["text"]
              for document in task["input"]["documents"] for block in document["blocks"]}
    checks = []
    for citation in evidence:
        source = blocks.get(_location(citation))
        valid = source is not None
        check = check_quote([source], 1, citation["quote"]) if valid else {
            "citation_verified": False, "status": "invalid_location"}
        checks.append({"document_id": citation["document_id"], "block_id": citation["block_id"],
                       "location_valid": valid, "quote_verified": check["citation_verified"],
                       "status": check["status"]})
    return checks


def score_one(task, prediction, status="ok"):
    """Score one attempt; syntax, content correctness, and citations stay separate.

    A correctly located quotation does not establish semantic support. Content
    correctness means agreement with the task's reference, not overall review
    quality. Schema-invalid outputs and failed runs receive zero content score.
    """
    from .benchmark_tasks import validate_prediction

    reference, kind = task["reference"], task["kind"]
    row = {"id": task["id"], "track": task["track"], "group_id": task["group_id"],
           "kind": kind, "completed": False, "prediction_valid": False,
           "content_score": 0.0, "content_correct": False, "citation_count": 0,
           "valid_citation_locations": 0, "verified_quotes": 0,
           "all_citations_verified": False, "content_correct_with_verified_citation": False,
           "answer_f1": 0.0 if kind == "qa" else None,
           "evidence_f1": 0.0 if kind == "qa" or "evidence" in reference else None,
           "citation_checks": []}
    if kind == "critique":
        row.update(expected_label=reference["verdict"], predicted_label="invalid",
                   error_types=reference.get("error_types", []), predicted_error_types=[])
    elif kind == "claim":
        row.update(expected_label=reference["verdict"], predicted_label="invalid",
                   pair_id=reference.get("pair_id"), family=reference.get("family"))
    elif kind == "selection":
        row.update(selected_id=None, tied_ids=[], ties_correct=False, eligibility_violation=False,
                   order_id=reference.get("order_id"), base_set_id=reference.get("base_set_id", task["group_id"]),
                   candidate_count=len(task["input"]["documents"]))
    elif kind == "qa":
        row.update(answer_types=sorted({answer["answer_type"] for answer in reference["answers"]}),
                   answerability_correct=False)
    else:
        raise ValueError(f"Unknown benchmark kind: {kind}")
    if status != "ok":
        row["failure"] = "run_failed"
        return row
    try:
        validate_prediction(task["input"], prediction)
    except (jsonschema.ValidationError, TypeError, ValueError):
        row["failure"] = "invalid_prediction"
        return row
    row.update(completed=True, prediction_valid=True)
    evidence = prediction["evidence"]
    checks = _citation_checks(task, evidence)
    row.update(citation_count=len(checks), citation_checks=checks,
               valid_citation_locations=sum(check["location_valid"] for check in checks),
               verified_quotes=sum(check["quote_verified"] for check in checks),
               all_citations_verified=bool(checks) and all(check["quote_verified"] for check in checks))
    if kind == "qa":
        answers = reference["answers"]
        row["answer_f1"] = max(answer_f1(prediction["answer"], answer["answer"]) for answer in answers)
        row["content_score"] = row["answer_f1"]
        row["evidence_f1"] = max(_set_f1(map(_location, evidence), map(_location, answer.get("evidence", [])))
                                 for answer in answers)
        row["answerability_correct"] = (_tokens(prediction["answer"]) == ["unanswerable"]) == all(
            answer["answer_type"] == "unanswerable" for answer in answers)
    elif kind in ("critique", "claim"):
        row["predicted_label"] = prediction["verdict"]
        row["content_score"] = float(prediction["verdict"] == reference["verdict"])
        if kind == "critique":
            row["predicted_error_types"] = prediction["error_types"]
        if "evidence" in reference:
            row["evidence_f1"] = _set_f1(map(_location, evidence), map(_location, reference["evidence"]))
    else:
        selected, acceptable = prediction["selected_id"], set(reference["acceptable_ids"])
        predicted_best = ({selected} if selected is not None else set()) | set(prediction["tied_ids"])
        row.update(selected_id=selected, tied_ids=prediction["tied_ids"],
                   content_score=float(selected in acceptable if acceptable else selected is None),
                   ties_correct=predicted_best == acceptable,
                   eligibility_violation=selected is not None and selected not in reference["eligible_ids"])
    row["content_correct"] = row["content_score"] == 1.0
    row["content_correct_with_verified_citation"] = row["content_correct"] and row["all_citations_verified"]
    return row


def _mean(values):
    values = [value for value in values if value is not None]
    return statistics.mean(values) if values else None


def _accounting(rows):
    result = {}
    for field in ("decision_steps", "reading_actions", "tool_calls", "api_calls",
                  "input_tokens", "output_tokens", "cached_input_tokens",
                  "estimated_cost_usd", "latency_seconds"):
        values = [row["usage"].get(field) for row in rows]
        known = [value for value in values if value is not None]
        for value in known:
            if not isinstance(value, (int, float)) or isinstance(value, bool) or not isfinite(value) or value < 0:
                raise ValueError(f"Invalid nonnegative accounting field: {field}")
        result[f"mean_{field}"] = statistics.mean(known) if len(known) == len(rows) else None
        result[f"known_total_{field}"] = sum(known)
        result[f"unknown_{field}_attempts"] = len(values) - len(known)
    result["billing_uncertain_attempts"] = sum(bool(row["usage"].get("billing_uncertain")) for row in rows)
    return result


def _classification(rows):
    labels = ("reliable", "deficient")
    confusion = {actual: {predicted: 0 for predicted in (*labels, "invalid")} for actual in labels}
    for row in rows:
        confusion[row["expected_label"]][row["predicted_label"]] += 1
    metrics = {}
    for label in labels:
        true_positive = confusion[label][label]
        predicted_count = sum(confusion[actual][label] for actual in labels)
        actual_count = sum(confusion[label].values())
        precision = true_positive / predicted_count if predicted_count else 0.0
        recall = true_positive / actual_count if actual_count else 0.0
        metrics[label] = {"true_positive": true_positive, "predicted": predicted_count, "actual": actual_count,
                          "precision": precision, "recall": recall,
                          "f1": 2 * precision * recall / (precision + recall) if precision + recall else 0.0}
    categories = sorted({category for row in rows for category in row["error_types"]})
    return {"labels": list(labels), "confusion": confusion, "per_class": metrics,
            "macro_f1": statistics.mean(value["f1"] for value in metrics.values()),
            "error_category_slices": {category: {
                "attempts": sum(category in row["error_types"] for row in rows),
                "content_success_rate": statistics.mean(row["content_correct"] for row in rows if category in row["error_types"]),
                "named_category_recall": statistics.mean(
                    row["completed"] and category in row["predicted_error_types"] for row in rows if category in row["error_types"])}
                for category in categories}}


def _summary(rows):
    result = {"attempts": len(rows), "distinct_tasks": len({row["id"] for row in rows}),
              "groups": len({row["group_id"] for row in rows}),
              "completed": sum(row["completed"] for row in rows),
              "completion_rate": statistics.mean(row["completed"] for row in rows),
              "content_correct": sum(row["content_correct"] for row in rows),
              "content_success_rate": statistics.mean(row["content_correct"] for row in rows),
              "mean_content_score": statistics.mean(row["content_score"] for row in rows),
              "mean_answer_f1": _mean(row["answer_f1"] for row in rows),
              "mean_evidence_f1": _mean(row["evidence_f1"] for row in rows),
              "citation_count": sum(row["citation_count"] for row in rows),
              "valid_citation_locations": sum(row["valid_citation_locations"] for row in rows),
              "verified_quotes": sum(row["verified_quotes"] for row in rows),
              "attempts_with_all_citations_verified": sum(row["all_citations_verified"] for row in rows),
              "content_correct_with_verified_citation": sum(row["content_correct_with_verified_citation"] for row in rows),
              **_accounting(rows)}
    result["quote_verification_rate"] = result["verified_quotes"] / result["citation_count"] if result["citation_count"] else None
    if rows[0]["kind"] == "critique":
        result["classification"] = _classification(rows)
    if rows[0]["kind"] == "qa":
        result["answerability_accuracy"] = statistics.mean(row["answerability_correct"] for row in rows)
        result["answer_type_slices"] = {answer_type: {
            "attempts": sum(answer_type in row["answer_types"] for row in rows),
            "mean_answer_f1": statistics.mean(row["answer_f1"] for row in rows if answer_type in row["answer_types"]),
            "mean_evidence_f1": statistics.mean(row["evidence_f1"] for row in rows if answer_type in row["answer_types"])}
            for answer_type in sorted({value for row in rows for value in row["answer_types"]})}
    if rows[0]["kind"] == "selection":
        result.update(eligibility_violations=sum(row["eligibility_violation"] for row in rows),
                      correct_tie_sets=sum(row["ties_correct"] for row in rows))
    return result


def _repetition_ids(repeats, observed):
    if repeats is None:
        values = list(observed)
    elif type(repeats) is int:
        if repeats < 1:
            raise ValueError("Repeats must be positive")
        values = list(range(1, repeats + 1))
    else:
        values = list(repeats)
    if not values or len(set(values)) != len(values) or any(type(value) is not int or value < 1 for value in values):
        raise ValueError("Choose distinct positive repetition IDs")
    if repeats is None and set(values) != set(range(1, max(values) + 1)):
        raise ValueError("Incomplete inferred repetition grid")
    return sorted(values)


def score_predictions(tasks, records, *, variants=None, repeats=None):
    """Require every selected task/variant/repetition; retain failed attempts.

    Unknown optional usage stays unknown. Per-track rates average attempts;
    pass^k averages task-level C(s,k)/C(n,k). Cluster intervals resample complete
    source-paper/study-family means rather than treating repeats as new papers.
    """
    tasks, records = list(tasks), list(records)
    indexed_tasks = {task["id"]: task for task in tasks}
    if not tasks or len(indexed_tasks) != len(tasks):
        raise ValueError("Choose a nonempty distinct task set")
    if not records:
        raise ValueError("No prediction records; no benchmark results exist")
    if any(not isinstance(record, dict) for record in records):
        raise ValueError("Prediction records must be JSON objects")
    if any(not isinstance(record.get("variant"), str) or not record["variant"].strip()
           or type(record.get("repeat")) is not int or record["repeat"] < 1 for record in records):
        raise ValueError("Prediction records need variant names and positive integer repetitions")
    observed_variants = {record.get("variant") for record in records}
    variants = sorted(observed_variants) if variants is None else list(variants)
    if not variants or any(not isinstance(value, str) or not value.strip() for value in variants) or len(set(variants)) != len(variants):
        raise ValueError("Choose distinct nonempty variant names")
    repeat_ids = _repetition_ids(repeats, {record.get("repeat") for record in records})
    if any(not isinstance(record.get("model"), str) or not record["model"].strip() for record in records):
        raise ValueError("Every prediction record needs a nonempty string model identity")
    models = {record["model"] for record in records}
    if len(models) != 1:
        raise ValueError("Do not pool different or missing model identities")
    indexed_records = {}
    for record in records:
        key = record.get("id"), record.get("variant"), record.get("repeat")
        if key in indexed_records:
            raise ValueError(f"Duplicate prediction cell: {key}")
        if key[0] not in indexed_tasks or key[1] not in variants or key[2] not in repeat_ids:
            raise ValueError(f"Unknown task, variant, or repetition: {key}")
        if type(key[2]) is not int or record.get("status") not in {"ok", "error"}:
            raise ValueError("Prediction records need a positive integer repeat and ok/error status")
        indexed_records[key] = record
    expected = {(task_id, variant, repeat) for task_id in indexed_tasks for variant in variants for repeat in repeat_ids}
    if set(indexed_records) != expected:
        raise ValueError(f"Incomplete prediction grid: {len(expected - indexed_records.keys())} missing cells")
    scored = []
    for key, record in sorted(indexed_records.items()):
        row = score_one(indexed_tasks[key[0]], record.get("prediction"), record["status"])
        row.update(variant=key[1], repeat=key[2], usage={field: record[field] for field in (
            "decision_steps", "reading_actions", "tool_calls", "api_calls",
            "input_tokens", "output_tokens", "cached_input_tokens", "estimated_cost_usd",
            "latency_seconds", "billing_uncertain") if field in record})
        scored.append(row)
    output = {}
    for variant in variants:
        variant_rows = [row for row in scored if row["variant"] == variant]
        tracks = {}
        for track in sorted({row["track"] for row in variant_rows}):
            rows = [row for row in variant_rows if row["track"] == track]
            by_task = {task_id: [row for row in rows if row["id"] == task_id] for task_id in sorted({row["id"] for row in rows})}
            per_group = {group: _summary([row for row in rows if row["group_id"] == group])
                         for group in sorted({row["group_id"] for row in rows})}
            summary = {**_summary(rows),
                       "per_repeat": {str(repeat): _summary([row for row in rows if row["repeat"] == repeat]) for repeat in repeat_ids},
                       "per_group": per_group,
                       "pass_power_k": {str(k): statistics.mean(comb(sum(row["content_correct"] for row in values), k) / comb(len(values), k)
                                                               for values in by_task.values()) for k in range(1, len(repeat_ids) + 1)},
                       "mean_group_content_score": statistics.mean(row["mean_content_score"] for row in per_group.values())}
            if rows[0]["kind"] == "claim":
                pairs = defaultdict(list)
                for row in rows:
                    if row.get("pair_id"):
                        pairs[row["pair_id"], row["repeat"]].append(row)
                complete_pairs = [pair for pair in pairs.values() if len(pair) == 2]
                summary["pair_accuracy"] = {"complete_pair_attempts": len(complete_pairs),
                    "incomplete_pair_attempts": sum(len(pair) != 2 for pair in pairs.values()),
                    "both_correct": sum(all(row["content_correct"] for row in pair) for pair in complete_pairs),
                    "rate": statistics.mean(all(row["content_correct"] for row in pair) for pair in complete_pairs) if complete_pairs else None}
            if rows[0]["kind"] == "selection":
                summary["per_order"] = {str(order): _summary([row for row in rows if row["order_id"] == order])
                                        for order in sorted({row["order_id"] for row in rows}, key=str)}
                summary["per_candidate_count"] = {str(count): _summary([row for row in rows if row["candidate_count"] == count])
                                                  for count in sorted({row["candidate_count"] for row in rows})}
                ordered_sets = defaultdict(list)
                for row in rows:
                    ordered_sets[row["base_set_id"], row["repeat"]].append(row)
                summary["order_consistency"] = [{"base_set_id": base, "repeat": repeat, "orders": len(values),
                    "all_orders_correct": all(row["content_correct"] for row in values),
                    "same_choice": len({row["selected_id"] for row in values}) == 1 if all(row["completed"] for row in values) else None}
                    for (base, repeat), values in sorted(ordered_sets.items())]
            tracks[track] = summary
        output[variant] = {"attempts": len(variant_rows), "tracks": tracks}
    paired = []
    for left, right in combinations(sorted(variants), 2):
        for track in sorted(output[left]["tracks"]):
            left_groups, right_groups = output[left]["tracks"][track]["per_group"], output[right]["tracks"][track]["per_group"]
            paired.append({"left": left, "right": right, "track": track,
                "unit": "source paper or synthetic study family", "direction": f"{left} minus {right}",
                "content_success_rate": _paired_interval([left_groups[group]["content_success_rate"] - right_groups[group]["content_success_rate"]
                                                         for group in sorted(left_groups)]),
                "mean_content_score": _paired_interval([left_groups[group]["mean_content_score"] - right_groups[group]["mean_content_score"]
                                                       for group in sorted(left_groups)])})
    return {"schema_version": "benchmark-score-v1", "model": next(iter(models)), "task_count": len(tasks),
            "variants": output, "paired_comparisons": paired, "items": scored,
            "metric_note": "Track metrics remain separate. Correct content plus matching quotation is not a semantic-support judgment; empty citations never count as verified-citation success."}
