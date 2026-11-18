# T14: RULER: What's the Real Context Size of Your Long-Context Language Models?

**baseline · ok**

1 model calls · 0 reads · 8.18 s · $0.000543

1 decisions · 0 tool calls · 24226 input tokens (24223 cached) · 601 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

RULER broadens long-context evaluation beyond single-needle retrieval with configurable synthetic tasks for retrieval, variable tracking, aggregation, and question answering. Evaluations of 10 models across 13 task configurations show substantial performance degradation on more complex tasks and longer inputs, illustrating why claimed context length and vanilla NIAH performance alone can be misleading. The benchmark and empirical comparisons are useful, though their conclusions are bounded by synthetic task design and selected model and configuration choices.

- **strength**: The benchmark’s configurable tasks probe multiple kinds of long-context behavior, rather than treating retrieval as a sufficient measure.
  - Page 2 · citation: not_found
  - Quote: "RULER contains diverse task domains beyond retrieval"

- **strength**: The reported evaluations support the central point that strong vanilla retrieval does not imply robust performance across the broader task suite.
  - Page 7 · citation: whitespace
  - Quote: "all models exhibit large degradation in RULER as sequence length increases."

- **limitation**: The authors explicitly frame synthetic inputs as a design choice; results therefore do not by themselves establish performance on naturally occurring long-context tasks.
  - Page 2 · citation: exact
  - Quote: "RULER consists solely of synthetic tasks"

- **uncertainty**: Effective context length depends on a chosen baseline threshold, so the reported effective lengths are conditional on that operational definition.
  - Page 6 · citation: whitespace
  - Quote: "We use the performance of Llama2-7b model at the 4K context length as the threshold."

Unresolved questions:

- How well do RULER scores predict performance on realistic long-context use cases, especially tasks not represented by its synthetic constructions?
- How sensitive are model rankings and effective-length conclusions to alternative thresholds, task mixtures, and model versions?
- The supplied paper reports selected configurations and evaluations; how stable are the findings across broader task configurations and independently run replications?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
