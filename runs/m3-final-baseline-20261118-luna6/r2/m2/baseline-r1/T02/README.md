# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**baseline · ok**

1 model calls · 0 reads · 8.23 s · $0.000508

1 decisions · 0 tool calls · 14416 input tokens (14413 cached) · 728 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

ReflExion adds a self-reflection step and a bounded natural-language memory to an LLM agent: after failure, the agent uses its trajectory and binary success feedback to form advice for a later attempt. The paper reports gains over retrying without reflection on AlfWorld and HotPotQA, and an inconclusive WebShop result. The approach is simple and potentially useful, but the evidence is preliminary and does not isolate reflection from other factors or establish how broadly the gains generalize.

- **strength**: The paper presents a straightforward, model-agnostic framing of reflection as advice carried across trials, and illustrates how it can change later actions.
  - Page 4 · citation: normalized
  - Quote: "Finally, we add the reflection to the agent’s memory, reset the environment, and start the next trial."

- **strength**: The AlfWorld evaluation reports a substantial cumulative improvement over the non-reflective agent, with a concrete task count and comparison.
  - Page 5 · citation: normalized
  - Quote: "Given the ability to reflect, the agent used ReAct to solve 97% of the given environments in 12 trials, failing to solve only 4 out of 134 tasks."

- **limitation**: The HotPotQA setup uses only 100 questions, and the paper does not report uncertainty estimates or repeated-run variation in the supplied results; the reported end result also differs between the abstract and results section.
  - Page 6 · citation: normalized
  - Quote: "Reflexion enabled the agent to successfully answer 54% of the questions from the dataset"

- **uncertainty**: The authors report limited improvement on WebShop and attribute failures partly to search-result quality, leaving open when the method helps versus when tool limitations dominate.
  - Page 10 · citation: normalized
  - Quote: "This observation may not be a direct limitation of the Reflexion approach, but it highlights the ability of a Reflexion agent to optimize reasoning trace and action execution but not complete awareness of the quality of the tools that it may be using."

Unresolved questions:

- How stable are the reported gains across independent runs, different task samples, and different LLMs?
- How much of the improvement comes from reflection itself versus added retries, prompt examples, or trajectory information retained in memory?
- What methods can reliably detect misleading or unhelpful reflections, and how do memory limits affect performance on longer tasks?
- The inspected paper reports 51% in the abstract and 54% in the HotPotQA results section; which figure is intended, and what accounts for the discrepancy?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
