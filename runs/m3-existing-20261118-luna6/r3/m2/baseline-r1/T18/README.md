# T18: Gorilla: Large Language Model Connected with Massive APIs

**baseline · ok**

1 model calls · 0 reads · 8.72 s · $0.000520

1 decisions · 0 tool calls · 17424 input tokens (17421 cached) · 690 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Gorilla presents a practical pipeline for API-call generation: fine-tune a LLaMA model on synthetic instruction–API pairs, optionally condition it on retrieved API documentation, and evaluate generated calls against a curated API set. The experiments show strong results in several zero-shot comparisons and illustrate adaptation to changed documentation. The evidence supports a useful contribution to API selection and call generation, but the benchmark and scoring setup constrain how broadly the findings can be interpreted.

- **strength**: The paper contributes a sizable, task-focused API dataset and a concrete training and retrieval pipeline, with reported comparisons across three API sources.
  - Page 4 · citation: whitespace
  - Quote: "For each of our 1,645 API datapoints, we sample 3 of 6 corresponding instruction examples to generate a total of 10 instruction-api pairs"

- **limitation**: The evaluation is not uniformly comparable across sources: for HuggingFace, the paper says most baselines are judged only on domain names, whereas Gorilla is evaluated differently. This limits the strength of direct model comparisons on that subset.
  - Page 7 · citation: whitespace
  - Quote: "for all the models except Gorilla, we only check if they can provide the correct domain names."

- **limitation**: The reported correctness measure is based on matching selected API-call syntax and arguments, not demonstrating that generated calls execute successfully or accomplish the requested task.
  - Page 13 · citation: whitespace
  - Quote: "We de-prioritize this as we haven’t tested the execution result of the code."

- **uncertainty**: The paper’s examples show documentation adaptation, but the supplied evaluation does not establish how reliably it generalizes to broader or independently sampled API changes. The reported results also show that retrieval quality matters substantially.
  - Page 5 · citation: wrong_page
  - Quote: "adding a non-optimal retriever at test time will sometime misguide the model and result in more errors."

Unresolved questions:

- How well would the method perform on APIs outside the three ML-focused sources and on documentation or requests not represented by the synthetic instruction data?
- Would the conclusions hold under execution-based or task-outcome evaluation, rather than AST matching and selected-argument checks?
- How robust is documentation-change adaptation across a larger, systematically evaluated set of API updates and retrieval errors?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
