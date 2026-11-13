# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**agent · ok**

4 model calls · 2 reads · 13.98 s · $0.001377

4 decisions · 4 tool calls · 12465 input tokens (5445 cached) · 916 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

SWE-bench contributes a sizable benchmark for real repository issue resolution, framing the task as patch generation and test execution across actual Python projects. Its staged filtering and realistic codebase requirements make it useful for evaluating repository-level coding, while the inspected evidence does not establish the full strength or robustness of its model comparisons.

- **strength**: The curation pipeline requires a test to change from failing to passing after the reference change, providing an execution-based relevance filter.
  - Page 2 · citation: whitespace
  - Quote: "We filter out task instances without at least one test where its status changes from a fail to pass"

- **strength**: Success is defined by applying the proposed patch and passing the task-associated tests.
  - Page 3 · citation: whitespace
  - Quote: "If the patch applies successfully and all of these tests pass we consider the proposed solution to have successfully resolved the issue."

- **limitation**: The task design is language-bounded in the inspected description: it is centered on Python repositories.
  - Page 2 · citation: whitespace
  - Quote: "12 popular open-source Python repositories on GitHub"

- **uncertainty**: I inspected the abstract and pages 2–3, but not the full results tables or construction appendices; baseline reliability and further dataset limitations therefore remain open.
  - Page 2 · citation: whitespace
  - Quote: "We evaluate SWE-bench on multiple state-of-the-art LMs and find that they fail to solve all except the simplest issues."

Unresolved questions:

- How sensitive are the reported comparisons to prompting, sampling, and execution variability?
- How frequently do the tests accept inadequate fixes or reject valid alternative solutions?
- What sampling and filtering biases are detailed in the uninspected appendices?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper's stated scope boundaries and limitations for a balanced assessment. | 2 matches on pages [2, 9] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect benchmark construction and validation details to evaluate dataset quality and evidence. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | The observed abstract, benchmark construction, task formulation, and feature description support a preliminary assessment; submit with explicit evidence limits. | citation_validation_failed; #3: hyphenation_ambiguous (pages [9]) | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the failed citation by relying only on exact excerpts observed in the read pages; retain the stated inspection gap. | review accepted | [event 22](trace.jsonl#L22) |
