# T18: Gorilla: Large Language Model Connected with Massive APIs

**agent · ok**

4 model calls · 3 reads · 11.73 s · $0.001346

4 decisions · 4 tool calls · 19053 input tokens (11864 cached) · 682 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

Gorilla fine-tunes a LLaMA-7B model to generate API calls and introduces APIBench, built from three ML model hubs. Its results show notable gains over the evaluated zero-shot LLM baselines on this benchmark, while retrieval-aware training offers a route to adapting calls to changing documentation. The work is useful and empirically grounded, but conclusions are bounded by a curated, synthetic-instruction benchmark and uneven evaluation criteria.

- **strength**: The paper reports strong benchmark performance for Gorilla without retrieval against the tested zero-shot baselines, especially on HuggingFace and TensorFlow Hub.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **strength**: The benchmark combines a sizable set of documented APIs with generated instruction/API pairs, providing a concrete, reproducible evaluation target as described by the authors.
  - Page 4 · citation: exact
  - Quote: "Dataset curation: 1,645 API calls. 94 from Torch Hub (exhaustive), 626 from TensorFlow Hub v2 (exhaustive) and 925 from HuggingFace (Top 20 in each domain)."

- **limitation**: The sampled HuggingFace and generated instruction data limit how far benchmark results establish performance across the full API ecosystem or naturally occurring requests.
  - Page 4 · citation: whitespace
  - Quote: "For each of our 1,645 API datapoints, we sample 3 of 6 corresponding instruction examples to generate a total of 10 instruction-api pairs"

- **limitation**: The comparison is not uniform across all API domains: for HuggingFace, most models are evaluated only on domain-name selection, whereas Gorilla is evaluated differently.
  - Page 7 · citation: whitespace
  - Quote: "for all the models except Gorilla, we only check if they can provide the correct domain names. So this problem reduces to picking one of the multiple choices."

Unresolved questions:

- How robust are the reported gains on real user requests and APIs outside the three evaluated hubs, particularly APIs not represented in training?
- How much does retrieval-aware adaptation improve measured accuracy under controlled, broad documentation updates, beyond the illustrative examples?
- I inspected pages 1, 3–4, and 6–8; I did not inspect the remaining methodology, later evaluation sections, appendices, or discussion, so further evidence and limitations may be present there.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Results"}` | Locate evaluation results to assess empirical support for the paper's central claims. | 8 matches on pages [4, 6, 7, 8] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 6, "end": 8}` | Inspect benchmark setup and reported scores, including caveats about retriever performance. | read pages [6, 7, 8] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 3, "end": 4}` | Review dataset construction and method details to contextualize benchmark scope. | read pages [3, 4] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Evidence covers the benchmark, dataset construction, central results, and retriever caveats; submit an independent assessment while noting uninspected material. | review accepted | [event 20](trace.jsonl#L20) |
