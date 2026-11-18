# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**deliberative_review · ok**

7 model calls · 3 reads · 68.49 s · $0.006702

7 decisions · 4 tool calls · 40941 input tokens (0 cached) · 3188 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

SWE-bench introduces 2,294 issue-linked tasks from 12 Python repositories, evaluated by applying model-generated patches and running tests. Its repository-scale task design and initial evaluations make a useful contribution; reported results show that the tested models solve few tasks under the paper’s retrieval conditions. The scope of those findings is qualified by the evaluation setup and incomplete inspection of the paper.

- **strength**: The collection pipeline filters candidate issue-linked pull requests using test changes and execution checks, including requiring at least one test to change from failing to passing.
  - Page 2 · citation: whitespace
  - Quote: "We filter out task instances without at least one test where its status changes from a fail to pass"

- **strength**: Reference solutions often span multiple parts of a codebase, giving the benchmark a repository-level scope beyond single-function code generation.
  - Page 3 · citation: whitespace
  - Quote: "SWE-bench’s reference solutions average editing 1.7 files, 3.0 functions, and 32.8 lines (added or removed)."

- **limitation**: The strongest reported result uses oracle-selected files, which the authors say is less realistic; the result therefore does not by itself establish performance in an unconstrained workflow.
  - Page 4 · citation: exact
  - Quote: "This “oracle” retrieval setting is less realistic"

- **uncertainty**: The reported GPT-4 results use only a random subset of tasks, a qualification relevant to interpreting comparisons. I inspected pages 1–6, plus partial text from pages 10 and 18; 38 pages were uninspected, so further qualifications or analyses remain unknown.
  - Page 6 · citation: whitespace
  - Quote: "Due to budget constraints we evaluate GPT-4 on a 25% random subset of SWE-bench"

Unresolved questions:

- How sensitive are the solve rates to alternative prompts, patch-generation procedures, and evaluation settings beyond those visible in the inspected pages?
- How often do fail-to-pass tests adequately capture the intended issue, and how well do the full test suites detect regressions outside the tests contributed with a pull request?
- What additional validation details, experimental results, or qualifications appear in the 38 uninspected pages?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the benchmark construction and validation sections: how GitHub issues are linked to merged pull requests, whether task instances and test-based success are checked for reliability, and what filtering or leakage controls are reported.; Inspect the evaluation setup and results, including model access, prompting/retrieval conditions, baselines, and whether the reported solve rates support the paper’s central claims; check for relevant qualifications elsewhere in the paper.; Only page 1 is available in the supplied evidence and 45 pages are uninspected. Locate page-specific verbati … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 5 matches on pages [2, 10, 18] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [2, 3] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [4, 5, 6] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: Observation 2 combines claims about patch evaluation, large codebases, and multi-file reference changes, but its quote directly supports only the patch-evaluation claim. Replace it with a quote that supports the scope claim too, or narrow the observation.; Target: Revise observation 2 so its claim is directly supported by its page-specific quote; page 3 includes the statement that reference solutions average edits to 1.7 files and 3.0 functions. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Revised observation 2 to use the page 3 reference-solution editing statistics, directly supporting its repository-level scope claim. The critic’s concern is addressed; the score is unchanged. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "filtering"}` | Inspect benchmark construction and validation evidence for task selection, test reliability, and leakage controls. | 5 matches on pages [2, 10, 18] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 2, "end": 3}` | Inspect benchmark construction and validation details, then read evaluation setup/results pages for supporting evidence. | read pages [2, 3] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 4, "end": 6}` | Inspect evaluation methodology/results and possible qualifications or limitations, since current evidence covers construction only. | read pages [4, 5, 6] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
