# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**deliberative_review · ok**

7 model calls · 3 reads · 30.91 s · $0.003922

7 decisions · 4 tool calls · 20405 input tokens (1426 cached) · 3091 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

SWE-bench makes a substantial benchmark contribution by turning real GitHub issues and codebases into execution-tested software-engineering tasks, with 2,294 instances across 12 Python repositories. The paper reports low resolution rates for leading models, presenting a challenging evaluation target. The inspected material supports the task design and its Python-only scope, but does not establish the detailed evaluation results or resolve possible issue–PR alignment and test-label concerns.

- **strength**: The benchmark grounds tasks in real repository issues and pull requests, and uses tests to assess proposed changes. This is a meaningful move beyond small, self-contained code-generation problems.
  - Page 1 · citation: exact
  - Quote: "across 12 popular Python repositories"

- **strength**: The construction process filters for issue-resolving PRs that modify tests, then requires a test to change from failing to passing. This provides a concrete execution-based signal, though the inspected text does not establish how often tests fully capture the issue or how alignment errors are handled.
  - Page 2 · citation: whitespace
  - Quote: "We filter out task instances without at least one test where its status changes from a fail to pass"

- **limitation**: The stated Python-only coverage is an explicit scope boundary, not evidence that the benchmark is defective. How well results generalize to other languages or software-engineering settings remains open.
  - Page 9 · citation: exact
  - Quote: "SWE-bench task instances are all in Python"

- **uncertainty**: The abstract reports low resolution rates, including results with an oracle retriever, but the inspected excerpts do not include the evaluation setup or result tables. Comparability of outcomes and the strength of the reported model conclusions therefore remain unverified here.
  - Page 1 · citation: exact
  - Quote: "even when provided with an oracle retriever"

Unresolved questions:

- How are issue–PR mismatches, incidental test changes, and cases where associated tests do not fully represent the requested behavior detected or mitigated?
- What exact execution, patch-validity, and test-outcome criteria underlie the reported resolution rates, and are model comparisons directly comparable?
- How representative are the selected popular repositories and filtered tasks of software engineering beyond the benchmark’s Python repository set?
- Important inspection gap: most pages were not available for review, including the detailed evaluation/results sections and much of the appendix. These observations are limited to the supplied excerpts.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the dataset construction and filtering sections to verify how issue–pull-request pairs and test-based labels are selected, and whether possible mismatches or leakage are addressed.; Inspect the evaluation setup and results for model, retrieval, and execution details; check whether the reported resolution rates are supported by comparable, clearly defined test outcomes.; Inspect the discussion and limitations for scope boundaries and threats to validity, including repository coverage and whether benchmark results support the paper’s broader claims about real-world software engin … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 1 matches on pages [15] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 2 matches on pages [2, 9] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | 5 matches on pages [2, 10, 18] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: Two observation quotes are not verified as verbatim by the citation check (the page 1 benchmark-size quote and the page 1 resolution-rate quote). Replace them with short exact spans visible in E1, such as “across 12 popular Python repositories” and “even when provided with an oracle retriever.” The other observations and the explicit inspection caveat are appropriately qualified.; Target: Correct the two unverified page 1 quotes, then recheck their citations against E1. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Replaced both unverified page 1 quotations with short exact spans visible in E1. The criticism about those citation mismatches is accepted; no score change is warranted. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "dataset construction"}` | Inspect methods for dataset curation and label construction, addressing the paper's central evidence and validity obligations. | 1 matches on pages [15] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "Limitations"}` | Inspect the paper's stated scope and threats to validity; then inspect dataset and evaluation evidence. | 2 matches on pages [2, 9] | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "Filtering"}` | Investigate construction and filtering evidence for issue-pull request pairing and benchmark labels. | 5 matches on pages [2, 10, 18] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
