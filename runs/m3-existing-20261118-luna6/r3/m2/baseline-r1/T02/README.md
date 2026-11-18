# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**baseline · ok**

1 model calls · 0 reads · 8.38 s · $0.000522

1 decisions · 0 tool calls · 14416 input tokens (14413 cached) · 756 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

ReflExion adds a natural-language memory of reflections from failed attempts to an LLM agent, using binary success feedback and simple heuristics to decide when to reflect. Its reported AlfWorld and HotPotQA results suggest that reflections can help an agent improve across retries, while the paper also reports little benefit on WebShop. The contribution is a straightforward, potentially useful mechanism, supported by benchmark experiments and illustrative trajectories, but the evidence is limited in scale and does not isolate the source or reliability of the gains.

- **strength**: The paper presents a concrete, general-purpose framework: after a failed trial, the agent produces a reflection from its trajectory and memory, then uses it in a subsequent attempt. The example trajectories make the proposed mechanism understandable.
  - Page 4 · citation: normalized
  - Quote: "Finally, we add the reflection to the agent’s memory, reset the environment, and start the next trial."

- **strength**: The benchmark results provide evidence that reflection can improve performance over repeated attempts, including a substantial reported AlfWorld gain over the ReAct baseline. These are the authors’ reported results, not independently reproduced findings.
  - Page 5 · citation: normalized
  - Quote: "Given the ability to reflect, the agent used ReAct to solve 97% of the given environments in 12 trials"

- **limitation**: The HotPotQA reporting is internally inconsistent: the abstract gives 51% and a 17-point improvement, whereas the results section reports 54% and a 20-point improvement. This discrepancy makes the headline figure unclear.
  - Page 1 · citation: exact
  - Quote: "We observe success rates of 97% and 51%, respectively"

- **uncertainty**: The evaluated samples are limited to 134 AlfWorld environments and 100 HotPotQA questions, and the supplied text does not report uncertainty estimates. The evidence therefore leaves open how stable the observed gains are across samples or runs.
  - Page 5 · citation: whitespace
  - Quote: "we ran the agent in 134 AlfWorld environments across six different tasks"

Unresolved questions:

- How much of the gains comes from the content of the self-generated reflections, versus simply retaining task-specific facts or trying again with additional context?
- Would the improvements remain similar across different random samples, repeated runs, and language models? The inspected paper text reports no uncertainty estimates.
- Which HotPotQA result should be treated as the headline outcome: the abstract’s 51% or the results section’s 54%?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
