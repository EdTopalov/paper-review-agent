# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**deliberative_review · ok**

7 model calls · 3 reads · 30.24 s · $0.005746

7 decisions · 4 tool calls · 34941 input tokens (0 cached) · 2776 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

OSWorld presents an executable virtual-computer environment and a 369-task Ubuntu benchmark intended to evaluate agents on varied desktop and web workflows. Its task-specific setup and outcome checks are a useful design for open-ended computer-use evaluation. The available text supports the benchmark’s construction and infrastructure, but provides limited evidence here for evaluator reliability or for the reported agent–human performance gap.

- **strength**: Tasks can begin from intermediate computer states, and the infrastructure supports task setup, agent interaction, and scripted evaluation.
  - Page 4 · citation: exact
  - Quote: "initializes the required state for the task through the Task Manager."

- **strength**: The paper describes example-wise evaluation as supporting diverse tasks and reliable evaluation of complex open-ended tasks; the excerpt does not show validation of evaluator reliability.
  - Page 5 · citation: exact
  - Quote: "The example-wise evaluation facilitates the diversity of tasks and reliable evaluation"

- **limitation**: The main task suite is defined on Ubuntu; the excerpt describes a smaller Windows set, so equivalent benchmark coverage across operating systems is not established by the inspected text.
  - Page 6 · citation: whitespace
  - Quote: "369 real computing tasks defined and executed on Ubuntu. Additionally, we provide a set of 43 tasks for Windows"

Unresolved questions:

- How consistently do custom evaluators recognize valid alternative ways of completing tasks, and how were their correctness and reliability checked?
- What agent and human evaluation procedures and detailed results support the reported performance gap and failure-mode analysis? The abstract reports headline results, but the relevant detailed results were not inspected.
- What limitations or scope qualifications are discussed later in the paper? Pages 1, 2, 4–6, 15, and 23 were available, with pages 2, 15, and 23 partial; 44 of 51 pages remain uninspected.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the benchmark/task construction and execution-based evaluation sections to verify how tasks, initial states, and success scripts are defined and whether evaluation reliability is supported.; Inspect agent and human evaluation results, including baselines and analysis, to assess whether the reported performance gap and stated failure modes follow from the evidence.; Inspect limitations and scope discussion, and relevant later sections, before treating any support or limitation as absent; only page 1 is currently available, so explicitly flag the remaining 50 uninspected pages. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 3 matches on pages [6, 15, 23] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 8 matches on pages [1, 2, 4] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [4, 5, 6] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The second observation's quotation is not supported verbatim by the supplied page-5 excerpt: it joins wording from the page-4 sentence with “dedicated functions” from page 5. Each observation needs a short quote from one PDF page. Replace it with a verbatim page-5 quotation or another verified quote.; Target: Replace the second observation’s quote with a verbatim span found on one inspected PDF page, then verify its page number. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Replaced the second observation’s unsupported combined quotation with a verbatim page-5 span. Updated the performance-evidence ledger to reflect the abstract’s reported headline results while retaining uncertainty about the detailed evaluation. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "limitations"}` | Locate the paper's scope/limitations discussion to assess boundaries and avoid inferring omissions. | 3 matches on pages [6, 15, 23] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "execution-based evaluation"}` | Inspect benchmark construction and evaluation evidence, including task setup and validation. | 8 matches on pages [1, 2, 4] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 4, "end": 6}` | Inspect task construction, execution evaluation, and benchmark scope to support evidence-based assessment. | read pages [4, 5, 6] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.68, "observations": 3}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
