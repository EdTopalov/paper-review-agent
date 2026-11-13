# T04: AgentBench: Evaluating LLMs as Agents

**baseline · ok**

1 model calls · 0 reads · 5.87 s · $0.004786

1 decisions · 0 tool calls · 36072 input tokens (0 cached) · 555 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AgentBench provides a broad interactive benchmark spanning eight environments and evaluates 25 language models using a shared evaluation toolkit. Its main contribution is the breadth of its tasks and the empirical comparison showing large performance differences between leading API models and the tested open-source models. The paper offers useful evidence and implementation detail, while its heterogeneous tasks and scoring choices make the overall ranking harder to interpret as a single measure of agent capability.

- **strength**: The benchmark covers varied interactive settings and reports results across a substantial set of models, supporting its value as a comparative testbed.
  - Page 3 · citation: exact
  - Quote: "We perform a thorough evaluation of 25 different LLMs using AgentBench"

- **limitation**: The aggregate score uses weights derived from the evaluated models’ average scores; this makes the overall ranking dependent on the selected model set and task mix.
  - Page 14 · citation: whitespace
  - Quote: "we utilize the reciprocal of the average score of all the tested LLMs in each task as a weight."

- **uncertainty**: The authors report that automatic judging in the lateral-thinking environment can be more permissive than human evaluation, leaving uncertainty about the reliability of some reported LTP metrics.
  - Page 30 · citation: whitespace
  - Quote: "automatic evaluation sometimes more tolerate for the agent, which make SGA and QR seem better than human evaluation"

Unresolved questions:

- How robust are the model rankings and aggregate scores to alternative task weights or changes in which models are included when calculating those weights?
- How much would LTP results change with human evaluation or a more reliable host and judge, given the stated discrepancy between automatic and human judgments?
- The supplied paper is a preprint and includes no later benchmark versions or follow-up evaluations; the assessment is limited to the supplied text and reported results.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
