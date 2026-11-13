# T14: RULER: What's the Real Context Size of Your Long-Context Language Models?

**baseline · ok**

1 model calls · 0 reads · 5.33 s · $0.003308

1 decisions · 0 tool calls · 24226 input tokens (0 cached) · 560 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

RULER broadens long-context language-model evaluation beyond single-needle retrieval with configurable synthetic retrieval, variable-tracking, aggregation, and QA tasks. Its evaluation of ten models shows that near-perfect vanilla NIAH results do not guarantee performance on more varied tasks or at longer lengths. The benchmark and failure analyses offer useful tools and evidence, though the reported conclusions are bounded by the benchmark’s synthetic design and evaluation choices.

- **strength**: The benchmark’s configurable tasks cover several distinct behaviors, including multi-item retrieval, tracing, aggregation, and QA, making it a substantive extension of vanilla NIAH.
  - Page 3 · citation: whitespace
  - Quote: "RULER comprises tasks across four categories: retrieval, multi-hop tracing, aggregation, and question answering"

- **strength**: The evaluation provides a clear empirical contrast between strong vanilla retrieval scores and weaker aggregate performance across the benchmark as context grows.
  - Page 7 · citation: whitespace
  - Quote: "Despite achieving nearly perfect performance on the passkey retrieval and the vanilla NIAH task (shown in Appendix E), all models exhibit large degradation in RULER as sequence length increases."

- **limitation**: The authors explicitly frame variable tracking and aggregation as proxies, so benchmark success does not directly establish broad discourse comprehension or real-world summarization ability.
  - Page 5 · citation: exact
  - Quote: "we introduce a new category as a proxy for summarization tasks"

- **uncertainty**: The main aggregate score uses a fixed threshold derived from Llama2-7B at 4K; how conclusions about effective context length change with other baselines or application-specific quality criteria remains open.
  - Page 6 · citation: whitespace
  - Quote: "We use the performance of Llama2-7b model at the 4K context length as the threshold."

Unresolved questions:

- How well do RULER results predict model performance on naturally occurring long documents and tasks, given the benchmark’s synthetic construction and proxy tasks?
- How sensitive are model rankings and effective-length conclusions to different answer-scoring choices, threshold baselines, and realistic context-length distributions?
- Would the reported failure patterns persist under different prompt formats or without in-context examples? The inspected material describes some task-specific prompt choices and a CWE example-removal check, but does not establish robustness across prompting variants.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
