# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**deliberative_review · ok**

8 model calls · 4 reads · 38.70 s · $0.011263

8 decisions · 5 tool calls · 76561 input tokens (0 cached) · 3411 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

SWE-agent introduces an agent-computer interface tailored to language models for repository-level software engineering and evaluates it on SWE-bench. The results show promising issue-resolution performance and Lite-split ablations in which interface choices correspond to substantial performance differences. The evidence is scoped to a particular benchmark, 12 Python repositories, and two large models; the headline comparison with RAG is not model-matched.

- **strength**: The paper reports automatically test-checked resolutions on both the full benchmark and its Lite subset, providing a substantial evaluation within this benchmark.
  - Page 5 · citation: exact
  - Quote: "solving 12.47% (286/2,294) of the full SWE-bench test set and 18.00% (54/300) of the Lite split."

- **strength**: Lite-split ablations report meaningful differences across interface configurations, including a shell-only editing comparison. These results support the claim that interface design matters in the tested setup.
  - Page 7 · citation: exact
  - Quote: "Without Linting, 15.0% ↓ 3.0"

- **limitation**: The headline 12.5% versus 3.8% comparison is not model-matched: 3.79% is reported for Claude 3 Opus in the RAG setting, while GPT-4 Turbo’s full-set RAG score is 1.31%. This makes the headline gap less informative as a controlled system comparison.
  - Page 6 · citation: exact
  - Quote: "w/ Claude 3 Opus 3.79 0.25 4.33 0.25"

- **uncertainty**: The observed evaluation covers 12 Python-package repositories and two models. Broader transfer is not established by the inspected evidence; this is an open question, not evidence that transfer fails.
  - Page 5 · citation: whitespace
  - Quote: "2,294 task instances from 12 different repositories of popular Python packages"

Unresolved questions:

- How robust are the ACI gains across other model families, programming languages, and repository distributions?
- How much of the full-benchmark improvement would remain in a same-model, otherwise matched comparison against RAG?
- Pages 4 and 14–25 were not inspected, and pages 2–3 were only partially observed. The supplied later-page excerpts (pages 11–13) are references; they do not resolve whether the uninspected discussion or appendices provide further limitations or evaluation details.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the methods and evaluation pages for the SWE-bench setup, comparison conditions, and evidence supporting the reported 12.5% versus 3.8% result.; Inspect the ACI experiments and analyses for evidence that interface design caused the reported performance differences, including relevant comparisons and limitations.; Review the remaining paper for scope boundaries and unresolved questions; only page 1 is currently observed, so do not treat uninspected material as absent. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [1, 2, 3, 5] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [5, 6, 7] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [8, 9, 10] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: investigate; Issues: The draft is appropriately qualified about the model-mismatched RAG comparison and the limits of the inspected evidence. However, 16 pages remain uninspected, so the paper’s stated limitations and any additional scope or evaluation details have not yet been reviewed.; Target: In the uninspected discussion and appendix pages, what explicit limitations or additional evaluation details bear on the generalizability of the reported SWE-agent results? | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | targeted_read | read pages [11, 12, 13] | [event 34](trace.jsonl#L34) · [event 39](trace.jsonl#L39) |
| 8 | revise | Draft revised; Changes: Retained the score and core assessment. Incorporated the additional supplied pages into the coverage account: pages 11–13 contain references, not further limitations or evaluation details. Clarified which pages remain uninspected and preserved uncertainty about what they may contain. | [event 40](trace.jsonl#L40) · [event 43](trace.jsonl#L43) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "SWE-bench"}` | Locate evaluation details, benchmark setup, and results relevant to the central performance claim. | 8 matches on pages [1, 2, 3, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Inspect evaluation setup, reported comparisons, and interface ablation evidence. | read pages [5, 6, 7] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 8, "end": 10}` | Inspect conclusion/limitations and evaluation evidence for open questions and scope boundaries. | read pages [8, 9, 10] | [event 22](trace.jsonl#L22) |
| 7 | read_pages `{"start": 11, "end": 13}` | Inspect appendix discussion for explicit scope limits and evaluation details. | read pages [11, 12, 13] | [event 37](trace.jsonl#L37) |
| 8 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 45](trace.jsonl#L45) |
