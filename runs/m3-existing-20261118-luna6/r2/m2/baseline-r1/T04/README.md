# T04: AgentBench: Evaluating LLMs as Agents

**baseline · ok**

1 model calls · 0 reads · 8.35 s · $0.000613

1 decisions · 0 tool calls · 36072 input tokens (36069 cached) · 505 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AgentBench offers a broad, practical benchmark for evaluating LLMs through multi-turn interaction across eight text-based environments, and reports results for 25 models. Its main contribution is the suite, evaluation toolkit, and cross-environment comparison; the results suggest large differences between leading API models and the open models tested. The breadth is valuable, though the aggregate score and some task-specific evaluation choices complicate interpretation.

- **strength**: The benchmark spans varied interactive settings and operational skills, rather than relying on a single environment or static question-answering tasks.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments, 5 of which are created in this paper for the first time"

- **strength**: The paper documents concrete dataset construction and validation procedures for at least some environments, including human review and executable checks for OS tasks.
  - Page 6 · citation: whitespace
  - Quote: "we curate 144 high-quality diverse OS evaluation samples accompanied with testing interactive environments and corresponding checking pipelines"

- **limitation**: The overall score depends on inverse-average task weights computed from the evaluated models, so its cross-task aggregation is tied to this particular model set.
  - Page 14 · citation: whitespace
  - Quote: "we utilize the reciprocal of the average score of all the tested LLMs in each task as a weight"

- **uncertainty**: The LTP evaluation relies partly on GPT-3.5-based judging, and the authors report that automatic evaluation can overestimate some metrics; how much this affects the reported comparisons is not established in the inspected text.
  - Page 30 · citation: whitespace
  - Quote: "automatic evaluation sometimes more tolerate for the agent, which make SGA and QR seem better than human evaluation"

Unresolved questions:

- How stable are the model rankings and aggregate conclusions under alternative task weights or evaluation sets?
- How sensitive are the LTP results and model comparisons to the automated host, key-point construction, and judging procedures?
- How representative are these task environments of real-world agent use beyond the selected datasets and model versions?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
