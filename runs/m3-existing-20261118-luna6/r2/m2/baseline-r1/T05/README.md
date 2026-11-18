# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**baseline · ok**

1 model calls · 0 reads · 6.36 s · $0.000431

1 decisions · 0 tool calls · 16657 input tokens (16654 cached) · 529 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.77

WebArena contributes a self-hostable, reproducible environment of functional web applications and an 812-task benchmark for evaluating agents on long-horizon, natural-language web tasks. Its central value is the combination of realistic interaction, multi-site tasks, and outcome-based evaluation; baseline results and error analysis illustrate the benchmark’s difficulty, though they do not establish broad conclusions about agent capabilities.

- **strength**: The environment combines standalone reproducibility with functional, multi-domain websites, tools, and knowledge resources.
  - Page 2 · citation: whitespace
  - Quote: "WebArena creates websites from four popular categories with functionality and data mimicking their real-world equivalents."

- **strength**: The benchmark evaluates whether task outcomes meet intent criteria, rather than requiring one reference action sequence.
  - Page 2 · citation: whitespace
  - Quote: "This evaluation is not only more reliable [40, 5, 33] than comparing the vanilla action sequences [25, 7] but also accommodates a range of potential valid paths to achieve the same goal"

- **limitation**: The authors report that some benchmark items cannot be completed because of missing evidence, permissions, or unsupported site functionality; these are labeled N/A.
  - Page 8 · citation: whitespace
  - Quote: "some tasks ( ∼4%) in our benchmark are not possible to complete."

- **uncertainty**: The reported baseline results are limited to two prompted agent designs and the specified GPT model versions, so they do not establish how other agent approaches perform on the benchmark.
  - Page 9 · citation: exact
  - Quote: "We design two LLM-prompt-based web agents as our baselines"

Unresolved questions:

- How robust are the task annotations and programmatic evaluators across all 812 tasks, particularly where fuzzy matching relies on an LLM judge?
- How sensitive are baseline success rates to prompt design, action budget, model sampling variability, or alternative observation modes?
- How well do the sampled website data and constrained site implementations represent web tasks beyond the included domains and northeast US map coverage?
- Inspection was limited to the supplied pages; detailed per-task results, full annotation materials, and the complete successful trajectory were not reviewed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
