# T04: AgentBench: Evaluating LLMs as Agents

**baseline · ok**

1 model calls · 0 reads · 8.08 s · $0.000706

1 decisions · 0 tool calls · 36072 input tokens (36069 cached) · 690 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AgentBench introduces an interactive benchmark spanning eight text-based environments and evaluates 25 API and open-source LLMs. Its breadth, executable task setups, and reported cross-environment results make it a useful contribution to evaluating LLMs as agents. The evidence supports a performance gap in this particular benchmark, while some evaluation choices and small test splits leave the generality and precision of the conclusions uncertain.

- **strength**: The benchmark’s breadth is a substantive contribution: it brings together diverse interactive tasks and reports results across 25 models.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments"

- **strength**: The paper describes concrete interaction and checking procedures, and reports a clear performance gap in its test results; this makes the central comparison inspectable, though it does not establish generalization beyond these settings.
  - Page 14 · citation: whitespace
  - Quote: "A clear performance gap exists between top commercial LLMs (e.g., gpt-4) and medium-sized open-sourced competitors."

- **limitation**: The overall score weights each environment by the reciprocal of its mean score across the evaluated models. This makes the aggregate ranking dependent on this model cohort and normalization choice, rather than only on task performance.
  - Page 14 · citation: whitespace
  - Quote: "we utilize the reciprocal of the average score of all the tested LLMs in each task as a weight."

- **uncertainty**: For lateral-thinking puzzles, the authors report that automatic evaluation can be more tolerant than human evaluation for some metrics and models. How much this affects the reported comparisons is not established in the inspected text.
  - Page 30 · citation: whitespace
  - Quote: "automatic evaluation sometimes more tolerate for the agent"

Unresolved questions:

- How robust are the model rankings and the overall score to alternative aggregation methods, especially given that the task weights are derived from the evaluated models?
- How would the findings change with larger test samples or evaluation on additional environments and models?
- How much do the lateral-puzzle evaluation discrepancies affect the benchmark’s reported results? I inspected the supplied pages, including the appendix material through page 38, but did not inspect implementation code or independently validate the evaluations.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
