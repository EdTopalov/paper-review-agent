"""Frozen task validation and mechanical evaluation; not semantic truth labels."""

from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict
from hashlib import sha256
import json
from pathlib import Path
import statistics
import subprocess

from .paper import Paper, file_hash
from .runner import run_review


def load_sample(path):
    path = Path(path).resolve()
    tasks = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    ids = [task["id"] for task in tasks]
    sources = [task["arxiv_id"] for task in tasks]
    if len(ids) != len(set(ids)) or len(sources) != len(set(sources)):
        raise ValueError("Duplicate task IDs or papers in frozen sample")
    for task in tasks:
        paper = (path.parent / task["paper_path"]).resolve()
        if not paper.is_relative_to(path.parent):
            raise ValueError("Task path must stay inside the sample directory")
        if file_hash(paper) != task["snapshot_sha256"]:
            raise ValueError(f"Snapshot hash mismatch: {task['id']}")
        snapshot = Paper.load(paper)
        if snapshot.snapshot.get("arxiv_id") != task["arxiv_id"]:
            raise ValueError(f"Paper identity mismatch: {task['id']}")
    return tasks


def mechanical_result(result):
    citations = result.get("citation_checks", [])
    return {"task_id": result["task_id"], "variant": result["variant"],
            "completed": result["status"] == "ok",
            "all_citations_match": bool(citations) and all(c["quote_matches"] for c in citations),
            "observation_count": len(citations),
            "matching_quotes": sum(c["quote_matches"] for c in citations)}


def summarize(out):
    out = Path(out)
    results = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(out.glob("*/*/result.json"))]
    summary = {}
    for variant in sorted({r["variant"] for r in results}):
        rows = [r for r in results if r["variant"] == variant]
        checks = [mechanical_result(r) for r in rows]
        costs = [r["estimated_cost_usd"] for r in rows if r["estimated_cost_usd"] is not None]
        summary[variant] = {
            "runs": len(rows), "distinct_tasks": len({r["task_id"] for r in rows}),
            "completed": sum(c["completed"] for c in checks),
            "all_quotes_match": sum(c["all_citations_match"] for c in checks),
            "quote_match_rate": (sum(c["matching_quotes"] for c in checks)
                                 / max(1, sum(c["observation_count"] for c in checks))),
            "mean_reading_actions": statistics.mean(r["reading_actions"] or 0 for r in rows),
            "mean_model_calls": statistics.mean(r["api_calls"] for r in rows),
            "mean_latency_seconds": statistics.mean(r["latency_seconds"] for r in rows),
            "median_latency_seconds": statistics.median(r["latency_seconds"] for r in rows),
            "mean_cost_usd": statistics.mean(costs) if len(costs) == len(rows) else None,
            "total_cost_usd": sum(costs) if len(costs) == len(rows) else None,
            "billing_uncertain_runs": sum(r["billing_uncertain"] for r in rows),
        }
    (out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    (out / "mechanical.jsonl").write_text("".join(json.dumps(mechanical_result(r)) + "\n" for r in results), encoding="utf-8")
    header = "| Variant | Completed | All quotes match | Reads/task | API calls/task | USD/task | Seconds/task |\n|---|---:|---:|---:|---:|---:|---:|\n"
    for name, row in summary.items():
        cost = f"{row['mean_cost_usd']:.6f}" if row["mean_cost_usd"] is not None else "unknown"
        header += (f"| {name} | {row['completed']}/{row['runs']} | {row['all_quotes_match']}/{row['runs']} | "
                   f"{row['mean_reading_actions']:.2f} | {row['mean_model_calls']:.2f} | {cost} | "
                   f"{row['mean_latency_seconds']:.2f} |\n")
    (out / "summary.md").write_text(header, encoding="utf-8")
    return summary


def evaluate(sample_path, out, config, variant="both", workers=2, repeats=1, limit=None):
    sample_path, out = Path(sample_path).resolve(), Path(out)
    tasks = load_sample(sample_path)
    if limit is not None:
        tasks = tasks[:limit]
    if not tasks:
        raise ValueError("Empty sample")
    out.mkdir(parents=True, exist_ok=True)
    variants = ["agent", "baseline"] if variant == "both" else [variant]
    revision = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=False).stdout.strip()
    # Include a digest of the actual working source, even before changes are committed.
    source_hash = sha256()
    for source in sorted(Path(__file__).parent.glob("*.py")):
        source_hash.update(source.name.encode())
        source_hash.update(source.read_bytes())
    experiment = {"sample_sha256": file_hash(sample_path), "task_ids": [t["id"] for t in tasks],
                  "config": asdict(config), "variants": variants, "repeats": repeats,
                  "git_revision": revision, "source_sha256": source_hash.hexdigest(),
                  "sample_path": str(sample_path), "workers": workers}
    experiment_path = out / "experiment.json"
    if experiment_path.exists():
        previous = json.loads(experiment_path.read_text(encoding="utf-8"))
        if previous != experiment:
            raise ValueError("Existing experiment has different inputs/code/config; choose a new --out")
    else:
        experiment_path.write_text(json.dumps(experiment, indent=2) + "\n", encoding="utf-8")
    jobs = []
    for repeat in range(1, repeats + 1):
        for task in tasks:
            for kind in variants:
                folder = out / f"{kind}-r{repeat}" / task["id"]
                if (folder / "result.json").exists():
                    print(f"Retaining existing result {folder}", flush=True)
                    continue
                if folder.exists():
                    raise ValueError(f"Incomplete run exists at {folder}; preserve it and choose a new output directory")
                jobs.append((task, kind, folder))
    with ThreadPoolExecutor(max_workers=workers) as pool:
        pending = {pool.submit(run_review, sample_path.parent / task["paper_path"], folder,
                               config, task["id"], kind, metadata=experiment): (task, kind)
                   for task, kind, folder in jobs}
        for future in as_completed(pending):
            task, kind = pending[future]
            result = future.result()
            print(f"{task['id']} {kind}: {result['status']}; calls={result['api_calls']}; "
                  f"seconds={result['latency_seconds']:.1f}", flush=True)
    return summarize(out)
