# T18: Gorilla: Large Language Model Connected with Massive APIs

**agent · ok**

7 model calls · 5 reads · 19.95 s · $0.003091

7 decisions · 7 tool calls · 45066 input tokens (27444 cached) · 1271 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

Gorilla presents an API-call benchmark and a fine-tuned LLaMA-7B system trained to use API documentation, reporting strong accuracy and reduced hallucination on APIBench. Its useful contribution is a systematic evaluation and training pipeline for selecting API calls across several ML model hubs, with evidence that retrieval-aware training can support documentation changes. Evidence is concentrated on curated ML-hub APIs and AST-match correctness, not verified execution across general-purpose APIs.

- **strength**: APIBench provides concrete coverage across three model hubs, with self-instruct prompts and an explicit structural correctness check.
  - Page 2 · citation: whitespace
  - Quote: "We exhaustively include every API call in TorchHub (94 API calls) and TensorHub (696 API calls); For HuggingFace, since the models come in a large number and lots of the models don’t have a specification, we choose the most downloaded 20 models per task category (in a total of 925)."

- **strength**: On the reported holdout benchmark, Gorilla’s zero-shot accuracy exceeds the listed baselines on each hub, though results vary by retrieval method.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: At evaluation, tested conventional retrievers can substantially underperform oracle retrieval, limiting practical retrieval benefits.
  - Page 7 · citation: whitespace
  - Quote: "using GPT-Index at evaluation results in 29.20% accuracy degradation, and using BM25 results in a 52.27% accuracy degradation."

- **uncertainty**: I inspected the abstract, dataset/method material, and evaluation pages, but not the full later discussion or appendices; broader execution validity and generalization beyond selected ML APIs remain unresolved.
  - Page 3 · citation: whitespace
  - Quote: "we focus on a much restricted domain: the synthesis of linear programs using API calls."

Unresolved questions:

- How often do generated calls execute successfully in real environments, rather than match an API subtree?
- How robust are results to independently authored user requests and API documentation beyond synthetic prompts derived from these hubs?
- Can retrieval methods close the observed gap to oracle retrieval under realistic documentation updates?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "evaluation"}` | Locate the paper’s evaluation evidence to assess support for its API-calling claims. | 8 matches on pages [3, 6, 7] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 6, "end": 8}` | Inspect benchmark setup, quantitative results, and retrieval limitations with page-specific evidence. | read pages [6, 7, 8] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Check whether authors explicitly describe evaluation scope or limitations to distinguish known boundaries from open questions. | 3 matches on pages [2, 9, 13] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 2, "end": 3}` | Verify the stated benchmark contribution and dataset construction before scoring the paper. | read pages [2, 3] | [event 20](trace.jsonl#L20) |
| 5 | search_paper `{"query": "not tested"}` | Check the paper’s explicit caveat about execution-level evaluation and its scope. | 0 matches | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence covers benchmark design, results, and retrieval caveats; submit an assessment while acknowledging limited inspection of later sections. | citation_validation_failed; #3: wrong_page (pages [7]) | [event 31](trace.jsonl#L31) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the retrieval limitation citation to the observed evaluation page and finalize the review. | review accepted | [event 37](trace.jsonl#L37) |
