"""V2: run the real PyAgent ReAct loop with the project's evidence contract.

PyAgent source and MIT license: https://github.com/pyagent-core/pyagent
The loop is imported, not copied. Its text tool protocol is intentionally part
of this variant. Only the project adapter determines whether a review is accepted.
"""

import asyncio
from concurrent.futures import ThreadPoolExecutor
import json

import jsonschema
from pyagent_patterns.advanced import ReAct
from pyagent_patterns.base import Agent, Role

from .agent_tools import PaperEvidence
from .prompts import AGENT_INSTRUCTIONS, PYAGENT_PROTOCOL
from .schema import TOOLS


# An engine control marker, never an alternative review submission interface.
ENGINE_FINISH_TOKEN = "__PAPER_REVIEW_STOP_AFTER_ACCEPTANCE__"


class _ReviewAccepted(Exception):
    """Stop before the next API request, outside ReAct's tool exception handler."""


class ReviewSession:
    def __init__(self, paper, calls, config, trace):
        self.paper, self.calls, self.config, self.trace = paper, calls, config, trace
        self.evidence = PaperEvidence(paper)
        self.accepted_review = None
        self.accepted_checks = None
        self.step = 0
        self.schemas = {tool["name"]: tool["parameters"] for tool in TOOLS}

    @property
    def call_id(self):
        # This is an adapter event ID, not a provider function-call ID.
        return f"pyagent-step-{self.step}"

    def observation(self, value):
        self.trace.write("tool_observation", step=self.step, call_id=self.call_id,
                         observation=value)
        return json.dumps(value, ensure_ascii=False)

    async def model(self, messages):
        # ReAct calls Agent.run again after a tool. This control exception exits
        # that call before ModelCalls, without a fabricated model response.
        if self.accepted_review is not None:
            raise _ReviewAccepted
        self.step += 1
        self.calls.stats["decision_steps"] = self.step
        available = TOOLS
        if self.calls.stats["reading_actions"] >= self.config.max_reads:
            available = [TOOLS[-1]]
            self.trace.write("reading_budget_exhausted", step=self.step,
                             remaining_tools=["submit_review"])
        instructions = (AGENT_INSTRUCTIONS.format(max_reads=self.config.max_reads)
                        + PYAGENT_PROTOCOL + "\nAvailable tool contracts:\n"
                        + json.dumps(available, ensure_ascii=False))
        # Replace the library's generic Thought/FINISH system instruction with
        # our rubric and action protocol. Keep its real conversation/observations.
        inputs = [{"role": message.role.value, "content": message.content}
                  for message in messages if message.role != Role.SYSTEM]
        response = self.calls.call(instructions=instructions, input=inputs)
        content = response.output_text
        name, arguments = ReAct._parse_action(content)
        engine_finish = ENGINE_FINISH_TOKEN in content
        if engine_finish:
            name, arguments = "premature_finish", "{}"
        self.trace.write("decision", step=self.step, action=name or "no_tool_call",
                         call_id=self.call_id, arguments=arguments,
                         protocol="pyagent-text-action-v1")
        if name and not engine_finish:
            self.calls.stats["tool_calls"] += 1
        if name not in self.schemas and not engine_finish:
            # ReAct itself supplies this observation for unknown/missing actions.
            # Record its exact text alongside a structured diagnostic.
            self.observation({"error": "unknown_tool" if name else "no_tool_call",
                              "engine_observation": (
                                  f"Unknown tool: {name}. Available: "
                                  + ", ".join(self.schemas))})
        return content

    def invoke(self, name, raw_arguments):
        from .runner import safe_error, validate_review

        try:
            arguments = json.loads(raw_arguments)
            jsonschema.validate(arguments, self.schemas[name])
            if name == "submit_review":
                validate_review(arguments["review"])
                self.calls.stats["submission_attempts"] += 1
                checks = self.evidence.check(arguments["review"])
                if self.calls.stats["first_submission_checks"] is None:
                    self.calls.stats["first_submission_checks"] = checks
                self.trace.write("tool_call", step=self.step, name=name, arguments=arguments)
                if all(check["citation_verified"] and check["observed"] for check in checks):
                    self.accepted_review = arguments["review"]
                    self.accepted_checks = checks
                    return self.observation({"accepted": True, "citation_checks": checks})
                self.calls.stats["rejected_submissions"] += 1
                return self.observation({
                    "error": "citation_validation_failed", "citation_checks": checks,
                    "hint": "Copy exact quotes from observed pages, or read matching pages before resubmitting. Preserve case, mathematical notation, and ambiguous hyphens.",
                })
            if self.calls.stats["reading_actions"] >= self.config.max_reads:
                return self.observation({"error": "reading_budget_exhausted",
                                         "hint": "Use submit_review; no reading actions remain."})
            self.calls.stats["reading_actions"] += 1
            self.trace.write("tool_call", step=self.step, name=name, arguments=arguments)
            value = (self.paper.search(arguments["query"]) if name == "search_paper"
                     else self.paper.read_pages(arguments["start"], arguments["end"]))
            self.evidence.remember(name, value)
            return self.observation(value)
        except (json.JSONDecodeError, jsonschema.ValidationError) as exc:
            return self.observation({"error": "invalid_arguments", "type": type(exc).__name__})
        except Exception as exc:
            return self.observation({"error": "tool_exception", **safe_error(exc)})

    async def run(self):
        tools = {name: (lambda payload, tool_name=name: self.invoke(tool_name, payload))
                 for name in self.schemas}
        pattern = ReAct(agent=Agent("paper-review-v2", self.model), tools=tools,
                        max_steps=self.config.max_reads + 3,
                        finish_token=ENGINE_FINISH_TOKEN)
        self.trace.write("harness_start", harness="pyagent-patterns.ReAct",
                         max_steps=self.config.max_reads + 3,
                         protocol="pyagent-text-action-v1")
        stop = "step_limit_or_engine_finish"
        try:
            await pattern.run(json.dumps(self.paper.introduction(), ensure_ascii=False))
        except _ReviewAccepted:
            stop = "accepted_before_next_model_request"
        if self.accepted_review is None:
            self.trace.write("harness_stop", reason=stop, accepted=False)
            if self.step >= self.config.max_reads + 3:
                raise RuntimeError("model_decision_budget_exhausted")
            raise RuntimeError("pyagent_finished_without_accepted_review")
        self.trace.write("harness_stop", reason=(stop if stop != "step_limit_or_engine_finish"
                                                 else "accepted_on_last_step"), accepted=True)
        return self.accepted_review, {
            "reading_actions": self.calls.stats["reading_actions"],
            "tool_calls": self.calls.stats["tool_calls"],
            "decision_steps": self.step,
            "evidence_observed": [check["observed"] for check in self.accepted_checks],
        }


def run_pyagent(paper, calls, config, trace):
    session = ReviewSession(paper, calls, config, trace)
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(session.run())
    # The public runner is synchronous; notebooks may already own an event loop.
    with ThreadPoolExecutor(max_workers=1) as pool:
        return pool.submit(lambda: asyncio.run(session.run())).result()
