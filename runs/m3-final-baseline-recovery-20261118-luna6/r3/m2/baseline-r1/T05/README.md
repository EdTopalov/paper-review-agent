# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**baseline · ok**

1 model calls · 0 reads · 6.69 s · $0.000435

1 decisions · 0 tool calls · 16657 input tokens (16654 cached) · 536 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

WebArena contributes a self-hosted, interactive web environment and an 812-task benchmark for evaluating agents on realistic, multi-step browser tasks. Its combination of functional websites, multiple observation/action modes, and outcome-oriented evaluation makes it a useful platform for measuring end-to-end task completion. Baseline results establish that the selected GPT agents struggle substantially, while the error analysis offers concrete failure categories.

- **strength**: The environment is designed for repeatable evaluation rather than depending on changing live websites, and ships with resettable, self-contained deployments.
  - Page 3 · citation: whitespace
  - Quote: "We achieve reproducibility by having the environment be standalone, not relying on live websites."

- **strength**: The benchmark evaluates task outcomes, including acceptable alternative action paths, rather than requiring agents to reproduce a reference action sequence.
  - Page 2 · citation: whitespace
  - Quote: "This evaluation is not only more reliable [40, 5, 33] than comparing the vanilla action sequences [25, 7] but also accommodates a range of potential valid paths to achieve the same goal"

- **limitation**: The authors report that some benchmark tasks cannot be completed because of missing evidence, permissions, or unsupported site functionality; these are explicitly labeled rather than silently treated as solvable.
  - Page 8 · citation: whitespace
  - Quote: "some tasks ( ∼4%) in our benchmark are not possible to complete."

- **uncertainty**: The reported agent results are narrow baselines: the experiments described here use text observations and a small set of prompted GPT agents. How well the benchmark supports other model families, modalities, or agent designs remains an open question.
  - Page 9 · citation: whitespace
  - Quote: "Primarily, we use an accessibility tree with element IDs as the observation space"

Unresolved questions:

- How robust are benchmark scores to alternative reasonable evaluation implementations, particularly the language-model-based fuzzy_match judgments?
- How representative are the selected sites, tasks, and user-history-based category choices of broader real-world web use beyond the authors' browsing sample?
- The inspected pages do not provide uncertainty estimates or repeated-run variability for the baseline success rates; how much do these results vary across runs and model sampling?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
