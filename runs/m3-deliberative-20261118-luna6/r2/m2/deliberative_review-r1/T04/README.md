# T04: AgentBench: Evaluating LLMs as Agents

**deliberative_review · ok**

8 model calls · 4 reads · 31.79 s · $0.004019

8 decisions · 5 tool calls · 21805 input tokens (1127 cached) · 2872 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.52

AgentBench proposes an eight-environment benchmark for interactive LLM agents and reports testing 25 models. The inspected pages describe concrete task construction and success-rate scoring for OS and database tasks, as well as a knowledge-graph task design. These details support the value of the benchmark concept, but most environments and the reported comparative results were not inspected, limiting assessment of its overall validity and claims.

- **strength**: The paper frames evaluation across multiple environments and reports releasing the data and evaluation tools, making the contribution broader than a single-task test.
  - Page 1 · citation: whitespace
  - Quote: "Datasets, environments, and an integrated evaluation package for AgentBench are released at https://github.com/THUDM/AgentBench."

- **strength**: The inspected OS and database sections give operational task designs and describe executable checks and success-rate metrics; OS tasks also mix human-curated and generated instructions.
  - Page 6 · citation: whitespace
  - Quote: "In the end, we curate 144 high-quality diverse OS evaluation samples accompanied with testing interactive environments and corresponding checking pipelines (i.e., scripts)."

- **uncertainty**: The abstract reports evaluation of 25 models and a substantial commercial/open-model gap, but the supplied pages do not show the results or conditions needed to judge that comparison. Most of the PDF, including results and broader scope discussion, was not inspected.
  - Page 1 · citation: whitespace
  - Quote: "there is a significant disparity in performance between them and open-sourced competitors."

Unresolved questions:

- How are the other five environments constructed and scored, and what validation supports the benchmark as a whole?
- What comparative results and prompting, tool-access, and robustness details support the reported model disparity?
- What scope limitations and intended-use discussion appear in the uninspected sections?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the benchmark’s eight environments, task construction, scoring procedures, and any validation evidence to assess whether they support the claimed multi-dimensional evaluation.; Check the reported evaluation of 25 models, including comparative results, prompting or tool-access conditions, and robustness or reproducibility details, to see whether the central performance claims follow from the evidence.; Review the paper’s discussion of scope, limitations, and intended use elsewhere in the PDF; only page 1 is currently observed, so claims about omitted support or limitations remai … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 1 matches on pages [2] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 1 matches on pages [2] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | 0 matches | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: investigate; Issues: The draft’s score of 0.43 is not well grounded in the supplied evidence: the abstract establishes the stated benchmark scope, but nearly all evidence needed to assess research value remains uninspected.; The first observation claims a release of datasets, environments, and an evaluation package, but its quote only supports the claim that the benchmark has eight environments. The release claim is stated elsewhere on page 1 and could be quoted directly.; The paper’s construction, evaluation evidence, and scope discussion remain largely uninspected; conclusion … | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | targeted_read | read pages [5, 6, 7] | [event 34](trace.jsonl#L34) · [event 39](trace.jsonl#L39) |
| 8 | revise | Draft revised; Changes: Updated the score modestly to reflect the concrete construction and scoring details on pages 5–7 while preserving uncertainty about overall validity and comparative claims. Replaced the mismatched release quote with a direct statement supporting that claim. The critic’s concern that the evidence is incomplete is consequential and is reflected in the score and unresolved questions; no conclusion is drawn about uninspected sections. | [event 40](trace.jsonl#L40) · [event 43](trace.jsonl#L43) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "limitations"}` | Locate the paper’s scope/limitations discussion and inspect evidence beyond the abstract for benchmark construction and evaluation. | 1 matches on pages [2] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Locate the paper’s stated scope and limitations to balance evaluation claims. | 1 matches on pages [2] | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "eight environments"}` | Find benchmark environment descriptions and evaluation protocol evidence. | 0 matches | [event 22](trace.jsonl#L22) |
| 7 | read_pages `{"start": 5, "end": 7}` | Inspect environment/scoring setup and initial evaluation evidence. | read pages [5, 6, 7] | [event 37](trace.jsonl#L37) |
| 8 | submit_review `{"review": {"score": 0.52, "observations": 3}}` | Submit after the enforced critique and source validation. | review accepted | [event 45](trace.jsonl#L45) |
