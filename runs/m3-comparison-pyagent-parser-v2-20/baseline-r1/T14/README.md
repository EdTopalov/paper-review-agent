# T14: RULER: What's the Real Context Size of Your Long-Context Language Models?

**baseline · ok**

1 model calls · 0 reads · 6.70 s · $0.003336

1 decisions · 0 tool calls · 24226 input tokens (0 cached) · 616 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

RULER broadens long-context evaluation beyond single-needle retrieval with configurable synthetic tasks for retrieval, variable tracking, aggregation, and QA. Evaluations across models and context lengths show substantial performance degradation on the broader task suite despite strong vanilla NIAH results. The benchmark offers a useful diagnostic framework, though its synthetic tasks and chosen effective-length threshold constrain how directly its scores generalize to real-world context use.

- **strength**: The benchmark’s configurable tasks test several distinct behaviors, and the authors report a task-correlation analysis to guide selection of representative configurations.
  - Page 16 · citation: whitespace
  - Quote: "tasks in each of the four categories (NIAH, VT, AG, QA) form cohesive clusters of their own without redundancy."

- **strength**: The reported evaluation supports the central finding that strong vanilla needle retrieval does not ensure strong performance across more varied long-context tasks.
  - Page 7 · citation: whitespace
  - Quote: "Despite achieving nearly perfect performance on the passkey retrieval and the vanilla NIAH task (shown in Appendix E), all models exhibit large degradation in RULER as sequence length increases."

- **limitation**: The benchmark’s synthetic design enables control but limits how directly results establish performance on natural long-context use; the QA component is an adaptation using distracting passages.
  - Page 5 · citation: whitespace
  - Quote: "This category is a real-world adaptation (Ivgi et al., 2023) of NIAH"

- **uncertainty**: The effective-length label depends on a particular baseline threshold, so how robust the resulting labels are to alternative thresholds remains unclear.
  - Page 6 · citation: whitespace
  - Quote: "We use the performance of Llama2-7b model at the 4K context length as the threshold."

Unresolved questions:

- How well do scores on these synthetic tasks predict performance on diverse real-world long-context applications?
- Would the model rankings and effective-length conclusions change substantially under other reasonable baseline thresholds or task weightings?
- The supplied text describes the benchmark and experiments, but I did not inspect executable benchmark code or independently verify the reported results.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
