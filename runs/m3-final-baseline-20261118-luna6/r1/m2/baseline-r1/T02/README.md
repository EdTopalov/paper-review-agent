# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**baseline · ok**

1 model calls · 0 reads · 11.62 s · $0.000493

1 decisions · 0 tool calls · 14416 input tokens (14413 cached) · 697 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

Refl e xion? Actually Refl exion (Reflexion) adds a natural-language memory of failure and an LLM-generated reflection between attempts, using a binary success signal and simple failure heuristics rather than policy training. The paper reports improved cumulative task completion over ReAct-only retries on AlfWorld and HotPotQA, while documenting little improvement on WebShop. The central contribution is a straightforward, broadly applicable trial-and-reflection framework, supported by promising but limited benchmark evaluations.

- **strength**: The paper presents a clear, training-free mechanism for carrying lessons between attempts: a heuristic triggers reflection, which is stored in working memory for the next trial.
  - Page 4 · citation: normalized
  - Quote: "Finally, we add the reflection to the agent’s memory, reset the environment, and start the next trial."

- **strength**: On AlfWorld, the reported cumulative success is high and the comparison with retries alone supports the claim that reflections can improve behavior across attempts.
  - Page 5 · citation: exact
  - Quote: "the agent used ReAct to solve 97% of the given environments in 12 trials"

- **limitation**: The HotPotQA reporting is internally inconsistent: the abstract gives 51%, while the results section reports 54%. This makes the exact headline result unclear, although both values indicate improvement over the stated 34% baseline.
  - Page 6 · citation: not_found
  - Quote: "Reﬂexion agent achieved 54% accuracy"

- **uncertainty**: The experiments use repeated attempts on the same task set and stop based on observed improvement; the supplied paper does not establish how robust gains are to different task samples, model settings, or repeated runs. This limits confidence in generalization, rather than demonstrating that the reported gains are invalid.
  - Page 5 · citation: whitespace
  - Quote: "we performed the runs with and without Reﬂexion starting from the initial trial until the agent’s ability to improve was saturated"

Unresolved questions:

- How much of the improvement persists across independent task samples, multiple random/model runs, and different LLMs?
- How sensitive are the results to the reflection prompt, memory limit, and heuristic thresholds, and what are the associated inference costs?
- What accounts for the discrepancy between the 51% HotPotQA result in the abstract and the 54% result in the results section?
- Can the approach reliably help when success signals are noisy or delayed, or when tool/search quality—not planning—is the main obstacle?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
