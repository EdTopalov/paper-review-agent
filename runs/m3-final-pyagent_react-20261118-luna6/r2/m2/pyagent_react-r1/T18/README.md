# T18: Gorilla: Large Language Model Connected with Massive APIs

**pyagent_react · ok**

5 model calls · 3 reads · 19.46 s · $0.002207

5 decisions · 5 tool calls · 37814 input tokens (28275 cached) · 1464 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.67

Gorilla fine-tunes a LLaMA-7B model on synthetic API-call instructions and optionally conditions it on retrieved API documentation. The paper contributes APIBench and evaluates API selection, hallucination, documentation changes, and constraint handling. Results show strong performance in several settings, while also revealing that retrieval quality materially affects outcomes. The benchmark and evaluation are useful but bounded: examples are synthetic, API coverage is selective, and correctness is assessed by matching a reference API rather than broad semantic equivalence.

- **strength**: The paper provides a sizeable, multi-hub API benchmark and a systematic evaluation setup.
  - Page 4 · citation: exact
  - Quote: "a total of 10 instruction-api pairs"

- **strength**: On the reported zero-shot benchmark, Gorilla scores higher than GPT-4 on all three hub datasets, with particularly large margins on HuggingFace and TensorFlow Hub.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: The correctness metric is reference-dataset matching, which does not establish semantic equivalence across valid alternative APIs.
  - Page 5 · citation: whitespace
  - Quote: "we compare their functional equivalence using the dataset we collected."

- **uncertainty**: The retrieval results leave practical performance dependent on better retrieval: the reported non-oracle methods sometimes fall well below oracle performance.
  - Page 7 · citation: whitespace
  - Quote: "using GPT-Index at evaluation results in 29.20% accuracy degradation, and using BM25 results in a 52.27% accuracy degradation."

Unresolved questions:

- How well does the approach perform on real user requests and APIs outside the selected ML hubs, given that the instruction examples are synthetically generated?
- How robust are the results to alternative test splits that hold out APIs, rather than dividing instruction–API pairs?
- How often do generated calls execute successfully and satisfy user intent when several APIs are semantically valid?
- I inspected pages 1–9, not the remainder of the paper; details or qualifications elsewhere may affect these questions.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the method and benchmark construction. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 7, "end": 9}` | Inspect evaluation results and experimental comparisons. | read pages [7, 8, 9] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 5, "end": 6}` | Inspect evaluation protocol and benchmark limitations. | read pages [5, 6] | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.67, "observations": 4}}` | Submit an evidence-based assessment using inspected method and result pages. | citation_validation_failed; #4: wrong_page (pages [7]) | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.67, "observations": 4}}` | Correct the retrieval citation to the observed page. | review accepted | [event 26](trace.jsonl#L26) |
