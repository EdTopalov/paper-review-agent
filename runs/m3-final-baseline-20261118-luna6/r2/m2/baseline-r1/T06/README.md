# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**baseline · ok**

1 model calls · 0 reads · 6.18 s · $0.000594

1 decisions · 0 tool calls · 35056 input tokens (35053 cached) · 487 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

SWE-bench introduces a large, execution-verified benchmark of real GitHub issue-to-patch tasks, documents its construction and evaluation, and reports early baselines showing that contemporary models solve few tasks. Its main contribution is a practical, extensible evaluation setting for repository-level software engineering, rather than a new modeling method. The evidence is substantial for benchmark construction and baseline difficulty, though the initial model comparisons are limited and depend on retrieval, context, and evaluation choices.

- **strength**: The benchmark derives tasks from merged issue-linked pull requests, checks that fixes change tests from failing to passing, and yields 2,294 instances from a much larger pool.
  - Page 2 · citation: hyphenation_ambiguous
  - Quote: "Through these stages of filtering, the original 90,000 PRs are filtered down to the 2,294 task instances"

- **strength**: The paper provides a concrete baseline finding that even oracle-selected files leave models with low resolution rates; this is evidence about the tested setups, not a general ceiling on model capability.
  - Page 6 · citation: wrong_page
  - Quote: "The best performing model, Claude 2, only achieves a mere 4.8% pass rate using the “oracle” retrieval context."

- **limitation**: The authors explicitly bound the benchmark’s language coverage to Python and present the experiments as baseline approaches rather than an exhaustive evaluation of methods.
  - Page 9 · citation: exact
  - Quote: "SWE-bench task instances are all in Python"

- **uncertainty**: The paper itself cautions that passing repository tests does not ensure solution quality, so how well benchmark resolution scores track maintainable, comprehensive engineering remains open.
  - Page 9 · citation: whitespace
  - Quote: "relying solely on this method is insufficient to guarantee reliable performance of model generations"

Unresolved questions:

- How representative are tasks selected from popular, well-maintained Python repositories of software engineering work in less popular projects, other languages, or production settings?
- How robust are the reported model rankings and low resolution rates to alternative retrieval, prompting, decoding, and patch-generation strategies?
- How well do test-based resolution outcomes correspond to expert judgments of correctness, maintainability, and completeness beyond the paper’s limited qualitative examples?
- I inspected the supplied main text and appendix excerpts; I did not independently verify the released data, code, or results.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
