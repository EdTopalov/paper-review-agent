# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**pyagent_react · ok**

6 model calls · 5 reads · 15.06 s · $0.003426

6 decisions · 6 tool calls · 48459 input tokens (26821 cached) · 907 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

InterCode makes a useful, extensible benchmark contribution by framing coding as interaction with executable environments and applying that framework to Bash and SQL tasks. Its experiments provide concrete evidence that feedback and prompting strategy can affect task success, while the paper is appropriately candid about limited task coverage and safety boundaries. The contribution is substantial as a framework and initial benchmark, though broader task coverage and stronger evidence about generality remain open.

- **strength**: The paper gives the benchmark a clear interactive formulation and supports flexible evaluation beyond exact-match scoring.
  - Page 4 · citation: whitespace
  - Quote: "InterCode exposes a reward function endpoint that has access to both the interaction history and the execution container, allowing for custom reward function definitions that can incorporate multiple signals."

- **strength**: The reported experiments demonstrate that interaction can substantially improve performance on these benchmark tasks; for example, GPT-4’s SQL success rate rises from 9.1% to 73.7%.
  - Page 7 · citation: exact
  - Quote: "gpt-4 19.8 7.2 4.6 3.0 9.1 87.5 76.7 66.7 52.4 73.7"

- **limitation**: The benchmark’s implemented coverage is narrow, and the authors identify expansion as future work; this limits claims about broad language or task generality, rather than invalidating the framework.
  - Page 9 · citation: whitespace
  - Quote: "At this time, the number of InterCode based environments is limited to SQL and Bash action spaces and datasets"

- **limitation**: Docker mitigates some risks but does not itself restrict the Bash and SQL action spaces; the authors warn against direct transfer to real systems without additional guardrails.
  - Page 26 · citation: whitespace
  - Quote: "the Bash and SQL InterCode environments currently do not explicitly impose any strict limitations on the action space."

Unresolved questions:

- How well do the observed benefits transfer to additional programming languages, environments, and independently constructed task sets?
- How sensitive are benchmark scores to task selection and the custom reward definitions, including output similarity and ordering criteria?
- What safety guardrails are needed for training or deploying agents beyond the isolated benchmark containers?
- I inspected the main benchmark formulation, selected experiment results, and limitations passages, but not the full appendix or all experimental details; these questions therefore remain open rather than established defects.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the benchmark design, task formulation, and claimed contributions. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect benchmark experiments and reported comparative results. | read pages [5, 6, 7] | [event 11](trace.jsonl#L11) |
| 3 | search_paper `{"query": "limitations"}` | Locate the authors’ stated scope boundaries and limitations. | 7 matches on pages [9, 13, 14, 26] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 8, "end": 9}` | Inspect aggregate prompting results and the limitations discussion. | read pages [8, 9] | [event 21](trace.jsonl#L21) |
| 5 | read_pages `{"start": 26, "end": 26}` | Inspect explicit safety caveats and stated limits of the environments. | read pages [26] | [event 26](trace.jsonl#L26) |
| 6 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Submit an evidence-based assessment using observed design, results, and limitation passages. | review accepted | [event 32](trace.jsonl#L32) |
