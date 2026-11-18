# T18: Gorilla: Large Language Model Connected with Massive APIs

**baseline · ok**

1 model calls · 0 reads · 7.04 s · $0.000478

1 decisions · 0 tool calls · 17424 input tokens (17421 cached) · 606 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Gorilla combines instruction fine-tuning of a LLaMA-7B model with retrieval-aware training to generate API calls from natural-language requests. The paper contributes an API benchmark spanning three ML model hubs and evaluates API selection, hallucination, documentation changes, and constraints. Results support strong zero-shot performance in the studied setting, but retrieval can reduce accuracy, and the evaluation measures API matching rather than whether generated calls execute successfully.

- **strength**: The benchmark and training setup provide a concrete, useful way to study API selection across multiple model hubs, and the reported zero-shot results show substantial gains for Gorilla on these datasets.
  - Page 7 · citation: normalized
  - Quote: "lightly fine-tuned Gorilla gets the state-of-the-art performance zero-shot over all the models"

- **limitation**: The principal accuracy metric checks whether selected API calls match the curated reference data; the paper does not establish that generated code executes correctly or behaves as intended.
  - Page 13 · citation: whitespace
  - Quote: "We de-prioritize this as we haven’t tested the execution result of the code."

- **limitation**: Retrieval is not reliably beneficial in the reported experiments: Gorilla’s BM25 results are notably below its zero-shot results on the listed datasets, so retrieval-aware training does not by itself resolve retriever quality issues.
  - Page 7 · citation: whitespace
  - Quote: "adding a non-optimal retriever at test time will sometime misguide the model and result in more errors."

- **uncertainty**: The evidence for adapting to documentation changes is illustrated with examples, but the supplied pages do not report a quantitative evaluation of adaptation across a broader set of changes.
  - Page 8 · citation: exact
  - Quote: "consider the scenario illustrated in Figure 6"

Unresolved questions:

- How often do the generated API calls execute successfully and accomplish the requested task, beyond matching the curated API references?
- How well does retrieval-aware adaptation generalize across a systematic range of documentation updates, rather than the examples shown?
- How sensitive are the reported results to the synthetic instruction data and the differences in evaluation procedures across the three hubs?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
