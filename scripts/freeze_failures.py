"""Save exact failed-decision inputs for M3, without making model calls."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "runs/m2-20261026"
CASES = [
    {"id": "F01", "task_id": "T02", "observation_index": 2,
     "problem": "A stated interface requirement becomes an unsupported transfer restriction.",
     "expected": "Do not assert that termination must be task-specific or that transfer is restricted as an established finding. Qualify the inference, or read more evidence before asserting it.",
     "root_cause": "The model expands a genuine requirement (termination heuristic and binary reward) into a stronger limitation. The quote establishes the requirement, not the claimed transfer restriction.",
     "evidence_pages": [7, 10], "certainty": "Interpretive failure; the transfer concern is plausible, but stated too categorically."},
    {"id": "F02", "task_id": "T06", "observation_index": 1,
     "problem": "Correct reported result is attributed to the wrong PDF page.",
     "expected": "If submitting this 4.8% quotation, cite PDF page 5 rather than page 6; alternatively retrieve and quote correct evidence with its actual page.",
     "root_cause": "A read_pages(5,6) observation concatenated two pages. The model retained the result but lost its page identity while constructing submit_review arguments.",
     "evidence_pages": [5, 6], "certainty": "Directly checked against frozen page text; the claim itself is not disproved."},
    {"id": "F03", "task_id": "T13", "observation_index": 0,
     "problem": "A quotation omits an internal parenthesis and is assigned to the wrong page.",
     "expected": "Use the exact page-3 sentence including '(Table 1)', or select another exact quotation. Do not submit the edited sentence as a verbatim quote from page 4.",
     "root_cause": "The model rewrites a source sentence while summarizing a three-page read. Output-schema validation checks types, not source fidelity; citation checks run after final submission and do not trigger recovery.",
     "evidence_pages": [3, 4], "certainty": "Directly checked against frozen text. The underlying summary is supported; the evidence representation is faulty."},
    {"id": "F04", "task_id": "T01", "decision_action": "search_paper", "decision_step": 1,
     "problem": "A keyword-bundle query is passed to an underspecified literal-phrase search tool and returns no matches.",
     "expected": "Use an actual literal keyword/phrase such as 'ALFWorld' if selecting search_paper, or read relevant pages. Do not assume bag-of-words retrieval when the tool implements literal matching.",
     "root_cause": "The tool description does not say it performs literal-phrase matching. A plausible web-search-style keyword bundle cannot match any contiguous passage. This is a tool-contract/prompt mismatch, followed by successful recovery at the cost of one reading action.",
     "evidence_pages": [1], "certainty": "The exact query and empty observation are in the trace. Similar empty searches occurred 23 times across all 20 agent runs."},
]


def main():
    target = ROOT / "data/failures"
    target.mkdir(exist_ok=True)
    for case in CASES:
        output = target / f"{case['id']}.json"
        if output.exists():
            continue  # Existing frozen prefixes are immutable.
        path = RUN / "agent-r1" / case["task_id"] / "trace.jsonl"
        with path.open(encoding="utf-8") as stream:
            events = [json.loads(line) for line in stream]
        action_name = case.get("decision_action", "submit_review")
        decision = next(e for e in reversed(events) if e["event"] == "decision" and e["action"] == action_name
                        and ("decision_step" not in case or e["step"] == case["decision_step"]))
        request = next(e for e in reversed(events) if e["event"] == "model_request" and e["seq"] < decision["seq"])
        result = json.loads(path.with_name("result.json").read_text(encoding="utf-8"))
        fixture = {**case, "trace": path.relative_to(ROOT).as_posix(),
                   "decision_step": decision["step"], "decision_seq": decision["seq"],
                   "model_request_seq": request["seq"],
                   "prefix_request": request["request"],
                   "observed_action": json.loads(decision["arguments"]),
                   "m3_protocol": "Replay prefix_request with a candidate policy. Prior function_call_output items are frozen tool stubs. Check the next action against expected; do not require one unique reading trajectory."}
        if "observation_index" in case:
            fixture["failed_observation"] = result["review"]["observations"][case["observation_index"]]
        else:
            fixture["failed_observation"] = next(e["observation"] for e in events
                if e["event"] == "tool_observation" and e["call_id"] == decision["call_id"])
        output.write_text(json.dumps(fixture, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"{case['id']}: {case['task_id']} decision step {decision['step']}, trace event {decision['seq']}")


if __name__ == "__main__":
    main()
