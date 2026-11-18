# T18: Gorilla: Large Language Model Connected with Massive APIs

**baseline · ok**

1 model calls · 0 reads · 8.60 s · $0.000531

1 decisions · 0 tool calls · 17424 input tokens (17421 cached) · 712 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Gorilla fine-tunes a LLaMA-7B model on synthetic API-use examples and trains it to use retrieved API documentation. The paper introduces APIBench and reports improved API-selection accuracy and reduced hallucination on its ML API benchmark, with demonstrations of adapting to documentation changes and respecting constraints. The contribution is useful, but its evaluation primarily measures matching the intended API rather than whether generated calls execute correctly or generalize to unseen APIs.

- **strength**: The paper provides a systematic benchmark and reports strong zero-shot results for Gorilla on the listed API collections, alongside comparisons with several language models.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: The holdout split is over instruction–API pairs, not described as a split by API. Thus, the reported results do not establish generalization to APIs absent from training.
  - Page 7 · citation: wrong_page
  - Quote: "The holdout test set was created by dividing the self-instruct dataset’s instruction, API pairs into training and testing sets."

- **limitation**: The central evaluation checks API identity and selected arguments, while executing generated calls is explicitly outside the paper’s focus; functional success in actual use therefore remains unestablished.
  - Page 5 · citation: exact
  - Quote: "While we do have a system to execute these APIs, that is not a focus of this paper."

Unresolved questions:

- How well does Gorilla generalize to APIs that are wholly absent from its fine-tuning data, rather than new prompts for APIs represented during training?
- Do the benchmark accuracy and hallucination results predict successful execution across real API environments, dependencies, and changing versions? The inspected results emphasize AST matching rather than execution.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
