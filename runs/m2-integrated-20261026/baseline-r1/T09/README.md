# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**baseline · ok**

1 model calls · 0 reads · 6.26 s · $0.002358

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

AGENTLESS presents a deliberately non-agentic pipeline for repository-level issue resolution: hierarchical code localization, sampled diff-based repair, regression-test filtering, and majority-vote selection. On SWE-bench Lite, the authors report 82/300 issues resolved at an average cost of $0.34, and introduce a manually filtered 252-issue variant. The work offers a useful, interpretable baseline and component analysis, though broad claims about comparative performance are constrained by reliance on reported results for other systems and a single model/benchmark setup.

- **strength**: The paper gives a concrete and reproducible-in-principle pipeline, separating localization into file, code-element, and edit-location stages before repair.
  - Page 4 · citation: whitespace
  - Quote: "AGENTLESS addresses this by using a simple three-step hierarchical localization process: 1) localize to selected files; 2) localize each selected files into relevant classes, functions, and variables; 3) localize to code edit locations."

- **strength**: The component results offer evidence that sampling/voting and test filtering improve the reported solve count over a single greedy patch, while also showing associated cost.
  - Page 8 · citation: not_found
  - Quote: "Starting with just generating a single sample (i.e., using greedy decoding), AGENTLESS can achieve 70 correct fixes while costing an average of$0.11 dollars per bug"

- **limitation**: Comparisons with prior systems are not uniformly controlled: several results are taken from external reports, and the paper notes that many systems' trajectories or source code are unavailable for verification.
  - Page 6 · citation: whitespace
  - Quote: "For baseline tools, we directly use the reported results either from the official leaderboard [29] or from the tool’s official paper/repository."

- **uncertainty**: The reported comparison does not establish how well the method generalizes beyond GPT-4o and SWE-bench Lite; the supplied evaluation specifies one implementation model and benchmark subset.
  - Page 6 · citation: exact
  - Quote: "We implement AGENTLESS using GPT-4o (gpt-4o-2024-05-13) [45]."

Unresolved questions:

- How robust are AGENTLESS's performance and cost results across other LLMs, model versions, repositories, and benchmarks?
- How reproducible are the comparisons when all systems are run under the same evaluation setup, and how sensitive are results to benchmark or environment versions?
- How consistent is the manual classification used to construct SWE-bench Lite-S across independent annotators? The inspected pages describe manual classification but do not provide an agreement measure.
- Inspection was limited to the supplied text/pages; implementation details beyond the described setup and any supplementary analyses not included here were not assessed.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes the three-stage hierarchical localization process—files, code elements, then edit locations—on PDF pp. 3–4. “Reproducible-in-principle” is appropriately qualified; the paper also says it open-sourced AGENTLESS (p. 1).
- Observation 2: **supported** — Table 3 and its discussion report 70 fixes for a single greedy sample at $0.11 average cost, 78 after multiple samples and majority voting, and 82 after test filtering, at $0.34 (PDF p. 8). This supports the stated improvements and associated cost.
- Observation 3: **supported** — The paper says baseline results are taken from the official leaderboard or tools’ papers/repositories, and notes that many closed-source systems provide neither source code nor trajectories for verification (PDF pp. 6–7).
- Observation 4: **supported** — The implementation uses GPT-4o and the evaluation focuses on SWE-bench Lite (PDF p. 6). The paper reports no broader evaluation across models or benchmarks, so the stated limit on what the comparison establishes is justified.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
