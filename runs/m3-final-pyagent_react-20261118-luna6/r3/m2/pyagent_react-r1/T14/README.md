# T14: RULER: What's the Real Context Size of Your Long-Context Language Models?

**pyagent_react · ok**

7 model calls · 5 reads · 18.09 s · $0.003427

7 decisions · 6 tool calls · 52539 input tokens (31158 cached) · 887 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

RULER expands long-context evaluation beyond vanilla needle retrieval with configurable synthetic retrieval, multi-hop tracking, aggregation, and QA tasks, then applies it to ten models across context lengths. Its results make a persuasive case that success on simple retrieval can overstate broader long-context capability. The benchmark is a useful contribution, while its synthetic proxies and operational definitions constrain how directly its scores generalize to real use.

- **strength**: The task suite tests several distinct behaviors beyond single-item retrieval and allows complexity and context to vary, making a more informative stress test than vanilla NIAH alone.
  - Page 3 · citation: whitespace
  - Quote: "RULER comprises tasks across four categories: retrieval, multi-hop tracing, aggregation, and question answering with all tasks configurable for varying length and complexity"

- **strength**: The evaluation uses 500 generated examples per task and length, and reports substantial performance degradation as context grows, supporting the central empirical claim across the evaluated models.
  - Page 6 · citation: whitespace
  - Quote: "For each task, we evaluate each model with 500 examples generated for each length from the series (4k, 8k, 16k, 32k, 64k, 128k)"

- **limitation**: The benchmark’s synthetic aggregation tasks are proxies for summarization rather than direct evaluations of realistic summarization, so their construct validity for that broader capability remains uncertain.
  - Page 5 · citation: exact
  - Quote: "we introduce a new category as a proxy for summarization tasks"

- **uncertainty**: The effective-length classification depends on a chosen baseline threshold; whether this threshold corresponds to satisfactory performance in practical applications is not established by the inspected evidence.
  - Page 6 · citation: whitespace
  - Quote: "We use the performance of Llama2-7b model at the 4K context length as the threshold."

Unresolved questions:

- How well do performance patterns on these synthetic tasks predict outcomes on realistic long-document workloads and applications?
- How sensitive are the effective-length conclusions to alternative thresholds, task mixes, and scoring rules?
- I inspected pages 1–9 and 16–17, but not the complete appendix, all per-task result tables, or the full prompt and scoring details; these could further qualify the reported comparisons.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark task design and evaluation methodology. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Inspect evaluation protocol and reported benchmark results. | read pages [5, 6, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 9}` | Inspect analysis conclusions and any explicit benchmark limitations. | read pages [8, 9] | [event 20](trace.jsonl#L20) |
| 5 | search_paper `{"query": "correlational study"}` | Check how benchmark task configurations were selected. | 2 matches on pages [6, 16] | [event 25](trace.jsonl#L25) |
| 6 | read_pages `{"start": 16, "end": 17}` | Inspect task-correlation evidence and appendix details. | read pages [16, 17] | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Submit evidence-based assessment after inspecting benchmark design, main results, analysis, and task-correlation appendix. | review accepted | [event 36](trace.jsonl#L36) |
