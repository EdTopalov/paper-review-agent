"""Frozen benchmark loading and integrity checks; no model interaction."""

from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import re

from .paper import file_hash


BENCHMARK_VERSION = "evidence-assessment-v1"
DEFAULT_BENCHMARK = Path("data/benchmark/v1")
KINDS = {"qasper": "qa", "reviewcritique": "critique", "controlled": "claim", "selection": "selection"}


def read_jsonl(path):
    return [json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path, rows):
    Path(path).write_text("".join(json.dumps(row, ensure_ascii=False, allow_nan=False) + "\n" for row in rows),
                          encoding="utf-8", newline="\n")


def inside(root, relative):
    path = (root / relative).resolve()
    if Path(relative).is_absolute() or not path.is_relative_to(root):
        raise ValueError(f"Benchmark path leaves its root: {relative}")
    return path


def block_map(public):
    return {(document["id"], block["id"]): block["text"]
            for document in public["documents"] for block in document["blocks"]}


def _validate_task(row, public, reference):
    task_id = row["id"]
    if row["track"] not in KINDS or row["kind"] != KINDS[row["track"]]:
        raise ValueError(f"Unknown track or mismatched task kind: {task_id}")
    if public.get("id") != task_id or reference.get("id") != task_id or public.get("kind") != row["kind"]:
        raise ValueError(f"Task identity mismatch: {task_id}")
    if row["split"] not in {"dev", "test"} or not row.get("group_id"):
        raise ValueError(f"Invalid split or group: {task_id}")
    if not isinstance(public.get("instructions"), str) or not public["instructions"].strip():
        raise ValueError(f"Missing task instructions: {task_id}")
    forbidden = {"reference", "answers", "expert_explanation", "label_origin", "acceptable_ids", "eligible_ids",
                 "pair_id", "condition", "facts", "verdict", "error_types"}
    if forbidden.intersection(public):
        raise ValueError(f"Reference-only fields in public task: {task_id}")
    documents = public.get("documents", [])
    ids = [document["id"] for document in documents]
    if not documents or len(ids) != len(set(ids)):
        raise ValueError(f"Missing or duplicate document IDs: {task_id}")
    for document in documents:
        blocks = document.get("blocks", [])
        block_ids = [block["id"] for block in blocks]
        if not blocks or len(block_ids) != len(set(block_ids)) or any(
                not isinstance(block["text"], str) or not block["text"].strip() for block in blocks):
            raise ValueError(f"Missing, duplicate, or empty source blocks: {task_id}")
    locations = block_map(public)
    references = reference.get("answers", []) if row["kind"] == "qa" else [reference]
    for answer in references:
        for evidence in answer.get("evidence", []):
            if (evidence["document_id"], evidence["block_id"]) not in locations:
                raise ValueError(f"Reference evidence is outside the task: {task_id}")
    if row["kind"] == "qa":
        if not public.get("question") or not references or any(
                answer.get("answer_type") not in {"extractive", "free_form", "yes_no", "unanswerable"}
                or not isinstance(answer.get("answer"), str) or not answer["answer"].strip()
                for answer in references):
            raise ValueError(f"Invalid QA reference: {task_id}")
    elif row["kind"] == "critique":
        if not public.get("comment") or reference.get("verdict") not in {"reliable", "deficient"}:
            raise ValueError(f"Invalid critique reference: {task_id}")
    elif row["kind"] == "claim":
        if not (public.get("statement") or public.get("question")) or reference.get("verdict") not in {
                "supported", "contradicted", "insufficient"} or not reference.get("pair_id"):
            raise ValueError(f"Invalid controlled reference: {task_id}")
    else:
        eligible, acceptable = reference.get("eligible_ids"), reference.get("acceptable_ids")
        if (not public.get("brief") or not isinstance(eligible, list) or not isinstance(acceptable, list)
                or len(eligible) != len(set(eligible)) or len(acceptable) != len(set(acceptable))
                or not set(acceptable) <= set(eligible) <= set(ids)):
            raise ValueError(f"Invalid selection reference: {task_id}")


def load_benchmark(root=DEFAULT_BENCHMARK, split=None, tracks=None):
    """Validate the entire frozen corpus before returning a requested subset."""
    root = Path(root).resolve()
    rows = read_jsonl(root / "manifest.jsonl")
    if not rows or len({row["id"] for row in rows}) != len(rows):
        raise ValueError("Benchmark manifest must have distinct, nonempty task IDs")
    settings = json.loads((root / "benchmark.json").read_text(encoding="utf-8"))
    if settings.get("version") != BENCHMARK_VERSION or settings.get("manifest_sha256") != file_hash(root / "manifest.jsonl"):
        raise ValueError("Benchmark version or manifest hash mismatch")
    for relative, fingerprint in settings.get("source_files", {}).items():
        if file_hash(inside(root, relative)) != fingerprint:
            raise ValueError(f"Benchmark source notice hash mismatch: {relative}")
    groups, pairs, tasks = defaultdict(set), defaultdict(list), []
    paper_splits = defaultdict(set)
    for row in rows:
        payload = {}
        for name in ("input", "reference"):
            path = inside(root, row[f"{name}_path"])
            if file_hash(path) != row[f"{name}_sha256"]:
                raise ValueError(f"Benchmark {name} hash mismatch: {row['id']}")
            payload[name] = json.loads(path.read_text(encoding="utf-8"))
        _validate_task(row, payload["input"], payload["reference"])
        groups[row["group_id"]].add(row["split"])
        if row["track"] in {"qasper", "reviewcritique"}:
            title = payload["input"]["documents"][0]["title"]
            normalized = re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()
            paper_splits[normalized].add(row["split"])
        if row["kind"] == "claim":
            pairs[payload["reference"]["pair_id"]].append({**row, **payload})
        tasks.append({**row, **payload})
    if any(len(splits) != 1 for splits in [*groups.values(), *paper_splits.values()]):
        raise ValueError("A source paper or study family crosses development/test splits")
    for pair_id, members in pairs.items():
        if (len(members) != 2 or len({member["split"] for member in members}) != 1
                or len({member["group_id"] for member in members}) != 1
                or len({member["reference"]["verdict"] for member in members}) != 2):
            raise ValueError(f"Controlled pair is incomplete or inconsistent: {pair_id}")
        statements = {member["input"].get("statement", member["input"].get("question")) for member in members}
        if len(statements) != 1:
            raise ValueError(f"Controlled pair changes its target statement: {pair_id}")
    if settings.get("tasks") != len(tasks):
        raise ValueError("Benchmark task count differs from the frozen catalog")
    if split is not None and split not in {"dev", "test"}:
        raise ValueError("Choose dev or test")
    if tracks is not None and (not tracks or set(tracks) - KINDS.keys()):
        raise ValueError("Choose known, nonempty benchmark tracks")
    return [task for task in tasks if (split is None or task["split"] == split)
            and (tracks is None or task["track"] in tracks)]


def freeze_catalog(root=DEFAULT_BENCHMARK):
    """Assemble prepared track manifests without downloading or invoking models."""
    root = Path(root).resolve()
    rows = []
    notices = {}
    for track in KINDS:
        rows.extend(read_jsonl(root / track / "manifest.jsonl"))
        for path in sorted((root / track).glob("*")):
            if path.is_file():
                notices[path.relative_to(root).as_posix()] = file_hash(path)
    rows.sort(key=lambda row: row["id"])
    write_jsonl(root / "manifest.jsonl", rows)
    settings = {"version": BENCHMARK_VERSION, "tasks": len(rows),
                "manifest_sha256": file_hash(root / "manifest.jsonl"), "source_files": notices,
                "counts": dict(sorted(Counter(f"{row['track']}/{row['split']}" for row in rows).items())),
                "status": "prepared_not_evaluated"}
    (root / "benchmark.json").write_text(json.dumps(settings, indent=2) + "\n", encoding="utf-8", newline="\n")
    load_benchmark(root)
    return settings


def benchmark_summary(root=DEFAULT_BENCHMARK):
    tasks = load_benchmark(root)
    return {"version": BENCHMARK_VERSION, "tasks": len(tasks),
            "counts": dict(sorted(Counter(f"{task['track']}/{task['split']}" for task in tasks).items())),
            "groups": {track: len({task['group_id'] for task in tasks if task['track'] == track}) for track in KINDS},
            "manifest_sha256": file_hash(Path(root) / "manifest.jsonl"), "model_calls": 0}


def export_inputs(root, out, *, split="test", tracks=None):
    """Export only public task inputs; reference files are never copied."""
    tasks = load_benchmark(root, split, tracks)
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    manifest = []
    for task in tasks:
        name = f"{task['id']}.json"
        (out / name).write_bytes(inside(Path(root).resolve(), task["input_path"]).read_bytes())
        manifest.append({"id": task["id"], "kind": task["kind"], "input_path": name,
                         "input_sha256": task["input_sha256"]})
    write_jsonl(out / "inputs.jsonl", manifest)
    return {"tasks": len(tasks), "split": split, "out": str(out), "reference_files_exported": 0}
