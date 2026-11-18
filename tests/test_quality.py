"""Human quality labels must remain blinded, explicit, and coverage-aware."""

from copy import deepcopy
import json

import pytest

from paper_review.quality import export_quality_packets, score_quality_labels, DIMENSIONS
from paper_review.paper import file_hash


def write_rows(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")


def fixture_experiment(tmp_path):
    sample_dir = tmp_path / "sample"
    sample_dir.mkdir()
    paper = sample_dir / "paper.json"
    paper.write_text(json.dumps({"title": "Fixture", "arxiv_id": "fixture", "pages": ["Evidence."]}),
                     encoding="utf-8")
    sample = sample_dir / "tasks.jsonl"
    write_rows(sample, [{"id": "T01", "arxiv_id": "fixture", "paper_path": "paper.json",
                         "snapshot_sha256": file_hash(paper)}])
    experiment = tmp_path / "experiment"
    review = {"score": 0.5, "summary": "Fixture", "observations": [
        {"kind": "strength", "claim": "Evidence.", "page": 1, "quote": "Evidence."}],
              "unresolved_questions": []}
    for variant, status in [("agent", "ok"), ("baseline", "error")]:
        write_rows(experiment / f"{variant}-r1" / "T01" / "trace.jsonl", [
            {"seq": 1, "event": "environment", "snapshot_sha256": file_hash(paper)},
            {"seq": 2, "event": "run_end", "result": {"task_id": "T01", "variant": variant,
                "status": status, "review": review if status == "ok" else None}}])
    return experiment, sample


def complete_labels(packet_dir, rater_id, value=2):
    rows = [json.loads(line) for line in (packet_dir / "labels-template.jsonl").read_text().splitlines()]
    for row in rows:
        row.update(rater_id=rater_id, dimensions={name: value for name in DIMENSIONS},
                   critical_factual_error=False, reason="Checked the fixture.", source_pages=[1])
        for claim in row["claim_labels"]:
            claim.update(verdict="supported", reason="Direct support.", source_pages=[1])
    path = packet_dir / f"{rater_id}.jsonl"
    write_rows(path, rows)
    return path


def test_packet_blinding_and_no_fabricated_quality(tmp_path):
    experiment, sample = fixture_experiment(tmp_path)
    packets = tmp_path / "packets"
    result = export_quality_packets(experiment, packets, sample)
    assert result["attempts"] == 2
    rows = [json.loads(line) for line in (packets / "packets.jsonl").read_text().splitlines()]
    assert all("variant" not in row and "repeat" not in row and "trace_path" not in row for row in rows)
    metrics = score_quality_labels(packets, [])
    assert metrics["human_labels_present"] is False
    assert metrics["variants"]["agent"]["quality_per_attempt"] is None
    assert metrics["variants"]["agent"]["adequate_review_rate"] is None
    assert metrics["variants"]["baseline"]["quality_per_attempt"] == 0
    assert metrics["variants"]["baseline"]["adequate_review_rate"] == 0
    with pytest.raises(FileExistsError):
        export_quality_packets(experiment, packets, sample)


def test_two_raters_disagreement_and_failed_attempt_denominator(tmp_path):
    experiment, sample = fixture_experiment(tmp_path)
    packets = tmp_path / "packets"
    export_quality_packets(experiment, packets, sample)
    first = complete_labels(packets, "rater-a", 2)
    second = complete_labels(packets, "rater-b", 0)
    assert score_quality_labels(packets, [first])["variants"]["agent"]["quality_per_attempt"] is None
    result = score_quality_labels(packets, [first, second])
    assert result["variants"]["agent"]["quality_per_attempt"] == 0.5
    assert result["variants"]["agent"]["adequate_review_rate"] == 0.5
    assert result["variants"]["baseline"]["attempts"] == 1
    assert len(result["disagreement_item_ids"]) == 1
    assert result["audit_agreement"]["rate"] is None
    with pytest.raises(ValueError, match="Duplicate rater"):
        score_quality_labels(packets, [first, first])


def test_rejects_incomplete_grid_and_invalid_labels(tmp_path):
    experiment, sample = fixture_experiment(tmp_path)
    path = experiment / "baseline-r2" / "T01" / "trace.jsonl"
    original = experiment / "baseline-r1" / "T01" / "trace.jsonl"
    path.parent.mkdir(parents=True)
    path.write_bytes(original.read_bytes())
    with pytest.raises(ValueError, match="same tasks and repetitions"):
        export_quality_packets(experiment, tmp_path / "invalid", sample)
    packets = tmp_path / "packets"
    export_quality_packets(experiment, packets, sample, repeats=[1])
    first = complete_labels(packets, "rater-a")
    rows = [json.loads(line) for line in first.read_text().splitlines()]
    for row in rows:
        row["dimensions"]["support"] = True
    write_rows(first, rows)
    with pytest.raises(ValueError, match="integer from 0 to 2"):
        score_quality_labels(packets, [first])


def test_snapshot_or_review_mutation_is_rejected(tmp_path):
    experiment, sample = fixture_experiment(tmp_path)
    packets = tmp_path / "packets"
    export_quality_packets(experiment, packets, sample)
    rows = [json.loads(line) for line in (packets / "packets.jsonl").read_text().splitlines()]
    modified = deepcopy(rows)
    next(row for row in modified if row["review"])["review"]["score"] = 0.9
    write_rows(packets / "packets.jsonl", modified)
    with pytest.raises(ValueError, match="review hash"):
        score_quality_labels(packets, [])


def test_source_snapshot_mismatch_and_missing_condition_are_rejected(tmp_path):
    experiment, sample = fixture_experiment(tmp_path)
    (experiment / "experiment.json").write_text(json.dumps({"variants": ["agent", "baseline", "third"]}))
    with pytest.raises(ValueError, match="same tasks and repetitions"):
        export_quality_packets(experiment, tmp_path / "missing", sample)
    (experiment / "experiment.json").write_text(json.dumps({"variants": ["agent", "baseline"]}))
    trace = experiment / "agent-r1" / "T01" / "trace.jsonl"
    rows = [json.loads(line) for line in trace.read_text().splitlines()]
    rows[0]["snapshot_sha256"] = "incorrect"
    write_rows(trace, rows)
    with pytest.raises(ValueError, match="Trace snapshot"):
        export_quality_packets(experiment, tmp_path / "mismatch", sample)


def test_audit_agreement_and_adjudication_preserve_independent_labels(tmp_path):
    from paper_review.audit import review_hash

    experiment, sample = fixture_experiment(tmp_path)
    trace = experiment / "agent-r1" / "T01" / "trace.jsonl"
    rows = [json.loads(line) for line in trace.read_text().splitlines()]
    rows.append({"seq": 3, "event": "audit_end", "record": {"status": "ok",
        "review_sha256": review_hash(rows[1]["result"]["review"]),
        "snapshot_sha256": rows[0]["snapshot_sha256"],
        "audit": {"observations": [{"index": 0, "verdict": "overstated"}]}}})
    write_rows(trace, rows)
    packets = tmp_path / "packets"
    export_quality_packets(experiment, packets, sample)
    first = complete_labels(packets, "rater-a", 2)
    second = complete_labels(packets, "rater-b", 0)
    adjudication = complete_labels(packets, "adjudicator", 1)
    with pytest.raises(ValueError, match="at least two independent"):
        score_quality_labels(packets, [first], adjudication_path=adjudication)
    result = score_quality_labels(packets, [first, second], adjudication_path=adjudication)
    assert result["variants"]["agent"]["quality_per_attempt"] == 0.5
    assert result["variants"]["agent"]["adjudicated"] == 1
    assert result["variants"]["agent"]["adequate_review_rate"] == 1
    assert len(result["disagreement_item_ids"]) == 1
    assert result["audit_agreement"]["matching_labels"] == 0
    assert result["audit_agreement"]["compared_claim_labels"] == 1


def test_declared_repeat_grid_includes_wholly_missing_repetitions(tmp_path):
    experiment, sample = fixture_experiment(tmp_path)
    for variant in ("agent", "baseline"):
        source = experiment / f"{variant}-r1" / "T01" / "trace.jsonl"
        target = experiment / f"{variant}-r2" / "T01" / "trace.jsonl"
        target.parent.mkdir(parents=True)
        target.write_bytes(source.read_bytes())
    (experiment / "experiment.json").write_text(json.dumps({
        "variants": ["agent", "baseline"], "task_ids": ["T01"], "repeats": 3}))
    with pytest.raises(ValueError, match="same tasks and repetitions"):
        export_quality_packets(experiment, tmp_path / "missing-r3", sample)
    result = export_quality_packets(experiment, tmp_path / "explicit-subset", sample, repeats=[1, 2])
    assert result["attempts"] == 4
    assert result["repeats"] == [1, 2]


@pytest.mark.parametrize("filename", ["packets.jsonl", "private/key.jsonl"])
def test_duplicate_packet_or_key_ids_are_rejected(tmp_path, filename):
    experiment, sample = fixture_experiment(tmp_path)
    packets = tmp_path / "packets"
    export_quality_packets(experiment, packets, sample)
    path = packets / filename
    rows = [json.loads(line) for line in path.read_text().splitlines()]
    write_rows(path, [*rows, rows[0]])
    with pytest.raises(ValueError, match="Duplicate"):
        score_quality_labels(packets, [])


def test_dropped_rows_cannot_reduce_the_protocol_denominator(tmp_path):
    experiment, sample = fixture_experiment(tmp_path)
    packets = tmp_path / "packets"
    export_quality_packets(experiment, packets, sample)
    public = [json.loads(line) for line in (packets / "packets.jsonl").read_text().splitlines()]
    dropped_id = public[0]["item_id"]
    write_rows(packets / "packets.jsonl", public[1:])
    private = [json.loads(line) for line in (packets / "private/key.jsonl").read_text().splitlines()]
    write_rows(packets / "private/key.jsonl", [row for row in private if row["item_id"] != dropped_id])
    with pytest.raises(ValueError, match="count or condition grid"):
        score_quality_labels(packets, [])


def test_self_valid_source_swap_is_rejected(tmp_path):
    experiment, sample = fixture_experiment(tmp_path)
    source = sample.parent / "paper.json"
    other_source = sample.parent / "other.json"
    other_paper = json.loads(source.read_text())
    other_paper.update(arxiv_id="different", title="A different paper", pages=["Different evidence."])
    other_source.write_text(json.dumps(other_paper), encoding="utf-8")
    tasks = [json.loads(line) for line in sample.read_text().splitlines()]
    tasks.append({"id": "T02", "arxiv_id": "different", "paper_path": "other.json",
                  "snapshot_sha256": file_hash(other_source)})
    write_rows(sample, tasks)
    for variant in ("agent", "baseline"):
        original = experiment / f"{variant}-r1" / "T01" / "trace.jsonl"
        rows = [json.loads(line) for line in original.read_text().splitlines()]
        rows[0]["snapshot_sha256"] = file_hash(other_source)
        rows[1]["result"]["task_id"] = "T02"
        write_rows(experiment / f"{variant}-r1" / "T02" / "trace.jsonl", rows)
    packets = tmp_path / "packets"
    export_quality_packets(experiment, packets, sample)
    rows = [json.loads(line) for line in (packets / "packets.jsonl").read_text().splitlines()]
    row = next(row for row in rows if row["paper_id"] == "T01")
    row.update(paper_id="T02", paper_path="papers/T02.json", snapshot_sha256=file_hash(other_source))
    assert file_hash(packets / row["paper_path"]) == row["snapshot_sha256"]
    write_rows(packets / "packets.jsonl", rows)
    with pytest.raises(ValueError, match="source identity"):
        score_quality_labels(packets, [])


def test_adequacy_requires_no_critical_error_and_counts_failed_attempts(tmp_path):
    experiment, sample = fixture_experiment(tmp_path)
    for variant in ("agent", "baseline"):
        original = experiment / f"{variant}-r1" / "T01" / "trace.jsonl"
        rows = [json.loads(line) for line in original.read_text().splitlines()]
        rows[1]["result"].update(status="error", review=None)
        write_rows(experiment / f"{variant}-r2" / "T01" / "trace.jsonl", rows)
    packets = tmp_path / "packets"
    export_quality_packets(experiment, packets, sample)
    first = complete_labels(packets, "rater-a", 2)
    second = complete_labels(packets, "rater-b", 2)
    rows = [json.loads(line) for line in second.read_text().splitlines()]
    for row in rows:
        row["critical_factual_error"] = True
    write_rows(second, rows)
    result = score_quality_labels(packets, [first, second])
    assert result["variants"]["agent"]["attempts"] == 2
    assert result["variants"]["agent"]["adequate_review_rate"] == 0.25
    assert result["variants"]["agent"]["quality_per_attempt"] == 0.5
    assert sorted(row["adequate_probability"] for row in result["variants"]["agent"]["items"]) == [0, 0.5]
