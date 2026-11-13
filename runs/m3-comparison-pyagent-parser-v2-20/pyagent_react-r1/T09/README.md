# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**pyagent_react · ok**

5 model calls · 2 reads · 12.57 s · $0.002132

5 decisions · 4 tool calls · 28887 input tokens (16568 cached) · 854 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AGENTLESS presents a simple, staged localization-and-repair method for repository-level software issues and reports competitive SWE-bench Lite performance at low inference cost. Its component analyses make the method and performance tradeoffs relatively interpretable. The reported result is promising, but comparisons rely partly on previously reported baselines, and the authors’ own benchmark analysis identifies problematic issue descriptions and solutions.

- **strength**: The approach is clearly decomposed into hierarchical localization followed by patch generation, filtering, and selection, making its core procedure easy to inspect.
  - Page 5 · citation: exact
  - Quote: "AGENTLESS solves repository-level issues using a simple step-by-step procedure."

- **strength**: The paper reports strong results against its listed baselines and provides component-level evidence: sampling and voting improve fixes, with test filtering adding further gains.
  - Page 8 · citation: whitespace
  - Quote: "Finally, the fullAGENTLESS performance is achieved by further applying filtering to select only the patches which can successfully pass the existing regressions tests."

- **limitation**: The authors identify benchmark cases where descriptions are insufficient or misleading, which complicates interpreting resolution rates as a clean measure of repair ability.
  - Page 9 · citation: whitespace
  - Quote: "there is a non-trivial percentage (9.3%) of problems which do not contain enough information."

- **uncertainty**: The comparisons are not uniformly based on reproduced runs: the paper says some baseline results are taken from existing reports, and notes that many closed-source systems lack trajectories for verification.
  - Page 6 · citation: whitespace
  - Quote: "For baseline tools, we directly use the reported results either from the official leaderboard [29] or from the tool’s official paper/repository."

Unresolved questions:

- How much of the reported advantage persists under the paper’s filtered SWE-bench Lite-S evaluation and under independently reproduced, matched-cost comparisons?
- How reliable and generalizable are the manual benchmark classifications, and how do the results change across models or repositories?
- Inspection covered pages 4–9 only; later pages, including any further analysis, discussion, or stated limitations, were not inspected.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 4, "end": 6}` | Inspect the method and benchmark results supporting the central performance claims. | read pages [4, 5, 6] | [event 6](trace.jsonl#L6) |
| 2 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 7, "end": 9}` | Inspect comparative results and the paper’s analysis of benchmark validity and limitations. | read pages [7, 8, 9] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 10, "end": 11}` | Inspect how the filtered benchmark is constructed and what limitations the authors report. | reading_budget_exhausted | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit an evidence-based assessment from the inspected method and results pages, noting the remaining coverage gap. | review accepted | [event 26](trace.jsonl#L26) |
