# T04: AgentBench: Evaluating LLMs as Agents

**baseline · ok**

1 model calls · 0 reads · 8.50 s · $0.000668

1 decisions · 0 tool calls · 36072 input tokens (36069 cached) · 615 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AgentBench offers a broad benchmark and shared evaluation toolkit for testing LLMs as agents across eight interactive environments, and reports results for 25 models. Its results show strong performance by leading API models relative to the open models tested, while also exposing substantial variation across environments. The work is a useful benchmark contribution, though its conclusions depend on heterogeneous task metrics and evaluation procedures, and some measurements are acknowledged to be imperfect.

- **strength**: The benchmark’s breadth and interactive framing are a substantial contribution: it spans system operation, databases, knowledge graphs, games, puzzles, household tasks, shopping, and browsing.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments"

- **strength**: The evaluation covers a sizeable range of models and reports a clear performance separation in its tested cohort, while also showing that results vary by environment.
  - Page 14 · citation: whitespace
  - Quote: "gpt-4 presents the best performance on 7 out of 8 datasets"

- **limitation**: The overall score combines heterogeneous environment metrics using weights based on the tested models’ average scores. This makes the aggregate comparison dependent on a particular normalization and model cohort.
  - Page 14 · citation: whitespace
  - Quote: "we utilize the reciprocal of the average score of all the tested LLMs in each task as a weight"

- **uncertainty**: The paper itself notes that automatic LTP evaluation can overestimate some measures, leaving uncertainty about how well those results reflect human judgments.
  - Page 30 · citation: whitespace
  - Quote: "automatic evaluation sometimes more tolerate for the agent"

Unresolved questions:

- How sensitive are overall model rankings to alternative aggregation methods or to changing the set of models used to calculate the task weights?
- How closely do the reported LTP results, and other automatically scored tasks, correspond to human evaluation at scale?
- The inspected material does not establish how stable the reported comparisons are across repeated runs or later model versions.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
