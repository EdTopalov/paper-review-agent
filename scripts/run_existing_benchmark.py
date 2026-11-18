"""Run a repeated agent comparison on the original M2 and assessment benchmarks.

Without --execute this validates plans only. Each immutable stage has one local
repetition; aggregate copies use the global round and retain source provenance.
"""

import argparse
from collections import Counter
from contextlib import redirect_stdout
import json
import os
from pathlib import Path
import sys
from datetime import datetime, timezone

from dotenv import load_dotenv

from paper_review.benchmark_data import DEFAULT_BENCHMARK, load_benchmark, read_jsonl
from paper_review.benchmark_runner import make_plan, run_plan
from paper_review.benchmark_scoring import score_predictions
from paper_review.evaluation import evaluate, load_sample
from paper_review.paper import file_hash
from paper_review.runner import Config, VARIANTS as AVAILABLE_VARIANTS, safe_error


DEFAULT_VARIANTS = ("agent", "pyagent_react", "baseline")
STAGES = [("core", ["qasper", "reviewcritique", "controlled"], 5),
          ("selection", ["selection"], 20)]


def write_json(path, value):
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
                         encoding="utf-8", newline="\n")
    temporary.replace(path)


def progress(out, **fields):
    fields["updated_at"] = datetime.now(timezone.utc).isoformat()
    write_json(out / "progress.json", fields)


def render_report(out, records, scores, completed_rounds, planned_rounds, planned_attempts,
                  m2_rounds, m2_planned, variants):
    m2_completed = sum(sum(value["runs"] for value in row["summary"].values()) for row in m2_rounds)
    lines = ["# Repeated agent comparison", "",
             f"Completed rounds: {completed_rounds}/{planned_rounds}. "
             f"Terminal attempts: {len(records) + m2_completed}/{planned_attempts}. "
             f"Benchmark: {len(records)}/{planned_attempts - m2_planned}; "
             f"original M2: {m2_completed}/{m2_planned}.", "",
             "[Progress](progress.json) · [Aggregate attempts](records.jsonl) · "
             "[Offline scores](scores.json)", "",
             "Methods: " + ", ".join(f"`{variant}`" for variant in variants) + ". "
             "Failed attempts remain in all-attempt content, cost, "
             "and latency denominators. Citation matching does not establish semantic support.", "",
             "Each round starts with the original M2 sample when enabled, followed by a "
             "benchmark core stage (five reading actions) and a selection stage "
             "(20 reading actions). Each stage has its own immutable configuration, source archive, "
             "records, and traces under `r<round>/<stage>/`. Stages use one local repeat. "
             "Aggregate copies set `repeat` to the global round, retain `source_repeat: 1` "
             "and `source_round`, and point `trace_path` to the original trace. Original "
             "trace identities are unchanged.", "",
             "Benchmark scores are refreshed only after both benchmark stages complete a full round. "
             "An unfinished next round can have additional aggregate records without "
             "entering the last complete-round scores.", ""]
    if scores is None:
        lines += ["No complete-round quality results exist yet.", ""]
    else:
        lines += ["| Method | Track | Attempts | Completed | Mean content score | Exact content success |",
                  "|---|---|---:|---:|---:|---:|"]
        for variant in variants:
            for track, summary in scores["variants"][variant]["tracks"].items():
                lines.append(f"| {variant} | {track} | {summary['attempts']} | "
                             f"{summary['completed']} | {summary['mean_content_score']:.4f} | "
                             f"{summary['content_success_rate']:.4f} |")
        lines += ["", "QA content score is answer F1; other content scores are reference-match "
                  "indicators. Exact QA success requires answer F1 of one. Per-class metrics, "
                  "evidence F1, pair accuracy, order diagnostics, repeated-run statistics, "
                  "costs, and grouped paired intervals are in `scores.json`.", ""]
    if m2_rounds:
        lines += ["## Original M2 sample", "",
                  "These 20-paper results use the unchanged review rubric and remain separate "
                  "from benchmark content scores. Citation verification is a mechanical measure, "
                  "not assessment quality. Each local stage uses one repeat; round numbers below "
                  "identify separate attempts. [Round summaries](m2-rounds.json).", "",
                  "| Round | Method | Completed / attempts | All citations verified | Mean USD / attempt |",
                  "|---|---|---:|---:|---:|"]
        for row in m2_rounds:
            for variant in variants:
                summary = row["summary"][variant]
                cost = summary["mean_cost_usd"]
                cost_text = f"{cost:.6f}" if cost is not None else "unknown"
                lines.append(f"| [{row['round']}](r{row['round']}/m2/README.md) | {variant} | "
                             f"{summary['completed']}/{summary['runs']} | "
                             f"{summary['all_citations_verified']} | {cost_text} |")
        lines += [""]
    (out / "README.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def prepare_plans(root, repeats, workers, model, seed, variants):
    if type(repeats) is not int or repeats < 1:
        raise ValueError("Repetitions must be positive")
    plans = []
    for round_number in range(1, repeats + 1):
        for stage, tracks, reads in STAGES:
            plan = make_plan(root, "test", tracks=tracks, variants=variants, repeats=1,
                             config=Config(model=model, max_reads=reads), workers=workers,
                             seed=seed + round_number)
            plans.append((round_number, stage, plan))
    return plans


def run(root, out, *, model="gpt-6-luna", repeats=5, workers=6, seed=20261118,
        execute=False, m2_sample=Path("data/eval/tasks.jsonl"), skip_m2=False,
        variants=None):
    if type(execute) is not bool:
        raise ValueError("Execution requires an explicit boolean opt-in")
    variants = list(DEFAULT_VARIANTS if variants is None else variants)
    if not variants or len(variants) != len(set(variants)) or set(variants) - set(AVAILABLE_VARIANTS):
        raise ValueError("Choose a nonempty list of distinct known variants")
    root, out = Path(root).resolve(), Path(out).resolve()
    plans = prepare_plans(root, repeats, workers, model, seed, variants)
    m2_sample = Path(m2_sample).resolve()
    m2_tasks = [] if skip_m2 else load_sample(m2_sample)
    if not skip_m2 and len(m2_tasks) != 20:
        raise ValueError("Expected the unchanged 20-paper M2 sample")
    tasks = load_benchmark(root, "test", [track for _, tracks, _ in STAGES for track in tracks])
    if Counter(task["track"] for task in tasks) != {
            "qasper": 20, "reviewcritique": 20, "controlled": 24, "selection": 12}:
        raise ValueError("Expected the frozen 76-task benchmark test split")
    benchmark_total = sum(plan["planned_runs"] for _, _, plan in plans)
    m2_per_round = len(m2_tasks) * len(variants)
    m2_total = m2_per_round * repeats
    total = benchmark_total + m2_total
    # Validate every stage before any output directory or model client exists.
    for round_number, stage, plan in plans:
        validation = run_plan(plan, out / f"r{round_number}" / stage)
        if validation["model_calls"] != 0:
            raise RuntimeError("Dry validation must not call models")
    if not execute:
        return {"status": "dry_run", "model_calls": 0, "rounds": repeats,
                "tasks_per_round": len(tasks), "variants": variants,
                "planned_attempts": total, "benchmark_planned_attempts": benchmark_total,
                "m2_planned_attempts": m2_total, "workers": workers, "out": str(out)}

    out.mkdir(parents=True, exist_ok=False)
    (out / "launcher.py").write_bytes(Path(__file__).read_bytes())
    stages = []
    for round_number in range(1, repeats + 1):
        if not skip_m2:
            stages.append((round_number, "m2", None))
        stages.extend(item for item in plans if item[0] == round_number)
    write_json(out / "experiment.json", {
        "model": model, "variants": variants, "rounds": repeats, "workers": workers,
        "seed": seed, "tasks_per_round": len(tasks), "planned_attempts": total,
        "benchmark_planned_attempts": benchmark_total, "m2_planned_attempts": m2_total,
        "m2_sample": str(m2_sample) if not skip_m2 else None,
        "m2_sample_sha256": file_hash(m2_sample) if not skip_m2 else None,
        "repeat_policy": "Stage traces retain local repeat=1; aggregate copies use global round and retain source_repeat/source_round.",
        "stages": [{"round": number, "stage": stage, "path": f"r{number}/{stage}",
                    "planned_attempts": plan["planned_runs"] if plan else m2_per_round,
                    "max_reads": plan["config"]["max_reads"] if plan else 5}
                   for number, stage, plan in stages]})
    records, scores, completed_rounds, m2_rounds = [], None, 0, []
    m2_completed = 0
    render_report(out, records, scores, completed_rounds, repeats, total, m2_rounds, m2_total, variants)
    active_round, active_stage, active_path, active_records_path, active_total = 0, None, None, None, 0

    def publish(status, stage_status=None, error=None):
        fields = {"status": status, "global_round": active_round,
                  "completed_rounds": completed_rounds, "stage": active_stage,
                  "stage_status": stage_status,
                  "completed_attempts": len(records) + m2_completed, "planned_attempts": total,
                  "benchmark_completed_attempts": len(records), "benchmark_planned_attempts": benchmark_total,
                  "m2_completed_attempts": m2_completed, "m2_planned_attempts": m2_total,
                  "stage_planned_attempts": active_total,
                  "active_progress_path": active_path, "active_records_path": active_records_path}
        if error is not None:
            fields["error"] = safe_error(error)
        progress(out, **fields)

    try:
        with (out / "records.jsonl").open("x", encoding="utf-8", newline="\n") as aggregate:
            for round_number, stage, plan in stages:
                active_round, active_stage = round_number, stage
                stage_out = out / f"r{round_number}" / stage
                active_path = str(stage_out / "progress.json")
                active_records_path = str(stage_out / "records.jsonl") if plan else None
                active_total = plan["planned_runs"] if plan else m2_per_round
                publish("running", "starting")
                if stage == "m2":
                    stage_out.mkdir(parents=True, exist_ok=False)
                    with (stage_out / "console.log").open("x", encoding="utf-8") as console:
                        with redirect_stdout(console):
                            summary = evaluate(m2_sample, stage_out, Config(model=model, max_reads=5),
                                               variants=variants, repeats=1, workers=workers,
                                               order_seed=seed + round_number)
                    if sum(value["runs"] for value in summary.values()) != m2_per_round:
                        raise ValueError("M2 attempt count differs from the frozen sample")
                    m2_completed += m2_per_round
                    m2_rounds.append({"round": round_number, "source_repeat": 1,
                                      "path": f"r{round_number}/m2", "summary": summary})
                    write_json(stage_out / "summary.json", summary)
                    write_json(out / "m2-rounds.json", m2_rounds)
                    render_report(out, records, scores, completed_rounds, repeats, total, m2_rounds, m2_total, variants)
                    publish("running", "complete")
                    continue
                run_plan(plan, stage_out, execute=True)
                local_records = read_jsonl(stage_out / "records.jsonl")
                if len(local_records) != plan["planned_runs"]:
                    raise ValueError("Stage attempt count differs from its plan")
                for original in local_records:
                    copied = {**original, "repeat": round_number, "source_round": round_number,
                              "source_repeat": original["repeat"], "stage": stage,
                              "trace_path": f"r{round_number}/{stage}/{original['trace_path']}"}
                    records.append(copied)
                    aggregate.write(json.dumps(copied, ensure_ascii=False, allow_nan=False) + "\n")
                aggregate.flush()
                if stage == STAGES[-1][0]:
                    scores = score_predictions(tasks, records, variants=variants, repeats=round_number)
                    write_json(out / "scores.json", scores)
                    completed_rounds = round_number
                render_report(out, records, scores, completed_rounds, repeats, total, m2_rounds, m2_total, variants)
                publish("running", "complete")
    except Exception as exc:
        publish("error", error=exc)
        raise
    active_stage, active_path, active_records_path, active_total = None, None, None, 0
    publish("complete")
    return {"status": "complete", "rounds": completed_rounds,
            "attempts": len(records) + m2_completed, "benchmark_attempts": len(records),
            "m2_attempts": m2_completed,
            "benchmark_completed_predictions": sum(record["status"] == "ok" for record in records),
            "m2_completed_predictions": sum(summary["completed"] for row in m2_rounds
                                             for summary in row["summary"].values()),
            "out": str(out), "progress": str(out / "progress.json")}


def main():
    # Invoke from the repository root before using any frozen source checkout.
    # Credentials remain in the process environment and are never serialized.
    load_dotenv(Path.cwd() / ".env", override=True)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_BENCHMARK)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--model", default="gpt-6-luna")
    parser.add_argument("--repeats", type=int, default=5)
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--seed", type=int, default=20261118)
    parser.add_argument("--variants", nargs="+", choices=AVAILABLE_VARIANTS,
                        default=list(DEFAULT_VARIANTS))
    parser.add_argument("--m2-sample", type=Path, default=Path("data/eval/tasks.jsonl"))
    parser.add_argument("--skip-m2", action="store_true")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()
    if args.execute and not os.environ.get("OPENAI_API_KEY"):
        parser.error("Set OPENAI_API_KEY before explicitly executing the benchmark")
    try:
        result = run(args.root, args.out, model=args.model, repeats=args.repeats,
                     workers=args.workers, seed=args.seed, execute=args.execute,
                     m2_sample=args.m2_sample, skip_m2=args.skip_m2, variants=args.variants)
    except Exception as exc:
        print(json.dumps({"status": "error", "error": safe_error(exc)}))
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
