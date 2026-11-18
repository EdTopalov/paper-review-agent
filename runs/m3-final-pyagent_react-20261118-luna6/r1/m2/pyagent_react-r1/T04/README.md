# T04: AgentBench: Evaluating LLMs as Agents

**pyagent_react · ok**

7 model calls · 5 reads · 20.95 s · $0.004461

7 decisions · 6 tool calls · 57559 input tokens (28000 cached) · 973 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AgentBench contributes a broad, interactive benchmark for evaluating LLMs as agents across eight environments, pairing task-specific environments and success measures with evaluations of 25 models. Its practical breadth and released evaluation toolkit make it a useful research testbed. The evidence supports a substantial benchmark contribution, while the paper itself notes limited evaluation scale and imperfect automated assessment in at least one environment.

- **strength**: The benchmark brings together diverse interactive environments, including five introduced in the paper, and measures agents across varied practical capabilities.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments, 5 of which are created in this paper for the first time"

- **limitation**: The evaluation has a relatively small core Test split, though the paper also describes larger Extend sets; representativeness and resulting uncertainty remain questions rather than demonstrated defects.
  - Page 13 · citation: exact
  - Quote: "One may find the total number of problems in Dev and Test are a bit small—289 and 1,141 respectively."

- **limitation**: For lateral-thinking puzzles, the authors report that automated evaluation can be more tolerant than human evaluation, especially for open-source models, which qualifies confidence in some reported metrics.
  - Page 30 · citation: whitespace
  - Quote: "automatic evaluation sometimes more tolerate for the agent, which make SGA and QR seem better than human evaluation, especially on open-sourced models."

- **uncertainty**: Web browsing task success is described as very low, and the paper uses step success as its main metric; how well this step-level measure tracks completion of full tasks remains open.
  - Page 12 · citation: exact
  - Quote: "even the best LLMs now can only achieve single-digit task success percentages."

Unresolved questions:

- How stable are model rankings across new task samples, model versions, and prompt choices?
- How well do the benchmark’s task-specific metrics, particularly step-level web browsing scores, predict successful completion of practical end-to-end goals?
- How much do the human and automated assessments agree across environments beyond the lateral-thinking evaluation discussed here?
- I inspected the introduction, selected environment and evaluation sections, and appendix pages on lateral-thinking assessment; I did not inspect the complete results tables or all environment-specific analyses, so conclusions about detailed model rankings and per-environment evidence remain uncertain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark design, environments, and evaluation criteria. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Inspect environment construction and scoring methodology. | read pages [5, 6, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 28, "end": 30}` | Inspect aggregate results, comparisons, and reported benchmark limitations. | read pages [28, 29, 30] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 17, "end": 19}` | Review headline model results and evaluation caveats. | read pages [17, 18, 19] | [event 25](trace.jsonl#L25) |
| 6 | read_pages `{"start": 11, "end": 13}` | Inspect reported benchmark outcomes and model-level comparisons. | read pages [11, 12, 13] | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit a balanced assessment using observed benchmark design and evaluation caveats. | review accepted | [event 36](trace.jsonl#L36) |
