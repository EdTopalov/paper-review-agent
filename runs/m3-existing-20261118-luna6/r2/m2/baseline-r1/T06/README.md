# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**baseline · ok**

1 model calls · 0 reads · 6.78 s · $0.000622

1 decisions · 0 tool calls · 35056 input tokens (35053 cached) · 543 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

SWE-bench introduces a substantial, execution-verified benchmark of 2,294 real GitHub issue–pull-request tasks across 12 Python repositories, and establishes baseline results showing that the evaluated models rarely solve them. Its realistic task construction and analysis of retrieval, context length, and patch-generation behavior make it a useful research contribution. The paper’s evidence is strongest for the benchmark and these initial baselines; conclusions are bounded by the Python-only dataset, the particular models and inference setup, and reliance on tests as the success criterion.

- **strength**: The benchmark connects real issues and merged fixes to executable tests, providing a concrete repository-level evaluation rather than isolated code completion.
  - Page 2 · citation: hyphenation_ambiguous
  - Quote: "Through these stages of filtering, the original 90,000 PRs are filtered down to the 2,294 task instances which comprise SWE-bench."

- **strength**: The experiments offer informative evidence that context selection and length matter: BM25 performance is low, and the reported collapsed-oracle ablation improves results for the tested models.
  - Page 6 · citation: whitespace
  - Quote: "In this setting, we see increases in performance, with GPT-4 jumping from 1.3% to 3.4% and Claude 2 from 4.8% to 5.9%."

- **limitation**: The authors explicitly bound the benchmark’s coverage to Python and recognize that passing tests does not establish the quality or reliability of generated code.
  - Page 9 · citation: normalized
  - Quote: "Lastly, while this work evaluates models using execution-based code testing, relying solely on this method is insufficient to guarantee reliable performance of model generations"

- **uncertainty**: The model comparisons are limited by uneven evaluation coverage and a single greedy generation per instance; how alternative sampling or repeated trials would affect the reported rates is not established here.
  - Page 6 · citation: whitespace
  - Quote: "Due to budget constraints we evaluate GPT-4 on a 25% random subset of SWE-bench in the “oracle” and BM25 27K retriever settings only."

Unresolved questions:

- How well would the benchmark’s construction and evaluation pipeline generalize to languages and repository ecosystems beyond Python?
- How sensitive are resolution rates and relative model rankings to multiple samples, alternative decoding strategies, or stronger repository-navigation agents?
- To what extent do test-based scores track human judgments of patch quality, maintainability, and correctness on behavior not covered by the selected tests?
- Inspection here is limited to the supplied pages and excerpts; detailed construction and training appendices beyond the included material were not assessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
