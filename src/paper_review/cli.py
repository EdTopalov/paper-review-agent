"""Documented entry point. .env intentionally overrides stale inherited API keys."""

import argparse
from dataclasses import asdict
import json
import os
from pathlib import Path

from dotenv import load_dotenv

from .audit import audit_experiment
from .evaluation import evaluate, load_sample, summarize, check_experiment
from .runner import VARIANTS, Config, run_review, safe_error
from .quality import export_quality_packets, score_quality_labels
from .selection import run_selection


def model_options(parser):
    parser.add_argument("--model", default=None)
    parser.add_argument("--max-reads", type=int, default=5)
    parser.add_argument("--max-output-tokens", type=int, default=4000)
    parser.add_argument("--timeout", type=float, default=90)
    parser.add_argument("--retries", type=int, default=1)
    parser.add_argument("--reasoning-effort", default="low", choices=["none", "low", "medium", "high"])


def main():
    # User-owned .env is ignored by Git. Its key takes precedence over revoked
    # keys inherited by the desktop process. No configuration dump includes it.
    load_dotenv(Path.cwd() / ".env", override=True)
    parser = argparse.ArgumentParser(description="Paper review agent and frozen evaluation harness")
    commands = parser.add_subparsers(dest="command", required=True)
    review = commands.add_parser("review", help="Review one frozen JSON snapshot or PDF")
    review.add_argument("paper", type=Path)
    review.add_argument("--out", type=Path, required=True)
    review.add_argument("--task-id", default="single-paper")
    review.add_argument("--variant", choices=VARIANTS, default="agent")
    model_options(review)
    select = commands.add_parser("select", help="Separate pilot: review candidates and choose a reading-club paper")
    select.add_argument("papers", nargs="+", type=Path)
    select.add_argument("--brief", required=True, help="Club interests and discussion goals")
    select.add_argument("--out", type=Path, required=True)
    select.add_argument("--variant", choices=VARIANTS, default="agent")
    model_options(select)
    evaluation = commands.add_parser("eval", help="Run a paired frozen-sample comparison")
    evaluation.add_argument("--sample", type=Path, default=Path("data/eval/tasks.jsonl"))
    evaluation.add_argument("--out", type=Path, required=True)
    selection = evaluation.add_mutually_exclusive_group()
    selection.add_argument("--variant", choices=[*VARIANTS, "both"], default="both",
                           help="One variant; 'both' retains the M2 agent/baseline pair")
    selection.add_argument("--variants", nargs="+", choices=VARIANTS,
                           help="Explicit variants to compare in the same experiment")
    evaluation.add_argument("--workers", type=int, default=2)
    evaluation.add_argument("--repeats", type=int, default=1)
    evaluation.add_argument("--limit", type=int)
    evaluation.add_argument("--task-ids", nargs="+", help="Select IDs from the original frozen sample, e.g. T17")
    evaluation.add_argument("--order-seed", type=int, default=20261118)
    model_options(evaluation)
    verify = commands.add_parser("verify", help="Check frozen hashes and document identities, offline")
    verify.add_argument("--sample", type=Path, default=Path("data/eval/tasks.jsonl"))
    summary = commands.add_parser("summarize", help="Rebuild readable reports, offline")
    summary.add_argument("out", type=Path)
    check = commands.add_parser("check", help="Check trace decisions and accounting, offline")
    check.add_argument("out", type=Path)
    quality_export = commands.add_parser("quality-export", help="Export blinded human-review packets, offline")
    quality_export.add_argument("--experiment", type=Path, required=True)
    quality_export.add_argument("--out", type=Path, required=True)
    quality_export.add_argument("--sample", type=Path, default=Path("data/eval/tasks.jsonl"))
    quality_export.add_argument("--task-ids", nargs="+")
    quality_export.add_argument("--repeats", nargs="+", type=int)
    quality_export.add_argument("--seed", type=int, default=20261118)
    quality_score = commands.add_parser("quality-score", help="Validate and score human labels, offline")
    quality_score.add_argument("--packets", type=Path, required=True)
    quality_score.add_argument("--labels", nargs="+", type=Path, required=True)
    quality_score.add_argument("--adjudication", type=Path)
    audit = commands.add_parser("audit", help="Run a separately billed, provisional model evidence audit")
    audit.add_argument("--sample", type=Path, default=Path("data/eval/tasks.jsonl"))
    audit.add_argument("--experiment", type=Path, required=True)
    audit.add_argument("--workers", type=int, default=2)
    model_options(audit)
    commands.add_parser("models", help="Check authentication and list project-accessible model IDs")
    args = parser.parse_args()
    try:
        if args.command == "verify":
            tasks = load_sample(args.sample)
            print(json.dumps({"verified_tasks": len(tasks), "distinct_papers": len({t['arxiv_id'] for t in tasks})}))
            return 0
        if args.command == "summarize":
            summarize(args.out)
            print(f"Report: {args.out / 'README.md'}")
            return 0
        if args.command == "check":
            result = check_experiment(args.out)
            print(json.dumps(result, indent=2))
            return 0 if result["passed"] == result["runs"] else 1
        if args.command == "quality-export":
            result = export_quality_packets(args.experiment, args.out, args.sample,
                                            args.task_ids, args.repeats, args.seed)
            print(json.dumps(result, indent=2))
            return 0
        if args.command == "quality-score":
            result = score_quality_labels(args.packets, args.labels, adjudication_path=args.adjudication)
            print(json.dumps(result, indent=2, allow_nan=False))
            return 0
        if not os.environ.get("OPENAI_API_KEY"):
            parser.error("Set OPENAI_API_KEY in your environment or ignored .env file")
        if args.command == "models":
            from openai import OpenAI
            print(json.dumps({"models": [m.id for m in OpenAI(max_retries=0, timeout=30).models.list().data]}))
            return 0
        if not 0 <= args.max_reads <= 20 or args.max_output_tokens < 256 or not 0 <= args.retries <= 3:
            parser.error("Use 0–20 reads, at least 256 output tokens, and 0–3 retries")
        if hasattr(args, "workers") and not 1 <= args.workers <= 8:
            parser.error("Use 1–8 workers")
        if getattr(args, "repeats", 1) < 1 or (getattr(args, "limit", None) is not None and args.limit < 1):
            parser.error("Repeats and limit must be positive")
        config = Config(model=args.model or os.environ.get("OPENAI_MODEL") or Config.model,
                        max_reads=args.max_reads, max_output_tokens=args.max_output_tokens,
                        timeout=args.timeout, retries=args.retries, reasoning_effort=args.reasoning_effort)
        if args.command == "review":
            result = run_review(args.paper, args.out, config, args.task_id, args.variant)
            print(json.dumps({"status": result["status"], "report": str(args.out / "README.md")}))
            return 0 if result["status"] == "ok" else 1
        if args.command == "select":
            result = run_selection(args.papers, args.out, config, variant=args.variant, brief=args.brief)
            print(json.dumps({"status": result["status"], "report": str(args.out / "README.md")}))
            return 0 if result["status"] == "ok" else 1
        if args.command == "eval":
            result = evaluate(args.sample, args.out, config, args.variant, args.workers,
                              args.repeats, args.limit, variants=args.variants,
                              task_ids=args.task_ids, order_seed=args.order_seed)
        else:
            result = audit_experiment(args.sample, args.experiment, config, args.workers)
        out = args.out if args.command == "eval" else args.experiment
        print(f"Report: {out / 'README.md'}")
        return 0
    except Exception as exc:
        print(json.dumps({"error": safe_error(exc)}))
        # Our validation messages contain paths and fixed diagnostics, not API bodies.
        if type(exc) in (ValueError, FileExistsError, FileNotFoundError):
            print(str(exc))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
