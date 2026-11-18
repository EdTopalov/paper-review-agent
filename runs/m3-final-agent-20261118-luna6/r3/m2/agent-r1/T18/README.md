# T18: Gorilla: Large Language Model Connected with Massive APIs

**agent · ok**

4 model calls · 3 reads · 10.24 s · $0.001306

4 decisions · 4 tool calls · 19208 input tokens (11994 cached) · 594 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

Gorilla presents a fine-tuned LLaMA-7B system for generating API calls, an APIBench dataset spanning three ML model hubs, and retriever-aware training intended to handle documentation changes. Its results support strong performance within that benchmark, especially in zero-shot settings, while also showing that practical retrieval quality materially affects outcomes.

- **strength**: The work contributes a concrete dataset and training pipeline: 1,645 APIs are converted into synthetic instruction/API pairs, with retriever-conditioned training explored.
  - Page 4 · citation: exact
  - Quote: "Dataset curation: 1,645 API calls."

- **strength**: On the reported holdout benchmark, Gorilla’s zero-shot overall accuracy exceeds the listed zero-shot baselines in each of the three hubs, supporting its central API-call generation claim in this scope.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: Coverage is deliberately selective rather than exhaustive across HuggingFace, so results do not establish general performance over its much larger model catalog.
  - Page 3 · citation: exact
  - Quote: "To filter these out, we pick the top 20 models from each domain."

- **limitation**: The reported experiments expose a substantial dependence on retriever quality: conventional retrievers fall well below the oracle setting, limiting the practical force of claims about test-time adaptability.
  - Page 7 · citation: whitespace
  - Quote: "using GPT-Index at evaluation results in 29.20% accuracy degradation, and using BM25 results in a 52.27% accuracy degradation."

Unresolved questions:

- How robust are conclusions to independently authored or non-synthetic user requests, given that instruction/API pairs are GPT-4-generated and divided into train/test sets?
- How well does AST subtree matching track executable correctness and whether generated calls satisfy the user’s intended task?
- The reviewed excerpts do not establish adaptation performance quantitatively across a broad set of documentation changes; the change examples are illustrative.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "evaluation"}` | Locate the paper’s evaluation evidence and reported comparisons. | 8 matches on pages [3, 6, 7] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 6, "end": 8}` | Read experimental setup, benchmark results, and retrieval limitations for evidence-based assessment. | read pages [6, 7, 8] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 3, "end": 4}` | Inspect dataset construction and method details to assess benchmark scope and training contribution. | read pages [3, 4] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Evidence covers dataset/method and core benchmark results; submit calibrated review while noting uninspected portions. | review accepted | [event 20](trace.jsonl#L20) |
