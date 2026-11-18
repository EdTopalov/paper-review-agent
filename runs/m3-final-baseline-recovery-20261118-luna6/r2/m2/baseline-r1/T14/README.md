# T14: RULER: What's the Real Context Size of Your Long-Context Language Models?

**baseline · ok**

1 model calls · 0 reads · 7.89 s · $0.000510

1 decisions · 0 tool calls · 24226 input tokens (24223 cached) · 535 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

RULER is a configurable synthetic benchmark intended to test long-context language models beyond simple needle retrieval, combining varied retrieval tasks with variable tracking, frequency aggregation, and QA. Its evaluation of ten models across 13 tasks and multiple sequence lengths provides evidence that strong vanilla NIAH performance does not imply robust performance on more complex long-context tasks. The benchmark and analysis are a substantial, practical contribution, though their synthetic task design and chosen scoring conventions limit how directly results generalize to naturalistic use.

- **strength**: The benchmark broadens evaluation beyond single-needle retrieval with configurable tasks that probe different behaviors.
  - Page 1 · citation: whitespace
  - Quote: "RULER introduces new task categoriesmulti-hop tracing and aggregation to test behaviors beyond searching from context."

- **strength**: The multi-model, multi-length evaluation supports the central finding that vanilla retrieval scores can overstate broader long-context capability.
  - Page 7 · citation: whitespace
  - Quote: "Despite achieving nearly perfect performance on the passkey retrieval and the vanilla NIAH task (shown in Appendix E), all models exhibit large degradation in RULER as sequence length increases."

- **limitation**: The benchmark is deliberately synthetic; this aids control but leaves open how well its task scores predict performance on natural long-context use.
  - Page 2 · citation: whitespace
  - Quote: "RULER consists solely of synthetic tasks, which offer the flexibility to control sequence length and task complexity."

- **uncertainty**: The reported effective-context threshold depends on a particular baseline and a qualitative cutoff, so the resulting lengths are not a threshold-independent property of the models.
  - Page 6 · citation: whitespace
  - Quote: "We use the performance of Llama2-7b model at the 4K context length as the threshold."

Unresolved questions:

- How well do RULER scores predict performance on naturalistic long-document tasks, especially when relevant information is not represented by synthetic patterns?
- How sensitive are effective-length conclusions and model rankings to alternative baselines, thresholds, and real-world sequence-length distributions?
- The inspected pages describe the benchmark and its experiments, but do not establish broad external validation of RULER against independently designed long-context evaluations.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
