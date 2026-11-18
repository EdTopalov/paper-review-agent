"""Blinded human assessment packets and offline, coverage-aware label scoring."""

from collections import defaultdict
from hashlib import sha256
import json
from pathlib import Path
import random
import statistics

from .audit import review_hash
from .evaluation import load_sample
from .paper import file_hash
from .trace import read_events, read_result


DIMENSIONS = ("support", "central_evidence_coverage", "calibration", "reading_club_usefulness")
VERDICTS = {"supported", "unsupported", "unclear"}


def _read_jsonl(path):
    with Path(path).open(encoding="utf-8") as stream:
        return [json.loads(line) for line in stream if line.strip()]


def _write_jsonl(path, rows):
    with Path(path).open("x", encoding="utf-8", newline="\n") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False, allow_nan=False) + "\n")


def _content_hash(value):
    return sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                             allow_nan=False).encode("utf-8")).hexdigest()


def _index_unique(rows, name):
    output = {}
    for row in rows:
        item_id = row["item_id"]
        if item_id in output:
            raise ValueError(f"Duplicate {name} ID: {item_id}")
        output[item_id] = row
    return output


def export_quality_packets(experiment_dir, out_dir, sample_path="data/eval/tasks.jsonl",
                           task_ids=None, repeats=None, seed=20261118):
    """Export all variants for each selected task/repetition, without API calls.

    The private key binds blind IDs to trace bytes, review hashes and conditions.
    Give annotators packets.jsonl, papers/ and a copy of labels-template.jsonl;
    withhold private/. A fresh directory is required to preserve prior labels.
    """
    root = Path(experiment_dir).resolve()
    sample_path = Path(sample_path).resolve()
    tasks = {row["id"]: row for row in load_sample(sample_path)}
    settings_path = root / "experiment.json"
    settings = json.loads(settings_path.read_text(encoding="utf-8")) if settings_path.exists() else {}
    planned_tasks = set(settings.get("task_ids", tasks))
    if not planned_tasks or planned_tasks - tasks.keys():
        raise ValueError("Experiment tasks must belong to the frozen sample")
    selected_tasks = set(task_ids) if task_ids is not None else planned_tasks
    if not selected_tasks or selected_tasks - planned_tasks:
        raise ValueError("Select one or more task IDs from the frozen sample")
    planned_repeats = None
    if "repeats" in settings:
        if type(settings["repeats"]) is not int or settings["repeats"] < 1:
            raise ValueError("Experiment repeat count must be a positive integer")
        planned_repeats = set(range(1, settings["repeats"] + 1))
    selected_repeats = set(repeats) if repeats is not None else None
    if selected_repeats is not None and (not selected_repeats or any(
            type(value) is not int or value < 1 for value in selected_repeats)):
        raise ValueError("Repetition IDs must be positive integers")
    if selected_repeats is not None and planned_repeats is not None and selected_repeats - planned_repeats:
        raise ValueError("Selected repetitions must belong to the experiment plan")
    if selected_repeats is None:
        selected_repeats = planned_repeats
    cells = {}
    all_variants = set(settings.get("variants", []))
    if "variants" in settings and (not all_variants or len(all_variants) != len(settings["variants"])):
        raise ValueError("Experiment variants must be nonempty and distinct")
    for path in sorted(root.glob("*/*/trace.jsonl")):
        variant, separator, raw_repeat = path.parent.parent.name.rpartition("-r")
        if not separator or not raw_repeat.isdigit():
            raise ValueError(f"Invalid repetition folder: {path.parent.parent.name}")
        repeat = int(raw_repeat)
        if "variants" in settings:
            if variant not in all_variants:
                raise ValueError(f"Trace variant is outside the experiment plan: {variant}")
        else:
            all_variants.add(variant)
        if repeat < 1 or (planned_repeats is not None and repeat not in planned_repeats):
            raise ValueError(f"Trace repetition is outside the experiment plan: {repeat}")
        task_id = path.parent.name
        if task_id not in selected_tasks or (selected_repeats is not None and repeat not in selected_repeats):
            continue
        result = read_result(path)
        if result is None:
            raise ValueError(f"Missing terminal result: {path}")
        if result["task_id"] != task_id or result["variant"] != variant:
            raise ValueError(f"Trace identity mismatch: {path}")
        environment = next((row for row in read_events(path) if row["event"] == "environment"), None)
        if environment is None or environment.get("snapshot_sha256") != tasks[task_id]["snapshot_sha256"]:
            raise ValueError(f"Trace snapshot does not match the frozen sample: {path}")
        cells[variant, task_id, repeat] = (path, result)
    if not cells:
        raise ValueError("No selected experiment attempts")
    repeat_ids = selected_repeats or {cell[2] for cell in cells}
    expected = {(variant, task_id, repeat) for variant in all_variants
                for task_id in selected_tasks for repeat in repeat_ids}
    if set(cells) != expected:
        raise ValueError("Human packet selection requires the same tasks and repetitions for every variant")
    packets, templates, keys = [], [], []
    for (variant, task_id, repeat), (path, result) in sorted(cells.items()):
        trace_hash = file_hash(path)
        completed = result["status"] == "ok" and bool(result.get("review"))
        review = result.get("review") if completed else None
        fingerprint = review_hash(review)
        identity = f"{seed}:{variant}:{task_id}:{repeat}:{trace_hash}:{fingerprint}"
        item_id = "Q" + sha256(identity.encode()).hexdigest()[:16]
        packet = {"item_id": item_id, "paper_id": task_id,
                  "paper_path": f"papers/{task_id}.json",
                  "snapshot_sha256": tasks[task_id]["snapshot_sha256"],
                  "completion": "completed" if completed else "failed", "review": review}
        packets.append(packet)
        templates.append({"item_id": item_id, "rater_id": "",
                          "dimensions": {name: None for name in DIMENSIONS},
                          "critical_factual_error": None, "reason": "", "source_pages": [],
                          "claim_labels": [{"index": index, "verdict": None, "reason": "",
                                            "source_pages": []}
                                           for index, _ in enumerate((review or {}).get("observations", []))]})
        audit = read_result(path, audit=True)
        if audit and audit.get("status") == "ok" and (
                audit.get("review_sha256") != fingerprint
                or audit.get("snapshot_sha256") != tasks[task_id]["snapshot_sha256"]):
            raise ValueError("Audit input hashes do not match the exported review and snapshot")
        keys.append({"item_id": item_id, "variant": variant, "task_id": task_id, "repeat": repeat,
                     "trace_path": path.relative_to(root).as_posix(), "trace_sha256": trace_hash,
                     "review_sha256": fingerprint, "packet_sha256": _content_hash(packet),
                     "snapshot_sha256": tasks[task_id]["snapshot_sha256"],
                     "arxiv_id": tasks[task_id]["arxiv_id"], "completion": packet["completion"],
                     "audit": audit.get("audit") if audit and audit.get("status") == "ok" else None})
    target = Path(out_dir).resolve()
    target.mkdir(parents=True, exist_ok=False)
    (target / "papers").mkdir()
    (target / "private").mkdir()
    for task_id in sorted(selected_tasks):
        source = sample_path.parent / tasks[task_id]["paper_path"]
        (target / "papers" / f"{task_id}.json").write_bytes(source.read_bytes())
    random.Random(seed).shuffle(packets)
    order = {row["item_id"]: index for index, row in enumerate(packets)}
    templates.sort(key=lambda row: order[row["item_id"]])
    _write_jsonl(target / "packets.jsonl", packets)
    _write_jsonl(target / "labels-template.jsonl", templates)
    _write_jsonl(target / "private" / "key.jsonl", keys)
    metadata = {"schema_version": "human-quality-v1", "seed": seed, "attempts": len(packets),
                "variants": sorted(all_variants), "task_ids": sorted(selected_tasks),
                "repeats": sorted(repeat_ids), "labels_status": "unlabelled",
                "dimensions": list(DIMENSIONS), "item_ids": sorted(order)}
    (target / "protocol.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    return metadata


def _validate_label(row, packet, page_count):
    if not isinstance(row.get("rater_id"), str) or not row["rater_id"].strip():
        raise ValueError("Every submitted label needs a nonempty rater_id")
    dimensions = row.get("dimensions", {})
    if not isinstance(dimensions, dict) or set(dimensions) != set(DIMENSIONS) or any(
            type(value) is not int or not 0 <= value <= 2 for value in dimensions.values()):
        raise ValueError("Every quality dimension must be an integer from 0 to 2")
    if type(row.get("critical_factual_error")) is not bool:
        raise ValueError("critical_factual_error must be true or false")
    if not isinstance(row.get("reason"), str) or not row["reason"].strip():
        raise ValueError("Every label needs an evidence-based reason")
    claims = row.get("claim_labels", [])
    count = len(packet["review"]["observations"])
    if not isinstance(claims, list) or not all(isinstance(claim, dict) for claim in claims):
        raise ValueError("claim_labels must be a list of observation labels")
    if [claim.get("index") for claim in claims] != list(range(count)):
        raise ValueError("Label every observation exactly once in its original order")
    for claim in claims:
        if (claim.get("verdict") not in VERDICTS or not isinstance(claim.get("reason"), str)
                or not claim["reason"].strip()):
            raise ValueError("Every claim needs a supported/unsupported/unclear verdict and reason")
    for entry in [row, *claims]:
        pages = entry.get("source_pages")
        if not isinstance(pages, list) or not pages or any(
                type(page) is not int or not 1 <= page <= page_count for page in pages):
            raise ValueError("Every review and claim label needs valid source_pages")


def score_quality_labels(packet_dir, label_paths, *, adjudication_path=None):
    """Validate human labels and return metrics; never infer or fabricate labels.

    At least two independent labels are required per completed item for a final
    quality estimate. Disagreements remain visible; an optional adjudication file
    supplies final labels after independent annotation. Failed reviews receive
    zero task utility and coverage, while unlabelled completions remain missing.
    """
    root = Path(packet_dir)
    packets = _index_unique(_read_jsonl(root / "packets.jsonl"), "packet")
    keys = _index_unique(_read_jsonl(root / "private" / "key.jsonl"), "private key")
    protocol = json.loads((root / "protocol.json").read_text(encoding="utf-8"))
    if protocol.get("schema_version") != "human-quality-v1" or protocol.get("dimensions") != list(DIMENSIONS):
        raise ValueError("Unknown quality protocol schema or dimensions")
    for field in ("variants", "task_ids", "repeats", "item_ids"):
        values = protocol.get(field)
        if not isinstance(values, list) or not values or len(set(values)) != len(values):
            raise ValueError(f"Protocol {field} must be a nonempty distinct list")
    if any(type(value) is not int or value < 1 for value in protocol["repeats"]):
        raise ValueError("Protocol repetition IDs must be positive integers")
    expected_cells = {(variant, task, repeat) for variant in protocol["variants"]
                      for task in protocol["task_ids"] for repeat in protocol["repeats"]}
    actual_cells = [(row["variant"], row["task_id"], row["repeat"]) for row in keys.values()]
    if (type(protocol.get("attempts")) is not int or protocol["attempts"] != len(expected_cells)
            or len(keys) != protocol["attempts"] or len(actual_cells) != len(set(actual_cells))
            or set(actual_cells) != expected_cells
            or set(protocol["item_ids"]) != keys.keys()):
        raise ValueError("Quality packet count or condition grid differs from the protocol")
    if packets.keys() != keys.keys():
        raise ValueError("Packet and private key IDs differ")
    for packet in packets.values():
        key = keys[packet["item_id"]]
        if packet["paper_id"] != key["task_id"] or packet["paper_path"] != f"papers/{key['task_id']}.json":
            raise ValueError("Packet source identity differs from its private key")
        if (packet["completion"] != key["completion"] or packet["completion"] not in {"completed", "failed"}
                or (packet["review"] is not None) != (packet["completion"] == "completed")):
            raise ValueError("Packet completion differs from its private key or review")
        paper_path = root / packet["paper_path"]
        paper = json.loads(paper_path.read_text(encoding="utf-8"))
        if (file_hash(paper_path) != packet["snapshot_sha256"]
                or packet["snapshot_sha256"] != key["snapshot_sha256"]
                or paper.get("arxiv_id") != key["arxiv_id"]):
            raise ValueError("Packet snapshot hash or source identity mismatch")
        if review_hash(packet["review"]) != key["review_sha256"]:
            raise ValueError("Packet review hash mismatch")
        if _content_hash(packet) != key["packet_sha256"]:
            raise ValueError("Public packet hash differs from its private key")
    labels = defaultdict(dict)
    adjudications = {}
    for path, adjudication in [(path, False) for path in label_paths] + (
            [(adjudication_path, True)] if adjudication_path else []):
        for row in _read_jsonl(path):
            item_id = row.get("item_id")
            if item_id not in packets:
                raise ValueError(f"Unknown packet ID: {item_id}")
            packet = packets[item_id]
            if packet["completion"] == "failed":
                continue
            paper = json.loads((root / packet["paper_path"]).read_text(encoding="utf-8"))
            _validate_label(row, packet, len(paper["pages"]))
            if adjudication:
                if item_id in adjudications:
                    raise ValueError("Duplicate adjudication")
                adjudications[item_id] = row
            else:
                if row["rater_id"] in labels[item_id]:
                    raise ValueError("Duplicate rater/item label")
                labels[item_id][row["rater_id"]] = row
    variants = defaultdict(list)
    disagreements = []
    audit_matches = audit_count = 0
    for item_id, packet in packets.items():
        key = keys[item_id]
        ratings = list(labels[item_id].values())
        completed = packet["completion"] == "completed"
        independent = len(ratings) >= 2
        if item_id in adjudications and not independent:
            raise ValueError("Adjudication requires at least two independent labels first")
        if independent:
            signatures = {json.dumps({"dimensions": row["dimensions"],
                                      "critical_factual_error": row["critical_factual_error"],
                                      "verdicts": [claim["verdict"] for claim in row["claim_labels"]]},
                                     sort_keys=True) for row in ratings}
            if len(signatures) > 1:
                disagreements.append(item_id)
        final = adjudications.get(item_id)
        selected = [final] if final else ratings
        dimension_means = {name: statistics.mean(row["dimensions"][name] for row in selected)
                           for name in DIMENSIONS} if independent else None
        utility = (sum(dimension_means.values()) / (2 * len(DIMENSIONS))) if independent else None
        adequate = statistics.mean(all(value >= 1 for value in row["dimensions"].values())
                                   and not row["critical_factual_error"] for row in selected) if independent else None
        if not completed:
            utility = 0.0
            adequate = 0.0
            dimension_means = {name: 0.0 for name in DIMENSIONS}
        if independent and key.get("audit"):
            # The existing M2 audit distinguishes overstated from unsupported;
            # both mean a claim is not fully supported at its stated scope.
            collapse = {"supported": "supported", "overstated": "unsupported",
                        "unsupported": "unsupported", "uncertain": "unclear"}
            audit_rows = key["audit"]["observations"]
            for rating in selected:
                for claim, audit in zip(rating["claim_labels"], audit_rows, strict=True):
                    if claim["index"] != audit["index"]:
                        raise ValueError("Audit observation indices differ from the packet")
                    audit_matches += claim["verdict"] == collapse[audit["verdict"]]
                    audit_count += 1
        variants[key["variant"]].append({"item_id": item_id, "completed": completed,
                                          "raters": len(ratings), "independently_labelled": independent,
                                          "adjudicated": final is not None,
                                          "critical_error_votes": sum(row["critical_factual_error"] for row in selected),
                                          "critical_error_judgments": len(selected),
                                          "dimensions": dimension_means, "utility": utility,
                                          "adequate_probability": adequate})
    output = {}
    for variant, rows in sorted(variants.items()):
        complete_labels = all(not row["completed"] or row["independently_labelled"] for row in rows)
        output[variant] = {"attempts": len(rows), "completed": sum(row["completed"] for row in rows),
                           "independently_labelled_completed": sum(row["completed"] and row["independently_labelled"]
                                                                   for row in rows),
                           "adjudicated": sum(row["adjudicated"] for row in rows),
                           "critical_error_votes": sum(row["critical_error_votes"] for row in rows),
                           "critical_error_judgments": sum(row["critical_error_judgments"] for row in rows),
                           "quality_per_attempt": statistics.mean(row["utility"] for row in rows)
                               if complete_labels else None,
                           "adequate_review_rate": statistics.mean(row["adequate_probability"] for row in rows)
                               if complete_labels else None,
                           "dimensions_per_attempt": {name: statistics.mean(row["dimensions"][name] for row in rows)
                                                      for name in DIMENSIONS} if complete_labels else None,
                           "items": rows}
    return {"schema_version": "human-quality-v1", "human_labels_present": any(labels.values()),
            "aggregation": "adjudicated labels where supplied; otherwise mean of independent human ratings",
            "disagreement_item_ids": disagreements, "variants": output,
            "audit_agreement": {"matching_labels": audit_matches, "compared_claim_labels": audit_count,
                                "rate": audit_matches / audit_count if audit_count else None,
                                "mapping": "supported; unsupported includes overstated; unclear includes uncertain"}}
