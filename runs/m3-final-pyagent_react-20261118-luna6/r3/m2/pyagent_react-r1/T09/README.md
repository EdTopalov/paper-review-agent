# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**pyagent_react · ok**

6 model calls · 4 reads · 14.54 s · $0.002023

6 decisions · 5 tool calls · 40679 input tokens (30077 cached) · 795 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AGENTLESS presents a simple, hierarchical localization-then-repair pipeline as a credible alternative to tool-using software engineering agents. On SWE-bench Lite, it reports 27.33% resolved at $0.34 average cost, with component analyses and a filtered 252-problem variant. The results support the approach as a useful baseline and show complementary fixes, while comparisons rely partly on prior reported results and the paper itself identifies harder cases where agentic tools may help.

- **strength**: The repair ablation shows incremental gains from candidate sampling and test filtering, and the reported cost remains low.
  - Page 8 · citation: whitespace
  - Quote: "Finally, the fullAGENTLESS performance is achieved by further applying filtering to select only the patches which can successfully pass the existing regressions tests."

- **strength**: The authors make benchmark quality a substantive part of the contribution, document issue-description problems, and evaluate on a filtered subset.
  - Page 10 · citation: exact
  - Quote: "We refer to our subset of 252 problems as SWE-bench Lite-S."

- **limitation**: Baseline comparison is not uniformly independently verified: the authors use published results, and most closed-source systems provide neither code nor trajectories.
  - Page 6 · citation: whitespace
  - Quote: "For baseline tools, we directly use the reported results either from the official leaderboard [29] or from the tool’s official paper/repository."

- **uncertainty**: The paper reports a concrete weakness for AGENTLESS on problems lacking location clues, but does not establish whether specific search tools or other changes would close that gap.
  - Page 11 · citation: whitespace
  - Quote: "the closed-source agent tools perform better compared to AGENTLESS in the case where no location clue is provided."

Unresolved questions:

- How robust are the comparisons to differences in baseline configurations and evaluation setups, given that baseline results are taken from reported sources?
- How would AGENTLESS perform on broader repository tasks beyond the filtered single-file bug-fixing subset described here?
- How repeatable are the manual issue classifications and resulting SWE-bench Lite-S exclusions? The inspected excerpts do not establish this.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the approach and benchmark evaluation details. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Check reported benchmark results, comparisons, and evaluation protocol. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 6, "end": 7}` | Inspect model configuration, baselines, and evaluation procedures. | read pages [6, 7] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 11, "end": 12}` | Inspect explicit scope caveats and discussion of the filtered benchmark. | read pages [11, 12] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit a balanced assessment based on inspected method, evaluation, and analysis pages. | review accepted | [event 30](trace.jsonl#L30) |
