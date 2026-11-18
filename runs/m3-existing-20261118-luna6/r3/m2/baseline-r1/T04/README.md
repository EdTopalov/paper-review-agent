# T04: AgentBench: Evaluating LLMs as Agents

**baseline · ok**

1 model calls · 0 reads · 7.05 s · $0.000625

1 decisions · 0 tool calls · 36072 input tokens (36069 cached) · 529 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AgentBench assembles eight interactive environments and evaluates 25 API-based and open-source LLMs using a shared evaluation toolkit. Its breadth and operational detail make it a useful early benchmark for studying multi-turn agent behavior; results show a substantial performance gap between leading API models and the tested medium-sized open models. The supplied paper supports the benchmark’s utility, while leaving questions about score comparability and some automated evaluation components.

- **strength**: The benchmark spans varied interactive settings, and the paper reports a concrete evaluation across 25 models. It also describes data construction, interaction protocols, and metrics for individual environments.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments"

- **limitation**: The aggregate score is weighted using each task’s average score across the evaluated models. This makes the headline score dependent on the particular model set, which may complicate interpretation across future evaluations with different models.
  - Page 14 · citation: whitespace
  - Quote: "we utilize the reciprocal of the average score of all the tested LLMs in each task as a weight."

- **limitation**: The authors report that the LTP automatic evaluator can be more permissive than human evaluation for some metrics, a relevant caveat for interpreting those results.
  - Page 30 · citation: whitespace
  - Quote: "automatic evaluation sometimes more tolerate for the agent"

Unresolved questions:

- How stable are task rankings and aggregate comparisons when the model pool changes, given that aggregate weights are calculated from the evaluated models’ average task scores?
- How much do the reported LTP results change under more extensive human assessment or an improved host/evaluation model?
- The paper describes test splits as kept and evaluation across 25 models, but the supplied text does not provide per-task uncertainty estimates or repeated-run variability; how robust are the reported comparisons to sampling and stochasticity?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
