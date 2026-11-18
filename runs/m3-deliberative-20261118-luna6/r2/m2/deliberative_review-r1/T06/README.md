# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**deliberative_review · ok**

7 model calls · 3 reads · 30.46 s · $0.003173

7 decisions · 4 tool calls · 16018 input tokens (1426 cached) · 2689 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.58

SWE-bench proposes 2,294 real-world GitHub issue-resolution tasks across 12 Python repositories, assessed by generating code changes and running tests. Its task framing extends beyond short, self-contained coding problems. The available excerpts are insufficient to thoroughly assess benchmark construction, evaluation reliability, or the reported results.

- **strength**: The benchmark frames the task as editing a repository to address an issue, aiming to assess more complex software work than standalone code generation.
  - Page 1 · citation: whitespace
  - Quote: "Given a codebase along with a description of an issue to be resolved, a language model is tasked with editing the codebase to address the issue."

- **uncertainty**: The abstract reports solve rates and an oracle-retriever condition, but the inspected material does not show the evaluation setup needed to assess those figures.
  - Page 1 · citation: exact
  - Quote: "even when provided with an oracle retriever."

- **uncertainty**: The appendix excerpt signals that construction and validation procedures are described, but it is truncated; their details and the validity of the issue-to-pull-request linkage remain unassessed.
  - Page 15 · citation: exact
  - Quote: "execution-based validation, and evaluation procedures"

Unresolved questions:

- How are issues linked to merged pull requests and tests, and what checks establish that the tests validate the intended fixes?
- What prompting, retrieval, and scoring procedures underlie the reported solve rates, and what measurement errors or limitations are discussed?
- What relevant caveats or additional evidence appear in the 44 uninspected pages?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the benchmark construction and validation sections to verify how GitHub issues, pull requests, and tests are linked, and whether the resulting tasks support the claimed real-world evaluation.; Inspect the evaluation setup and results for model prompting, retrieval conditions, scoring, and evidence behind the reported solve rates; check whether the paper discusses sources of measurement error or limitations.; Inspect the remaining pages for relevant evidence and caveats: only page 1 is currently available, so do not treat uninspected material as missing support. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 1 matches on pages [15] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 1 matches on pages [15] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | 1 matches on pages [15] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The second observation’s quotation is not verified as verbatim: the source splits “respectively” across a line with a hyphen (“re- spectively”), while the draft removes the hyphen. Replace it with a shorter exact span, such as “even when provided with an oracle retriever.”; Target: Revise the quote in the second observation to match page 1 verbatim; retain the caveat that the reported solve rates cannot be assessed from the inspected evaluation details. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Replaced the second observation’s quote with the exact observed phrase “even when provided with an oracle retriever.” The available evidence does not justify changing the score; major construction and evaluation details remain uninspected. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "dataset construction"}` | Locate benchmark construction details, validation, evaluation and limitations to assess the paper with page-specific evidence. | 1 matches on pages [15] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "dataset construction"}` | Inspect benchmark construction evidence linking issues, pull requests, and tests. | 1 matches on pages [15] | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "dataset construction"}` | Inspect how issue/PR pairs are curated and validated, addressing benchmark provenance. | 1 matches on pages [15] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.58, "observations": 3}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
