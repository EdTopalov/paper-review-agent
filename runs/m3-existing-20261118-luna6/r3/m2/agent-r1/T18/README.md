# T18: Gorilla: Large Language Model Connected with Massive APIs

**agent · ok**

4 model calls · 3 reads · 8.13 s · $0.001252

4 decisions · 4 tool calls · 18679 input tokens (11891 cached) · 594 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Gorilla combines API-focused instruction fine-tuning of a LLaMA-7B model with retrieval-aware training, and introduces APIBench for selecting API calls across three ML model hubs. The work offers a useful benchmark and credible evidence that retrieval and task-specific tuning can improve API-call accuracy and documentation adaptation, but its evaluation is bounded to ML APIs and a proxy for functional correctness rather than execution in real tool workflows.

- **strength**: The benchmark and synthetic instruction data provide a concrete, reusable evaluation and training contribution at meaningful scale.
  - Page 4 · citation: exact
  - Quote: "Dataset curation: 1,645 API calls. 94 from Torch Hub (exhaustive), 626 from TensorFlow Hub v2 (exhaustive) and 925 from HuggingFace (Top 20 in each domain)."

- **strength**: Results show retrieval can help materially in some settings, including high accuracy with oracle retrieval, while making clear that retrieval is not uniformly beneficial.
  - Page 8 · citation: exact
  - Quote: "Gorilla with Oracle retriever"

- **limitation**: The correctness evaluation maps calls to the collected dataset and focuses on one call; it does not establish semantic correctness or successful execution in broader workflows.
  - Page 5 · citation: whitespace
  - Quote: "Since we only consider one API call in this paper, checking if the AST of the candidate API call is a sub-tree of the reference API call reveals which API is being used in the dataset."

- **limitation**: The work explicitly bounds its empirical focus to ML APIs, leaving generalization to other API domains unresolved.
  - Page 9 · citation: whitespace
  - Quote: "With the goal of wanting to have a challenging dataset, we chose ML APIs, given their functional similarity."

Unresolved questions:

- How well does the system work when API calls must be executed, chained, or debugged in realistic end-to-end workflows?
- How robust are the findings beyond ML model hubs and beyond the dataset's synthetic instruction distribution?
- I inspected pages 1–5 and 8–9; training implementation specifics, full experimental protocol, and remaining result tables were not examined.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 3}` | Inspect the paper's method and benchmark setup to assess the claimed contribution. | read pages [2, 3] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 5}` | Read training and retrieval details plus benchmark evaluation choices. | read pages [4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 9}` | Inspect reported results and testing design to evaluate evidential strength. | read pages [8, 9] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Evidence covers benchmark construction, retrieval-aware training, results and stated scope; submit concise assessment while noting uninspected details. | review accepted | [event 20](trace.jsonl#L20) |
