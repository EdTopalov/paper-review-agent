# T14: RULER: What's the Real Context Size of Your Long-Context Language Models?

**pyagent_react · ok**

6 model calls · 4 reads · 14.47 s · $0.001925

6 decisions · 5 tool calls · 41935 input tokens (32040 cached) · 737 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

RULER broadens long-context evaluation beyond single-needle retrieval through configurable synthetic tasks covering retrieval, multi-hop variable tracking, aggregation, and QA. Its evaluations expose performance degradation and distinct failure modes across ten models, making it a useful diagnostic benchmark. The findings are bounded by synthetic task design and the selected models and configurations; appendices and later pages were not inspected.

- **strength**: The benchmark offers configurable task diversity beyond retrieval, enabling controlled tests of different long-context behaviors.
  - Page 2 · citation: whitespace
  - Quote: "RULER includes diverse task domains beyond retrieval"

- **strength**: The evaluation uses a stated multi-task protocol across lengths and examples, and reports aggregate comparative performance.
  - Page 6 · citation: whitespace
  - Quote: "For each task, we evaluate each model with 500 examples generated for each length"

- **strength**: The reported results show a substantial gap between vanilla retrieval success and broader long-context performance.
  - Page 7 · citation: whitespace
  - Quote: "all models exhibit large degradation in RULER as sequence length increases."

- **limitation**: The authors explicitly frame synthetic inputs as a design choice; how well these tasks capture real-world long-context use remains unanswered, not demonstrated as a defect.
  - Page 2 · citation: exact
  - Quote: "RULER consists solely of synthetic tasks"

Unresolved questions:

- How well do RULER scores predict performance on realistic long-document tasks and user workloads?
- How sensitive are the conclusions to the selected task configurations, scoring procedure, and model set?
- Appendices and pages beyond page 9 were not inspected, so further methodological details and qualifications may remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark task definitions and evaluation methodology. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Inspect evaluation protocol, model results, and reported limitations. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 5, "end": 7}` | Check benchmark generation, scoring, and main comparative results. | read pages [5, 6, 7] | [event 20](trace.jsonl#L20) |
| 5 | search_paper `{"query": "limitations"}` | Check whether the paper explicitly states scope limitations. | 0 matches | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Submit an evidence-based assessment from the inspected benchmark, methods, and results pages. | review accepted | [event 30](trace.jsonl#L30) |
