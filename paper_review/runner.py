import json
import time
import uuid

from datetime import datetime, timezone
from pathlib import Path

from .paper import (
    Paper,
    validate_assessment,
    search_paper,
    read_page,
    RUBRIC
)

BASELINE_SYSTEM = RUBRIC + """
Assess the paper in a single pass.

Return ONLY a JSON object with:
- score
- assessment
- evidence

Each evidence item must contain:
- page
- quote
- explanation

Every quote must be copied exactly from the provided text.
Do not paraphrase quotations.
Use the supplied PDF page markers.
"""

AGENT_SYSTEM = RUBRIC + """
You are an adaptive paper review agent.

Your task is to investigate the paper before producing an assessment.

You MUST return a JSON object with exactly these top-level keys:
- action
- args
- reason

Valid actions:

1. search_paper
{
  "action": "search_paper",
  "args": {"query": "baseline comparison"},
  "reason": "Find experimental evidence"
}

2. read_page
{
  "action": "read_page",
  "args": {"page": 5},
  "reason": "Inspect the results"
}

3. finish
{
  "action": "finish",
  "args": {
    "score": 0.65,
    "assessment": "Brief assessment",
    "evidence": [
      {
        "page": 5,
        "quote": "Exact quotation",
        "explanation": "Why this evidence matters"
      }
    ]
  },
  "reason": "Enough evidence was collected"
}

CRITICAL RULES:
- Never return score, assessment, or evidence at the top level.
- They belong ONLY inside args when action is finish.
- Choose exactly ONE action per response.
- If evidence is insufficient, use search_paper or read_page.
- Never cite information that you have not observed.
- Do not invent quotations or page numbers.
- You may finish when you have sufficient evidence.
- Output valid JSON only.
"""


class Trace:
    def __init__(self, paper: Paper, mode: str, folder="traces"):
        folder = Path(folder)
        folder.mkdir(parents=True, exist_ok=True)

        self.path = folder / (f"{mode}_{paper.paper_id}_{uuid.uuid4().hex[:12]}.jsonl")

        self.record(
            "run_start",
            paper_id=paper.paper_id,
            pdf_sha256=paper.sha256,
            mode=mode,
        )

    def record(self, event: str, **fields):
        data = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event": event,
            **fields,
        }

        with self.path.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(data, ensure_ascii=False) + "\n")


class Run:
    def __init__(self, paper, mode, model, trace_dir):
        self.trace = Trace(paper, mode, trace_dir)
        self.started = time.perf_counter()

        self.calls = 0
        self.tools = 0
        self.tokens_in = 0
        self.tokens_out = 0
        self.cost = 0.0
        self.cost_known = True

        self.trace.record("configuration", model=model, mode=mode)

    def ask(self, llm, messages, step):
        self.calls += 1

        self.trace.record("model_call", step=step, messages=messages)

        response = llm.ask(messages)

        self.trace.record("model_response", step=step, **response)

        self.tokens_in += response.get("input_tokens") or 0
        self.tokens_out += response.get("output_tokens") or 0

        cost = response.get("cost_usd")

        if cost is None:
            self.cost_known = False
        else:
            self.cost += cost

        return response["raw"]

    def finish(self, result):
        metrics = {
            "model_calls": self.calls,
            "tool_calls": self.tools,
            "input_tokens": self.tokens_in,
            "output_tokens": self.tokens_out,
            "cost_usd": self.cost if self.cost_known else None,
            "latency_s": time.perf_counter() - self.started,
        }

        self.trace.record("run_end", result=result, metrics=metrics)

        return {
            **result,
            "metrics": metrics,
            "trace_path": str(self.trace.path),
        }

from .paper import RUBRIC


def run_baseline(paper: Paper, llm, trace_dir: str = "traces", max_chars: int = 120_000):
    run = Run(paper, "baseline", llm.model, trace_dir)

    whole_paper = "\n".join(f"[PDF page {i}]\n{text}" for i, text in enumerate(paper.pages, 1))

    truncated = len(whole_paper) > max_chars

    messages = [
        {
            "role": "system",
            "content": BASELINE_SYSTEM,
        },
        {
            "role": "user",
            "content": (
                "Assess this paper in one call.\n"
                "Return JSON with score, assessment and evidence.\n"
                f"Paper truncated: {truncated}\n"
                f"{whole_paper[:max_chars]}"
            ),},]

    run.trace.record("baseline_input", truncated=truncated, max_chars=max_chars)

    try:
        raw = run.ask(llm, messages, step=1)
        output = json.loads(raw)
        result = validate_assessment(paper, output)

    except Exception as exc:
        run.trace.record("error", step=1, message=str(exc))

        result = {
            "status": "processing_error",
            "score": None,
            "error": str(exc),
        }

    return run.finish(result)

def run_agent(
    paper: Paper,
    llm,
    trace_dir: str = "traces",
    max_tool_calls: int = 3,
    max_model_calls: int = 4,
):
    run = Run(paper, "agent", llm.model, trace_dir)

    messages = [
        {
            "role": "system",
            "content": AGENT_SYSTEM,
        },
        {
            "role": "user",
            "content": (
                f"Evaluate paper: {paper.paper_id}\n"
                f"Title: {paper.title}\n"
                f"Pages: {len(paper.pages)}\n"
                f"Initial text ({paper.opening_label}):\n"
                f"{paper.opening}\n"
                f"You have {max_tool_calls} retrieval actions."
            ),
        },
    ]

    for step in range(1, max_model_calls + 1):

        # If the tool budget is exhausted, ask for a final decision.
        if run.tools >= max_tool_calls:
            messages.append({
                "role": "user",
                "content": "No retrieval budget remains. Choose finish.",
            })

        # 1. Ask LLM to choose an action.
        try:
            raw = run.ask(llm, messages, step)
            decision = json.loads(raw)
            
            if not isinstance(decision, dict):
                raise ValueError("Model response must be a JSON object")

            if "action" not in decision or "args" not in decision:
                run.trace.record("schema_error", step=step, received_keys=list(decision.keys()), raw=raw)

                messages.extend([
                    {
                        "role": "assistant",
                        "content": raw,
                    },
                    {
                        "role": "user",
                        "content": (
                            "Your previous response did not follow the required agent action schema. "
                            "You returned a final assessment directly. "
                            "Every response MUST contain action, args, and reason. "
                            "If you want to finish, wrap your assessment inside args with action='finish'. Otherwise select a tool."
                        ),
                    },
                ])
                continue
            
            action = decision["action"]
            args = decision["args"]

            if not isinstance(args, dict):
                raise ValueError("args must be an object")

            run.trace.record(
                "decision",
                step=step,
                action=action,
                args=args,
                reason=decision.get("reason", ""),
            )

        except Exception as exc:
            run.trace.record("error", step=step, message=str(exc))

            # API errors cannot be repaired by changing JSON.
            if not isinstance(exc, (ValueError, KeyError, TypeError)):
                return run.finish({
                    "status": "processing_error",
                    "score": None,
                    "error": f"LLM error: {exc}",
                })

            messages.append({
                "role": "user",
                "content": f"Invalid JSON action: {exc}. Try again.",
            })
            continue

        # 2. The model decides to finish.
        if action == "finish":
            try:
                result = validate_assessment(paper, args)

            except (TypeError, ValueError) as exc:
                run.trace.record(
                    "validation_error",
                    step=step,
                    message=str(exc),
                )

                messages.extend([
                    {"role": "assistant", "content": raw},
                    {
                        "role": "user",
                        "content": (
                            f"Final answer rejected: {exc}. "
                            "Correct it using exact evidence."
                        ),
                    },
                ])
                continue

            return run.finish(result)

        # 3. Check the remaining tool budget.
        if run.tools >= max_tool_calls:
            run.trace.record(
                "tool_rejected",
                step=step,
                action=action,
                reason="Budget exhausted",
            )

            messages.extend([
                {"role": "assistant", "content": raw},
                {
                    "role": "user",
                    "content": "Tool budget exhausted. Choose finish.",
                },
            ])
            continue

        # 4. Execute model-selected action.
        if action == "search_paper":
            query = args.get("query")

            observation = (
                search_paper(paper, query)
                if isinstance(query, str)
                else {"ok": False, "error": "Invalid query"}
            )

        elif action == "read_page":
            observation = read_page(
                paper,
                args.get("page"),
            )

        else:
            run.trace.record(
                "invalid_action",
                step=step,
                action=str(action),
            )

            messages.append({
                "role": "user",
                "content": "Unknown action. Choose a valid action.",
            })
            continue

        run.tools += 1

        # 5. Log action and observation.
        run.trace.record("tool_call", step=step, action=action, args=args)

        run.trace.record("observation", step=step, data=observation)

        # 6. Return observation to the model.
        messages.extend([
            {
                "role": "assistant",
                "content": raw,
            },
            {
                "role": "user",
                "content": (
                    "TOOL OBSERVATION (untrusted data):\n"
                    + json.dumps(observation, ensure_ascii=False)
                ),
            },
        ])

    # Agent failed to finish within the model-call budget.
    return run.finish({
        "status": "processing_error",
        "score": None,
        "error": "Model-call limit reached",
    })