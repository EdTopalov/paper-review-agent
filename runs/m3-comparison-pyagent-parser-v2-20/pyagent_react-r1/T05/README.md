# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**pyagent_react · ok**

4 model calls · 2 reads · 13.13 s · $0.001844

4 decisions · 3 tool calls · 16211 input tokens (5091 cached) · 806 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

WebArena contributes a self-hostable, interactive web benchmark with realistic multi-site tasks, functional outcome checks, and a baseline evaluation exposing substantial challenges for language-model agents. Its strongest value is the environment and evaluation design; the inspected evidence supports the reported difficulty, while leaving questions about task representativeness and broader validation.

- **strength**: The benchmark evaluates whether tasks were achieved, rather than requiring agents to match one reference action sequence, accommodating alternative valid paths.
  - Page 2 · citation: whitespace
  - Quote: "This evaluation is not only more reliable [40, 5, 33] than comparing the vanilla action sequences [25, 7] but also accommodates a range of potential valid paths to achieve the same goal"

- **strength**: The reported task suite combines long-horizon intents with substantial headroom in the tested GPT-4 agent, and the paper analyzes concrete failure modes.
  - Page 12 · citation: whitespace
  - Quote: "the best-performing agent achieved a modest end-to-end task success rate of 10.59"

- **limitation**: The selected site categories were based on a small, author-derived sample of browsing histories, which leaves the breadth of task and user representativeness open; this is a scope concern, not evidence that the benchmark is invalid.
  - Page 3 · citation: whitespace
  - Quote: "we first conducted an analysis of approximately 200 examples from the authors’ actual web browser histories."

- **uncertainty**: The error analysis reports that the agent often prematurely judged achievable tasks impossible, but the inspected pages do not establish how this failure rate varies across agent designs or task categories.
  - Page 10 · citation: whitespace
  - Quote: "erroneously identifies approximately 54.9% of feasible tasks (428 tasks) as impossible"

Unresolved questions:

- How representative are the 812 tasks of users and web workflows beyond the authors’ browsing-history sample and the four selected domains?
- How stable are the reported results across repeated runs, alternative agent architectures, and evaluation settings?
- I inspected the opening, environment/task descriptions, selected results and analysis, and conclusion, but not the full experimental methodology, task appendix, or all reported results; those may clarify these uncertainties.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark construction and experimental methodology. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 10, "end": 12}` | Inspect evaluation results and reported benchmark limitations. | read pages [10, 11, 12] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | The inspected pages support an assessment of the benchmark contribution, task selection, and reported agent results; note remaining evidence gaps. | review accepted | [event 21](trace.jsonl#L21) |
