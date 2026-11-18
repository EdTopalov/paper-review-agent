# T04: AgentBench: Evaluating LLMs as Agents

**baseline · ok**

1 model calls · 0 reads · 11.93 s · $0.000704

1 decisions · 0 tool calls · 36072 input tokens (36069 cached) · 686 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AgentBench introduces an interactive benchmark spanning eight text-based environments and evaluates 25 API and open-source LLMs. Its breadth, task-specific evaluation setups, and reported cross-model results make it a useful contribution to agent evaluation. The evidence is chiefly benchmark performance under the authors’ chosen prompts, test splits, and scoring procedures; the supplied paper does not establish how robust the rankings are to those choices.

- **strength**: The benchmark covers varied interaction settings and reports results for a sizable model set, supporting its contribution as a broad evaluation resource.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments"

- **strength**: The paper provides concrete comparative evidence, including per-environment scores and an overall score across 25 evaluated models.
  - Page 14 · citation: whitespace
  - Quote: "A clear performance gap exists between top commercial LLMs (e.g., gpt-4) and medium-sized open-sourced competitors."

- **limitation**: The lateral-puzzle evaluation relies partly on an automated judge, and the authors report that it can be more lenient than human evaluation, especially for open-source models.
  - Page 30 · citation: whitespace
  - Quote: "automatic evaluation sometimes more tolerate for the agent"

- **uncertainty**: The overall score weights tasks using their average scores across the evaluated models; it is unclear how stable the resulting aggregate comparisons are under alternative weights or model sets.
  - Page 14 · citation: whitespace
  - Quote: "we utilize the reciprocal of the average score of all the tested LLMs in each task as a weight."

Unresolved questions:

- How sensitive are model rankings and the headline performance gap to alternative aggregation weights, prompting choices, and interaction limits?
- How well do the benchmark results generalize beyond the specific test splits and model versions evaluated?
- What is the impact of automated evaluation and task-specific scoring choices on results, particularly for lateral-thinking puzzles?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
