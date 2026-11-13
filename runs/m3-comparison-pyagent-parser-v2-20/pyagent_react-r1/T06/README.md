# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**pyagent_react · ok**

4 model calls · 2 reads · 12.05 s · $0.001890

4 decisions · 3 tool calls · 16941 input tokens (5473 cached) · 804 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SWE-bench introduces a substantial repository-level software engineering benchmark built by linking GitHub issues to merged pull requests and validating instances with execution-based tests. Its scale, realistic inputs, and explicit filtering pipeline make a useful evaluation resource; the paper also reports low success for evaluated models. The evidence inspected supports the benchmark design and evaluation framing, while leaving questions about representativeness and test-based validity open.

- **strength**: The benchmark construction uses a clear multi-stage filter, including a fail-to-pass test criterion and checks against installation or runtime failures.
  - Page 2 · citation: whitespace
  - Quote: "We filter out task instances without at least one test where its status changes from a fail to pass"

- **strength**: The evaluation requires both a patch that applies and successful execution of task-associated tests, a concrete criterion for issue resolution.
  - Page 3 · citation: whitespace
  - Quote: "If the patch applies successfully and all of these tests pass we consider the proposed solution to have successfully resolved the issue."

- **limitation**: The task collection is bounded to popular Python repositories, so transfer to other ecosystems and less prominent projects is not established by this design.
  - Page 2 · citation: whitespace
  - Quote: "We start by collecting pull requests (PRs) from 12 popular open-source Python repositories on GitHub"

- **uncertainty**: The authors acknowledge that reference-edited files may not supply all context; the inspected pages do not establish how often this affects the oracle comparison.
  - Page 4 · citation: whitespace
  - Quote: "edited files alone may not include all the required context to understand exactly how software will behave when interacting with unseen parts of the code."

Unresolved questions:

- How well do the benchmark instances and reported model results generalize to repositories outside the selected Python projects?
- How reliably do the associated tests capture the full intent of issue resolution, including valid alternative fixes?
- I inspected pages 1–4 and 10 only; I did not inspect the full results, detailed error analysis, or appendices, so this assessment cannot resolve further experimental or dataset-quality questions.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 10, "end": 12}` | Inspect benchmark construction and task validation details. | read pages [10, 11, 12] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark methodology and model evaluation results. | read pages [2, 3, 4] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Submit an evidence-based assessment using the inspected abstract, benchmark-method, and setup pages. | review accepted | [event 21](trace.jsonl#L21) |
