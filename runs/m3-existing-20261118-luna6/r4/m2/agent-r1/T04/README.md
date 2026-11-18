# T04: AgentBench: Evaluating LLMs as Agents

**agent · ok**

6 model calls · 5 reads · 11.18 s · $0.001966

6 decisions · 6 tool calls · 24088 input tokens (11540 cached) · 603 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

AgentBench contributes a broad interactive benchmark spanning eight text-operable environments and evaluates 25 LLMs, with released evaluation resources. Its reported results show substantial gaps between leading API models and many open models, while the paper also surfaces concrete interaction challenges. It is a valuable benchmark contribution, though the inspected evidence does not establish how robust the rankings are beyond its particular tasks and scoring setup.

- **strength**: The benchmark combines newly created and adapted environments to cover varied agent tasks, an appreciable contribution to evaluation scope.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments, 5 of which are created in this paper for the first time"

- **strength**: The reported evaluation offers broad model coverage and a striking measured disparity, while performance is notably nonuniform across environments.
  - Page 14 · citation: whitespace
  - Quote: "gpt-4 presents the best performance on 7 out of 8 datasets in AgentBench"

- **limitation**: The overall score is a constructed weighted average based on the models tested, so comparisons and future use depend on that choice of weighting.
  - Page 14 · citation: whitespace
  - Quote: "we utilize the reciprocal of the average score of all the tested LLMs in each task as a weight"

- **uncertainty**: The authors acknowledge that the benchmark is not comprehensive and is still evolving; the inspected passages do not resolve how much its current tasks represent practical agent use more broadly.
  - Page 3 · citation: exact
  - Quote: "there are definitely more scenarios and tasks to cover in LLM-as-agent evaluation."

Unresolved questions:

- How stable are model rankings to alternative overall-score choices or changes in the evaluated model pool?
- How well do these eight environments predict agent performance on practical scenarios outside the benchmark?
- The inspected passages do not provide enough detail to assess task-level sample sizes or variability of the reported results.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the authors' discussion of scope and limitations. | 1 matches on pages [2] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect benchmark design and environments to assess contribution and coverage. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "evaluation results"}` | Find empirical evidence and evaluation details for the benchmark's conclusions. | 0 matches | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "GPT-4"}` | Locate reported model results and score comparisons in the evaluation section. | 8 matches on pages [2, 3, 5, 14, 15] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 14, "end": 15}` | Read benchmark results and the authors' analysis of observed agent challenges. | read pages [14, 15] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Evidence covers benchmark scope, reported comparisons, scoring method, and identified constraints; submit a balanced paper assessment. | review accepted | [event 31](trace.jsonl#L31) |
