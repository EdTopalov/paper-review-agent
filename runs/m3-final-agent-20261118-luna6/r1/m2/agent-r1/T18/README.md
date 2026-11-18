# T18: Gorilla: Large Language Model Connected with Massive APIs

**agent · ok**

5 model calls · 4 reads · 14.14 s · $0.001440

5 decisions · 5 tool calls · 23478 input tokens (15464 cached) · 599 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Gorilla combines instruction fine-tuning of a LLaMA-based model with API documentation retrieval, and introduces APIBench for evaluating API-call generation across three ML API ecosystems. Its held-out benchmark results show strong performance and reduced hallucinations in several settings, while retrieval-aware training is presented as a way to adapt calls to changing documentation. The evidence is useful but bounded to ML APIs and generated-call matching rather than demonstrated execution in deployed tool workflows.

- **strength**: The paper reports competitive held-out results, including Gorilla’s high zero-shot performance, but not uniform dominance across retriever conditions.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **strength**: The work provides a benchmark and evaluates multiple models and retrieval settings on a held-out split of its collected instruction/API pairs.
  - Page 6 · citation: whitespace
  - Quote: "We emphasize that we have maintained a holdout test set on which we report our findings."

- **limitation**: The declared benchmark scope is ML APIs, so evidence here does not establish performance across the broader API ecosystem.
  - Page 9 · citation: whitespace
  - Quote: "we chose ML APIs, given their functional similarity."

- **uncertainty**: The inspected material does not establish execution correctness or performance in live tool-use settings; conclusions are based on generated call evaluation and curated datasets.
  - Page 6 · citation: whitespace
  - Quote: "We then compare this to our dataset, to see if the API dataset has a subtree match."

Unresolved questions:

- How well does the approach generalize to non-ML APIs, larger evolving catalogs, and user requests outside the collected data distribution?
- Do the reported call-structure and documentation-change results translate into reliable execution and outcomes in live API workflows?
- How sensitive are results to benchmark construction and the model-generated instruction/API pairs? The pages inspected did not cover dataset generation details or full experimental protocols.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "experiments"}` | Locate the paper's evaluation evidence and reported comparisons. | 3 matches on pages [4, 6, 10] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 6, "end": 8}` | Read quantitative evaluation, benchmark details, and stated scope/limitations. | read pages [6, 7, 8] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Check whether the authors explicitly state limitations or evaluation scope. | 3 matches on pages [2, 9, 13] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 9, "end": 9}` | Read the stated limitations and conclusion to calibrate scope. | read pages [9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit an evidence-based assessment using the inspected evaluation and limitation pages. | review accepted | [event 25](trace.jsonl#L25) |
