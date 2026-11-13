# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**pyagent_react · ok**

5 model calls · 2 reads · 20.61 s · $0.002810

5 decisions · 5 tool calls · 34676 input tokens (20767 cached) · 1728 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

OSWorld contributes a controllable desktop-computer environment and a 369-task benchmark spanning applications and cross-application workflows, with task-specific execution-based evaluation. Its varied baselines and human comparison offer evidence that current agents struggle on these tasks. The contribution is substantial, though conclusions are bounded by the benchmark and evaluated agent setups.

- **strength**: The benchmark presents example-specific evaluation as a way to assess diverse, complex tasks.
  - Page 5 · citation: whitespace
  - Quote: "The example-wise evaluation facilitates the diversity of tasks and reliable evaluation of complex, real-world, open-ended tasks."

- **strength**: The reported results provide a clear model–human performance comparison and show large gaps across task categories.
  - Page 10 · citation: exact
  - Quote: "Human Performance 75.00% 71.79% 70.51% 73.47% 73.27% 72.36%"

- **uncertainty**: The reported baseline findings are bounded by the tested interaction budget; whether they persist under other budgets remains unresolved.
  - Page 10 · citation: whitespace
  - Quote: "We heuristically request the agents to complete the tasks within a max step limit of 15, which is enough for most tasks."

- **limitation**: Task-specific evaluator construction requires a broad set of functions for retrieving and assessing varied data.
  - Page 5 · citation: whitespace
  - Quote: "As a result, we construct a vast collection of functions that make final wrangling and retrieve files and data information of varying types, categories, and granularities"

Unresolved questions:

- How well do the benchmark’s tasks and evaluation scripts represent computer use beyond the included applications and curated tasks?
- Do baseline rankings and low success rates persist under other prompting, action, and interaction-budget choices?
- I inspected the abstract and selected pages 3–5 and 9–11, not the full paper or appendices; detailed task coverage, implementation, and robustness evidence remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 3, "end": 5}` | Inspect benchmark design, task composition, and evaluation methodology. | read pages [3, 4, 5] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 9, "end": 11}` | Inspect benchmark scale, baseline results, and any stated scope limitations. | read pages [9, 10, 11] | [event 11](trace.jsonl#L11) |
| 3 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Submit an evidence-based assessment from the inspected abstract, environment, and benchmark results. | citation_validation_failed; #1: not_found | [event 17](trace.jsonl#L17) |
| 4 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Correct the unverified page-5 quotation using an exact observed excerpt. | citation_validation_failed; #1: wrong_page (pages [4]) | [event 23](trace.jsonl#L23) |
| 5 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Use a page-5 quotation confirmed in the observed text. | review accepted | [event 29](trace.jsonl#L29) |
