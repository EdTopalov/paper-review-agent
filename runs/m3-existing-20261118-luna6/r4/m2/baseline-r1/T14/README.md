# T14: RULER: What's the Real Context Size of Your Long-Context Language Models?

**baseline · ok**

1 model calls · 0 reads · 8.66 s · $0.000549

1 decisions · 0 tool calls · 24226 input tokens (24223 cached) · 613 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

RULER is a configurable synthetic benchmark intended to measure long-context language-model behavior beyond single-needle retrieval. It combines retrieval variants, variable tracking, word-frequency aggregation, and question answering with distractor documents, then evaluates 10 models across context lengths. Results show that strong vanilla NIAH performance does not reliably predict performance on more demanding tasks, and reveal substantial degradation with longer inputs and greater task complexity.

- **strength**: The benchmark tests several distinct behaviors and allows context length and task complexity to vary, supporting the paper’s central case that a single retrieval test is too narrow.
  - Page 2 · citation: not_found
  - Quote: "RULER contains diverse task domains beyond retrieval"

- **strength**: The evaluation includes a substantial and clearly described sweep: 13 tasks, 500 generated examples per task and length, and multiple context lengths. The reported results provide concrete evidence of failures beyond vanilla retrieval.
  - Page 6 · citation: whitespace
  - Quote: "For each task, we evaluate each model with 500 examples generated for each length from the series (4k, 8k, 16k, 32k, 64k, 128k)"

- **limitation**: The benchmark’s broad framing of long-context understanding relies partly on deliberately narrow synthetic proxies, such as word counting and variable assignment; success or failure on these tasks does not by itself establish performance on natural long-document reasoning or summarization.
  - Page 5 · citation: exact
  - Quote: "we introduce a new category as a proxy for summarization tasks"

- **limitation**: The headline notion of effective context length depends on a chosen baseline threshold, so the resulting cutoff is a benchmark convention rather than a threshold independently established as satisfactory for users or applications.
  - Page 6 · citation: whitespace
  - Quote: "We use the performance of Llama2-7b model at the 4K context length as the threshold."

Unresolved questions:

- How well do RULER scores and its synthetic task behaviors predict performance on realistic long-document tasks and user workloads?
- How sensitive are model rankings and effective-length conclusions to the selected task mix, the baseline threshold, and the recall-based scoring procedure?
- The supplied paper includes task-correlation analysis and selected configurations, but how stable are these choices across a broader set of models and alternative task designs?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
