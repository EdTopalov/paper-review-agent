"""Save inspectable benchmark plans without clients, model calls, or run folders."""

import argparse
import json
from pathlib import Path

from paper_review.benchmark_data import DEFAULT_BENCHMARK, load_benchmark
from paper_review.benchmark_runner import make_plan, run_plan
from paper_review.runner import Config, VARIANTS


def smoke_tasks(root):
    tasks = load_benchmark(root, "dev")
    qa = next(task["id"] for task in tasks if task["track"] == "qasper")
    critique = [task for task in tasks if task["track"] == "reviewcritique"]
    critique_group = critique[0]["group_id"]
    critique_ids = [task["id"] for task in critique if task["group_id"] == critique_group]
    controlled = [task for task in tasks if task["track"] == "controlled"]
    pair = controlled[0]["reference"]["pair_id"]
    controlled_ids = [task["id"] for task in controlled if task["reference"]["pair_id"] == pair]
    selection = next(task["id"] for task in tasks if task["track"] == "selection")
    if len(critique_ids) != 2 or len(controlled_ids) != 2:
        raise ValueError("Development smoke needs a same-paper critique pair and a controlled pair")
    return [qa, *critique_ids, *controlled_ids], [selection]


def prepare(root, out, *, workers=6):
    root, out = Path(root), Path(out)
    core_ids, selection_ids = smoke_tasks(root)
    specifications = [
        ("dev-core-smoke-luna6", "dev", "gpt-6-luna", 1, 5,
         ["qasper", "reviewcritique", "controlled"], core_ids, 20261118),
        ("dev-selection-smoke-luna6", "dev", "gpt-6-luna", 1, 20,
         ["selection"], selection_ids, 20261118),
    ]
    for model, suffix, seed in (("gpt-6-luna", "luna6", 20261118),
                                 ("gpt-5.6-luna", "luna56", 20261119)):
        specifications.extend([
            (f"test-core-{suffix}-r3", "test", model, 3, 5,
             ["qasper", "reviewcritique", "controlled"], None, seed),
            (f"test-selection-{suffix}-r3", "test", model, 3, 20,
             ["selection"], None, seed),
        ])
    plans = []
    for name, split, model, repeats, reads, tracks, task_ids, seed in specifications:
        plan = make_plan(root, split, tracks=tracks, variants=list(VARIANTS),
                         repeats=repeats, workers=workers,
                         config=Config(model=model, max_reads=reads), seed=seed, task_ids=task_ids)
        # A relative root travels with the repository; --root supports other locations.
        plan["benchmark_root"] = root.as_posix()
        validation = run_plan(plan, out / "unused-dry-run-output", root_override=root)
        if validation["model_calls"] != 0:
            raise RuntimeError("Planning must remain offline")
        plans.append((name, plan))
    out.mkdir(parents=True, exist_ok=False)
    for name, plan in plans:
        (out / f"{name}.json").write_text(json.dumps(plan, indent=2) + "\n", encoding="utf-8", newline="\n")
    return [{"plan": f"{name}.json", "tasks": plan["tasks"], "planned_runs": plan["planned_runs"],
             "max_reads": plan["config"]["max_reads"], "status": plan["status"]}
            for name, plan in plans]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_BENCHMARK)
    parser.add_argument("--out", type=Path, default=Path("milestones/benchmark-plans"))
    parser.add_argument("--workers", type=int, default=6)
    args = parser.parse_args()
    print(json.dumps({"plans": prepare(args.root, args.out, workers=args.workers), "model_calls": 0}, indent=2))


if __name__ == "__main__":
    main()
