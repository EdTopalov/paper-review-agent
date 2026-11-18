# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**baseline · ok**

1 model calls · 0 reads · 5.73 s · $0.000587

1 decisions · 0 tool calls · 35056 input tokens (35053 cached) · 473 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

SWE-bench introduces a large, execution-evaluated benchmark of real GitHub issue/PR pairs for repository-level code editing, and establishes baseline results showing that the tested models solve few tasks. Its main value is a realistic task formulation and a documented construction pipeline; the results also expose context-selection and patch-generation difficulties. The evidence supports the benchmark and its initial baseline claims, but does not establish that the benchmark fully represents software engineering or that its scores generalize beyond the selected Python repositories and evaluation setup. I inspected the supplied main text and appendix excerpts (pages 1–46); no later material was supplied.

- **strength**: The benchmark’s task construction uses real issues and patches, then filters candidates with execution checks for tests that change from failing to passing, giving the benchmark a concrete verification basis.
  - Page 2 · citation: whitespace
  - Quote: "We filter out task instances without at least one test where its status changes from a fail to pass"

- **strength**: The evaluation demonstrates substantial difficulty for the tested systems: even under reference-file oracle retrieval, the best reported resolution rate is low.
  - Page 6 · citation: not_found
  - Quote: "Claude 2 only achieves a mere 4.8% pass rate using the “oracle” retrieval context."

- **limitation**: The authors explicitly bound the initial benchmark to Python and identify broader language/domain coverage as future work; conclusions should therefore be scoped accordingly.
  - Page 9 · citation: exact
  - Quote: "SWE-bench task instances are all in Python"

- **uncertainty**: The paper acknowledges that passing tests alone does not ensure a dependable or high-quality patch, leaving the relationship between benchmark success and practical engineering quality unresolved.
  - Page 9 · citation: whitespace
  - Quote: "relying solely on this method is insufficient to guarantee reliable performance of model generations"

Unresolved questions:

- How representative are issues from these 12 popular Python repositories of software engineering tasks in less popular projects, other languages, and different development practices?
- How sensitive are reported solve rates to the selected issue/PR linking, test-file, and execution-validation filters, and to the generated-patch repair step?
- How well do test-passing benchmark scores predict human judgments of patch correctness, maintainability, and usefulness in real development workflows?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
