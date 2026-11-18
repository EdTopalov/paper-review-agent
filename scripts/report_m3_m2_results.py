"""Build the original 20-paper M2 appendix from terminal traces, entirely offline.

Only complete repetitions shared by all four methods enter each model block.
Trace files remain in place; virtual paths adapt global launcher rounds to the
existing repetition statistics without copying or changing the raw evidence.
"""

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
from hashlib import sha256
import json
from math import isfinite
import os
from pathlib import Path
import statistics

from paper_review.evaluation import load_sample, mechanical_result, repetition_statistics
from paper_review.paper import file_hash


REPOSITORY = Path(__file__).resolve().parents[1]
VARIANTS = ("agent", "pyagent_react", "deliberative_review", "baseline")
DEFAULT_EXPERIMENTS = (
    "runs/m3-existing-20261118-luna6",
    "runs/m3-deliberative-20261118-luna6",
)
MEANS = {"decision_steps": "mean_decision_steps", "reading_actions": "mean_reading_actions",
         "tool_calls": "mean_tool_calls", "api_calls": "mean_model_calls",
         "input_tokens": "mean_input_tokens", "output_tokens": "mean_output_tokens",
         "latency_seconds": "mean_latency_seconds"}


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def display_path(path):
    path = Path(path).resolve()
    return path.relative_to(REPOSITORY).as_posix() if path.is_relative_to(REPOSITORY) else path.as_posix()


def read_terminal(path):
    """Read physical JSONL lines; an unfinished last line is an active attempt."""
    start, result, digest = None, None, sha256()
    with Path(path).open("rb") as stream:
        for line in stream:
            digest.update(line)
            if not line.strip():
                continue
            try:
                event = json.loads(line)
            except (json.JSONDecodeError, UnicodeDecodeError):
                if not line.endswith(b"\n"):
                    return None
                raise ValueError(f"Malformed persisted trace: {path}") from None
            if event.get("event") == "run_start":
                if start is not None:
                    raise ValueError(f"Duplicate run_start: {path}")
                start = event
            elif event.get("event") == "run_end":
                if result is not None:
                    raise ValueError(f"Duplicate run_end: {path}")
                result = event["result"]
    if result is None:
        return None
    if start is None:
        raise ValueError(f"Terminal trace has no run_start: {path}")
    return {"start": start, "result": result, "sha256": digest.hexdigest()}


def attempt_summary(rows):
    checks = [mechanical_result(row) for row in rows]
    verified = [check["completed"] and check["all_citations_verified"] is True for check in checks]
    available = all(check["all_citations_verified"] is not None for check in checks)
    costs = [row.get("estimated_cost_usd") for row in rows]
    output = {"attempts": len(rows), "completed": sum(check["completed"] for check in checks),
              "verified_successes": sum(verified) if available else None,
              "completion_rate": statistics.mean(check["completed"] for check in checks),
              "verified_success_rate": statistics.mean(verified) if available else None,
              "mean_cost_usd": statistics.mean(costs) if all(value is not None for value in costs) else None,
              "unknown_cost_attempts": sum(value is None for value in costs),
              "billing_uncertain_attempts": sum(bool(row.get("billing_uncertain")) for row in rows),
              "error_counts": dict(Counter(json.dumps(row["error"], sort_keys=True)
                                           for row in rows if row.get("error")))}
    for field, name in MEANS.items():
        values = [row[field] for row in rows]
        if any(isinstance(value, bool) or not isinstance(value, (int, float)) or not isfinite(value)
               or value < 0 for value in values):
            raise ValueError(f"Invalid recorded metric: {field}")
        output[name] = statistics.mean(values)
    if any(value is not None and (isinstance(value, bool) or not isinstance(value, (int, float))
                                 or not isfinite(value) or value < 0) for value in costs):
        raise ValueError("Invalid recorded cost")
    return output


def collect_model(experiments, task_ids, sample_sha256):
    """Validate immutable stage identities and select complete common rounds."""
    attempts, provenance, notes = {}, [], []
    configurations, rubrics, checkers = set(), set(), set()
    sources = defaultdict(set)
    model = None
    for root in experiments:
        root = Path(root).resolve()
        settings = read_json(root / "experiment.json")
        if model is not None and model != settings["model"]:
            raise ValueError("Do not pool different models")
        model = settings["model"]
        if settings.get("m2_sample_sha256") != sample_sha256:
            raise ValueError(f"Original M2 sample differs: {root}")
        for plan_path in sorted(root.glob("r*/m2/experiment.json")):
            stage = plan_path.parent
            raw_round = stage.parent.name[1:]
            if not raw_round.isdigit() or int(raw_round) < 1:
                raise ValueError(f"Invalid global round: {stage}")
            number, plan = int(raw_round), read_json(plan_path)
            methods = plan["variants"]
            if (plan.get("sample_sha256") != sample_sha256 or set(plan["task_ids"]) != set(task_ids)
                    or len(plan["task_ids"]) != len(task_ids) or plan["repeats"] != 1
                    or plan["config"]["model"] != model or not methods
                    or len(methods) != len(set(methods)) or set(methods) - set(VARIANTS)
                    or set(methods) - set(settings["variants"])):
                raise ValueError(f"Stage does not match the frozen M2 sample: {stage}")
            configurations.add(json.dumps(plan["config"], sort_keys=True))
            rubrics.add(plan["rubric_version"])
            checkers.add(plan["checker_version"])
            allowed = {stage / f"{variant}-r1" / task / "trace.jsonl"
                       for variant in methods for task in task_ids}
            if set(stage.glob("*/*/trace.jsonl")) - allowed:
                raise ValueError(f"Unexpected trace identity: {stage}")
            for variant in methods:
                key = variant, number
                if key in attempts:
                    raise ValueError(f"Duplicate method/global round: {model}/{key}")
                sources[variant].add(plan["source_sha256"])
                terminal = {}
                for task in task_ids:
                    path = stage / f"{variant}-r1" / task / "trace.jsonl"
                    row = read_terminal(path) if path.exists() else None
                    if row is None:
                        continue
                    start, result = row["start"], row["result"]
                    if (result.get("task_id") != task or result.get("variant") != variant
                            or result.get("model") != model or result.get("status") not in ("ok", "error")
                            or start.get("task_id") != task or start.get("variant") != variant
                            or start.get("config") != plan["config"]
                            or start.get("metadata", {}).get("source_sha256") != plan["source_sha256"]
                            or start.get("metadata", {}).get("sample_sha256") != sample_sha256
                            or result.get("checker_version") != plan["checker_version"]
                            or result.get("rubric_version") != plan["rubric_version"]):
                        raise ValueError(f"Trace identity or provenance mismatch: {path}")
                    terminal[task] = {**row, "path": path}
                attempts[key] = terminal
                if len(terminal) != len(task_ids):
                    notes.append(f"Excluded incomplete {variant} round {number}: "
                                 f"{len(terminal)}/{len(task_ids)} terminal attempts.")
            progress_path = stage / "progress.json"
            progress = read_json(progress_path) if progress_path.exists() else {}
            provenance.append({"experiment": display_path(root), "global_round": number,
                               "plan_path": display_path(plan_path), "source_archive": display_path(stage / "source.zip"),
                               "source_sha256": plan["source_sha256"], "git_revision": plan.get("git_revision"),
                               "sample_sha256": sample_sha256, "config": plan["config"], "variants": methods,
                               "variant_metadata": plan.get("variant_metadata"), "workers": plan.get("workers"),
                               "order_seed": plan.get("order_seed"), "started_at": progress.get("started_at"),
                               "updated_at": progress.get("updated_at")})
    if len(configurations) > 1 or len(rubrics) > 1 or len(checkers) > 1:
        raise ValueError("Compared M2 stages use different resource limits, rubrics, or citation checkers")
    if any(len(values) != 1 for values in sources.values()):
        raise ValueError("A method changes frozen source within a model block")
    complete = {variant: sorted(number for (method, number), rows in attempts.items()
                               if method == variant and set(rows) == set(task_ids)) for variant in VARIANTS}
    common = sorted(set.intersection(*(set(complete[variant]) for variant in VARIANTS)))
    return {"model": model, "attempts": attempts, "common_rounds": common,
            "complete_rounds_by_method": complete, "provenance": provenance, "notes": notes,
            "source_sha256_by_method": {variant: next(iter(values)) for variant, values in sources.items()}}


def summarize_model(collected, task_ids, out):
    common, records, trace_rows = collected["common_rounds"], [], []
    # The shared helper requires dense repeats. Keep a reversible global-round
    # mapping so an interrupted middle round never relabels raw trace identities.
    repeat_map = {index: number for index, number in enumerate(common, 1)}
    for analysis_repeat, global_round in repeat_map.items():
        for variant in VARIANTS:
            for task in task_ids:
                row = collected["attempts"][variant, global_round][task]
                result = row["result"]
                virtual = Path(f"{variant}-r{analysis_repeat}") / task / "trace.jsonl"
                records.append((virtual, result))
                trace_rows.append({"global_round": global_round, "analysis_repeat": analysis_repeat,
                    "source_repeat": 1, "variant": variant, "task_id": task, "trace_path": display_path(row["path"]),
                    "trace_link": Path(os.path.relpath(row["path"], out)).as_posix(),
                    "trace_sha256": row["sha256"], "status": result["status"],
                    "verified_success": result["status"] == "ok" and mechanical_result(result)["all_citations_verified"] is True,
                    "score": result.get("review", {}).get("score") if result.get("review") else None,
                    **{field: result[field] for field in MEANS},
                    "estimated_cost_usd": result.get("estimated_cost_usd"), "error": result.get("error")})
    repeated = repetition_statistics(records) if records else {}  # Once per model.
    methods = {}
    for variant in VARIANTS:
        rows = [result for _, result in records if result["variant"] == variant]
        if not rows:
            continue
        per_repeat = [{"global_round": number, **attempt_summary(
            [collected["attempts"][variant, number][task]["result"] for task in task_ids])} for number in common]
        methods[variant] = {**attempt_summary(rows), "per_repeat": per_repeat,
                            "repetition_statistics": repeated[variant]}
    return {key: value for key, value in collected.items() if key != "attempts"} | {
        "analysis_repeat_to_global_round": repeat_map, "methods": methods, "attempts": trace_rows}


def number(value, digits=2):
    return "unknown" if value is None else f"{value:.{digits}f}"


def render_markdown(report, out):
    lines = ["# Original 20-paper review results", "",
        "[Machine-readable results, per-paper statistics, and raw trace links](m2-results.json)", "",
        "Each model block uses only complete repetitions shared by all four methods. "
        "Every included repetition has the unchanged 20 papers. Failed attempts remain in "
        "completion, token, cost, and latency denominators. Verified success means a completed "
        "review whose citations all pass the source checker; it does not measure assessment quality.", "",
        "Steps are controller decisions; calls are API requests including retries. Tokens, USD "
        "and seconds are means per attempted paper, including failures. Unknown costs stay unknown.", ""]
    if (out / "checks.json").exists():
        lines += ["[Trace checks](checks.json) retain intermediate argument-validation flags separately. "
                  "Such flags do not remove terminal attempts from this comparison.", ""]
    for model, block in report["models"].items():
        rounds = block["common_rounds"]
        lines += [f"## {model}", "", f"Shared global rounds: {rounds or 'none yet'}. "
                  f"Denominator per method: 20 × {len(rounds)} = {20 * len(rounds)} attempts.", ""]
        if not rounds:
            lines += ["No complete comparison is available yet.", ""]
            continue
        lines += ["| Method | Completed | Verified | Steps | Calls | Input tokens | Output tokens | USD/task | Seconds/task |",
                  "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
        for variant in VARIANTS:
            row = block["methods"][variant]
            lines.append(f"| {variant} | {row['completed']}/{row['attempts']} | "
                f"{row['verified_successes']}/{row['attempts']} | {row['mean_decision_steps']:.2f} | "
                f"{row['mean_model_calls']:.2f} | {row['mean_input_tokens']:.0f} | "
                f"{row['mean_output_tokens']:.0f} | {number(row['mean_cost_usd'], 6)} | "
                f"{row['mean_latency_seconds']:.2f} |")
        lines += ["", "Per-repetition variation (counts are out of 20):", "",
                  "| Method | Completed by round | Verified by round | USD/task by round | Seconds/task by round |",
                  "|---|---|---|---|---|"]
        for variant in VARIANTS:
            rows = block["methods"][variant]["per_repeat"]
            cells = [variant] + [", ".join(number(row[field], digits) for row in rows)
                for field, digits in (("completed", 0), ("verified_successes", 0),
                                      ("mean_cost_usd", 6), ("mean_latency_seconds", 2))]
            lines.append("| " + " | ".join(cells) + " |")
        lines += ["", "Verified pass^k (all k attempts succeed):", "",
                  "| Method | " + " | ".join(f"k={k}" for k in range(1, len(rounds) + 1)) + " |",
                  "|---|" + "---:|" * len(rounds)]
        for variant in VARIANTS:
            values = block["methods"][variant]["repetition_statistics"]["pass_power_k"]
            lines.append("| " + variant + " | " + " | ".join(
                number(values[str(k)] if values else None, 3) for k in range(1, len(rounds) + 1)) + " |")
        lines += ["", "Paired verified-success difference versus baseline (percentage points):", "",
                  "| Method | Mean difference | 95% paper bootstrap interval |", "|---|---:|---:|"]
        for variant in VARIANTS[:-1]:
            left, right = sorted((variant, "baseline"))
            estimate = block["methods"][left]["repetition_statistics"]["paired_comparisons"][right]["verified_success_rate"]
            sign = 1 if left == variant else -1
            mean = estimate["mean_difference"]
            interval = estimate["ci95"]
            mean_text = number(sign * mean * 100 if mean is not None else None)
            bounds = sorted(sign * value * 100 for value in interval) if interval else None
            interval_text = f"[{bounds[0]:.2f}, {bounds[1]:.2f}]" if bounds else "unavailable"
            lines.append(f"| {variant} | {mean_text} | {interval_text} |")
        lines.append("")
    lines += ["For a paper with s verified successes in n repetitions, pass^k is "
        "C(s,k)/C(n,k), averaged over the 20 papers. It estimates success on every one "
        "of k independent attempts; independence is an assumption. Few repetitions cannot "
        "establish stable reliability or capture future provider changes.", "",
        "The JSON includes paired 95% bootstrap intervals over 20 papers, keeping each "
        "paper's repetitions together (2,000 resamples; fixed seed). Review-score differences "
        "describe rating disagreement, without a ground-truth quality score. Models remain "
        "separate. Different methods can have different frozen source archives and start times; "
        "the recorded scheduling blocks do not control provider drift or shared-load latency.", "",
        "Rebuild offline from the repository root:", "", "```shell",
        "python scripts/report_m3_m2_results.py " + " ".join(report["experiments"]) + " --out " + display_path(out),
        "```", ""]
    (out / "M2.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def generate(experiments, out, *, sample=REPOSITORY / "data/eval/tasks.jsonl"):
    roots, out = [Path(path).resolve() for path in experiments], Path(out).resolve()
    if len(roots) != len(set(roots)):
        raise ValueError("Do not supply an experiment directory twice")
    tasks = load_sample(sample)
    if len(tasks) != 20:
        raise ValueError("Expected the unchanged 20-paper M2 sample")
    task_ids, sample_sha256 = [task["id"] for task in tasks], file_hash(sample)
    by_model = defaultdict(list)
    for root in roots:
        by_model[read_json(root / "experiment.json")["model"]].append(root)
    report = {"schema_version": "m3-original-m2-results-v1", "generated_at": datetime.now(timezone.utc).isoformat(),
              "sample_sha256": sample_sha256, "task_ids": task_ids,
              "experiments": [display_path(path) for path in roots], "models": {}}
    for model, paths in by_model.items():
        report["models"][model] = summarize_model(collect_model(paths, task_ids, sample_sha256), task_ids, out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "m2-results.json").write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
                                         encoding="utf-8", newline="\n")
    render_markdown(report, out)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("experiments", type=Path, nargs="*", default=list(DEFAULT_EXPERIMENTS))
    parser.add_argument("--sample", type=Path, default=REPOSITORY / "data/eval/tasks.jsonl")
    parser.add_argument("--out", type=Path, default=Path("milestones/M3-results"))
    args = parser.parse_args()
    report = generate(args.experiments, args.out, sample=args.sample)
    print(json.dumps({"out": str(args.out), "complete_rounds": {
        model: block["common_rounds"] for model, block in report["models"].items()}, "model_calls": 0}, indent=2))


if __name__ == "__main__":
    main()
