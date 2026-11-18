# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**pyagent_react · ok**

3 model calls · 2 reads · 21.70 s · $0.001446

3 decisions · 3 tool calls · 10362 input tokens (6588 cached) · 1817 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

SWE-bench contributes a substantial repository-level software engineering benchmark built from real GitHub issues and associated pull requests, with execution-based filtering and tests to evaluate generated patches. The inspected material supports a clear, practical task formulation and reports meaningful scale and task characteristics. The assessment remains provisional because later experimental results and appendices were not inspected.

- **strength**: The construction pipeline filters candidate tasks using issue links, test changes, and observed fail-to-pass tests, rather than relying solely on issue/PR association.
  - Page 2 · citation: whitespace
  - Quote: "We filter out task instances without at least one test where its status changes from a fail to pass"

- **strength**: The evaluation checks both issue-related tests and the broader repository test suite, while allowing patches that differ from the reference solution.
  - Page 3 · citation: whitespace
  - Quote: "If the patch applies successfully and all of these tests pass we consider the proposed solution to have successfully resolved the issue."

- **limitation**: The task collection is explicitly selective: it focuses on popular Python repositories, and filtering requires PRs that modify test files and pass installation/runtime checks. This defines a useful scope, but does not establish representativeness of all software engineering work.
  - Page 2 · citation: exact
  - Quote: "we use a 3-stage pipeline as follows."

- **uncertainty**: The authors acknowledge that oracle retrieval is unrealistic and may omit necessary context; the inspected pages do not resolve how much this affects comparisons.
  - Page 4 · citation: whitespace
  - Quote: "This “oracle” retrieval setting is less realistic, since a software engineer working on addressing an issue does not know a priori which files may need to be modified."

Unresolved questions:

- How robust are the reported model comparisons to choices of prompts, retrieval configuration, and evaluation procedure?
- How often do the selected tests accept a patch that does not fully resolve the issue, or reject a valid alternative implementation?
- What do the full experimental results and appendices show about model performance, construction quality, and dataset limitations? The inspected evidence covers only pages 1–4.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "oracle retriever"}` | Locate reported model evaluation results. | 1 matches on pages [1] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect dataset construction and benchmark design. | read pages [2, 3, 4] | [event 11](trace.jsonl#L11) |
| 3 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Assess the benchmark from the abstract and inspected pages 2–4; note evidence gaps beyond these pages. | review accepted | [event 16](trace.jsonl#L16) |
