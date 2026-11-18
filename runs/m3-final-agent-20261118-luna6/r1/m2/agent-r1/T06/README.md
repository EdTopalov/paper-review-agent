# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**agent · ok**

5 model calls · 4 reads · 10.23 s · $0.001478

5 decisions · 5 tool calls · 23612 input tokens (15499 cached) · 650 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.79

SWE-bench makes a substantial benchmark contribution by turning real GitHub issues and repository snapshots into executable, patch-based software-engineering tasks, with a filtered set of 2,294 instances and baseline evaluations. Its realistic scope and test-based verification are valuable; the reported model success rates also expose a challenging capability gap. Its evidence is for a Python-only benchmark and execution-based pass criteria, not a complete measure of patch quality or software-engineering competence.

- **strength**: The benchmark construction links genuine issues and pull requests to code snapshots and filters tasks using tests that change from failing to passing, giving the evaluation a meaningful, executable target.
  - Page 2 · citation: whitespace
  - Quote: "We filter out task instances without at least one test where its status changes from a fail to pass"

- **strength**: The evaluation provides concrete baseline evidence that the benchmark challenges tested systems, including under an oracle context condition; this is evidence about those evaluated systems, not a universal ceiling.
  - Page 2 · citation: whitespace
  - Quote: "Claude 2 and GPT-4 only resolve 4.8% and 1.7% of tasks respec- tively; even using an oracle that retrieves the files to edit from a reference solution."

- **limitation**: The task collection is limited to Python, so the paper does not establish coverage or benchmark behavior across other languages and domains.
  - Page 9 · citation: exact
  - Quote: "SWE-bench task instances are all in Python"

- **limitation**: Passing execution-based tests does not establish that a generated patch is comprehensive, efficient, or readable; the authors explicitly qualify the metric’s sufficiency.
  - Page 9 · citation: whitespace
  - Quote: "relying solely on this method is insufficient to guarantee reliable performance of model generations"

Unresolved questions:

- How representative are the selected popular repositories and filtered issue/PR pairs of software maintenance beyond those projects?
- How would rankings and conclusions change under broader human review of patch correctness, maintainability, readability, and test coverage?
- I inspected the abstract, benchmark-construction page, and final discussion, but not the detailed experimental tables, full filtering analysis, or appendices; those details could refine confidence in the reported comparisons.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Find the authors’ stated scope boundaries and limitations for a balanced assessment. | 2 matches on pages [2, 9] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 8, "end": 10}` | Inspect discussion, limitations, and concluding claims across the paper’s final sections. | read pages [8, 9, 10] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "4.8%"}` | Locate the headline evaluation results to assess empirical support for the benchmark’s claims. | 6 matches on pages [1, 2, 5, 6, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 2, "end": 2}` | Read benchmark construction and task definition for dataset design and validation details. | read pages [2] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.79, "observations": 4}}` | Evidence covers the benchmark design, headline baseline results, and explicit limitations; submit a balanced assessment while noting sections not inspected. | review accepted | [event 25](trace.jsonl#L25) |
