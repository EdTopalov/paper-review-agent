# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**deliberative_review · ok**

7 model calls · 3 reads · 30.43 s · $0.005736

7 decisions · 4 tool calls · 35354 input tokens (1274 cached) · 2946 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

AGENTLESS presents a simple, hierarchical localization-and-repair pipeline for repository-level software issues, using sampled patches, regression-test filtering, and majority voting. It reports resolving 82 of 300 SWE-bench Lite issues and contributes a manually filtered Lite-S subset to address identified issue-quality concerns. The approach is a useful, interpretable baseline, but the inspected evidence does not establish generalization beyond these benchmarks or allow full verification of comparisons with closed-source systems.

- **strength**: The method is specified as a staged workflow that filters candidate patches and uses voting to select a submission.
  - Page 5 · citation: whitespace
  - Quote: "We filter out any patches with syntax and regression tests errors, and finally select the patch for submission using classic majority voting."

- **strength**: The paper reports a concrete SWE-bench Lite result; this is a benchmark-specific result, not evidence by itself of broader generalization.
  - Page 6 · citation: whitespace
  - Quote: "AGENTLESS is able to solve 82 out of 300 problems (27.33%)."

- **limitation**: Some comparisons are difficult to verify independently: the authors report that most closed-source baselines did not provide trajectories, and that baseline results were taken from prior reports or the leaderboard.
  - Page 6 · citation: whitespace
  - Quote: "For baseline tools, we directly use the reported results either from the official leaderboard [29] or from the tool’s official paper/repository."

- **uncertainty**: Lite-S excludes issues judged problematic, but commercial tools were not rerun on the modified set. The inspected excerpts do not establish the reliability or transferability of the filtering judgments.
  - Page 10 · citation: whitespace
  - Quote: "not able to run commercial tools ourselves on the modified problems, we simply exclude the problematic problems in the below evaluation."

Unresolved questions:

- How sensitive are solve rate and cost to the GPT-4o version, sampling budget, and implementation details?
- How reproducible are comparisons when baseline results come from separate reports and some tools cannot be rerun on Lite-S?
- Do the Lite-S filtering judgments and AGENTLESS’s performance hold on other repositories, benchmark versions, or less curated real-world issues?
- The supplied excerpts do not include the full results tables, detailed issue-classification procedure, or limitations discussion, so those aspects remain unassessed.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the method and evaluation pages to verify the two-phase localization/repair procedure and how the reported solve rate and cost were measured and compared with other agents.; Check results and analysis pages for evidence supporting the central performance claim, including benchmark splits, baselines, and any uncertainty or caveats.; Inspect the SWE-bench Lite-S construction and limitations discussion to assess the stated issue-quality concerns and whether the paper bounds the scope of its conclusions. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 3 matches on pages [2, 3, 12] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 8 matches on pages [3, 10, 11, 12] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [4, 5, 6] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The second observation says it supports a cost claim, but its quote only reports the solve rate. Either remove the cost wording or cite the paper’s cost statement with its page number. The supplied excerpts do not include the full comparative results table, so the comparative cost claim cannot be checked here. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Removed the cost claim from the observation about the solve-rate quote, as the supplied excerpts do not show comparative cost results. Retained the score and other conclusions; the available evidence does not require a score change. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "limitations"}` | Inspect the paper's stated scope and limitations to balance its benchmark claims. | 3 matches on pages [2, 3, 12] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "SWE-bench Lite-S"}` | Inspect dataset construction and evaluation evidence to assess the paper's key claims and stated scope. | 8 matches on pages [3, 10, 11, 12] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 4, "end": 6}` | Inspect method pages for localization and repair details and relevant evidence for the claimed approach. | read pages [4, 5, 6] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
