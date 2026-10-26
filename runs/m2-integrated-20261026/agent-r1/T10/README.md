# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**agent · ok**

5 model calls · 4 reads · 11.56 s · $0.001975

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

SWE-agent makes a substantial, practically relevant contribution by treating the agent-computer interface as a design variable for repository-level software engineering. Its custom search, editing, feedback, and context-management tools are evaluated on SWE-bench and supported by interface ablations, showing notable gains over the tested shell-only and retrieval baselines. The evidence is meaningful but bounded to two leading closed models and the benchmark/setup described; the paper also reports persistent inefficient agent behavior.

- **strength**: The paper articulates a coherent ACI design methodology, emphasizing simplicity, efficient actions, informative feedback, and guardrails.
  - Page 3 · citation: exact
  - Quote: "Environment feedback should be informative."

- **strength**: The reported benchmark results show a clear improvement over the tested baselines, with interface ablations supporting the claim that design choices matter.
  - Page 6 · citation: exact
  - Quote: "w/ GPT-4 Turbo 12.47 1.59 18.00 1.67"

- **limitation**: The main reported results are restricted to two leading models; transfer of the ACI findings to other models is not established by the evaluated results described here.
  - Page 5 · citation: exact
  - Quote: "All results, ablations, and analysis are based on two leading LMs"

- **limitation**: The behavioral analysis identifies a potentially important persistence failure: agents often continue a routine without recognizing dead ends or changing approach.
  - Page 8 · citation: whitespace
  - Quote: "agents rarely deviate from this pattern but they rarely recognize dead ends or reset their problem solving approach."

Unresolved questions:

- How well do the ACI principles and performance gains transfer to other model families, open models, or substantially different software engineering tasks?
- Which individual ACI components contribute most reliably across repositories and tasks, beyond the reported Lite ablations?
- Inspection covered pages 1–9, including the main design, results, and discussion, but not pages 10–25 (including appendices); implementation details and any further caveats or analyses there remain unassessed.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — Page 3 explicitly lays out the four principles—simple actions, efficient actions, informative feedback, and guardrails—and relates them to the interface design and ablations.
- Observation 2: **supported** — Pages 5–7 report SWE-agent results against the tested baselines and Lite ablations; for example, page 6 shows 18.0% resolved versus 11.0% for the shell-only agent on SWE-bench Lite, with several ablations performing worse than the full interface.
- Observation 3: **supported** — Page 5 says the results, ablations, and analysis use two models. The paper does report results with both GPT-4 Turbo and Claude 3 Opus (pages 2 and 6), but does not establish transfer to additional model families.
- Observation 4: **supported** — Page 8 reports from manual inspection that agents rarely deviate from the repeated edit-and-test pattern and rarely recognize dead ends or reset their approach.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper’s stated scope boundaries or limitations for a balanced assessment. | 4 matches on pages [3, 9, 10] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 5}` | Inspect core ACI design and benchmark methodology/results to assess novelty and support. | read pages [3, 4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 6, "end": 7}` | Review quantitative comparisons and ablation evidence, including experimental outcomes. | read pages [6, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 9}` | Inspect conclusion and discussion for declared implications or scope caveats. | read pages [8, 9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Evidence covers the contribution, benchmark results, interface ablations, and reported agent behavior; submit a balanced review while noting evaluation scope. | review accepted | [event 25](trace.jsonl#L25) |
