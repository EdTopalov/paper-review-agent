# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**agent · ok**

6 model calls · 4 reads · 16.38 s · $0.001718

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

SWE-bench contributes a substantial, realistic benchmark of issue-resolution tasks drawn from real GitHub repositories, framing code generation as repository-level engineering evaluated against tests. The reported baselines show difficulty for evaluated models, and the authors clearly identify Python-only coverage and test-based evaluation as scope limitations.

- **strength**: The benchmark grounds tasks in real GitHub issues and pull requests across multiple Python repositories.
  - Page 1 · citation: exact
  - Quote: "2,294 software engi-\nneering problems drawn from real GitHub issues and corresponding pull requests\nacross 12 popular Python repositories."

- **strength**: The paper reports low performance on the benchmark even with oracle retrieval, supporting its claim that these tasks challenge the tested models.
  - Page 1 · citation: exact
  - Quote: "Claude 2 and GPT-4 solve a mere4.8% and 1.7% of instances re-\nspectively, even when provided with an oracle retriever."

- **limitation**: The current task collection covers only Python, so generalization to other languages and domains remains unestablished.
  - Page 9 · citation: whitespace
  - Quote: "SWE-bench task instances are all in Python; we hope to ap-\nply SWE-bench’s task instance collection procedure to expand its coverage to more programming languages and domains."

- **limitation**: Execution-based tests alone do not guarantee that generated solutions are reliable.
  - Page 9 · citation: exact
  - Quote: "relying solely on this method is insufficient to guarantee reliable performance of\nmodel generations"

Unresolved questions:

- I did not inspect the benchmark-construction procedure or detailed experimental sections; how are issue/PR pairs filtered and test relevance validated, and how robust are headline results across model configurations?
- How well does benchmark success correlate with expert judgments of correctness, maintainability, and usefulness in real engineering work?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — Page 1 states that the 2,294 tasks come from real GitHub issues and corresponding pull requests across 12 Python repositories; page 2 describes those as user-submitted issues and solutions.
- Observation 2: **supported** — Pages 1–2 report low solve rates for Claude 2 and GPT-4 even with oracle retrieval, and page 5 reports Claude 2’s 4.8% oracle pass rate. This supports the qualified claim that the benchmark challenges the evaluated models.
- Observation 3: **supported** — Page 9 states that all task instances are in Python and presents expanding language and domain coverage as future work; generalization beyond the current collection is therefore unestablished.
- Observation 4: **supported** — Page 9 explicitly says relying solely on execution-based testing is insufficient to guarantee reliable model generations, noting that outputs can be less comprehensive, efficient, or readable than human-written solutions.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper’s stated scope boundaries and limitations for a balanced assessment. | 2 matches on pages [2, 9] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 8, "end": 10}` | Read discussion and limitations, plus nearby empirical findings, to evaluate scope and evidence. | read pages [8, 9, 10] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "oracle retriever"}` | Find the reported evaluation setup and headline results to substantiate the benchmark’s empirical contribution. | 1 matches on pages [1] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Submit an evidence-based assessment using inspected abstract, discussion, and limitations pages; note evaluation details not inspected. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1]); #2: hyphenation_ambiguous (pages [1]); #3: hyphenation_ambiguous (pages [9]) | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 1, "end": 1}` | Retrieve exact abstract wording for citation validation after the prior quote check flagged hyphenation ambiguity. | read pages [1] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Resubmit with exact observed quotations, preserving the PDF’s hyphenation and spelling. | review accepted | [event 30](trace.jsonl#L30) |
