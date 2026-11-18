# T04: AgentBench: Evaluating LLMs as Agents

**baseline · ok**

1 model calls · 0 reads · 6.89 s · $0.000573

1 decisions · 0 tool calls · 36072 input tokens (36069 cached) · 424 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

AgentBench contributes a broad, interactive benchmark and evaluation toolkit for assessing LLMs across eight text-based environments, and reports results for 25 models. The breadth and practical task designs make it useful for studying agent behavior beyond static QA, while the paper’s own caveats—especially heterogeneous metrics and automated judging in lateral-thinking puzzles—temper how strongly its aggregate conclusions can be interpreted. I inspected the supplied pages, including the main evaluation and appendices; I did not independently inspect the released code or underlying datasets.

- **strength**: The benchmark covers varied environments and agent capabilities, with both newly built and adapted tasks.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments, 5 of which are created in this paper for the first time"

- **strength**: The authors evaluate a comparatively broad set of models and provide an integrated evaluation toolkit, making the work a practical resource as well as a results paper.
  - Page 3 · citation: exact
  - Quote: "We perform a thorough evaluation of 25 different LLMs using AgentBench"

- **limitation**: The aggregate score depends on inverse-average task weights derived from the evaluated model set, which complicates interpretation and comparability beyond that set.
  - Page 14 · citation: whitespace
  - Quote: "we utilize the reciprocal of the average score of all the tested LLMs in each task as a weight"

- **limitation**: The LTP paper explicitly notes that automatic evaluation can be more permissive than human evaluation, so some reported puzzle metrics may overstate performance.
  - Page 30 · citation: whitespace
  - Quote: "automatic evaluation sometimes more tolerate for the agent, which make SGA and QR seem better than human evaluation"

Unresolved questions:

- How robust are the model rankings to alternate aggregation choices, given the task-specific metrics and weighting scheme?
- How much do the LTP results and broader conclusions change under human evaluation rather than the automated judging pipeline?
- How representative are the benchmark tasks of deployment settings beyond the particular simulated environments and datasets used here?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
