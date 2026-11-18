# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**deliberative_review · ok**

7 model calls · 3 reads · 37.57 s · $0.005252

7 decisions · 4 tool calls · 29504 input tokens (1426 cached) · 3476 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

SWE-bench contributes an execution-based benchmark of repository-scale software engineering tasks, linking real GitHub issues to code changes and tests. The supplied excerpts support its task formulation and filtering approach, and the abstract reports low model success rates. Most of the paper—including detailed results and much of the appendix—was not inspected, so the evaluation evidence and the benchmark’s full validation cannot be assessed here.

- **strength**: The benchmark frames the task as resolving an issue with a patch that passes related tests.
  - Page 2 · citation: exact
  - Quote: "The task is to generate a pull request that addresses a given issue and passes tests related to the issue."

- **strength**: The stated evaluation applies the patch and treats passing the associated tests as success.
  - Page 3 · citation: whitespace
  - Quote: "If the patch applies successfully and all of these tests pass we consider the proposed solution to have successfully resolved the issue."

- **limitation**: The authors identify Python-only coverage as a scope boundary; generalization to other languages remains an open question in the inspected material.
  - Page 9 · citation: exact
  - Quote: "SWE-bench task instances are all in Python"

- **uncertainty**: The abstract says evaluation of existing benchmarks has become saturated, but the supplied excerpts do not establish how broadly that claim is supported.
  - Page 1 · citation: exact
  - Quote: "existing benchmarks have become saturated"

Unresolved questions:

- How are evaluation instances split, and what evidence addresses possible contamination or representativeness?
- What detailed configurations, baselines, and results support the reported model success rates?
- How robust are the tests as measures of issue resolution, and how does performance vary across repositories or task types?
- Only pages 1–4 and partial pages 9 and 15 were inspected; most of the paper, including the full discussion and results, remains unreviewed.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the benchmark construction and dataset sections to verify how the 2,294 issue–pull-request instances are selected, linked to tests, and split, including any stated representativeness or leakage limitations.; Inspect the evaluation setup and results pages to check whether the reported model success rates follow from the tested configurations, baselines, and patch-verification procedure.; Inspect the paper’s limitations and discussion, and gather exact page-numbered quotations supporting 2–4 observations; note that only page 1 is currently available and most of the paper remains  … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 1 matches on pages [15] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 2 matches on pages [2, 9] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [2, 3, 4] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The page 2 quotation does not match the supplied text verbatim: the source breaks “instances” as “in-\nstancess” (printed as “in-\nstaces” in the excerpt), so replace it with a verified contiguous quote. The page 1 quotation also fails the citation check; use a shorter exact span or remove it.; The first observation’s quote supports the filtering count, but not all of its claim about issue-linked changes and tests. Narrow the claim or cite a quote that supports it.; The draft appropriately flags the limited inspection, but the evaluation-rate observation should  … | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Replaced the citation-failing quotations with exact observed spans and narrowed claims to what each quotation supports. Kept the evaluation evidence explicitly qualified; the supplied excerpts do not permit verification of detailed results. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "dataset construction"}` | Investigate benchmark construction and seek specific, page-citable evidence beyond the supplied first page. | 1 matches on pages [15] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Inspect the paper’s discussion of scope and limitations before assessing benchmark claims. | 2 matches on pages [2, 9] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark construction, dataset selection and linkage evidence. | read pages [2, 3, 4] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
