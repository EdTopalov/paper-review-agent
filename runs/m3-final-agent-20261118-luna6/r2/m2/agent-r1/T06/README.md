# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**agent · ok**

5 model calls · 3 reads · 18.09 s · $0.001467

5 decisions · 5 tool calls · 22434 input tokens (15938 cached) · 1022 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SWE-bench makes a substantial benchmark contribution by turning real GitHub issues and merged fixes into repository-scale code-editing tasks with executable tests. Its filtering pipeline and realistic task formulation are clearly described, and initial model evaluations illustrate the benchmark’s difficulty. The evidence supports the benchmark’s usefulness, while the paper bounds coverage to Python and notes that passing tests alone cannot ensure solution quality.

- **strength**: The benchmark pipeline connects issue-linked pull requests with tests that demonstrably change from failing to passing, strengthening the relevance of its evaluation targets.
  - Page 2 · citation: whitespace
  - Quote: "We filter out task instances without at least one test where its status changes from a fail to pass"

- **strength**: The task formulation evaluates patches in the repository context rather than isolated code completion, with a clear execution-based success criterion.
  - Page 3 · citation: whitespace
  - Quote: "If the patch applies successfully and all of these tests pass we consider the proposed solution to have successfully resolved the issue."

- **strength**: The reported baselines provide a concrete initial demonstration that the benchmark challenges leading models under the evaluated settings.
  - Page 2 · citation: exact
  - Quote: "Claude 2 and GPT-4 only resolve 4.8% and 1.7% of tasks"

- **limitation**: The authors explicitly limit the task collection to Python and caution that test-based evaluation does not fully measure human-valued solution qualities; these are scope boundaries, not evidence that the benchmark pipeline fails.
  - Page 9 · citation: exact
  - Quote: "SWE-bench task instances are all in Python;"

Unresolved questions:

- How representative are the selected repositories and filtered issue/PR instances of software engineering work beyond the included popular Python projects?
- How sensitive are benchmark conclusions to test coverage, task selection, and evaluation cases where a valid solution differs from the reference tests?
- The inspected excerpts do not include detailed experimental protocols or appendix analyses, so comparisons among models and robustness of the reported baselines remain uncertain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper’s stated scope limits to assess benchmark validity and boundaries. | 2 matches on pages [2, 9] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect benchmark construction and task validation details supporting the contribution. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 9}` | Review reported baseline results and explicit limitations before scoring the benchmark. | read pages [8, 9] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Evidence covers the benchmark design, execution filters, evaluation, baseline claims, and stated limitations; submit an independent assessment. | citation_validation_failed; #3: hyphenation_ambiguous (pages [2]) | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Correct the ambiguous citation by using the exact separately observed model percentages without the line-wrapped phrase. | review accepted | [event 25](trace.jsonl#L25) |
