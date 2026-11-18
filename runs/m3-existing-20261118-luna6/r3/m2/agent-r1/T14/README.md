# T14: RULER: What's the Real Context Size of Your Long-Context Language Models?

**agent · ok**

5 model calls · 4 reads · 10.27 s · $0.001566

5 decisions · 5 tool calls · 26488 input tokens (17877 cached) · 653 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

RULER broadens long-context evaluation beyond single-needle retrieval with configurable synthetic tasks spanning retrieval, multi-hop tracing, aggregation, and QA. Evaluations across ten models show that strong vanilla NIAH performance does not ensure robust performance on more complex tasks or at claimed context lengths, and the paper analyzes several failure modes. Its controlled benchmark and substantial evaluation are useful contributions, while the synthetic design limits conclusions about realistic long-document use.

- **strength**: The benchmark meaningfully expands the evaluation target beyond basic retrieval while allowing controlled variation in length and difficulty.
  - Page 2 · citation: whitespace
  - Quote: "RULER includes diverse task domains beyond retrieval, reduces reliance on parametric knowledge with synthetic input, and offers flexibility to control the contexts for different sequence lengths and task complexities."

- **strength**: The paper reports a sizeable, structured comparison, with 500 generated examples per task and context length and 13 tasks.
  - Page 6 · citation: whitespace
  - Quote: "For each task, we evaluate each model with 500 examples generated for each length from the series (4k, 8k, 16k, 32k, 64k, 128k)"

- **strength**: The evaluation supports the central finding that passing simple NIAH tests is not sufficient evidence of broader long-context capability.
  - Page 7 · citation: whitespace
  - Quote: "Despite achieving nearly perfect performance on the passkey retrieval and the vanilla NIAH task (shown in Appendix E), all models exhibit large degradation in RULER as sequence length increases."

- **limitation**: The benchmark’s entirely synthetic task design is an explicit scope boundary; its results alone do not establish performance on realistic long documents.
  - Page 2 · citation: exact
  - Quote: "Compared to existing realistic benchmarks (Table 1),RULER consists solely of synthetic tasks"

Unresolved questions:

- How well do RULER task scores predict performance on realistic long-document workloads or user tasks?
- How sensitive are the model comparisons and effective-context thresholds to alternative task mixtures, scoring choices, and baseline thresholds?
- I inspected pages 1–3 and 6–9; detailed appendices, including task-correlation analysis, full task configurations, and per-task results, remain uninspected.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Results"}` | Locate the paper’s evaluation results to assess empirical support. | 8 matches on pages [2, 6, 7, 9, 14] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect benchmark design and stated contributions for concrete support and scope. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 6, "end": 7}` | Review experimental setup and main results to evaluate evidence quality. | read pages [6, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 9}` | Inspect discussion and explicit limitations to identify caveats and unanswered scope questions. | read pages [8, 9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Evidence covers benchmark design, evaluation setup/results, and stated synthetic-task scope; submit a balanced assessment with remaining external-validity uncertainty. | review accepted | [event 25](trace.jsonl#L25) |
