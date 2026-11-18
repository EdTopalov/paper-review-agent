# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**deliberative_review · ok**

7 model calls · 3 reads · 29.40 s · $0.006375

7 decisions · 4 tool calls · 41121 input tokens (1243 cached) · 2776 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

InterCode provides a practical framework for evaluating interactive coding agents through code actions and execution feedback, instantiated with Bash and SQL tasks adapted from existing datasets. Its reported experiments suggest that interaction and explicit reasoning prompts can improve performance on these tasks. The contribution is substantial as a benchmark and environment-building effort, though the evaluated settings are limited and do not establish broad generalization.

- **strength**: The paper specifies an interaction loop and task-completion metric, alongside Bash and SQL reward procedures. This makes the core evaluation protocol concrete, though it does not establish that every grading choice captures task correctness.
  - Page 4 · citation: whitespace
  - Quote: "We use the Success Rate (SR) metric, defined as the proportion of task episodes where r = 1."

- **strength**: The reported comparisons find higher success rates in interactive settings for the evaluated models and tasks. The inspected results do not establish whether this advantage generalizes beyond these settings.
  - Page 6 · citation: whitespace
  - Quote: "performance across different levels of task difficulty (SQL) and different file systems (Bash) is superior in the interactive setting for all models"

- **limitation**: The authors report that the CTF demonstration has only four instances. This bounds the evidence for that extension, without by itself invalidating the framework’s broader extensibility claim.
  - Page 26 · citation: exact
  - Quote: "this demonstration currently only has four task instances."

- **limitation**: The safety discussion says Docker mitigates harmful-command risks, but cautions that direct transfer to real systems may still pose risks. This is a stated boundary on safe use, not evidence that the benchmark’s isolated execution is unsafe.
  - Page 26 · citation: whitespace
  - Quote: "a direct sim-to-real transfer of an InterCode-trained agent to a real system may put the system at risk."

Unresolved questions:

- How robust are the reported gains to different datasets, task constructions, and evaluation choices?
- How much do the reward functions’ exact-match, lexical-similarity, and output-order criteria affect measured success rates?
- How well do the environments and results scale to additional languages, larger task collections, and more varied interactive coding settings? Important gaps remain: the supplied excerpts cover only selected pages, and later sections and appendices were only partially inspected.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect benchmark construction and evaluation protocol for the Bash and SQL tasks, including whether interactive feedback and success criteria are well-defined and reproducible.; Check the reported model/prompt results and comparisons to determine whether evidence supports claims about benefits, difficulty, and benchmark viability.; Inspect later sections for limitations, safety and execution-environment details, and any additional validation; only page 1 is currently available, so do not treat uninspected material as absent. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 7 matches on pages [9, 13, 14, 26] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [3, 4, 5] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | 8 matches on pages [4, 6, 7, 8] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The page 26 observation combines the CTF dataset-size limitation with a safety claim, but its quoted sentence supports only the CTF claim. Revise to cite a quote that supports the safety statement or separate the claims with appropriate evidence. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Separated the CTF dataset-size point from the safety point and supplied a distinct observed page 26 quotation supporting the safety claim. No score change was warranted. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "limitations"}` | Locate the paper's own scope and limitation discussion before evaluating it. | 7 matches on pages [9, 13, 14, 26] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 3, "end": 5}` | Inspect core benchmark construction and evaluation evidence for Bash/SQL and model results. | read pages [3, 4, 5] | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "Success Rate"}` | Inspect empirical results and model comparisons to assess benchmark claims. | 8 matches on pages [4, 6, 7, 8] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
