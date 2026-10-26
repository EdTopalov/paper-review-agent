"""Apply the integrated checker to saved outputs, without rewriting any run."""

import argparse
from collections import Counter
import json
from pathlib import Path

from paper_review.citations import CHECKER_VERSION
from paper_review.evaluation import load_sample
from paper_review.paper import Paper, file_hash


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("experiment", type=Path)
    parser.add_argument("--sample", type=Path, default=Path("data/eval/tasks.jsonl"))
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    tasks = {t["id"]: t for t in load_sample(args.sample)}
    rows = []
    for path in sorted(args.experiment.glob("*/*/result.json")):
        result = json.loads(path.read_text(encoding="utf-8"))
        if result["status"] != "ok":
            continue
        task = tasks[result["task_id"]]
        paper = Paper.load(args.sample.parent / task["paper_path"])
        rows.append({"task_id": task["id"], "variant": result["variant"],
                     "source_result_sha256": file_hash(path),
                     "citation_checks": paper.check_citations(result["review"])})
    summary = {}
    for variant in sorted({row["variant"] for row in rows}):
        subset = [row for row in rows if row["variant"] == variant]
        counts = Counter(c["status"] for row in subset for c in row["citation_checks"])
        summary[variant] = {
            "reviews": len(subset),
            "all_strict_quotes": sum(all(c["quote_matches"] for c in row["citation_checks"]) for row in subset),
            "all_citations_verified": sum(all(c["citation_verified"] for c in row["citation_checks"]) for row in subset),
            "status_counts": dict(sorted(counts.items())),
        }
    report = {"checker_version": CHECKER_VERSION, "source_experiment": args.experiment.as_posix(),
              "model_calls": 0, "changed_model_outputs": False, "summary": summary, "tasks": rows}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
