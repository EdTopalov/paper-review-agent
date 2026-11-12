"""Small Responses API loop; the model chooses reading actions and termination.

# API pattern: https://developers.openai.com/api/docs/guides/function-calling
# Architectural idea: ReAct, https://arxiv.org/abs/2210.03629 (CC BY 4.0).
# This implementation is original; no third-party agent framework code is copied.
"""

from dataclasses import asdict, dataclass
import importlib.metadata
import json
import math
from pathlib import Path
import time

import jsonschema
from openai import OpenAI, APIConnectionError, APIStatusError, APITimeoutError

from .paper import Paper, file_hash
from .citations import CHECKER_VERSION
from .agent_tools import PaperEvidence
from .prompts import AGENT_INSTRUCTIONS, PROMPT_VERSION, PYAGENT_PROMPT_VERSION, RUBRIC, RUBRIC_VERSION
from .schema import REVIEW_SCHEMA, TOOLS
from .trace import Trace
from .reporting import render_run


# Standard text-token USD / 1M, checked 2026-10-26 against official model pages.
# https://developers.openai.com/api/docs/models/gpt-5.4-mini
# https://developers.openai.com/api/docs/models/gpt-4.1-mini
# https://developers.openai.com/api/docs/models/gpt-6-luna
PRICES = {
    "gpt-6-luna": (0.1, 0.01, 0.5, 0.125),
    "gpt-5.4-mini-2026-03-17": (0.75, 0.075, 4.5, 0.9375),
    "gpt-5.4-mini": (0.75, 0.075, 4.5, 0.9375),
    "gpt-4.1-mini-2025-04-14": (0.4, 0.1, 1.6, 0.4),
    "gpt-4.1-mini": (0.4, 0.1, 1.6, 0.4),
}

VARIANTS = ("agent", "pyagent_react", "baseline")


def variant_metadata(variant):
    if variant not in VARIANTS:
        raise ValueError(f"Unknown variant: {variant}")
    details = {"prompt_version": PROMPT_VERSION, "harness": "project-native"}
    if variant == "pyagent_react":
        try:
            version = importlib.metadata.version("pyagent-patterns")
        except importlib.metadata.PackageNotFoundError:
            version = None
        details.update(prompt_version=PYAGENT_PROMPT_VERSION,
                       harness="pyagent-patterns.ReAct", harness_version=version,
                       protocol="pyagent-text-action-v1")
    elif variant == "baseline":
        details["harness"] = "one-shot"
    return details


@dataclass
class Config:
    model: str = "gpt-6-luna"
    max_reads: int = 5
    max_output_tokens: int = 4000
    timeout: float = 90
    retries: int = 1
    reasoning_effort: str = "low"
    max_paper_chars: int = 600000


def safe_error(exc):
    # API exception messages can echo credential fragments. Log type/status only.
    return {"type": type(exc).__name__, "status_code": getattr(exc, "status_code", None)}


class ModelCalls:
    def __init__(self, client, config, trace):
        self.client, self.config, self.trace = client, config, trace
        self.stats = {"api_calls": 0, "successful_model_calls": 0, "input_tokens": 0,
                      "cached_input_tokens": 0, "cache_write_tokens": 0, "output_tokens": 0,
                      "reading_actions": 0, "tool_calls": 0, "decision_steps": 0,
                      "submission_attempts": 0, "rejected_submissions": 0,
                      "first_submission_checks": None,
                      "estimated_cost_usd": 0.0 if config.model in PRICES else None,
                      "billing_uncertain": False}

    def call(self, **request):
        config = self.config
        request = {"model": config.model, "store": False, "service_tier": "default",
                   "max_output_tokens": config.max_output_tokens, **request}
        if config.model.startswith(("gpt-5", "gpt-6")):
            request["reasoning"] = {"effort": config.reasoning_effort}
        for attempt in range(config.retries + 1):
            self.stats["api_calls"] += 1
            self.trace.write("model_request", attempt=attempt + 1, request=request)
            start = time.perf_counter()
            try:
                response = self.client.responses.create(**request)
            except (APIStatusError, APIConnectionError, APITimeoutError) as exc:
                error = safe_error(exc)
                self.trace.write("model_error", error=error,
                                 latency_seconds=time.perf_counter() - start)
                if isinstance(exc, APIConnectionError):
                    self.stats["billing_uncertain"] = True
                retryable = error["status_code"] in (408, 409, 429, 500, 502, 503, 504) \
                    or isinstance(exc, APIConnectionError)
                if not retryable or attempt == config.retries:
                    raise
                self.trace.write("retry", next_attempt=attempt + 2, delay_seconds=attempt + 1)
                time.sleep(attempt + 1)
                continue
            self.stats["successful_model_calls"] += 1
            self.trace.write("model_response", response=response.model_dump(mode="json"),
                             latency_seconds=time.perf_counter() - start)
            usage = response.usage
            if usage is None:
                self.stats["billing_uncertain"] = True
                self.stats["estimated_cost_usd"] = None
            else:
                cached = getattr(usage.input_tokens_details, "cached_tokens", 0) or 0
                writes = getattr(usage.input_tokens_details, "cache_write_tokens", 0) or 0
                self.stats["input_tokens"] += usage.input_tokens
                self.stats["cached_input_tokens"] += cached
                self.stats["cache_write_tokens"] += writes
                self.stats["output_tokens"] += usage.output_tokens
                rates = PRICES.get(config.model)
                if rates and self.stats["estimated_cost_usd"] is not None:
                    long_input = usage.input_tokens > 272000 and config.model.startswith(("gpt-5", "gpt-6"))
                    input_multiplier, output_multiplier = (2, 1.5) if long_input else (1, 1)
                    self.stats["estimated_cost_usd"] += (((usage.input_tokens-cached-writes)*rates[0]
                                                         + cached*rates[1] + writes*rates[3])*input_multiplier
                                                        + usage.output_tokens*rates[2]*output_multiplier) / 1e6
            return response


def validate_review(review):
    jsonschema.validate(review, REVIEW_SCHEMA)
    if not math.isfinite(review["score"]) or not review["summary"].strip() or any(
        not observation["claim"].strip() for observation in review["observations"]
    ):
        raise ValueError("invalid_review_content")


def agent(paper, calls, config, trace):
    history = [{"role": "user", "content": json.dumps(paper.introduction(), ensure_ascii=False)}]
    reads = 0
    tool_calls = 0
    evidence = PaperEvidence(paper)
    instructions = AGENT_INSTRUCTIONS.format(max_reads=config.max_reads)
    for step in range(1, config.max_reads + 4):
        calls.stats["decision_steps"] = step
        available = TOOLS if reads < config.max_reads else [TOOLS[-1]]
        if reads == config.max_reads:
            trace.write("reading_budget_exhausted", step=step, remaining_tools=["submit_review"])
        response = calls.call(instructions=instructions, input=history, tools=available,
                              parallel_tool_calls=False, tool_choice="required")
        history.extend(item.model_dump(mode="json") for item in response.output)
        actions = [item for item in response.output if item.type == "function_call"]
        if not actions:
            trace.write("decision", step=step, action="no_tool_call", response_status=response.status)
            history.append({"role": "user", "content": "Choose a reading tool or submit_review."})
            continue
        for action in actions:
            tool_calls += 1
            calls.stats["tool_calls"] = tool_calls
            trace.write("decision", step=step, action=action.name, call_id=action.call_id,
                        arguments=action.arguments)
            try:
                arguments = json.loads(action.arguments)
                schema = next((tool["parameters"] for tool in available if tool["name"] == action.name), None)
                if schema is None:
                    observation = {"error": "unknown_or_unavailable_tool"}
                else:
                    jsonschema.validate(arguments, schema)
                    if action.name == "submit_review":
                        validate_review(arguments["review"])
                        calls.stats["submission_attempts"] += 1
                        checks = evidence.check(arguments["review"])
                        if calls.stats["first_submission_checks"] is None:
                            calls.stats["first_submission_checks"] = checks
                        trace.write("tool_call", step=step, name=action.name, arguments=arguments)
                        if all(check["citation_verified"] and check["observed"] for check in checks):
                            trace.write("tool_observation", step=step, call_id=action.call_id,
                                        observation={"accepted": True, "citation_checks": checks})
                            return arguments["review"], {"reading_actions": reads, "tool_calls": tool_calls,
                                                         "decision_steps": step,
                                                         "evidence_observed": [check["observed"] for check in checks]}
                        calls.stats["rejected_submissions"] += 1
                        observation = {"error": "citation_validation_failed", "citation_checks": checks,
                                       "hint": "Copy exact quotes from observed pages, or read matching pages before resubmitting. Preserve case, mathematical notation, and ambiguous hyphens."}
                    else:
                        reads += 1  # Errors and empty searches still consume reading actions.
                        calls.stats["reading_actions"] = reads
                        trace.write("tool_call", step=step, name=action.name, arguments=arguments)
                        if action.name == "search_paper":
                            observation = paper.search(arguments["query"])
                        else:
                            observation = paper.read_pages(arguments["start"], arguments["end"])
                        evidence.remember(action.name, observation)
            except (json.JSONDecodeError, jsonschema.ValidationError) as exc:
                observation = {"error": "invalid_arguments", "type": type(exc).__name__}
            except Exception as exc:
                observation = {"error": "tool_exception", **safe_error(exc)}
            trace.write("tool_observation", step=step, call_id=action.call_id, observation=observation)
            history.append({"type": "function_call_output", "call_id": action.call_id,
                            "output": json.dumps(observation, ensure_ascii=False)})
    raise RuntimeError("model_decision_budget_exhausted")


def baseline(paper, calls, trace):
    calls.stats["decision_steps"] = 1
    response = calls.call(instructions=RUBRIC, input=[{"role": "user", "content": paper.full_text()}],
                          text={"format": {"type": "json_schema", "name": "paper_review",
                                           "schema": REVIEW_SCHEMA, "strict": True}})
    trace.write("decision", step=1, action="final_answer", content=response.output_text)
    review = json.loads(response.output_text)
    validate_review(review)
    calls.stats["submission_attempts"] = 1
    calls.stats["first_submission_checks"] = paper.check_citations(review)
    return review, {"reading_actions": 0, "tool_calls": 0, "decision_steps": 1}


def run_review(paper_path, out, config, task_id, variant="agent", client=None, metadata=None):
    details = variant_metadata(variant)
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    trace = Trace(out / "trace.jsonl", context={"task_id": task_id, "variant": variant})
    start = time.perf_counter()
    versions = {package: importlib.metadata.version(package)
                for package in ("openai", "pypdf", "jsonschema")}
    trace.write("run_start", task_id=task_id, variant=variant, config=asdict(config),
                prompt_version=details["prompt_version"], rubric_version=RUBRIC_VERSION,
                checker_version=CHECKER_VERSION, paper_path=str(paper_path),
                dependencies=versions, pricing_usd_per_million=PRICES.get(config.model),
                pricing_checked="2026-10-26", metadata=metadata or {}, harness=details,
                trace_version=2)
    calls = ModelCalls(client or OpenAI(max_retries=0, timeout=config.timeout), config, trace)
    result = {"task_id": task_id, "variant": variant, "model": config.model,
              "prompt_version": details["prompt_version"], "rubric_version": RUBRIC_VERSION,
              "harness": details,
              "checker_version": CHECKER_VERSION, "status": "error", "review": None,
              "reading_actions": None, "tool_calls": None, "decision_steps": None}
    try:
        paper = Paper.load(paper_path)
        trace.write("environment", snapshot_sha256=file_hash(paper_path),
                    paper_metadata={k: v for k, v in paper.snapshot.items() if k != "pages"})
        if len(paper.full_text()) > config.max_paper_chars:
            raise ValueError("paper_exceeds_documented_input_limit")
        if variant == "agent":
            review, trajectory = agent(paper, calls, config, trace)
        elif variant == "baseline":
            review, trajectory = baseline(paper, calls, trace)
        else:
            try:
                from .pyagent_runner import run_pyagent
            except ModuleNotFoundError as exc:
                if exc.name and exc.name.startswith("pyagent_patterns"):
                    raise RuntimeError("pyagent_dependency_missing") from exc
                raise
            review, trajectory = run_pyagent(paper, calls, config, trace)
        validate_review(review)
        result.update(status="ok", review=review, **trajectory)
        result["citation_checks"] = paper.check_citations(review)
    except Exception as exc:
        result["error"] = safe_error(exc)
        # Only our own fixed error codes are safe to include verbatim.
        if type(exc) in (ValueError, RuntimeError) and str(exc) in {
            "paper_has_no_extractable_text", "paper_exceeds_documented_input_limit",
            "model_decision_budget_exhausted",
            "invalid_review_content",
            "pyagent_dependency_missing", "pyagent_finished_without_accepted_review",
        }:
            result["error"]["code"] = str(exc)
        trace.write("run_error", error=result["error"])
    finally:
        result.update(calls.stats)
        result["latency_seconds"] = time.perf_counter() - start
        trace.write("run_end", result=result)
        try:
            render_run(out / "trace.jsonl")
        except Exception as exc:
            trace.write("report_error", error=safe_error(exc))
        finally:
            trace.close()
    return result
