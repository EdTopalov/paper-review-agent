# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**baseline · ok**

1 model calls · 0 reads · 7.97 s · $0.000494

1 decisions · 0 tool calls · 16572 input tokens (16569 cached) · 657 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AGENTLESS presents a straightforward, non-agentic pipeline for repository-level issue repair: hierarchical code localization followed by patch generation, filtering, and voting. On SWE-bench Lite, it reports 82/300 fixes at an average cost of $0.34, and it contributes a manual problem classification and filtered 252-problem variant. The results support the value of this design on the evaluated benchmark, but comparisons rely substantially on previously reported baseline results, and the paper identifies harder cases where agent-based tools do better.

- **strength**: The paper reports competitive repair performance with a clear and relatively low-cost method, and includes ablations showing gains from sampling, voting, and test filtering.
  - Page 7 · citation: not_found
  - Quote: "AGENTLESS is able to achieve the highest performance of 27.33% (82 / 300) on SWE-bench Lite."

- **strength**: The manual benchmark analysis identifies concrete issue-description problems and yields a filtered evaluation set; the paper reports that broad rankings remain similar on it.
  - Page 10 · citation: exact
  - Quote: "We refer to our subset of 252 problems as SWE-bench Lite-S."

- **limitation**: Some comparisons are not independently verified in this study: baseline results are taken from published or leaderboard reports, and the authors note that many closed-source tools lack trajectories.
  - Page 6 · citation: whitespace
  - Quote: "For baseline tools, we directly use the reported results either from the official leaderboard [29] or from the tool’s official paper/repository."

- **uncertainty**: The reported results suggest a relative weakness on cases without location clues, but do not establish whether adding particular search capabilities would close that gap.
  - Page 11 · citation: whitespace
  - Quote: "the closed-source agent tools perform better compared to AGENTLESS in the case where no location clue is provided."

Unresolved questions:

- How robust are the reported solve rates and cost estimates to repeated runs, model-version changes, and variation in sampling?
- Would the relative performance persist under a common rerun of all baselines with matched models, evaluation settings, and cost accounting?
- Can targeted repository search improve AGENTLESS on issues without location clues while retaining its simplicity and low cost?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
