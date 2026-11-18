# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**baseline · ok**

1 model calls · 0 reads · 6.81 s · $0.000600

1 decisions · 0 tool calls · 35056 input tokens (35053 cached) · 498 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

SWE-bench introduces a substantial, practically motivated benchmark for repository-level software engineering: 2,294 issue-and-pull-request tasks from 12 Python repositories, evaluated by applying model-generated patches and running tests. Its construction pipeline, baseline comparisons, retrieval analyses, and qualitative cases provide useful evidence that the tested models struggled with these tasks. The paper is especially valuable as an evaluation framework and diagnostic study, though its experiments are baseline-oriented and its scope and test-based measure leave meaningful limits on what performance establishes.

- **strength**: The benchmark connects real issue reports to accepted fixes and checks patches through executable tests, a concrete and scalable evaluation design.
  - Page 2 · citation: whitespace
  - Quote: "we apply the PR’s test content, and log the associated test results before and after the PR’s other content is applied."

- **strength**: The paper reports sharply low baseline resolution rates and a useful retrieval comparison, supporting its claim that the benchmark was difficult for the evaluated models.
  - Page 6 · citation: wrong_page
  - Quote: "The best performing model, Claude 2, only achieves a mere 4.8% pass rate using the “oracle” retrieval context."

- **limitation**: The authors explicitly limit the dataset to Python, so the benchmark’s empirical findings do not directly establish difficulty across languages or software domains.
  - Page 9 · citation: exact
  - Quote: "SWE-bench task instances are all in Python"

- **limitation**: Passing the benchmark’s tests is not sufficient evidence of software quality; the authors acknowledge test-based evaluation cannot guarantee reliable, comprehensive, or readable solutions.
  - Page 9 · citation: whitespace
  - Quote: "relying solely on this method is insufficient to guarantee reliable performance of model generations"

Unresolved questions:

- How well would results generalize to less popular repositories, other programming languages, or software projects with different testing and maintenance practices?
- How sensitive are measured resolution rates to the benchmark’s issue/PR matching, test-selection, and filtering pipeline, including the risk that tests incompletely represent the stated issue?
- The paper says the experiments establish simple baselines and focuses on a limited set of model and retrieval approaches; how much could stronger repository-navigation or interactive tool-using systems improve performance?
- Inspection was limited to the supplied text, including the main paper and portions of the appendix; the full construction/evaluation code and all implementation details were not independently inspected.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
