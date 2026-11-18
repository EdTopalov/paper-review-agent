# T14: RULER: What's the Real Context Size of Your Long-Context Language Models?

**baseline · ok**

1 model calls · 0 reads · 7.16 s · $0.000542

1 decisions · 0 tool calls · 24226 input tokens (24223 cached) · 598 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

RULER is a configurable synthetic benchmark that extends needle retrieval with multi-item retrieval, variable tracking, aggregation, and QA, then uses it to compare long-context models across sequence lengths. Its results illustrate that strong vanilla NIAH performance does not ensure comparable performance on more complex tasks. The benchmark and broad evaluation are useful contributions, though the tasks are proxies for naturalistic abilities and some headline judgments depend on chosen scoring and threshold conventions.

- **strength**: The benchmark broadens evaluation beyond single-item retrieval with tasks that vary in type, quantity, and complexity.
  - Page 1 · citation: whitespace
  - Quote: "RULER expands upon the vanilla NIAH test to encompass variations with diverse types and quantities of needles."

- **strength**: The main comparison evaluates ten models across 13 tasks and multiple context lengths, with 500 generated examples per task and length.
  - Page 6 · citation: whitespace
  - Quote: "For each task, we evaluate each model with 500 examples generated for each length"

- **limitation**: The effective-length label relies on a specific baseline threshold, so the label is a benchmark convention rather than a threshold-independent measure.
  - Page 6 · citation: whitespace
  - Quote: "We use the performance of Llama2-7b model at the 4K context length as the threshold."

- **uncertainty**: The paper motivates synthetic tasks as proxies for broader capabilities, but the supplied pages do not establish how well success on these tasks transfers to real-world long-context use.
  - Page 5 · citation: exact
  - Quote: "a proxy for summarization tasks"

Unresolved questions:

- How robust are model rankings and effective-length conclusions to alternative baseline thresholds, task weights, and answer-scoring rules?
- To what extent do results on the synthetic tracing and aggregation tasks predict performance on natural discourse understanding and summarization?
- How representative are the evaluated models and prompt/configuration choices of current long-context deployments?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
