# T11: Executable Code Actions Elicit Better LLM Agents

**pyagent_react · ok**

4 model calls · 1 reads · 12.37 s · $0.001424

4 decisions · 2 tool calls · 27882 input tokens (21276 cached) · 772 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

The paper proposes executable Python as a flexible, composable action format for LLM agents, evaluated against JSON and text formats, and introduces a fine-tuning dataset and agent. Its reported comparisons across 17 LLMs provide useful evidence of benefits, especially on the multi-turn benchmark, but the inspected evidence also shows substantial performance variation and a benchmark based on a limited set of curated tasks. I inspected the supplied first page and PDF pages 5–7 only; this leaves the broader evaluation, training results, and limitations sections unassessed.

- **strength**: The reported multi-turn results favor CodeAct for a majority of the evaluated models, supporting the paper’s central empirical claim in this benchmark.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs)"

- **strength**: The benchmark is described as spanning multiple task domains and using manually curated instances, providing a concrete evaluation beyond a single task type.
  - Page 5 · citation: whitespace
  - Quote: "It contains 82 human-curated instances, spanning tasks including web browsing, finance, travel itinerary planning, science, and information processing."

- **limitation**: The dataset construction keeps only the most challenging instances; how this selection affects representativeness or reported performance is unresolved, rather than a demonstrated flaw.
  - Page 7 · citation: exact
  - Quote: "We down-sample each dataset by keeping only the most challenging instances"

- **uncertainty**: The paper reports a large open-/closed-source performance gap on M3ToolEval, so CodeAct alone does not establish strong task-solving performance across model families.
  - Page 5 · citation: whitespace
  - Quote: "the best open-source model achieving 13.4% while the best closed-source model gpt-4-1106-preview 74.4%"

Unresolved questions:

- How robust are the reported format advantages across tasks, model versions, and evaluation settings beyond the inspected benchmark results?
- How do the CodeActAgent fine-tuning results and general-capability evaluations support the claims about instruction tuning? Those sections were not inspected.
- What safeguards and execution constraints govern the Python interpreter in practical deployments? The inspected pages do not establish this.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 5, "end": 7}` | Inspect benchmark design and comparative results. | read pages [5, 6, 7] (text truncated by tool) | [event 6](trace.jsonl#L6) |
| 2 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 11](trace.jsonl#L11) |
| 3 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit an evidence-based assessment using the abstract and inspected benchmark and dataset passages. | review accepted | [event 19](trace.jsonl#L19) |
