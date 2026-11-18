# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**deliberative_review · ok**

6 model calls · 3 reads · 41.33 s · $0.004928

6 decisions · 4 tool calls · 32100 input tokens (0 cached) · 1851 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

AGENTLESS presents a simple, interpretable two-phase pipeline for repository-level software issue resolution: hierarchical code localization followed by patch generation and filtering. On SWE-bench Lite, the authors report 82 of 300 issues resolved at an average cost of $0.34. Its contribution is a competitive, comparatively simple baseline and a manual analysis of benchmark issues, though the available evidence does not establish broad generality beyond this evaluation.

- **strength**: The paper gives a concrete and relatively transparent account of its localization-and-repair method, including patch filtering and selection.
  - Page 5 · citation: whitespace
  - Quote: "We filter out any patches with syntax and regression tests errors, and finally select the patch for submission using classic majority voting."

- **strength**: The reported Lite result is tied to an explicit benchmark size and evaluation setup; the authors report solving 82 of 300 issues.
  - Page 6 · citation: whitespace
  - Quote: "We observe that AGENTLESS is able to solve 82 out of 300 problems (27.33%)."

- **limitation**: The central comparison is qualified by the authors’ account that many leading systems are closed-source, limiting independent verification of their methods and trajectories.
  - Page 6 · citation: whitespace
  - Quote: "many of the top techniques are closed-source/commercial and did not release any source code to reproduce experiments or even trajectories for further verification."

- **uncertainty**: The paper reports manually identified benchmark issues and a filtered set, but the inspected excerpts do not provide enough detail to assess the classification and exclusion decisions or their effect on the comparison.
  - Page 1 · citation: whitespace
  - Quote: "we manually classified the problems in SWE-bench Lite and found problems with exact ground truth patch or insufficient/misleading issue descriptions."

Unresolved questions:

- How do the Lite-S classification and exclusion rules affect the relative performance of AGENTLESS and the compared systems?
- How robust are the results across other benchmarks, model versions, or repository-level task distributions?
- What are the detailed results and limitations discussed in the uninspected portions of the paper?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the method and results pages to verify how the localization-and-repair pipeline is implemented and whether the reported solve rate and cost are supported by the evaluation details.; Check the comparisons with other agents and the SWE-bench Lite-S analysis, including how issues were classified or excluded and whether those choices affect the central performance claims.; Inspect limitations and evaluation setup elsewhere in the paper; only page 1 is currently available, so do not treat uninspected passages as missing evidence. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 7 matches on pages [1, 3, 6, 7, 8, 10] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [4, 5, 6] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | 3 matches on pages [2, 3, 12] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: approve | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "27.33%"}` | Locate the evaluation results and supporting experimental details. | 7 matches on pages [1, 3, 6, 7, 8, 10] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 4, "end": 6}` | Inspect method and main evaluation evidence, including implementation and comparisons. | read pages [4, 5, 6] | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "limitations"}` | Inspect stated scope/limitations and nearby discussion to address evaluation caveats. | 3 matches on pages [2, 3, 12] | [event 22](trace.jsonl#L22) |
| 6 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 34](trace.jsonl#L34) |
