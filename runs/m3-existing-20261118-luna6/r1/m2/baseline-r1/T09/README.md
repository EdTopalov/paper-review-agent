# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**baseline · ok**

1 model calls · 0 reads · 11.24 s · $0.002395

1 decisions · 0 tool calls · 16572 input tokens (0 cached) · 648 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AGENTLESS presents a simple, hierarchical localization-and-repair pipeline for repository-level software issues, showing that a non-agentic approach can be competitive on SWE-bench Lite at relatively low reported cost. It also manually classifies benchmark issues and proposes a filtered subset, SWE-bench Lite-S. The work offers a useful baseline and evaluation perspective, though comparisons with prior systems and the new subset have important validation limits.

- **strength**: The paper describes a clear, reproducible-in-principle pipeline and evaluates localization, patch selection, and filtering separately; its ablations indicate that sampling/voting and test filtering improve the reported solve count.
  - Page 8 · citation: whitespace
  - Quote: "We can further improve performance to 78 fixes by sampling the LLM multiple times and selecting a patch using majority voting."

- **strength**: The manual issue analysis surfaces concrete benchmark concerns, and the authors construct a filtered subset rather than relying only on the original aggregate score.
  - Page 9 · citation: whitespace
  - Quote: "we observe that 4.3% of issues contain the exact ground truth patch in the issue description"

- **limitation**: Comparisons with prior systems are not uniformly based on runs performed by the authors, limiting how directly the reported rankings establish a controlled comparison.
  - Page 6 · citation: whitespace
  - Quote: "For baseline tools, we directly use the reported results either from the official leaderboard [29] or from the tool’s official paper/repository."

- **uncertainty**: The proposed filtered benchmark is not evaluated against commercial tools by the authors, so its comparative rankings depend on available results rather than fresh evaluations on the modified set.
  - Page 10 · citation: whitespace
  - Quote: "as we are not able to run commercial tools ourselves on the modified problems"

Unresolved questions:

- How stable are AGENTLESS's solve rate and cost across repeated runs, model versions, and evaluation environments?
- Would independent annotators applying the issue-classification criteria produce similar categories and the same SWE-bench Lite-S membership?
- How would commercial and open-source systems compare if all were rerun under the same setup on SWE-bench Lite-S?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
