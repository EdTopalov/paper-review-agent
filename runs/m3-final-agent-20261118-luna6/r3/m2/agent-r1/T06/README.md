# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**agent · ok**

7 model calls · 4 reads · 18.20 s · $0.002069

7 decisions · 7 tool calls · 40432 input tokens (31948 cached) · 1423 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SWE-bench makes a substantial contribution by operationalizing repository-scale software issue resolution as an execution-tested benchmark built from real GitHub issues and merged fixes. Its scale, realistic task formulation, and baseline evaluations offer a useful testbed, while its Python-only coverage and test-based success criterion bound what its results establish.

- **strength**: The benchmark construction filters linked pull requests using test changes and execution evidence, anchoring tasks in real maintenance work while requiring a demonstrated test transition.
  - Page 2 · citation: whitespace
  - Quote: "We filter out task instances without at least one test where its status changes from a fail to pass"

- **strength**: The paper reports low resolution rates for proprietary models with oracle retrieval, evidence supporting its claim that the benchmark is challenging.
  - Page 2 · citation: whitespace
  - Quote: "Using a BM25 retriever, performance drops further to 1.96% for Claude 2."

- **limitation**: The benchmark covers Python tasks only, explicitly limiting language and domain generalization of the dataset as presented.
  - Page 9 · citation: exact
  - Quote: "SWE-bench task instances are all in Python"

- **limitation**: Passing tests is not sufficient to establish broader software quality; the authors caution that test-based evaluation does not ensure comprehensive, efficient, or readable solutions.
  - Page 9 · citation: whitespace
  - Quote: "relying solely on this method is insufficient to guarantee reliable performance of model generations"

Unresolved questions:

- How representative are the selected repositories and filtered issues of software engineering beyond these popular Python projects?
- How would conclusions about model capability change with independent assessments of patch quality beyond passing the associated tests?
- How well do the baseline results hold under later model/tooling approaches, which the paper explicitly treats as future directions?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper's explicit discussion of benchmark limitations and scope. | 2 matches on pages [2, 9] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect benchmark construction and task definition for evidence on dataset design. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 9}` | Read evaluation findings and the authors' stated limitations to balance contribution and evidence. | read pages [8, 9] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Submit a balanced assessment grounded in the inspected benchmark design, results summary, and explicit limitations. | citation_validation_failed; #1: hyphenation_ambiguous (pages [2]); #2: hyphenation_ambiguous (pages [2]) | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 2, "end": 2}` | Retrieve exact source wording for the two page-2 claims after citation validation flagged hyphenation. | read pages [2] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Resubmit the assessment with exact page-2 wording preserved, alongside the verified scope and evaluation caveats. | citation_validation_failed; #2: hyphenation_ambiguous (pages [2]) | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Replace the hyphenated results quote with exact non-hyphenated wording observed on page 2 and finalize the assessment. | review accepted | [event 35](trace.jsonl#L35) |
