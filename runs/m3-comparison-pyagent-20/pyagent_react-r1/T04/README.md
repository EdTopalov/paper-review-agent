# T04: AgentBench: Evaluating LLMs as Agents

**pyagent_react · ok**

5 model calls · 2 reads · 23.72 s · $0.002683

5 decisions · 5 tool calls · 31940 input tokens (19441 cached) · 1854 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.7

AgentBench introduces an interactive, multi-environment benchmark and evaluation toolkit for assessing LLMs as agents, and reports results for 25 models across eight environments. Its practical task variety and model comparisons are useful contributions; evidence is bounded by relatively small standard test sets and a particular prompting and scoring setup. I inspected only the abstract and pages 3–5 and 12–14, so this review may miss relevant detail elsewhere in the paper.

- **strength**: The reported model comparison is intended to inform future research directions in LLM-as-agent capabilities.
  - Page 3 · citation: whitespace
  - Quote: "It illuminates the state of the art in LLM-as-Agent and highlights areas for improvement."

- **strength**: The paper reports a broad model comparison and task-level scores; on the reported standard test, GPT-4 leads on seven of eight environments.
  - Page 14 · citation: whitespace
  - Quote: "gpt-4 presents the best performance on 7 out of 8 datasets in AgentBench"

- **limitation**: The authors acknowledge that the standard development and test splits are small in sample count. Multi-turn interaction increases evaluation effort, but the size still leaves uncertainty about score stability across task samples.
  - Page 13 · citation: exact
  - Quote: "One may find the total number of problems in Dev and Test are a bit small—289 and 1,141 respectively."

- **uncertainty**: The results reflect the specified benchmark setup, including CoT prompting and environment-specific metrics. The inspected pages do not establish whether rankings persist under alternative prompting, agent strategies, or benchmark distributions.
  - Page 5 · citation: whitespace
  - Quote: "we evaluate LLMs with the most primitive CoT in AgentBench"

Unresolved questions:

- How stable are the reported rankings and aggregate scores across repeated runs or larger and differently sampled test sets?
- Would the model comparisons change substantially under alternative prompting or agent strategies, rather than the stated primitive CoT setup?
- Detailed environment construction, results beyond the inspected table, and later discussion of limitations were not inspected.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 3, "end": 5}` | Inspect the benchmark environments and evaluation design. | read pages [3, 4, 5] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 12, "end": 14}` | Inspect reported benchmark results and evaluation caveats. | read pages [12, 13, 14] | [event 11](trace.jsonl#L11) |
| 3 | submit_review `{"review": {"score": 0.7, "observations": 4}}` | Submit an assessment based on the abstract and inspected benchmark-design and results pages, while noting the limited page coverage. | citation_validation_failed; #1: hyphenation_ambiguous (pages [3]) | [event 17](trace.jsonl#L17) |
| 4 | submit_review `{"review": {"score": 0.7, "observations": 4}}` | Correct the page 3 citation using an exact observed sentence and retain validated evidence for the other observations. | citation_validation_failed; #1: not_found | [event 23](trace.jsonl#L23) |
| 5 | submit_review `{"review": {"score": 0.7, "observations": 4}}` | Replace the invalid citation with an exact, observed quote from page 3. | review accepted | [event 29](trace.jsonl#L29) |
