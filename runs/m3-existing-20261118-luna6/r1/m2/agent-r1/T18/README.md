# T18: Gorilla: Large Language Model Connected with Massive APIs

**agent · ok**

5 model calls · 4 reads · 10.06 s · $0.001866

5 decisions · 5 tool calls · 29129 input tokens (18173 cached) · 662 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Gorilla presents a practical pipeline for API-call generation: curated API documentation and synthetic instruction pairs fine-tune a 7B model, with optional retrieval-aware training intended to improve correctness and adaptability to documentation changes. The benchmark and comparisons provide useful evidence within ML model-hub APIs, but conclusions depend on a narrow domain, synthetic held-out prompts, and an AST-based proxy for correctness.

- **strength**: The work provides a sizable, explicit benchmark and a reproducible evaluation framing for API selection across three model hubs.
  - Page 2 · citation: whitespace
  - Quote: "We choose three major model hubs for dataset construction: TorchHub, TensorHub and HuggingFace."

- **strength**: Reported results show Gorilla’s fine-tuned zero-shot model outperforming the compared GPT-4 baseline on all three listed datasets, while also illustrating that retrieval quality matters.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: The test split is drawn from synthetic instruction/API pairs, so the reported holdout does not establish performance on independently authored real-user requests.
  - Page 6 · citation: whitespace
  - Quote: "The holdout test set was created by dividing the self-instruct dataset’s instruction, API pairs into training and testing sets."

- **limitation**: The correctness metric identifies dataset API matches rather than semantic equivalence across valid alternatives, limiting what accuracy can establish; the authors also explicitly restrict the scope to one API call.
  - Page 5 · citation: whitespace
  - Quote: "Since we only consider one API call in this paper, checking if the AST of the candidate API call is a sub-tree of the reference API call reveals which API is being used in the dataset."

Unresolved questions:

- How well would performance transfer to real user queries, APIs outside ML model hubs, or multi-step API use?
- How sensitive are conclusions to prompt generation and the AST-match metric, especially where multiple APIs can satisfy a request?
- I inspected the main text excerpts through page 9, not the remaining pages or appendix; details of training, statistical variability, and additional limitations remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 3}` | Inspect method and dataset design to assess the claimed API-calling contribution. | read pages [2, 3] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 5}` | Review training, evaluation setup, and benchmark construction details. | read pages [4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 9}` | Inspect quantitative comparisons and reported evaluation outcomes. | read pages [8, 9] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 6, "end": 7}` | Check benchmark protocols and baseline comparisons for important methodological qualifications. | read pages [6, 7] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Evidence covers benchmark scope, evaluation protocol, reported results, and stated limitations; submit concise assessment while flagging uninspected appendix details. | review accepted | [event 25](trace.jsonl#L25) |
