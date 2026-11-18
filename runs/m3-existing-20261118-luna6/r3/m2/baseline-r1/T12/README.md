# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**baseline · ok**

1 model calls · 0 reads · 5.66 s · $0.000530

1 decisions · 0 tool calls · 26994 input tokens (26991 cached) · 520 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

InterCode presents a reusable framework and benchmark for interactive code generation, modeling code as actions and execution results as observations. Its Bash and SQL environments adapt existing datasets, and baseline experiments show that interaction and reasoning-oriented prompts can improve task success, while also exposing persistent difficulties in using feedback. The work is a useful benchmark contribution with concrete implementation and empirical evidence, though the evaluation covers only two environments and leaves important questions about generality and measurement open.

- **strength**: The framework makes interactive coding tasks modular and extensible, with Docker-based execution and customizable reward design.
  - Page 4 · citation: whitespace
  - Quote: "InterCode decomposes the construction of an interactive coding task into three modular parts: (1) environment construction, (2) data collection, and (3) reward design."

- **strength**: The experiments provide evidence that interaction can improve success over single-turn generation, including a large SQL gain for GPT-4.
  - Page 6 · citation: whitespace
  - Quote: "with a notable multi-fold increase for GPT-4 (9.1% → 73.7%) on the InterCode-SQL task."

- **limitation**: The authors identify a narrow current range of implemented environments, limiting the demonstrated breadth of the framework.
  - Page 9 · citation: whitespace
  - Quote: "At this time, the number of InterCode based environments is limited to SQL and Bash action spaces and datasets"

- **uncertainty**: The reported gains do not by themselves establish that the benchmark or interaction benefits generalize beyond the selected tasks, models, and prompts; broader evaluation remains an open question.
  - Page 26 · citation: whitespace
  - Quote: "The InterCode codebase currently features two tasks with Bash and SQL programming languages as action spaces."

Unresolved questions:

- How well do the framework and interaction-related findings transfer to additional programming languages, execution environments, and task families?
- How sensitive are benchmark success rates to reward-function choices, especially Bash lexical-output similarity and SQL ordering requirements?
- Would comparisons across a broader range of models, prompt designs, and independently curated tasks support the same conclusions about the benefits of interaction?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
