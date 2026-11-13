# T18: Gorilla: Large Language Model Connected with Massive APIs

**agent · ok**

3 model calls · 2 reads · 8.18 s · $0.001441

3 decisions · 3 tool calls · 10626 input tokens (1503 cached) · 590 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Gorilla fine-tunes a LLaMA-based model for API-call generation and introduces APIBench spanning HuggingFace, TorchHub, and TensorHub APIs. Reported results show strong performance on this benchmark and explore retrieval-aware training and adaptation to documentation changes. The work is useful and empirically grounded, though conclusions are limited by the benchmark’s scope and the substantial gap between oracle and practical retrieval.

- **strength**: On the reported holdout benchmark, Gorilla’s zero-shot fine-tuned model achieves higher overall accuracy than the listed zero-shot baselines across all three API collections.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **strength**: The paper compares retrieval settings and finds oracle-retriever training can improve accuracy, while documenting the limitations of available test-time retrievers.
  - Page 7 · citation: whitespace
  - Quote: "using GPT-Index at evaluation results in 29.20% accuracy degradation, and using BM25 results in a 52.27% accuracy degradation."

- **limitation**: Evaluation is based on an instruction/API-pair holdout split from the self-instruct dataset, and the paper acknowledges incomplete API coverage affects how some systems are scored.
  - Page 6 · citation: whitespace
  - Quote: "The holdout test set was created by dividing the self-instruct dataset’s instruction, API pairs into training and testing sets."

- **uncertainty**: The pages inspected describe documentation-change adaptation through examples, but do not establish how broadly or quantitatively that capability generalizes beyond the illustrated changes.
  - Page 8 · citation: whitespace
  - Quote: "This includes alterations such as upgrading the FCN’s ResNet-50 backbone to ResNet-101, as demonstrated in the second column of the figure."

Unresolved questions:

- How well do these results transfer to APIs and documentation outside the three benchmark collections?
- What quantitative evaluation, if any, establishes robustness across a broader range of test-time documentation updates?
- I inspected the abstract and pages 6–8, not the full paper; further methods, dataset details, and limitations elsewhere may alter this assessment.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Results"}` | Find the paper’s evaluation section to inspect empirical support. | 8 matches on pages [4, 6, 7, 8] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 6, "end": 8}` | Inspect reported benchmark outcomes and evaluation caveats on pages 6–8. | read pages [6, 7, 8] | [event 10](trace.jsonl#L10) |
| 3 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | I inspected the abstract and evaluation pages 6–8; submitting a bounded assessment based on the benchmark results and stated retriever limitations. | review accepted | [event 16](trace.jsonl#L16) |
