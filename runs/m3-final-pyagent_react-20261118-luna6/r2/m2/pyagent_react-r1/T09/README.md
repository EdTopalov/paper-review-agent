# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**pyagent_react · ok**

6 model calls · 3 reads · 18.48 s · $0.002304

6 decisions · 5 tool calls · 41874 input tokens (31358 cached) · 1352 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AGENTLESS presents a transparent, fixed-pipeline alternative to autonomous repository-coding agents: hierarchical code localization followed by candidate patch generation, filtering, and ranking. On SWE-bench Lite it reports 82/300 resolved at an average cost of $0.34, and offers a manual benchmark audit plus a filtered 252-problem subset. The practical contribution is substantial, though comparative claims partly depend on reported results for tools the authors could not independently rerun.

- **strength**: The paper reports a concrete, competitive benchmark result and cost for its simple approach, with a stepwise repair comparison that supports the utility of sampling and test filtering.
  - Page 7 · citation: exact
  - Quote: "27.33% (82 / 300) on SWE-bench Lite."

- **strength**: The authors conduct a problem-level audit and create a filtered set, making benchmark quality part of the contribution.
  - Page 10 · citation: exact
  - Quote: "We refer to our subset of 252 problems as SWE-bench Lite-S."

- **limitation**: The comparison is not a uniform independent rerun: for commercial tools the authors could only exclude problematic instances from reported original results, limiting what the filtered comparison can establish.
  - Page 10 · citation: whitespace
  - Quote: "as we are not able to run commercial tools ourselves on the modified problems, we simply exclude the problematic problems in the below evaluation."

- **uncertainty**: The paper identifies a potential weakness of the agentless design on issues without location clues; this is a reported evaluation result and future improvement area, not a demonstrated general failure beyond that setting.
  - Page 11 · citation: whitespace
  - Quote: "the closed-source agent tools perform better compared to AGENTLESS in the case where no location clue is provided."

Unresolved questions:

- Would the relative performance and cost advantage persist under a common, independently rerun evaluation protocol for all compared tools?
- How well would the method generalize across other repositories, benchmark versions, or LLM backends?
- I inspected pages 2–4 and 6–11, not the full paper; evidence in uninspected sections, including any further limitations or implementation details, remains unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the method and benchmark evaluation details. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 6, "end": 8}` | Check benchmark results and comparison evidence. | read pages [6, 7, 8] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 9, "end": 11}` | Inspect benchmark curation findings and evaluation on the filtered set. | read pages [9, 10, 11] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit an evidence-based assessment using the inspected method, results, and benchmark-analysis pages. | citation_validation_failed; #1: not_found | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the benchmark-result citation with the exact observed wording. | review accepted | [event 30](trace.jsonl#L30) |
