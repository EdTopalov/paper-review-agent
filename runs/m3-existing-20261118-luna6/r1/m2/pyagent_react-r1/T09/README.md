# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**pyagent_react · ok**

4 model calls · 3 reads · 13.65 s · $0.001737

4 decisions · 4 tool calls · 26387 input tokens (16866 cached) · 758 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

AGENTLESS presents a simple, hierarchical localization-and-repair pipeline for repository-level software issues and evaluates it on SWE-bench Lite. The paper’s strongest contribution is a reproducible, interpretable baseline that reports competitive resolution performance at low API cost, alongside an analysis identifying problematic benchmark instances and a filtered subset. Its evidence is useful but bounded by comparisons that include tools the authors could not rerun and by evaluation on one benchmark and one reported model configuration.

- **strength**: The paper reports competitive performance and cost for its GPT-4o setup on SWE-bench Lite, providing a concrete case for a less complex approach.
  - Page 7 · citation: exact
  - Quote: "AGENTLESS\n GPT-4o 82 (27.33%) $0.34 42,376"

- **strength**: The component analysis reports increasing solved issues as multiple samples, voting, and test filtering are added, and also quantifies the cost.
  - Page 8 · citation: exact
  - Quote: "+ test filtering\n(full AGENTLESS) 82 (27.33%) $0.34"

- **strength**: The authors systematically classify issue-description and solution information, and use the findings to motivate a filtered evaluation set.
  - Page 9 · citation: whitespace
  - Quote: "we observe that 4.3% of issues contain the exact ground truth patch in the issue description"

- **limitation**: The filtered comparison does not include fresh runs of commercial tools on the modified benchmark, limiting how directly the Lite-S comparison can be interpreted.
  - Page 10 · citation: exact
  - Quote: "as we are not able to run commercial\ntools ourselves on the modified problems"

Unresolved questions:

- How robust are the reported results to different LLMs, model versions, or sampling settings?
- How would Lite-S rankings change if commercial tools were evaluated directly on the same modified instances?
- How well does the approach generalize beyond SWE-bench Lite and the repository/task setting examined here?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the proposed localization and repair process and its evaluation setup. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 7, "end": 9}` | Inspect benchmark results, comparisons, and the construction of the filtered evaluation set. | read pages [7, 8, 9] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 10, "end": 11}` | Inspect the filtered benchmark results and any stated caveats about evaluation. | read pages [10, 11] | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Submit an evidence-based assessment using the inspected method, results, and evaluation pages. | review accepted | [event 21](trace.jsonl#L21) |
