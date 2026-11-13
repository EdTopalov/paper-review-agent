# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**baseline · ok**

1 model calls · 0 reads · 4.97 s · $0.004657

1 decisions · 0 tool calls · 35056 input tokens (0 cached) · 551 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

SWE-bench introduces a substantial, execution-based benchmark for repository-level software issue resolution, built from 2,294 issue–pull-request pairs across 12 Python repositories, and reports baseline performance for proprietary and fine-tuned models. Its main contribution is a realistic task formulation and dataset pipeline that exposes challenges beyond short code generation; the paper also provides useful diagnostic analyses. Evidence is meaningful but chiefly establishes the benchmark’s construction and difficulty under a limited set of retrieval, prompting, and model setups, rather than validating broader claims about real-world engineering capability.

- **strength**: The benchmark construction connects real issue reports and accepted fixes to executable regression tests, and filters out instances that do not demonstrate a fail-to-pass test transition.
  - Page 2 · citation: whitespace
  - Quote: "We filter out task instances without at least one test where its status changes from a fail to pass"

- **strength**: The paper demonstrates that the evaluated models perform poorly under its tested settings, including when reference-edited files are supplied as context.
  - Page 6 · citation: wrong_page
  - Quote: "The best performing model, Claude 2, only achieves a mere 4.8% pass rate using the “oracle” retrieval context."

- **limitation**: The authors explicitly scope the dataset to Python, so the reported benchmark coverage does not establish performance across programming languages or software domains.
  - Page 9 · citation: exact
  - Quote: "SWE-bench task instances are all in Python"

- **uncertainty**: The paper says its experiments are intended as simple baselines, leaving open how substantially stronger agentic or tool-using systems would perform; those approaches are proposed as future work rather than evaluated here.
  - Page 9 · citation: whitespace
  - Quote: "our experiments aim to establish a baseline of the simplest and most straight-forward approaches for this task"

Unresolved questions:

- How well do the benchmark’s collection and evaluation criteria transfer to repositories in other languages and to less popular or differently maintained projects?
- How much would results change with interactive repository exploration, execution feedback, or multiple generation attempts, rather than the paper’s tested retrieval and generation setups?
- To what extent do passing the selected tests and matching the benchmark’s resolution criterion capture patch quality, maintainability, and correctness beyond those tests?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
