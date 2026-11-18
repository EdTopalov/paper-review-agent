"""Plan benchmark comparisons offline; execute only through an explicit opt-in.

Every architecture uses the existing reading controller with the same assessment
contract. Reference labels are used only by the offline scorer, never the model.
"""

from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict
from datetime import datetime, timedelta, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import random
import re
import statistics
import subprocess
import time
from zipfile import ZipFile, ZIP_DEFLATED

from openai import OpenAI

from .benchmark_data import (BENCHMARK_VERSION, DEFAULT_BENCHMARK, load_benchmark,
                             read_jsonl)
from .paper import file_hash
from .reporting import render_deliberative_phases
from .runner import VARIANTS, Config, ModelCalls, PRICES, agent, baseline, safe_error, variant_metadata
from .trace import Trace, read_events, read_result


PLAN_VERSION = "benchmark-plan-v1"
PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _source_files():
    paths = sorted(Path(__file__).parent.glob("*.py"))
    paths += [PROJECT_ROOT / name for name in ("pyproject.toml", "requirements-m2.txt", "requirements-m3.txt")
              if (PROJECT_ROOT / name).is_file()]
    return paths


def source_fingerprint():
    fingerprint = sha256()
    for path in _source_files():
        fingerprint.update(path.relative_to(PROJECT_ROOT).as_posix().encode("utf-8"))
        fingerprint.update(path.read_bytes())
    return fingerprint.hexdigest()


def _json_hash(value):
    return sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                             allow_nan=False).encode("utf-8")).hexdigest()


def make_plan(root=DEFAULT_BENCHMARK, split="test", tracks=None, variants=None,
              repeats=3, config=None, workers=3, seed=20261118, *, task_ids=None):
    """Validate frozen inputs and return a reproducible plan without API clients."""
    root = Path(root).resolve()
    config = config or Config()
    variants = list(VARIANTS if variants is None else variants)
    if not variants or len(variants) != len(set(variants)) or set(variants) - set(VARIANTS):
        raise ValueError("Choose a nonempty list of distinct known variants")
    if type(repeats) is not int or repeats < 1 or type(workers) is not int or not 1 <= workers <= 8:
        raise ValueError("Use positive repetitions and 1-8 workers")
    if type(seed) is not int:
        raise ValueError("The scheduling seed must be an integer")
    if (not config.model or not 0 <= config.max_reads <= 20 or config.max_output_tokens < 256
            or not 0 <= config.retries <= 3 or config.timeout <= 0):
        raise ValueError("Invalid model execution limits")
    tasks = load_benchmark(root, split, tracks)
    if task_ids is not None:
        requested = list(task_ids)
        if (not requested or len(requested) != len(set(requested))
                or set(requested) - {task["id"] for task in tasks}):
            raise ValueError("Choose distinct task IDs from the selected split and tracks")
        tasks = [task for task in tasks if task["id"] in requested]
    if not tasks:
        raise ValueError("The selected benchmark slice is empty")
    if any(not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}", task["id"]) for task in tasks):
        raise ValueError("Benchmark IDs must be safe distinct directory names")
    jobs = [{"id": task["id"], "variant": variant, "repeat": repeat,
             "job_id": f"{variant}-r{repeat}/{task['id']}"}
            for repeat in range(1, repeats + 1) for task in tasks for variant in variants]
    random.Random(seed).shuffle(jobs)
    revision = subprocess.run(["git", "rev-parse", "HEAD"], cwd=PROJECT_ROOT,
                              capture_output=True, text=True, check=False).stdout.strip()
    return {"plan_version": PLAN_VERSION, "benchmark_version": BENCHMARK_VERSION,
            "benchmark_root": str(root), "manifest_sha256": file_hash(root / "manifest.jsonl"),
            "benchmark_settings_sha256": file_hash(root / "benchmark.json"),
            "source_sha256": source_fingerprint(), "git_revision": revision,
            "split": split, "tracks": sorted({task["track"] for task in tasks}),
            "task_ids": [task["id"] for task in tasks], "variants": variants,
            "variant_metadata": {variant: variant_metadata(variant) for variant in variants},
            "repeats": repeats, "config": asdict(config), "workers": workers, "seed": seed,
            "jobs": jobs, "tasks": len(tasks), "planned_runs": len(jobs),
            "track_tasks": dict(sorted(Counter(task["track"] for task in tasks).items())),
            "status": "planned_not_executed"}


def _validate_plan(plan, root_override):
    if plan.get("plan_version") != PLAN_VERSION or plan.get("benchmark_version") != BENCHMARK_VERSION:
        raise ValueError("Unknown benchmark plan version")
    root = Path(root_override or plan["benchmark_root"]).resolve()
    expected = make_plan(root, plan["split"], plan["tracks"], plan["variants"],
                         plan["repeats"], Config(**plan["config"]), plan["workers"], plan["seed"],
                         task_ids=plan["task_ids"])
    for field in ("manifest_sha256", "benchmark_settings_sha256", "source_sha256", "task_ids",
                  "variant_metadata", "jobs", "tasks", "planned_runs", "track_tasks"):
        if plan.get(field) != expected[field]:
            raise ValueError(f"Benchmark plan no longer matches its frozen inputs or source: {field}")
    return root


def run_one(public, out, config, task_id, variant, client=None, metadata=None, *, client_factory=None):
    """Execute a public task using a shared controller; no reference parameter exists."""
    from .benchmark_tasks import AssessmentContract, BenchmarkPaper, TASK_PROMPT_VERSION

    if public.get("id") != task_id:
        raise ValueError("Public benchmark task identity mismatch")
    details = variant_metadata(variant)
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    metadata = metadata or {}
    repeat = metadata.get("repeat", 1)
    trace = Trace(out / "trace.jsonl", context={"task_id": task_id, "variant": variant, "repeat": repeat})
    started = time.perf_counter()
    trace.write("run_start", config=asdict(config), trace_version=2,
                benchmark_version=BENCHMARK_VERSION, task_kind=public["kind"],
                prompt_version=TASK_PROMPT_VERSION, harness=details,
                public_task_sha256=_json_hash(public), metadata=metadata,
                pricing_usd_per_million=PRICES.get(config.model))
    calls = ModelCalls(None, config, trace)
    result = {"id": task_id, "task_id": task_id, "kind": public["kind"],
              "variant": variant, "repeat": repeat, "model": config.model,
              "status": "error", "prediction": None, "citation_checks": [],
              "benchmark_version": BENCHMARK_VERSION, "prompt_version": TASK_PROMPT_VERSION,
              "harness": details}
    try:
        paper = BenchmarkPaper(public)
        contract = AssessmentContract(paper, config)
        if len(paper.full_text()) > config.max_paper_chars:
            raise ValueError("paper_exceeds_documented_input_limit")
        if client is not None:
            calls.client = client
        elif client_factory is not None:
            calls.client = client_factory()
        else:
            calls.client = OpenAI(max_retries=0, timeout=config.timeout)
        if variant == "agent":
            prediction, trajectory = agent(paper, calls, config, trace, contract=contract)
        elif variant == "deliberative_review":
            from .deliberative_runner import run_deliberative
            prediction, trajectory = run_deliberative(paper, calls, config, trace, contract=contract)
        elif variant == "baseline":
            prediction, trajectory = baseline(paper, calls, trace, contract=contract)
        else:
            from .pyagent_runner import run_pyagent
            prediction, trajectory = run_pyagent(paper, calls, config, trace, contract=contract)
        contract.validate(prediction)
        result.update(status="ok", prediction=prediction, **trajectory)
        result["citation_checks"] = contract.source_checks(prediction)
    except Exception as exc:
        result["error"] = safe_error(exc)
        if type(exc) in (ValueError, RuntimeError) and str(exc) in {
                "model_decision_budget_exhausted", "paper_exceeds_documented_input_limit",
                "paper_has_no_extractable_text", "pyagent_finished_without_accepted_review",
                "duplicate_evidence", "invalid_selection_candidate",
                "deliberative_infeasible_budget"}:
            result["error"]["code"] = str(exc)
        trace.write("run_error", error=result["error"])
    finally:
        result.update(calls.stats)
        result["latency_seconds"] = time.perf_counter() - started
        trace.write("run_end", result=result)
        trace.close()
        _render_run(out, result)
    return result


def write_progress(out, plan, records, started, status, *, started_at=None, runner_errors=(), error=None):
    """Publish complete JSON snapshots with wall-throughput estimates.

    Completed means a persisted terminal attempt, including model failures.
    Infrastructure errors without an attempt record remain in the remaining
    count and are identified separately. Timings use the latest 20 attempts.
    """
    out = Path(out)
    now = datetime.now(timezone.utc)
    elapsed = max(0.0, time.perf_counter() - started)
    started_at = started_at or (now - timedelta(seconds=elapsed)).isoformat()
    completed = len(records)
    succeeded = sum(row["status"] == "ok" for row in records)
    remaining = plan["planned_runs"] - completed
    throughput = completed / elapsed if completed and elapsed else None
    eta = remaining / throughput if throughput else (0.0 if not remaining else None)
    recent = [row["latency_seconds"] for row in records[-20:]]
    progress = {"schema_version": "benchmark-progress-v1", "status": status,
                "started_at": started_at, "updated_at": now.isoformat(),
                "model": plan["config"]["model"], "variants": plan["variants"],
                "source_sha256": plan.get("source_sha256"), "manifest_sha256": plan.get("manifest_sha256"),
                "total": plan["planned_runs"], "completed": completed, "succeeded": succeeded,
                "failed": completed - succeeded, "remaining": remaining,
                "elapsed_seconds": elapsed, "recent_attempts": len(recent),
                "recent_mean_attempt_seconds": statistics.mean(recent) if recent else None,
                "recent_p50_attempt_seconds": statistics.median(recent) if recent else None,
                "wall_throughput_attempts_per_second": throughput, "eta_remaining_seconds": eta,
                "eta_finish_at": (now + timedelta(seconds=eta)).isoformat() if eta is not None else None,
                "infrastructure_errors": len(runner_errors)}
    if runner_errors:
        progress["latest_runner_error"] = runner_errors[-1]
    if error is not None:
        progress["error"] = safe_error(error)
    temporary = out / "progress.json.tmp"
    with temporary.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(progress, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(out / "progress.json")


def run_plan(plan, out, *, execute=False, client_factory=None, root_override=None):
    """Validate by default. Only execute=True can create clients or run directories."""
    if type(execute) is not bool:
        raise ValueError("Execution requires an explicit boolean opt-in")
    root = _validate_plan(plan, root_override)
    if not execute:
        return {"status": "dry_run", "tasks": plan["tasks"], "planned_runs": plan["planned_runs"],
                "variants": plan["variants"], "repeats": plan["repeats"], "model_calls": 0,
                "out": str(out), "execution_enabled": False}
    tasks = [task for task in load_benchmark(root, plan["split"], plan["tracks"])
             if task["id"] in plan["task_ids"]]
    by_id = {task["id"]: task for task in tasks}
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    started_at = datetime.now(timezone.utc).isoformat()
    started = time.perf_counter()
    config = Config(**plan["config"])
    records = []
    runner_errors = []

    def dispatch(job):
        task = by_id[job["id"]]
        metadata = {"repeat": job["repeat"], "track": task["track"],
                    "input_sha256": task["input_sha256"], "manifest_sha256": plan["manifest_sha256"],
                    "source_sha256": plan["source_sha256"], "plan_sha256": _json_hash(plan)}
        result = run_one(task["input"], out / job["job_id"], config, job["id"],
                         job["variant"], metadata=metadata, client_factory=client_factory)
        return {**result, "track": task["track"], "trace_path": job["job_id"] + "/trace.jsonl"}

    try:
        write_progress(out, plan, records, started, "running", started_at=started_at)
        (out / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        with ZipFile(out / "source.zip", "x", compression=ZIP_DEFLATED) as archive:
            for path in _source_files():
                archive.write(path, path.relative_to(PROJECT_ROOT).as_posix())
        with (out / "records.jsonl").open("x", encoding="utf-8", newline="\n") as stream, \
                (out / "runner_errors.jsonl").open("x", encoding="utf-8", newline="\n") as error_stream:
            with ThreadPoolExecutor(max_workers=plan["workers"]) as pool:
                pending = {pool.submit(dispatch, job): job for job in plan["jobs"]}
                try:
                    for future in as_completed(pending):
                        try:
                            record = future.result()
                        except Exception as exc:
                            failure = {**pending[future], "error": safe_error(exc)}
                            runner_errors.append(failure)
                            error_stream.write(json.dumps(failure, ensure_ascii=False) + "\n")
                            error_stream.flush()
                            os.fsync(error_stream.fileno())
                        else:
                            stream.write(json.dumps(record, ensure_ascii=False, allow_nan=False) + "\n")
                            stream.flush()
                            os.fsync(stream.fileno())
                            records.append(record)
                        write_progress(out, plan, records, started, "running", started_at=started_at, runner_errors=runner_errors)
                except BaseException as exc:
                    for future in pending:
                        future.cancel()
                    write_progress(out, plan, records, started, "error", started_at=started_at, runner_errors=runner_errors, error=exc)
                    raise
        if runner_errors:
            raise RuntimeError("benchmark_worker_failed")
        from .benchmark_scoring import score_predictions
        scores = score_predictions(tasks, records, variants=plan["variants"], repeats=plan["repeats"])
        (out / "scores.json").write_text(json.dumps(scores, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
                                          encoding="utf-8", newline="\n")
        _render_report(out, plan, records, scores)
        write_progress(out, plan, records, started, "finished", started_at=started_at)
        return {"status": "executed", "runs": len(records), "completed": sum(row["status"] == "ok" for row in records),
                "out": str(out), "scores": scores}
    except BaseException as exc:
        write_progress(out, plan, records, started, "error", started_at=started_at, runner_errors=runner_errors, error=exc)
        raise


def _render_run(out, result):
    lines = [f"# {result['task_id']}", "", f"{result['variant']} · repeat {result['repeat']} · {result['status']}", "",
             f"{result['api_calls']} API calls · {result['input_tokens']} input tokens · "
             f"{result['output_tokens']} output tokens · estimated USD {result['estimated_cost_usd']}", "",
             "[Full trace](trace.jsonl). This output contains no reference labels.", "",
             "```json", json.dumps(result.get("prediction") or result.get("error"), ensure_ascii=False, indent=2), "```", ""]
    phase_report = render_deliberative_phases(read_events(out / "trace.jsonl"))
    if phase_report:
        lines += [phase_report, ""]
    (out / "README.md").write_text("\n".join(lines), encoding="utf-8")


def _render_report(out, plan, records, scores):
    lines = ["# Evidence-assessment benchmark experiment", "",
             f"Model: `{plan['config']['model']}`. Split: `{plan['split']}`. "
             f"{plan['tasks']} tasks per variant and {plan['repeats']} repetitions.", "",
             "[Frozen plan](plan.json) · [Evaluated source](source.zip) · "
             "[Per-track quality scores](scores.json) · [Attempt records](records.jsonl)", "",
             "Completion is a returned prediction, not a correctness score. Quality is reported separately "
             "for each track; evidence matching does not establish that the explanation is sound. "
             "Costs include failed attempts and retries.", "",
             "| Variant | Completed / attempts | Calls / attempt | Input/output tokens / attempt | USD / attempt | Seconds / attempt |",
             "|---|---:|---:|---:|---:|---:|"]
    for variant in plan["variants"]:
        rows = [row for row in records if row["variant"] == variant]
        costs = [row["estimated_cost_usd"] for row in rows]
        cost = f"{statistics.mean(costs):.6f}" if all(value is not None for value in costs) else "unknown"
        lines.append(f"| {variant} | {sum(row['status'] == 'ok' for row in rows)}/{len(rows)} | "
                     f"{statistics.mean(row['api_calls'] for row in rows):.2f} | "
                     f"{statistics.mean(row['input_tokens'] for row in rows):.1f}/"
                     f"{statistics.mean(row['output_tokens'] for row in rows):.1f} | {cost} | "
                     f"{statistics.mean(row['latency_seconds'] for row in rows):.2f} |")
    lines += ["", "## Content by track", "",
              "Repeat values show run variation before pooling. Failures remain in every denominator. "
              "The JSON report includes evidence F1, category slices, group intervals, and per-attempt costs.", "",
              "| Track | Variant | Primary measure | Each repeat | Pooled |",
              "|---|---|---|---|---:|"]
    for track in plan["tracks"]:
        for variant in plan["variants"]:
            summary = scores["variants"][variant]["tracks"][track]
            if track == "qasper":
                metric, value = "Answer F1", lambda row: row["mean_answer_f1"]
            elif track == "reviewcritique":
                metric, value = "Binary macro-F1", lambda row: row["classification"]["macro_f1"]
            else:
                metric, value = "Choice accuracy" if track == "selection" else "Verdict accuracy", lambda row: row["content_success_rate"]
            repeats = "; ".join(f"r{repeat}: {value(row):.3f}" for repeat, row in summary["per_repeat"].items())
            lines.append(f"| {track} | {variant} | {metric} | {repeats} | {value(summary):.3f} |")
    lines += ["", "## Attempts", ""]
    lines += [f"- [{row['variant']}-r{row['repeat']}/{row['id']}]({Path(row['trace_path']).parent.as_posix()}/README.md): {row['status']}"
              for row in sorted(records, key=lambda row: (row["variant"], row["repeat"], row["id"]))]
    lines += [""]
    (out / "README.md").write_text("\n".join(lines), encoding="utf-8")


def check_runs(out):
    """Check trace integrity and accounting; model failures remain valid outcomes."""
    out = Path(out)
    plan = json.loads((out / "plan.json").read_text(encoding="utf-8"))
    records = read_jsonl(out / "records.jsonl")
    expected = {(job["id"], job["variant"], job["repeat"]): job for job in plan["jobs"]}
    actual = [(row["id"], row["variant"], row["repeat"]) for row in records]
    if len(actual) != len(set(actual)) or set(actual) != set(expected):
        raise ValueError("Benchmark attempt records differ from the planned grid")
    rows = []
    for record in records:
        key = record["id"], record["variant"], record["repeat"]
        path = out / expected[key]["job_id"] / "trace.jsonl"
        events = read_events(path)
        result = read_result(path)
        flags = {"terminal_result": result is not None,
                 "sequence": [event["seq"] for event in events] == list(range(1, len(events) + 1)),
                 "identity": all(event.get("task_id") == key[0] and event.get("variant") == key[1]
                                 and event.get("repeat") == key[2] for event in events),
                 "call_accounting": sum(event["event"] == "model_request" for event in events) == record["api_calls"],
                 "response_accounting": sum(event["event"] == "model_response" for event in events) == record["successful_model_calls"],
                 "reading_budget": record["reading_actions"] <= plan["config"]["max_reads"],
                 "decision_budget": record["decision_steps"] <= (1 if key[1] == "baseline" else plan["config"]["max_reads"] + 3),
                 "result_identity": bool(result and all(result.get(field) == record.get(field)
                                                        for field in result))}
        rows.append({"id": key[0], "variant": key[1], "repeat": key[2], "checks": flags,
                     "all_checks_pass": all(flags.values())})
    return {"runs": len(rows), "passed": sum(row["all_checks_pass"] for row in rows),
            "failures": [row for row in rows if not row["all_checks_pass"]]}
