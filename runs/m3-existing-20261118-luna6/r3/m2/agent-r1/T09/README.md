# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**agent · ok**

5 model calls · 4 reads · 9.48 s · $0.001661

5 decisions · 5 tool calls · 27455 input tokens (18093 cached) · 651 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

AGENTLESS presents a deliberately simple, staged localization-and-repair method for repository-level software issues and reports competitive SWE-bench Lite performance at low inference cost. Its contribution also includes a manual audit of benchmark issue quality and a filtered subset, making the paper useful both as a baseline and as a critique of evaluation practice. The evidence is meaningful but remains bounded by one benchmark and comparisons that partly rely on other systems’ reported results.

- **strength**: The paper gives a concrete and interpretable alternative to autonomous tool-using agents, with hierarchical localization followed by candidate patching and filtering.
  - Page 2 · citation: exact
  - Quote: "AGENTLESS follows a simple two phase process: localization and repair."

- **strength**: The reported evaluation supports a strong cost/performance case: 82 of 300 issues are resolved for an average $0.34, and the paper reports 71 resolved on its filtered subset.
  - Page 7 · citation: whitespace
  - Quote: "AGENTLESS  GPT-4o 82 (27.33%) $0.34 42,376 34.3% 51.0% 68.7%"

- **strength**: The manual issue audit identifies material benchmark complications and motivates a transparent filtered evaluation, rather than treating the original leaderboard as unproblematic.
  - Page 9 · citation: exact
  - Quote: "4.3% of issues contain the exact ground truth patch in the issue description"

- **limitation**: Cross-system comparisons are not uniformly reproducible in this study: the authors use results reported elsewhere for baselines, and many commercial systems lack source code or trajectories. This limits how directly the ranking can be verified.
  - Page 6 · citation: whitespace
  - Quote: "For baseline tools, we directly use the reported results either from the official leaderboard [29] or from the tool’s official paper/repository."

Unresolved questions:

- Would the performance and cost advantage persist under independent reruns with a common evaluation setup and comparable model/API settings?
- How robust is the manual classification and the resulting SWE-bench Lite-S selection to annotator disagreement or alternative criteria?
- The inspected pages cover the method overview, setup, principal results, and benchmark analysis; later discussion and conclusion details were not inspected, so additional qualifications or limitations may remain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "SWE-bench Lite-S"}` | Inspect the paper's revised benchmark results and stated rationale. | 8 matches on pages [3, 10, 11, 12] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Review method details and benchmark issue audit claims. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Check empirical results, cost comparison, and filtered benchmark methodology. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 6, "end": 7}` | Inspect evaluation setup and baselines for context on the reported performance. | read pages [6, 7] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Sufficient evidence gathered on method, results, benchmark audit, and comparison caveats. | review accepted | [event 25](trace.jsonl#L25) |
