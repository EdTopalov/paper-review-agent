# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**pyagent_react · ok**

5 model calls · 3 reads · 13.27 s · $0.001674

5 decisions · 4 tool calls · 28215 input tokens (19427 cached) · 764 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

InterCode contributes a reusable POMDP-style framework for interactive coding with execution feedback and implements Bash and SQL benchmarks adapted from existing datasets. Its experiments show that interaction and prompting strategy can substantially affect task success, while offering a concrete testbed for studying these behaviors. The contribution is valuable as infrastructure and benchmark design, though the evaluated environments and task coverage are limited.

- **strength**: The framework separates environment, data, and reward design, and its execution-based setup supports task-specific evaluation beyond exact code matching.
  - Page 4 · citation: whitespace
  - Quote: "InterCode exposes a reward function endpoint that has access to both the interaction history and the execution container"

- **strength**: The experiments report a substantial benefit from interaction for some models and tasks, including a large SQL gain for GPT-4.
  - Page 6 · citation: whitespace
  - Quote: "with a notable multi-fold increase for GPT-4 (9.1% → 73.7%) on the InterCode-SQL task."

- **limitation**: The authors explicitly scope the implemented benchmark to two action spaces and datasets; this limits the breadth of empirical validation, while not negating the framework's extensibility goal.
  - Page 9 · citation: whitespace
  - Quote: "At this time, the number of InterCode based environments is limited to SQL and Bash action spaces and datasets;"

- **uncertainty**: Success varies by prompting strategy and task type, so the reported gains do not establish one generally best interactive approach.
  - Page 8 · citation: whitespace
  - Quote: "tasks solved by both strategies withgpt-3.5-turbo make up 57% (407/708) and 27.6% (21/76) of the union of all successfully solved InterCode-SQL and InterCode-Bash tasks respectively."

Unresolved questions:

- How well do the framework and reported patterns generalize to additional programming languages, datasets, and interactive task types?
- How sensitive are the benchmark results to dataset grounding, reward-function choices, and task-specific evaluation criteria?
- I inspected pages 1–9 only; the remaining paper, including appendices and full methodological details, was not reviewed, so assessment of those details is incomplete.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the framework design and benchmark construction. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Inspect task implementation details and benchmark evaluation results. | read pages [5, 6, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 9}` | Check strategy comparisons and stated scope limitations. | read pages [8, 9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit an evidence-based review using the inspected framework, results, and limitations pages. | review accepted | [event 25](trace.jsonl#L25) |
