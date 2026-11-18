# T04: AgentBench: Evaluating LLMs as Agents

**pyagent_react · ok**

6 model calls · 5 reads · 18.44 s · $0.002167

6 decisions · 6 tool calls · 27175 input tokens (15645 cached) · 1140 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AgentBench offers a useful, broad benchmark for interactive LLM agents, combining five newly created environments with three adapted datasets and evaluating 25 models. Its practical value is supported by explicit task setups and metrics, and its web-browsing section candidly notes constraints that affect interpretation. The inspected evidence supports a substantial benchmark contribution, while leaving questions about cross-environment comparability and robustness open.

- **strength**: The benchmark spans varied agent tasks rather than relying on a single environment, with five new settings and three adapted datasets.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments, 5 of which are created in this paper for the first time"

- **strength**: The paper describes a concrete evaluation protocol and a task-level measure for WebShop, including a 500-instruction test subset and graded rewards.
  - Page 11 · citation: exact
  - Quote: "We adopt the first 500 entries of 12,087 instructions as test set"

- **limitation**: For web browsing, the reported primary metric is step success rather than end-to-end task completion; this is a stated measurement choice, not evidence that the benchmark has no task-level metric.
  - Page 12 · citation: whitespace
  - Quote: "We report Step Success Rate as the main metric showing the independent accuracy of each action step"

- **uncertainty**: The reported Mind2Web results may depend on candidate filtering and prompting choices, so direct comparison with the original benchmark is limited by setup differences.
  - Page 12 · citation: whitespace
  - Quote: "the GPT-3.5 results can diverge from the original paper [ 19] under topk of 50 setting and different prompting strategies."

Unresolved questions:

- How stable are model rankings under alternative prompting, candidate filtering, and repeated runs?
- How should scores with different task metrics and success criteria be compared or aggregated across the eight environments?
- I inspected the abstract, introductory material, and selected evaluation pages, not the full results tables or all environment details; those portions could change the assessment of empirical support and limitations.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "8 distinct environments"}` | Locate the benchmark environment descriptions and scope. | 5 matches on pages [1, 2, 3] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect benchmark design and stated contributions. | read pages [2, 3] | [event 11](trace.jsonl#L11) |
| 3 | search_paper `{"query": "evaluation protocol"}` | Locate model-testing and scoring procedures. | 0 matches | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "success rate"}` | Find reported benchmark outcomes and evaluation measures. | 8 matches on pages [6, 7, 11, 12] | [event 21](trace.jsonl#L21) |
| 5 | read_pages `{"start": 11, "end": 12}` | Inspect evaluation caveats and web-browsing metrics. | read pages [11, 12] | [event 26](trace.jsonl#L26) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit a balanced assessment based on the benchmark scope, reported evaluation setup, and observed caveats. | review accepted | [event 32](trace.jsonl#L32) |
