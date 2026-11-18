# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**agent · ok**

7 model calls · 5 reads · 15.34 s · $0.002767

7 decisions · 7 tool calls · 38947 input tokens (22630 cached) · 1046 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SWE-bench contributes a sizeable, realistic benchmark for repository-level issue resolution, connecting GitHub issues and merged fixes to executable tests. Its construction pipeline and baseline evaluations make it useful for measuring capabilities beyond short-form code generation. Reported results and disclosed limitations also underscore that test success is not a complete measure of software quality.

- **strength**: The benchmark is grounded in real development tasks and staged filtering yields a substantial collection.
  - Page 2 · citation: exact
  - Quote: "Through these stages of filtering, the original 90,000 PRs are filtered down to the 2,294 task in-\nstances which comprise SWE-bench."

- **strength**: The reported baseline performance supports the task's difficulty, including in a privileged retrieval setting.
  - Page 2 · citation: exact
  - Quote: "Claude 2 and GPT-4 only resolve 4.8% and 1.7% of tasks respec-\ntively; even using an oracle that retrieves the files to edit from a reference solution."

- **limitation**: The authors explicitly bound evaluated coverage to Python and state an intended expansion; this is a scope boundary, not a demonstrated failure of generalization.
  - Page 9 · citation: whitespace
  - Quote: "SWE-bench task instances are all in Python; we hope to ap-\nply SWE-bench’s task instance collection procedure to expand its coverage to more programming languages and domains."

- **limitation**: Execution-based testing alone does not establish patch quality, a concern the authors acknowledge.
  - Page 9 · citation: exact
  - Quote: "relying solely on this method is insufficient to guarantee reliable performance of\nmodel generations"

Unresolved questions:

- How well would the collection and evaluation approach transfer to other languages and repository ecosystems?
- How sensitive are conclusions to repository selection and the available test coverage?
- What evaluation methods can capture maintainability, completeness, and readability alongside test passing?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper's stated limitations to assess scope and unresolved concerns. | 2 matches on pages [2, 9] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 8, "end": 10}` | Inspect evaluation results and discussion/limitations supporting an evidence-based assessment. | read pages [8, 9, 10] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "2,294"}` | Find benchmark construction details and dataset scale evidence. | 3 matches on pages [1, 2, 23] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "4.8%"}` | Locate quantitative model performance results to judge empirical support. | 6 matches on pages [1, 2, 5, 6, 7] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 2, "end": 2}` | Read the benchmark construction page to verify task provenance and filtering. | read pages [2] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Evidence gathered on benchmark scale, filtering, results, and disclosed limitations; provide independent assessment. | citation_validation_failed; #1: hyphenation_ambiguous (pages [2]); #2: hyphenation_ambiguous (pages [2]); #3: hyphenation_ambiguous (pages [9]) | [event 31](trace.jsonl#L31) |
| 7 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Correct quote matching by preserving the page text's exact line-break hyphenation and submit the assessment. | review accepted | [event 37](trace.jsonl#L37) |
