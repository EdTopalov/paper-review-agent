# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**baseline · ok**

1 model calls · 0 reads · 7.13 s · $0.000426

1 decisions · 0 tool calls · 16657 input tokens (16654 cached) · 518 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

WebArena contributes a self-hosted, interactive web environment and an 812-task benchmark for evaluating agents on realistic, multi-step web tasks. Its use of functional outcome checks and multiple application domains makes it a useful evaluation platform; baseline results also illustrate the difficulty of the tasks, though the reported agent comparison is narrow.

- **strength**: The environment combines standalone, interactive applications and supports varied browser observations and actions, offering a practical basis for reproducible agent evaluation.
  - Page 3 · citation: whitespace
  - Quote: "We achieve reproducibility by having the environment be standalone, not relying on live websites."

- **strength**: The benchmark targets high-level tasks and evaluates task outcomes rather than requiring agents to reproduce one action sequence.
  - Page 2 · citation: whitespace
  - Quote: "This evaluation is not only more reliable [40, 5, 33] than comparing the vanilla action sequences [25, 7] but also accommodates a range of potential valid paths to achieve the same goal"

- **limitation**: The authors explicitly identify a meaningful scope boundary: some benchmark tasks cannot be completed in the environment, and these are labeled N/A.
  - Page 8 · citation: whitespace
  - Quote: "some tasks ( ∼4%) in our benchmark are not possible to complete."

- **uncertainty**: The reported baseline evidence is limited to two prompting styles and two model configurations; broader agent comparisons would help establish how generally the benchmark results characterize agent capability.
  - Page 9 · citation: exact
  - Quote: "We design two LLM-prompt-based web agents as our baselines"

Unresolved questions:

- How robust are the task success results to changes in model sampling settings, prompt design, and repeated runs? The paper notes high-temperature sampling and variance but does not report uncertainty estimates in the inspected results.
- How reliable are the programmatic evaluators and the GPT-3.5-based fuzzy-match judgments across the full benchmark? The inspected pages describe evaluation procedures but do not report an independent evaluator validation.
- How well do the sampled applications and data represent web tasks outside the selected domains and the northeast-US map region?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
