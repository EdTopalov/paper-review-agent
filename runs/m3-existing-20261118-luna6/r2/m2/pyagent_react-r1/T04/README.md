# T04: AgentBench: Evaluating LLMs as Agents

**pyagent_react · ok**

7 model calls · 5 reads · 18.88 s · $0.004581

7 decisions · 6 tool calls · 58724 input tokens (28716 cached) · 1086 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AgentBench contributes a broad, interactive benchmark spanning eight environments and evaluates 25 API and open-source LLMs with a shared toolkit. The benchmark’s breadth and concrete execution-based tasks make it useful for studying agent behavior; its results document large performance differences across models and tasks. The evidence supports a substantial benchmark contribution, while the paper itself recognizes that the suite is evolving and has coverage limits.

- **strength**: The benchmark combines diverse interactive environments, including five introduced in the paper, rather than focusing on a single agent setting.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments, 5 of which are created in this paper for the first time"

- **strength**: The authors report evaluation of 25 models and publish per-environment results; the reported scores show substantial variation across model types and tasks.
  - Page 14 · citation: whitespace
  - Quote: "A clear performance gap exists between top commercial LLMs (e.g., gpt-4) and medium-sized open-sourced competitors."

- **limitation**: The authors state the standard test split is small in item count, though interactions make evaluation expensive. This is a scope constraint, not by itself evidence that the reported results are invalid.
  - Page 13 · citation: exact
  - Quote: "One may find the total number of problems in Dev and Test are a bit small—289 and 1,141 respectively."

- **uncertainty**: The overall score uses task weights derived from average performance across the evaluated models; whether this weighting produces stable comparisons with different model cohorts remains unresolved in the inspected text.
  - Page 14 · citation: whitespace
  - Quote: "we utilize the reciprocal of the average score of all the tested LLMs in each task as a weight."

Unresolved questions:

- How robust are model rankings to changes in task weights, model cohorts, and evaluation prompts?
- How representative are the benchmark tasks of deployment settings beyond the selected environments and model sizes?
- I inspected pages 1–7 and 12–16, not the intervening environment descriptions, appendices, or all implementation details; those could qualify the assessment of task construction and reproducibility.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark design and claimed contributions. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Inspect evaluation protocol and reported benchmark outcomes. | read pages [5, 6, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 18, "end": 20}` | Inspect aggregate results and discussion of benchmark limitations. | read pages [18, 19, 20] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 12, "end": 14}` | Inspect main quantitative results and evaluation interpretation. | read pages [12, 13, 14] | [event 25](trace.jsonl#L25) |
| 6 | read_pages `{"start": 15, "end": 16}` | Inspect authors’ interpretation and stated scope limitations. | read pages [15, 16] | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit a balanced assessment grounded in inspected methods, results, and discussion pages. | review accepted | [event 36](trace.jsonl#L36) |
