"""Sort independently completed reviews; processing errors never become low scores."""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="A variant directory containing task/result.json files")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    rows = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(args.directory.glob("*/result.json"))]
    if not rows:
        parser.error("No result.json files found")
    ranked = sorted([r for r in rows if r["status"] == "ok"],
                    key=lambda r: (-r["review"]["score"], r["task_id"]))
    result = {"ranking": [{"task_id": r["task_id"], "score": r["review"]["score"],
                           "summary": r["review"]["summary"]} for r in ranked],
              "processing_errors": [{"task_id": r["task_id"], "error": r["error"]}
                                    for r in rows if r["status"] != "ok"],
              "note": "Scores remain absolute; equal scores use task ID as a deterministic display tie-break."}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"ranked": len(ranked), "output": str(args.out)}))


if __name__ == "__main__":
    main()
