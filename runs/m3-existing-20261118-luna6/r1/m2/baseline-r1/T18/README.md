# T18: Gorilla: Large Language Model Connected with Massive APIs

**baseline · ok**

1 model calls · 0 reads · 9.11 s · $0.002525

1 decisions · 0 tool calls · 17424 input tokens (0 cached) · 694 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Gorilla presents a practical pipeline for generating API calls by fine-tuning a LLaMA-7B model on a curated corpus of ML APIs, with retrieval-aware training intended to help it use updated documentation. Its benchmark results show promising gains over several prompted baselines in API identification and reduced hallucination, while also revealing that retrieval quality can substantially affect performance. The contribution is useful and supported by broad experiments on the paper’s benchmark, but the evaluation measures API matching rather than successful execution and has a notable comparability caveat for HuggingFace.

- **strength**: The paper contributes a concrete benchmark and training approach, and reports strong zero-shot results for Gorilla on the included API collections.
  - Page 7 · citation: normalized
  - Quote: "lightly fine-tuned Gorilla gets the state-of-the-art performance zero-shot over all the models"

- **strength**: The experiments make an important practical qualification: retrieval does not reliably help unless the retrieved documentation is suitable.
  - Page 7 · citation: whitespace
  - Quote: "adding a non-optimal retriever at test time will sometime misguide the model and result in more errors."

- **limitation**: The reported API-matching metric does not establish that generated code runs or accomplishes the requested task; the appendix explicitly says execution results were not tested.
  - Page 13 · citation: whitespace
  - Quote: "we haven’t tested the execution result of the code."

- **limitation**: HuggingFace comparisons are not fully like-for-like: most baselines are evaluated only on domain names, while Gorilla is evaluated differently, limiting the strength of direct performance comparisons.
  - Page 7 · citation: whitespace
  - Quote: "for all the models except Gorilla, we only check if they can provide the correct domain names."

Unresolved questions:

- How well does the approach generalize to APIs or API documentation not represented in the training set, rather than new instructions drawn from the same API collection?
- Do Gorilla’s generated calls execute successfully and satisfy user intent in end-to-end tasks, beyond matching selected API names and arguments?
- How robust are the documentation-change results across a broader set of changes and retrieval errors? The supplied evidence illustrates adaptation with examples, but does not establish performance across a large change set.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
