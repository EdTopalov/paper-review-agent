# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**agent · ok**

5 model calls · 3 reads · 12.63 s · $0.001457

5 decisions · 5 tool calls · 22318 input tokens (15822 cached) · 1005 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.79

SWE-bench makes a substantial benchmark contribution: it builds an execution-evaluated set of real GitHub issue-resolution tasks at repository scale and uses it to establish challenging initial model baselines. Its practical realism and test-based evaluation are strong, while the Python-only scope and limits of tests as a quality measure constrain what its scores establish.

- **strength**: A staged filtering pipeline turns real merged changes into benchmark tasks and requires issue linkage and a fail-to-pass test.
  - Page 2 · citation: whitespace
  - Quote: "We filter out task instances without at least one test where its status changes from a fail to pass"

- **strength**: The task formulation makes generated patches concrete and executable against tests.
  - Page 3 · citation: whitespace
  - Quote: "If the patch applies successfully and all of these tests pass we consider the proposed solution to have successfully resolved the issue."

- **strength**: Results indicate substantial difficulty even with oracle file retrieval.
  - Page 2 · citation: whitespace
  - Quote: "Claude 2 and GPT-4 only resolve 4.8% and 1.7% of tasks respec- tively; even using an oracle that retrieves the files to edit from a reference solution."

- **limitation**: The authors acknowledge Python-only coverage and that tests alone do not guarantee reliable or high-quality generations.
  - Page 9 · citation: whitespace
  - Quote: "relying solely on this method is insufficient to guarantee reliable performance of model generations"

Unresolved questions:

- How well do the instance selection and test-based success criterion represent software issues beyond the 12 selected Python repositories?
- How would results change with broader measures of patch quality, such as maintainability, readability, or human review?
- I inspected the opening, task construction/formulation, one qualitative case study, and discussion, but not the full experiment tables or appendices; detailed baseline comparisons and construction robustness therefore remain uncertain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper's explicit scope and limitations to assess benchmark validity. | 2 matches on pages [2, 9] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect benchmark construction and instance validation evidence. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 9}` | Inspect reported evaluation findings and authors' stated limitations. | read pages [8, 9] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.79, "observations": 4}}` | Evidence covers benchmark construction, task formulation, example analysis, and stated scope limitations; submit an evidence-based assessment. | citation_validation_failed; #3: hyphenation_ambiguous (pages [2]) | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.79, "observations": 4}}` | Correct the one citation rejected due to source line-break hyphenation; use exact observed wording and retain verified evidence. | review accepted | [event 25](trace.jsonl#L25) |
