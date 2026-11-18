# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**baseline · ok**

1 model calls · 0 reads · 6.28 s · $0.000609

1 decisions · 0 tool calls · 35056 input tokens (35053 cached) · 516 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

This paper introduces SWE-bench, a benchmark of 2,294 issue-and-pull-request tasks from 12 Python repositories, with execution-based validation, and reports baseline results for proprietary models and fine-tuned SWE-Llama. Its main contribution is a realistic, extensible repository-level evaluation setting; the experiments and qualitative cases show that these baselines solve few tasks and expose challenges in context selection, patch generation, and codebase reasoning.

- **strength**: The benchmark construction connects real issues and merged fixes to tests that demonstrate a change in behavior, providing a concrete evaluation target at repository scale.
  - Page 2 · citation: whitespace
  - Quote: "We filter out task instances without at least one test where its status changes from a fail to pass"

- **strength**: The evaluation demonstrates both low baseline resolution rates and a substantial sensitivity to retrieval context, making context selection a meaningful part of the task.
  - Page 5 · citation: whitespace
  - Quote: "When evaluated in the BM25 retrieval setting, Claude 2’s performance drops to1.96%."

- **limitation**: The authors explicitly bound the benchmark to Python and identify test-based evaluation as insufficient to assess qualities such as readability and comprehensiveness.
  - Page 9 · citation: exact
  - Quote: "SWE-bench task instances are all in Python"

- **uncertainty**: The reported model results use greedy decoding and one generation per instance, so the paper does not establish how results vary across sampling or repeated attempts. I inspected the main paper and the inference details, not every appendix section.
  - Page 24 · citation: exact
  - Quote: "we only generate a single patch file per instance."

Unresolved questions:

- How well do the benchmark’s issue descriptions and selected tests represent the range and quality of real software engineering tasks beyond these repositories and Python?
- How would success rates change with repeated sampling, stronger retrieval, or interactive agent workflows, rather than the paper’s single-generation baseline?
- How reliably do passing selected tests indicate a correct, maintainable fix, given the authors’ stated concern that execution-based testing alone cannot guarantee quality?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
