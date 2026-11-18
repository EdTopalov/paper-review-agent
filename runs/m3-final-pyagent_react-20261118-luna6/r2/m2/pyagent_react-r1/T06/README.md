# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**pyagent_react · ok**

7 model calls · 4 reads · 26.56 s · $0.002467

7 decisions · 7 tool calls · 46382 input tokens (37687 cached) · 2007 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SWE-bench introduces a substantial, execution-based benchmark of repository-scale software engineering tasks built from real GitHub issues and pull requests, and establishes baseline results for several models. Its realism, scale, and updateable construction are valuable contributions; the evaluation also shows that measured success depends on retrieval and context. The evidence is bounded by the Python-only task set and the authors’ stated baseline focus. I inspected pages 1–3, 5–7, and 9–10, not the appendices’ detailed construction procedures or all experimental analyses.

- **strength**: The task formulation links issue descriptions to code edits and evaluates proposed patches by running associated tests, making the benchmark concretely verifiable.
  - Page 3 · citation: whitespace
  - Quote: "If the patch applies successfully and all of these tests pass we consider the proposed solution to have successfully resolved the issue."

- **strength**: The baseline results show that even the best-performing evaluated model succeeds on a small fraction of tasks in the oracle-retrieval setting.
  - Page 5 · citation: whitespace
  - Quote: "The best performing model, Claude 2, only achieves a mere 4.8% pass rate using the “oracle” retrieval context."

- **limitation**: The benchmark’s task instances are restricted to Python, limiting the language and domain scope of the reported evaluation.
  - Page 9 · citation: exact
  - Quote: "SWE-bench task instances are all in Python"

- **limitation**: Passing tests alone does not establish that a generated solution is reliable or comparable in quality to a human solution; this is an acknowledged evaluation boundary.
  - Page 9 · citation: whitespace
  - Quote: "relying solely on this method is insufficient to guarantee reliable performance of model generations"

Unresolved questions:

- How representative are the selected repositories and filtered tasks of software engineering beyond the included Python projects?
- How do the detailed collection and test-selection procedures affect benchmark coverage and the robustness of the pass-rate metric?
- How would stronger agent-based approaches or software engineering tools change the results? The inspected discussion presents these as future directions, not results.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the authors’ stated scope boundaries and caveats. | 2 matches on pages [2, 9] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect benchmark construction and task-validation details. | read pages [2, 3] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 5, "end": 7}` | Inspect model comparisons and experimental evidence. | read pages [5, 6, 7] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 9, "end": 10}` | Inspect discussion, stated limitations, and benchmark caveats. | read pages [9, 10] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Submit a source-grounded assessment based on the inspected overview, evaluation, and discussion pages. | citation_validation_failed; #2: not_found | [event 26](trace.jsonl#L26) |
| 6 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Resubmit with directly copied excerpts from inspected pages after citation validation flagged one quote. | citation_validation_failed; #2: wrong_page (pages [5]) | [event 31](trace.jsonl#L31) |
| 7 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Correct the retrieval-results citation to the observed page where that excerpt appears. | review accepted | [event 36](trace.jsonl#L36) |
