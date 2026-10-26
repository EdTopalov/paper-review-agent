"""Frozen task validation and mechanical evaluation; not semantic truth labels."""

from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict
from hashlib import sha256
import json
from pathlib import Path
import statistics
import subprocess
from zipfile import ZipFile, ZIP_DEFLATED

import jsonschema

from .paper import Paper, file_hash
from .runner import run_review
from .citations import CHECKER_VERSION
from .prompts import PROMPT_VERSION, RUBRIC_VERSION
from .trace import read_events, read_result
from .reporting import render_run, render_experiment
from .schema import TOOLS


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
    verified_available = "checker_version" in result
    first = result.get("first_submission_checks") or []
    return {"task_id": result["task_id"], "variant": result["variant"],
            "completed": result["status"] == "ok",
            "all_citations_match": bool(citations) and all(c["quote_matches"] for c in citations),
            "observation_count": len(citations),
            "matching_quotes": sum(c["quote_matches"] for c in citations),
            "all_citations_verified": (bool(citations) and all(c["citation_verified"] for c in citations))
                if verified_available else None,
            "verified_citations": sum(c["citation_verified"] for c in citations) if verified_available else None,
            "first_submission_verified": bool(first) and all(c["citation_verified"] for c in first)
                if verified_available else None,
            "first_submission_observed": bool(first) and all(c.get("observed", True) for c in first)
                if verified_available else None}


def validate_experiment_runs(root, records):
    """Require every planned run and keep result identities bound to their folders."""
    settings_path = root / "experiment.json"
    if not settings_path.exists():
        return  # Standalone traces and selected archived failures have no plan.
    settings = json.loads(settings_path.read_text(encoding="utf-8"))
    expected = {root / f"{variant}-r{repeat}" / task_id / "trace.jsonl"
                for variant in settings["variants"]
                for repeat in range(1, settings["repeats"] + 1)
                for task_id in settings["task_ids"]}
    actual = {path for path, _ in records}
    missing = sorted(path.relative_to(root).as_posix() for path in expected - actual)
    unexpected = sorted(path.relative_to(root).as_posix() for path in actual - expected)
    if missing or unexpected:
        raise ValueError(f"Experiment run set mismatch: missing={missing}; unexpected={unexpected}")
    for path, result in records:
        if result is not None and (result["task_id"] != path.parent.name
                                   or result["variant"] != path.parent.parent.name.rsplit("-r", 1)[0]):
            raise ValueError(f"Run identity mismatch: {path.relative_to(root).as_posix()}")


def summarize(out):
    out = Path(out)
    records = [(p, read_result(p)) for p in sorted(out.glob("*/*/trace.jsonl"))]
    validate_experiment_runs(out, records)
    if not records or any(result is None for _, result in records):
        raise ValueError("No completed trace set found; inspect incomplete runs before summarizing")
    results = [result for _, result in records]
    summary = {}
    for variant in sorted({r["variant"] for r in results}):
        rows = [r for r in results if r["variant"] == variant]
        checks = [mechanical_result(r) for r in rows]
        costs = [r["estimated_cost_usd"] for r in rows if r["estimated_cost_usd"] is not None]
        verification_available = all(c["all_citations_verified"] is not None for c in checks)
        summary[variant] = {
            "runs": len(rows), "distinct_tasks": len({r["task_id"] for r in rows}),
            "completed": sum(c["completed"] for c in checks),
            "all_quotes_match": sum(c["all_citations_match"] for c in checks),
            "quote_match_rate": (sum(c["matching_quotes"] for c in checks)
                                 / max(1, sum(c["observation_count"] for c in checks))),
            "all_citations_verified": sum(c["all_citations_verified"] for c in checks) if verification_available else None,
            "citation_verification_rate": sum(c["verified_citations"] for c in checks)
                / max(1, sum(c["observation_count"] for c in checks)) if verification_available else None,
            "first_submission_verified": sum(c["first_submission_verified"] for c in checks) if verification_available else None,
            "first_submission_observed": sum(c["first_submission_observed"] for c in checks) if verification_available else None,
            "mean_rejected_submissions": statistics.mean(r.get("rejected_submissions", 0) for r in rows),
            "recovered_citation_runs": sum(r.get("rejected_submissions", 0) > 0 and r["status"] == "ok" for r in rows),
            "citation_status_counts": {status: sum(c.get("status") == status for r in rows for c in r.get("citation_checks", []))
                                       for status in ("exact", "whitespace", "normalized", "wrong_page", "hyphenation_ambiguous", "not_found")},
            "mean_reading_actions": statistics.mean(r["reading_actions"] or 0 for r in rows),
            "mean_model_calls": statistics.mean(r["api_calls"] for r in rows),
            "mean_latency_seconds": statistics.mean(r["latency_seconds"] for r in rows),
            "median_latency_seconds": statistics.median(r["latency_seconds"] for r in rows),
            "mean_cost_usd": statistics.mean(costs) if len(costs) == len(rows) else None,
            "total_cost_usd": sum(costs) if len(costs) == len(rows) else None,
            "billing_uncertain_runs": sum(r["billing_uncertain"] for r in rows),
        }
    audits = {p: audit for p, _ in records if (audit := read_result(p, audit=True))}
    for path, _ in records:
        render_run(path)
    render_experiment(out, summary, records, audits)
    return summary


def check_experiment(root):
    """Inspect trajectories without generating additional files."""
    root = Path(root)
    paths = [root / "trace.jsonl"] if (root / "trace.jsonl").exists() else sorted(root.glob("*/*/trace.jsonl"))
    if not paths:
        raise ValueError("No traces found")
    records = [(path, read_result(path)) for path in paths]
    validate_experiment_runs(root, records)
    schemas = {tool["name"]: tool["parameters"] for tool in TOOLS}
    rows = []
    for path, result in records:
        events = read_events(path)
        end = next((i for i, e in enumerate(events) if e["event"] == "run_end"), len(events) - 1)
        run = events[:end + 1]
        decisions = [e for e in run if e["event"] == "decision"]
        reads = [e for e in run if e["event"] == "tool_call" and e["name"] in ("search_paper", "read_pages")]
        valid_arguments = True
        for decision in decisions:
            if decision["action"] == "final_answer":
                continue
            try:
                jsonschema.validate(json.loads(decision["arguments"]), schemas[decision["action"]])
            except (KeyError, ValueError, jsonschema.ValidationError):
                valid_arguments = False
        flags = {
            "sequence": [e["seq"] for e in events] == list(range(1, len(events) + 1)),
            "terminal_result": result is not None,
            "reading_budget": len(reads) <= events[0]["config"]["max_reads"],
            "valid_arguments": valid_arguments,
            "call_accounting": sum(e["event"] == "model_request" for e in run) == (result or {}).get("api_calls"),
            "response_accounting": sum(e["event"] == "model_response" for e in run) == (result or {}).get("successful_model_calls"),
            "stop_recorded": (bool(decisions) and decisions[-1]["action"] in ("submit_review", "final_answer"))
                or bool(result and result.get("error")),
        }
        audit_starts = [i for i, e in enumerate(events) if e["event"] == "audit_start"]
        if audit_starts:
            audit_events = events[audit_starts[-1]:]
            audit = read_result(path, audit=True)
            flags["audit_terminal_result"] = audit is not None
            flags["audit_call_accounting"] = sum(e["event"] == "model_request" for e in audit_events) == (audit or {}).get("api_calls")
            flags["audit_response_accounting"] = sum(e["event"] == "model_response" for e in audit_events) == (audit or {}).get("successful_model_calls")
        rows.append({"trace": str(path), "checks": flags, "all_checks_pass": all(flags.values())})
    return {"runs": len(rows), "passed": sum(r["all_checks_pass"] for r in rows),
            "failures": [r for r in rows if not r["all_checks_pass"]]}
def evaluate(sample_path, out, config, variant="both", workers=2, repeats=1, limit=None):
    sample_path, out = Path(sample_path).resolve(), Path(out)
    tasks = load_sample(sample_path)
    if any(task["instructions_version"] != RUBRIC_VERSION for task in tasks):
        raise ValueError("Sample instructions do not match the frozen common rubric")
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
                  "prompt_version": PROMPT_VERSION, "rubric_version": RUBRIC_VERSION,
                  "checker_version": CHECKER_VERSION,
                  "sample_path": str(sample_path), "workers": workers}
    experiment_path = out / "experiment.json"
    if experiment_path.exists():
        previous = json.loads(experiment_path.read_text(encoding="utf-8"))
        if previous != experiment:
            raise ValueError("Existing experiment has different inputs/code/config; choose a new --out")
    else:
        experiment_path.write_text(json.dumps(experiment, indent=2) + "\n", encoding="utf-8")
        project = Path(__file__).resolve().parents[2] / "pyproject.toml"
        with ZipFile(out / "source.zip", "x", compression=ZIP_DEFLATED) as archive:
            for source in sorted(Path(__file__).parent.glob("*.py")):
                archive.write(source, "src/paper_review/" + source.name)
            if project.exists():
                archive.write(project, project.name)
            lockfile = project.with_name("requirements-m2.txt")
            if lockfile.exists():
                archive.write(lockfile, lockfile.name)
    jobs = []
    for repeat in range(1, repeats + 1):
        for task in tasks:
            for kind in variants:
                folder = out / f"{kind}-r{repeat}" / task["id"]
                if (folder / "trace.jsonl").exists() and read_result(folder / "trace.jsonl") is not None:
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
