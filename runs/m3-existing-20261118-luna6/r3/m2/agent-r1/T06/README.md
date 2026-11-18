# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**agent · ok**

5 model calls · 3 reads · 13.34 s · $0.001599

5 decisions · 5 tool calls · 24355 input tokens (16856 cached) · 1017 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SWE-bench contributes a large, execution-verified benchmark of repository-scale software engineering tasks grounded in real GitHub issues and merged fixes. Its realistic task formulation and baseline evaluations expose substantial challenges for contemporary models, while the initial evidence is limited to Python repositories and relatively simple approaches; tests alone do not establish patch quality.

- **strength**: The benchmark construction connects real issue reports to merged changes and filters tasks through executable test outcomes, making the task more grounded than short, synthetic code completion.
  - Page 2 · citation: whitespace
  - Quote: "We filter out task instances without at least one test where its status changes from a fail to pass"

- **strength**: The task scale and baseline results make a useful case that repository-level issue resolution is a challenging capability, not captured by simpler coding benchmarks.
  - Page 2 · citation: whitespace
  - Quote: "Claude 2 and GPT-4 only resolve 4.8% and 1.7% of tasks respec- tively; even using an oracle that retrieves the files to edit from a reference solution."

- **limitation**: The benchmark coverage is explicitly confined to Python, limiting conclusions about software engineering across languages and domains.
  - Page 9 · citation: exact
  - Quote: "SWE-bench task instances are all in Python"

- **limitation**: Passing tests is not a complete quality criterion; the authors explicitly note that test-based evaluation cannot guarantee reliable or maintainable generations.
  - Page 9 · citation: whitespace
  - Quote: "relying solely on this method is insufficient to guarantee reliable performance of model generations"

Unresolved questions:

- How representative are the selected repositories and filtered issues of software maintenance beyond popular Python projects?
- How well do test-pass results correlate with human judgments of correctness, maintainability, and completeness across the benchmark?
- How much would stronger retrieval, interactive agent workflows, or tool use change the reported baseline results?
- I inspected the opening, construction and task formulation, selected results, and discussion pages; detailed appendices and the full experimental methodology were not reviewed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper's stated scope and benchmark limitations for a balanced assessment. | 2 matches on pages [2, 9] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect benchmark construction and validation details to judge dataset quality and evaluation design. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 7, "end": 9}` | Review results and discussion limitations to assess evidence and stated benchmark scope. | read pages [7, 8, 9] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | The benchmark design, evaluation criteria, reported results and explicit limitations have been inspected; submit a balanced paper assessment. | citation_validation_failed; #2: hyphenation_ambiguous (pages [2]) | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Correct the model-result quotation using the exact wording observed on page 2 and resubmit the review. | review accepted | [event 25](trace.jsonl#L25) |
