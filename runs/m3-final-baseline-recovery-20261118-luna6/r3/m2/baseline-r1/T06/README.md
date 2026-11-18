# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**baseline · ok**

1 model calls · 0 reads · 7.64 s · $0.000627

1 decisions · 0 tool calls · 35056 input tokens (35053 cached) · 552 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

SWE-bench introduces an execution-verified benchmark of 2,294 real GitHub issue–pull-request tasks across 12 Python repositories, alongside a 19,000-instance training set and baseline evaluations. Its central contribution is a realistic repository-level evaluation setting that exposes substantial gaps in the tested models’ ability to locate relevant code, produce effective patches, and pass tests. The construction pipeline and experimental findings are useful and reasonably well documented, though conclusions are bounded by the Python-only task pool, selective repository/task filtering, and the specific models and inference setup evaluated.

- **strength**: The paper provides a concrete, multi-stage construction pipeline and filters for tasks whose reference changes are testable and nontrivial.
  - Page 2 · citation: hyphenation_ambiguous
  - Quote: "Through these stages of filtering, the original 90,000 PRs are filtered down to the 2,294 task instances"

- **strength**: The evaluation makes a compelling case that these baselines struggled in this benchmark, including with oracle-selected files; that result is evidence about this setup, not a general measure of all software-engineering capability.
  - Page 6 · citation: wrong_page
  - Quote: "The best performing model, Claude 2, only achieves a mere 4.8% pass rate using the “oracle” retrieval context."

- **limitation**: The authors explicitly bound the benchmark to Python and identify expansion to other languages and domains as future work.
  - Page 9 · citation: exact
  - Quote: "SWE-bench task instances are all in Python"

- **limitation**: Passing tests is not presented as a sufficient measure of solution quality; the authors caution that generated code may be less comprehensive, efficient, or readable than human solutions.
  - Page 9 · citation: whitespace
  - Quote: "relying solely on this method is insufficient to guarantee reliable performance of model generations"

Unresolved questions:

- How representative are the benchmark tasks of software issues outside the selected popular Python repositories, given the construction filters and repository selection strategy?
- How do results change with repeated sampling or alternative inference strategies, given that the reported generation setup uses a single greedy patch per instance?
- To what extent would stronger retrieval, interactive tool use, or human evaluation of maintainability and correctness change the conclusions drawn from test-based pass rates?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
