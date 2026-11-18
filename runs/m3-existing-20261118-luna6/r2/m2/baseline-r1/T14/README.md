# T14: RULER: What's the Real Context Size of Your Long-Context Language Models?

**baseline · ok**

1 model calls · 0 reads · 7.15 s · $0.000564

1 decisions · 0 tool calls · 24226 input tokens (24223 cached) · 643 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

RULER is a configurable synthetic benchmark intended to measure long-context language-model behavior beyond single-item needle retrieval. It combines retrieval variants, variable tracking, frequency aggregation, and QA, and uses it to evaluate models at multiple context lengths. The reported results show that strong vanilla NIAH scores can coexist with substantial drops on more complex tasks and longer inputs.

- **strength**: The benchmark broadens evaluation beyond simple retrieval and allows task difficulty and context length to be varied. The paper also describes a task-correlation analysis used to select a representative subset.
  - Page 3 · citation: whitespace
  - Quote: "RULER comprises tasks across four categories: retrieval, multi-hop tracing, aggregation, and question answering with all tasks configurable for varying length and complexity"

- **strength**: The reported evaluation supports the central point that passing vanilla retrieval tests does not establish robust performance across the benchmark: all tested models show declines as context grows, and performance varies substantially across task types.
  - Page 7 · citation: whitespace
  - Quote: "Despite achieving nearly perfect performance on the passkey retrieval and the vanilla NIAH task (shown in Appendix E), all models exhibit large degradation in RULER as sequence length increases."

- **limitation**: The benchmark's synthetic aggregation tasks are proxies rather than direct tests of natural-language summarization or broader discourse understanding, limiting how far those results alone can support claims about such capabilities.
  - Page 5 · citation: exact
  - Quote: "we introduce a new category as a proxy for summarization tasks"

- **uncertainty**: The effective-context designation depends on a chosen baseline threshold, so the resulting lengths are operational benchmark comparisons rather than a threshold-independent measure of usable context. The supplied pages do not establish how sensitive conclusions are to alternative thresholds.
  - Page 6 · citation: whitespace
  - Quote: "We use the performance of Llama2-7b model at the 4K context length as the threshold."

Unresolved questions:

- How well do scores on these synthetic tasks predict performance on naturally occurring long-context tasks, especially real summarization and multi-document reasoning?
- How sensitive are effective-context claims and model rankings to alternative baselines, thresholds, task mixes, and aggregation of task scores?
- The supplied paper pages include appendices with task configurations and additional tables, but not the full underlying generated examples or per-example outputs; how robust are the reported findings to changes in prompt wording, templates, and data generation?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
