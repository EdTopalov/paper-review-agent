"""Validate the new controller on seven development attempts; opt in to API calls.

Default execution validates frozen data and plans only. Results from this small
execution check are development diagnostics, never held-out benchmark results.
"""

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path

from dotenv import load_dotenv

from paper_review.benchmark_data import DEFAULT_BENCHMARK
from paper_review.benchmark_runner import check_runs, make_plan, run_plan
from paper_review.evaluation import check_experiment
from paper_review.runner import Config, run_review
from prepare_benchmark_plans import smoke_tasks


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_BENCHMARK)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--model", default="gpt-6-luna")
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--execute", action="store_true", help="Issue billed model requests")
    args = parser.parse_args()
    core_ids, selection_ids = smoke_tasks(args.root)
    plans = {
        "core": make_plan(args.root, split="dev", tracks=["controlled", "qasper", "reviewcritique"],
                          variants=["deliberative_review"], repeats=1,
                          config=Config(model=args.model), workers=args.workers, task_ids=core_ids),
        "selection": make_plan(args.root, split="dev", tracks=["selection"],
                               variants=["deliberative_review"], repeats=1,
                               config=Config(model=args.model, max_reads=20), workers=1, task_ids=selection_ids),
    }
    if len(core_ids) != 5 or len(selection_ids) != 1:
        raise ValueError("Development check requires five core cases and one selection case")
    for name, plan in plans.items():
        validation = run_plan(plan, args.out / name)
        if validation["model_calls"] != 0:
            raise RuntimeError("Planning must not issue model calls")
    print(json.dumps({"status": "ready" if args.execute else "dry_run", "model": args.model,
                      "variant": "deliberative_review", "core_ids": core_ids,
                      "selection_ids": selection_ids, "planned_attempts": 7,
                      "model_calls_so_far": 0}, indent=2), flush=True)
    if not args.execute:
        return 0
    load_dotenv(PROJECT_ROOT / ".env", override=True)
    if not os.environ.get("OPENAI_API_KEY"):
        parser.error("Set OPENAI_API_KEY before explicitly executing development checks")
    args.out.mkdir(parents=True, exist_ok=False)
    for name, plan in plans.items():
        (args.out / f"{name}-plan.json").write_text(json.dumps(plan, indent=2) + "\n", encoding="utf-8")

    def original_review():
        result = run_review(PROJECT_ROOT / "data/dev/toy.json", args.out / "original-review",
                            Config(model=args.model), "synthetic-development",
                            variant="deliberative_review")
        checks = check_experiment(args.out / "original-review")
        return {"attempts": 1, "completed": int(result["status"] == "ok"),
                "operational_checks": checks}

    def benchmark(name):
        result = run_plan(plans[name], args.out / name, execute=True)
        return {"attempts": result["runs"], "completed": result["completed"],
                "operational_checks": check_runs(args.out / name)}

    with ThreadPoolExecutor(max_workers=3) as pool:
        pending = {"original-review": pool.submit(original_review),
                   **{name: pool.submit(benchmark, name) for name in plans}}
        outcomes = {name: future.result() for name, future in pending.items()}
    valid = all(row["operational_checks"]["passed"] == row["operational_checks"]["runs"]
                for row in outcomes.values())
    completed = sum(row["completed"] for row in outcomes.values())
    summary = {"status": "passed" if valid and completed == 7 else "inspect_failures",
               "completed": completed, "attempts": 7, "outcomes": outcomes,
               "scope": "Development execution check; content accuracy is reported separately."}
    (args.out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2), flush=True)
    return 0 if summary["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
