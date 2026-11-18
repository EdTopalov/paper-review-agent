# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**baseline · ok**

1 model calls · 0 reads · 6.95 s · $0.000606

1 decisions · 0 tool calls · 35056 input tokens (35053 cached) · 510 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

SWE-bench introduces a substantial, execution-based benchmark for repository-level software engineering: 2,294 issue-and-patch tasks from 12 Python repositories, plus a separate training set and baseline evaluations. Its realistic task formulation and analysis of retrieval and context challenges make a useful contribution, while the paper’s own limitations and filtering design mean its scores should be read as performance on this particular benchmark setup—not a complete measure of software engineering ability.

- **strength**: The benchmark pipeline ties real issue descriptions and merged PRs to runnable tests, with filtering for tasks where the reference solution changes at least one test from failing to passing. This provides a concrete, reproducible evaluation target.
  - Page 2 · citation: whitespace
  - Quote: "We filter out task instances without at least one test where its status changes from a fail to pass"

- **strength**: The experiments provide informative evidence that context selection is a major bottleneck: the reported best proprietary-model result remains low even with reference-patch files supplied, and BM25 performance is lower still.
  - Page 5 · citation: exact
  - Quote: "Claude 2, only achieves a mere 4.8% pass rate using the “oracle” retrieval context."

- **limitation**: The benchmark is restricted to Python and popular repositories, and execution-based tests cannot establish that passing patches are robust, readable, or comprehensive. The authors explicitly recognize these boundaries.
  - Page 9 · citation: whitespace
  - Quote: "relying solely on this method is insufficient to guarantee reliable performance of model generations"

- **uncertainty**: The main results are tied to a narrow baseline setup, including greedy single-sample generation; the paper encourages other methods, but the supplied evaluation does not establish how performance changes with sampling or stronger interactive agent workflows.
  - Page 24 · citation: exact
  - Quote: "we only generate a single patch file per instance."

Unresolved questions:

- How well do benchmark outcomes generalize to less popular repositories, other programming languages, and software work not captured by issue-linked PRs?
- How much do the low solve rates reflect model reasoning limits versus retrieval, prompt construction, patch formatting, or execution-harness choices?
- Would human review or broader behavioral checks change conclusions about the quality and practical usefulness of patches that pass the benchmark tests?
- I inspected the supplied pages 1–46; the cited appendix material includes additional qualitative examples and technical details, but I did not independently validate the released data or reproduce the experiments.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
