# T04: AgentBench: Evaluating LLMs as Agents

**agent · ok**

5 model calls · 4 reads · 10.04 s · $0.001534

5 decisions · 5 tool calls · 22848 input tokens (13949 cached) · 596 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AgentBench contributes a broad, interactive benchmark spanning eight text-based environments and evaluates 25 LLMs, with a released toolkit intended to make cross-model assessment practical. Its varied tasks and reported model comparisons make it a useful early testbed for agent capabilities, while sample-size constraints, benchmark-specific scoring, and the limited inspected protocol details temper how broadly to interpret its rankings.

- **strength**: The benchmark brings together diverse interactive settings, including five newly created environments, rather than evaluating agents on a single task family.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments, 5 of which are created in this paper for the first time"

- **strength**: The reported evaluation shows a marked gap between the top API model and the tested open-source models across the benchmark's aggregate score.
  - Page 14 · citation: exact
  - Quote: "gpt-4 0613 4.41"

- **limitation**: The authors explicitly note that the standard test set contains a modest number of problems; repeated interaction turns increase evaluation effort but do not remove uncertainty from sample coverage.
  - Page 13 · citation: exact
  - Quote: "the total number of problems in Dev and Test are a bit small—289 and 1,141 respectively."

- **limitation**: The aggregate ranking depends on inverse-average task weights computed from the tested model set, so the overall score is a benchmark-specific convention rather than a task-neutral measure.
  - Page 14 · citation: whitespace
  - Quote: "we utilize the reciprocal of the average score of all the tested LLMs in each task as a weight."

Unresolved questions:

- How sensitive are aggregate rankings to alternative weighting choices or changes in the set of evaluated models?
- How representative are these task samples and simulated environments of deployment settings beyond the benchmark?
- I inspected pages 2–4 and 13–15 plus keyword-search excerpts; I did not inspect the full task-construction details, all analyses, or the paper's later discussion, so further methodological caveats may remain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Check the paper's stated scope boundaries and caveats for assessment. | 1 matches on pages [2] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark design and stated motivations beyond the abstract. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "GPT-4"}` | Locate reported evaluation results and evidence about model comparisons. | 8 matches on pages [2, 3, 5, 14, 15] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 13, "end": 15}` | Inspect results and evaluation protocol context for supporting evidence. | read pages [13, 14, 15] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence covers benchmark scope, sample counts, protocol, and comparative results; submit a balanced assessment noting inspected gaps. | review accepted | [event 25](trace.jsonl#L25) |
