# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**baseline · ok**

1 model calls · 0 reads · 10.57 s · $0.000512

1 decisions · 0 tool calls · 14416 input tokens (14413 cached) · 735 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

ReFlexion adds a natural-language reflection and memory step between attempts by an LLM agent, using binary success feedback and simple heuristics to guide retry behavior. The reported results on AlfWorld and HotPotQA suggest that this approach can improve performance across trials without fine-tuning. The contribution is useful and clearly illustrated, but the empirical support is limited by the small evaluation samples and by missing information in the inspected report about run-to-run variability.

- **strength**: The paper presents a simple, concrete mechanism for turning failed attempts into advice stored for later trials, and illustrates how it can redirect an agent's plan.
  - Page 4 · citation: normalized
  - Quote: "Finally, we add the reflection to the agent’s memory, reset the environment, and start the next trial."

- **strength**: On the reported AlfWorld evaluation, the reflection-enabled agent substantially improves its cumulative task success rate over trials.
  - Page 5 · citation: whitespace
  - Quote: "the agent used ReAct to solve 97% of the given environments in 12 trials, failing to solve only 4 out of 134 tasks."

- **limitation**: The HotPotQA results are reported inconsistently: the abstract gives 51%, while the results section reports 54%. This makes the exact final score unclear, though both sections claim improvement over the baseline.
  - Page 6 · citation: not_found
  - Quote: "Reﬂexion agent was able to successfully answer 54% of the questions from the dataset"

- **uncertainty**: The inspected results report outcomes for 134 AlfWorld environments and a 100-question HotPotQA dataset, but do not establish how stable the gains are across repeated runs or different samples. The paper also reports no improvement on WebShop, suggesting the approach may depend on whether reflection can address the relevant failure mode.
  - Page 10 · citation: whitespace
  - Quote: "The agent achieved a 33% → 34% accuracy improvement in the baseline run and a mere33% → 35% accuracy improvement in the Reﬂexion run"

Unresolved questions:

- How much do the reported gains vary across random seeds, task samples, and model runs?
- How sensitive are results to the reflection prompts, memory limit, retry budget, and success-detection heuristic?
- Can the approach improve performance when failures arise from tool or search quality rather than the agent's reasoning, as suggested by the WebShop discussion?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
