# T04: AgentBench: Evaluating LLMs as Agents

**agent · ok**

6 model calls · 5 reads · 12.22 s · $0.002070

6 decisions · 6 tool calls · 23500 input tokens (10140 cached) · 635 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

AgentBench contributes a practical, multi-environment benchmark for interactive LLM-agent evaluation, combining five newly created environments with three adapted ones and reporting results for 25 models. Its breadth and operationalized tasks make it useful for comparative research, while its own framing as an evolving scheme and the inspected evidence leave questions about generalizability and comparability across environments.

- **strength**: The benchmark broadens agent evaluation beyond a single task family, spanning eight environments and a range of capabilities.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments, 5 of which are created in this paper for the first time"

- **strength**: The OS tasks include executable checks and a documented human/generative construction process, supporting evaluation beyond free-form answers.
  - Page 6 · citation: whitespace
  - Quote: "we curate 144 high-quality diverse OS evaluation samples accompanied with testing interactive environments and corresponding checking pipelines"

- **strength**: The paper reports a substantial cross-model comparison and environment-specific outcomes, including GPT-4 leading on most datasets.
  - Page 14 · citation: whitespace
  - Quote: "gpt-4 presents the best performance on 7 out of 8 datasets in AgentBench"

- **limitation**: The authors explicitly present coverage as incomplete and the evaluation scheme as still evolving; this bounds claims of comprehensiveness.
  - Page 3 · citation: exact
  - Quote: "there are definitely more scenarios and tasks to cover in LLM-as-agent evaluation."

Unresolved questions:

- How robust are model rankings to prompt choices, sampling variability, and environment-specific scoring/weighting? I did not inspect the full evaluation methodology or appendices.
- How representative are the benchmark tasks of real-world agent use beyond the selected environments and curated samples?
- I inspected pages 1–6 and search excerpts from pages 14–15; I did not examine the full results, later analysis, or appendices, so additional caveats or validation may be present.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the authors’ stated scope and limitations to assess benchmark coverage and caveats. | 1 matches on pages [2] | [event 5](trace.jsonl#L5) |
| 2 | search_paper `{"query": "eight environments"}` | Find the benchmark environment descriptions and evaluation setup for assessing breadth. | 0 matches | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 2, "end": 4}` | Inspect the benchmark motivation, task taxonomy, and design details on the next pages. | read pages [2, 3, 4] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 5, "end": 6}` | Read empirical results and evaluation methodology to judge how strongly the benchmark claims are supported. | read pages [5, 6] | [event 20](trace.jsonl#L20) |
| 5 | search_paper `{"query": "GPT-4"}` | Locate aggregate experimental findings to verify evidence behind performance comparisons. | 8 matches on pages [2, 3, 5, 14, 15] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | The observed pages establish a broad benchmark design, dataset construction, and results; submit a balanced assessment while noting uninspected methodological details. | review accepted | [event 31](trace.jsonl#L31) |
