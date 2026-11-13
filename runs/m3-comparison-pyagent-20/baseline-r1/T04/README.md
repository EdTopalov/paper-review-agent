# T04: AgentBench: Evaluating LLMs as Agents

**baseline · ok**

1 model calls · 0 reads · 6.00 s · $0.004829

1 decisions · 0 tool calls · 36072 input tokens (0 cached) · 640 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AgentBench offers a practical, multi-environment benchmark for evaluating LLMs through interactive tasks rather than static prompts. Its eight environments, shared evaluation toolkit, and study of 25 models provide a useful early picture of agent capabilities, with results showing strong variation across tasks and a substantial gap between leading API models and the open models tested. The breadth is valuable, though benchmark scores depend on heterogeneous task designs and some automated evaluation procedures.

- **strength**: The benchmark’s central contribution is its broad coverage of interactive settings, including both newly constructed and adapted environments.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments, 5 of which are created in this paper for the first time"

- **strength**: The paper reports a sizeable evaluation and includes task-level results that reveal uneven model performance rather than relying only on an aggregate score.
  - Page 14 · citation: whitespace
  - Quote: "gpt-4 presents the best performance on 7 out of 8 datasets in AgentBench"

- **limitation**: The authors acknowledge that automated evaluation for lateral-thinking puzzles can be overly permissive, which limits confidence in some reported metrics for that environment.
  - Page 30 · citation: whitespace
  - Quote: "automatic evaluation sometimes more tolerate for the agent"

- **uncertainty**: The overall score uses inverse average performance across the evaluated models as task weights; how stable comparisons are to other weighting choices is left unresolved in the inspected material.
  - Page 14 · citation: whitespace
  - Quote: "we utilize the reciprocal of the average score of all the tested LLMs in each task as a weight"

Unresolved questions:

- How robust are model rankings and the headline API-versus-open-model gap to alternative overall-score weighting schemes and to variation in test samples?
- How much would the LTP results change with a more reliable host and evaluator, given the stated tendency of the automatic evaluation to be more tolerant than human evaluation?
- The paper notes that AgentBench is evolving, but the inspected results cover a particular set of models, versions, prompts, and task subsets; how well do the conclusions generalize beyond those evaluation conditions?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
