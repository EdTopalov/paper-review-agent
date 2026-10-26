"""Check recorded decisions and budget compliance without prescribing a path."""

import json
from pathlib import Path
import sys

import jsonschema

from paper_review.schema import TOOLS


def main():
    root = Path(sys.argv[1])
    rows = []
    schemas = {tool["name"]: tool["parameters"] for tool in TOOLS}
    for path in sorted(root.glob("*/*/trace.jsonl")):
        with path.open(encoding="utf-8") as stream:
            events = [json.loads(line) for line in stream]
        if not events or events[0]["event"] != "run_start":
            continue
        start, final = events[0], events[-1]
        decisions = [e for e in events if e["event"] == "decision"]
        reads = [e for e in events if e["event"] == "tool_call" and e["name"] in ("search_paper", "read_pages")]
        observations = [e for e in events if e["event"] == "tool_observation"]
        valid_arguments = True
        for decision in decisions:
            if decision["action"] == "final_answer":
                continue
            try:
                jsonschema.validate(json.loads(decision["arguments"]), schemas[decision["action"]])
            except (KeyError, ValueError, jsonschema.ValidationError):
                valid_arguments = False
        result = final.get("result", {})
        flags = {
            "sequence_complete": [e["seq"] for e in events] == list(range(1, len(events) + 1)),
            "reading_budget_respected": len(reads) <= start["config"]["max_reads"],
            "valid_tool_arguments": valid_arguments,
            "model_calls_accounted": sum(e["event"] == "model_request" for e in events) == result.get("api_calls"),
            "responses_accounted": sum(e["event"] == "model_response" for e in events) == result.get("successful_model_calls"),
            "terminal_event_saved": final["event"] == "run_end",
            "stop_decision_recorded": bool(decisions) and decisions[-1]["action"] in ("submit_review", "final_answer"),
        }
        rows.append({"task_id": start["task_id"], "variant": start["variant"],
                     "trace": path.relative_to(root).as_posix(), "checks": flags,
                     "all_checks_pass": all(flags.values()),
                     "empty_search_results": sum(o["observation"].get("matches") == [] for o in observations),
                     "tool_error_observations": sum("error" in o["observation"] for o in observations)})
    (root / "trajectory_checks.jsonl").write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
    summary = {"runs": len(rows), "all_checks_pass": sum(row["all_checks_pass"] for row in rows),
               "empty_search_results": sum(row["empty_search_results"] for row in rows),
               "tool_error_observations": sum(row["tool_error_observations"] for row in rows)}
    (root / "trajectory_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary))
    return 0 if rows and all(row["all_checks_pass"] for row in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
