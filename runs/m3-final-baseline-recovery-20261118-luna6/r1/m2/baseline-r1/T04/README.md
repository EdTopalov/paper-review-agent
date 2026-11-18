# T04: AgentBench: Evaluating LLMs as Agents

**baseline · ok**

1 model calls · 0 reads · 9.37 s · $0.000675

1 decisions · 0 tool calls · 36072 input tokens (36069 cached) · 629 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

AgentBench introduces an interactive benchmark spanning eight text-based environments and reports evaluations of 25 API and open-source LLMs. Its breadth, task-specific environments, and released evaluation toolkit make it a useful contribution to assessing LLMs as agents; its results also show substantial performance differences across models and tasks. The evidence is informative but should be interpreted in light of heterogeneous metrics, a constructed overall-score weighting scheme, and some evaluation components that rely on GPT-3.5-based judging.

- **strength**: The benchmark covers a notably broad range of interactive settings, with varied tasks and action spaces rather than a single agent environment.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments, 5 of which are created in this paper for the first time"

- **strength**: The paper reports a sizeable evaluation and provides a clear headline comparison, while also showing that performance varies by environment.
  - Page 14 · citation: whitespace
  - Quote: "gpt-4 presents the best performance on 7 out of 8 datasets in AgentBench"

- **limitation**: The aggregate score depends on weights derived from the evaluated models’ average scores, so interpretation and comparisons may depend on this particular normalization.
  - Page 14 · citation: whitespace
  - Quote: "we utilize the reciprocal of the average score of all the tested LLMs in each task as a weight."

- **limitation**: The authors report that the LTP automatic evaluator can be more lenient than human evaluation, a stated limitation for some reported measures.
  - Page 30 · citation: whitespace
  - Quote: "automatic evaluation sometimes more tolerate for the agent, which make SGA and QR seem better than human evaluation"

Unresolved questions:

- How sensitive are model rankings and the overall score to alternative task weights or aggregation methods?
- How much would human evaluation or a separately validated judge change the LTP results, especially for open-source models?
- The paper describes a 25-model evaluation and reports task-level results, but the inspected material does not provide uncertainty estimates; how stable are the comparisons across repeated runs or different task samples?
- Assessment is based on the supplied paper, including its appendices; no external verification of the released environments or reported results was performed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
