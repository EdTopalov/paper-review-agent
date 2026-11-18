# T11: Executable Code Actions Elicit Better LLM Agents

**pyagent_react · ok**

4 model calls · 2 reads · 12.98 s · $0.002004

4 decisions · 3 tool calls · 23217 input tokens (11129 cached) · 765 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes CodeAct, using executable Python as a flexible action interface for multi-turn LLM agents, and evaluates it against text and JSON actions. It also releases a 7k-trajectory instruction-tuning dataset and fine-tuned agents. The controlled comparisons and out-of-domain tests support the approach, though benchmark scale, overlap with training domains, and the evaluation’s scope constrain how broadly the results can be interpreted.

- **strength**: The comparison spans 17 LLMs and reports a consistent aggregate advantage for CodeAct on the authors’ multi-tool benchmark, including fewer turns for many models.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs), similar to the trend in §2.2."

- **limitation**: M3ToolEval is a small, manually curated benchmark, so its results alone leave uncertainty about performance across larger or independently sampled task sets.
  - Page 5 · citation: whitespace
  - Quote: "It contains 82 human-curated instances, spanning tasks including web browsing, finance, travel itinerary planning, science, and information processing."

- **strength**: The authors report both in-domain and out-of-domain agent evaluation, and test whether CodeAct-trained agents transfer to text-action tasks and retain general capabilities.
  - Page 9 · citation: whitespace
  - Quote: "hence we report separate numbers for MINT’s in- and out-of-domain performance."

- **uncertainty**: The training data includes domains used in evaluation, so the reported in-domain results do not establish generalization to unseen task domains; the separate out-of-domain results help address but do not resolve that question.
  - Page 9 · citation: exact
  - Quote: "MINT includes ALFWorld and MATH"

Unresolved questions:

- How well does CodeAct compare with text or JSON actions on larger, independently curated multi-tool benchmarks?
- How sensitive are the results to interpreter design, available libraries, and safety restrictions on executable code?
- How much of the gains persists on agent tasks with no domain overlap or benchmark-specific adaptation?
- I inspected the abstract and selected pages covering the benchmark, data construction, and evaluation; I did not inspect the full appendices, prompts, or all reported ablations, so details there remain uncertain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 7, "end": 9}` | Inspect benchmark design and reported comparisons. | read pages [7, 8, 9] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 4, "end": 6}` | Inspect the core CodeAct benchmark results and evaluation details. | read pages [4, 5, 6] (text truncated by tool) | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit a balanced assessment based on observed benchmark, training-data, and evaluation pages. | review accepted | [event 20](trace.jsonl#L20) |
