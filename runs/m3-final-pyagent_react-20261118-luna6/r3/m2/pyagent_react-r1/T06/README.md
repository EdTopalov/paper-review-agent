# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**pyagent_react · ok**

8 model calls · 4 reads · 21.92 s · $0.002393

8 decisions · 6 tool calls · 52099 input tokens (41685 cached) · 1349 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.82

SWE-bench introduces a large, execution-evaluated benchmark of real GitHub issues paired with codebase snapshots and reference pull requests, and establishes baseline performance for several language models. Its realistic repository-level tasks and reproducible collection framework offer substantial value for studying software engineering capabilities, while its initial Python-only scope and test-based success criterion leave meaningful limits.

- **strength**: The benchmark frames repository issues as patch-generation tasks evaluated against repository tests.
  - Page 2 · citation: whitespace
  - Quote: "Each task requires generating a patch describing changes to apply to the existing codebase."

- **strength**: The paper reports very low resolution rates even with oracle file retrieval, supporting the case that these tasks challenge the evaluated models under the study’s setup.
  - Page 5 · citation: whitespace
  - Quote: "The best performing model, Claude 2, only achieves a mere 4.8% pass rate using the “oracle” retrieval context."

- **limitation**: The authors explicitly bound the initial dataset to Python, limiting what this release directly establishes about other languages and domains; they identify expansion as future work.
  - Page 9 · citation: whitespace
  - Quote: "SWE-bench task instances are all in Python; we hope to ap- ply SWE-bench’s task instance collection procedure to expand its coverage to more programming languages and domains."

- **limitation**: Passing execution-based tests is not a complete quality measure: the authors note it does not ensure generations are comprehensive, efficient, or readable.
  - Page 9 · citation: whitespace
  - Quote: "relying solely on this method is insufficient to guarantee reliable performance of model generations"

Unresolved questions:

- How well do the benchmark tasks and reported results generalize beyond the 12 selected Python repositories?
- How might resolution rankings change under evaluation of patch quality beyond test outcomes, including maintainability and readability?
- I inspected the paper’s opening pages, main experimental results, and discussion, but not the appendices’ detailed construction, filtering, or reproducibility procedures; those details remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark construction and evaluation methodology. | read pages [2, 3, 4] | [event 14](trace.jsonl#L14) |
| 4 | read_pages `{"start": 5, "end": 7}` | Check reported model results and benchmark evaluation caveats. | read pages [5, 6, 7] | [event 19](trace.jsonl#L19) |
| 5 | search_paper `{"query": "limitations"}` | Locate the paper’s stated scope limitations. | 2 matches on pages [2, 9] | [event 24](trace.jsonl#L24) |
| 6 | read_pages `{"start": 8, "end": 10}` | Review discussion of scope boundaries and future directions. | read pages [8, 9, 10] | [event 29](trace.jsonl#L29) |
| 7 | submit_review `{"review": {"score": 0.82, "observations": 4}}` | Submit an evidence-grounded assessment of the benchmark and its stated scope. | citation_validation_failed; #1: hyphenation_ambiguous (pages [2]) | [event 34](trace.jsonl#L34) |
| 8 | submit_review `{"review": {"score": 0.82, "observations": 4}}` | Replace the citation flagged for ambiguous hyphenation with an exact observed sentence. | review accepted | [event 39](trace.jsonl#L39) |
