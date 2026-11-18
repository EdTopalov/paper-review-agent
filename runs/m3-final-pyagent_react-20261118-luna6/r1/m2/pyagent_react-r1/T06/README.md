# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**pyagent_react · ok**

6 model calls · 4 reads · 16.87 s · $0.001988

6 decisions · 6 tool calls · 41905 input tokens (33370 cached) · 1176 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SWE-bench introduces a substantial repository-scale coding benchmark built from real GitHub issues and merged fixes, with an execution-based pipeline and baseline evaluations showing that tested models resolve few tasks. Its realistic task setting and extensible construction make it useful for studying software-engineering capabilities, while the Python-only dataset, test-based success criterion, and baseline-oriented experiments bound what the results establish.

- **strength**: The benchmark’s construction links real issue/PR pairs to tests that change from failing to passing, and filters out tasks that fail installation or runtime checks.
  - Page 2 · citation: whitespace
  - Quote: "We filter out task instances without at least one test where its status changes from a fail to pass"

- **strength**: The reported baseline results demonstrate a challenging evaluation setting: even with reference-file oracle retrieval, the best listed model resolves a small fraction of tasks.
  - Page 5 · citation: whitespace
  - Quote: "The best performing model, Claude 2, only achieves a mere 4.8% pass rate using the “oracle” retrieval context."

- **limitation**: The authors explicitly bound the benchmark’s current coverage to Python and acknowledge that passing tests alone does not establish reliable, comprehensive, efficient, or readable solutions.
  - Page 9 · citation: exact
  - Quote: "SWE-bench task instances are all in Python"

Unresolved questions:

- How well would the task-collection and evaluation approach transfer to programming languages and software domains beyond Python?
- How representative are these issue/PR-derived tasks of software engineering work outside the selected repositories and their test practices?
- How would stronger agent-based or tool-augmented approaches perform under comparable evaluation conditions? I inspected the main construction and results sections and the discussion, not the full appendices or every experiment detail.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark construction and evaluation methodology. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 5, "end": 6}` | Inspect model results and evaluation caveats. | read pages [5, 6] | [event 11](trace.jsonl#L11) |
| 3 | search_paper `{"query": "limitations"}` | Locate the authors’ stated scope boundaries and limitations. | 2 matches on pages [2, 9] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 8, "end": 9}` | Inspect discussion of limitations and future directions. | read pages [8, 9] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.78, "observations": 3}}` | Evidence covers benchmark construction, evaluation results, and stated scope limitations. | citation_validation_failed; #2: wrong_page (pages [5]) | [event 26](trace.jsonl#L26) |
| 6 | submit_review `{"review": {"score": 0.78, "observations": 3}}` | Correct the model-results citation to the observed table page and use exact quoted wording for the limitation. | review accepted | [event 31](trace.jsonl#L31) |
