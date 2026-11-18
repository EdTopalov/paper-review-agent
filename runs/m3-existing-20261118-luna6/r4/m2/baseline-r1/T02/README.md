# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**baseline · ok**

1 model calls · 0 reads · 8.22 s · $0.000472

1 decisions · 0 tool calls · 14416 input tokens (14413 cached) · 656 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

Reflxion adds a natural-language reflection and persistent working memory between trials of an LLM agent, with a simple heuristic to trigger reflection and binary success/failure feedback. The paper reports improved cumulative task completion over retry-only ReAct baselines on AlfWorld and HotPotQA, and a small, inconclusive WebShop evaluation. This is a useful, concrete demonstration of trial-to-trial learning without fine-tuning, but the evidence is limited to a narrow set of benchmarks and does not establish how robustly the gains generalize.

- **strength**: The approach is simple and operationally clear: a heuristic triggers reflection on trajectory history and feedback, which is stored for a subsequent attempt.
  - Page 4 · citation: normalized
  - Quote: "Finally, we add the reflection to the agent’s memory, reset the environment, and start the next trial."

- **strength**: The AlfWorld evaluation reports a substantial cumulative improvement over the baseline, though the comparison is across repeated trials rather than a single-attempt accuracy comparison.
  - Page 5 · citation: normalized
  - Quote: "Given the ability to reflect, the agent used ReAct to solve 97% of the given environments in 12 trials"

- **limitation**: The HotPotQA result is based on only 100 questions, and the paper gives inconsistent headline success figures: the abstract says 51%, while the results section reports 54%.
  - Page 6 · citation: whitespace
  - Quote: "Reﬂexion agent achieved 32% accuracy in the ﬁrst trials"

- **uncertainty**: The paper reports benchmark outcomes but the supplied discussion does not establish how stable the gains are across model settings or repeated experimental runs; the reported results alone leave that generality uncertain.
  - Page 10 · citation: not_found
  - Quote: "We used GPT-3.0 and GPT 3.5 to power a ReAct agent"

Unresolved questions:

- How much do outcomes vary across random seeds, question/task samples, and LLM versions, and are the reported gains statistically stable?
- How sensitive are improvements to the reflection prompt, memory limit, trial budget, and heuristic thresholds?
- Would the approach retain its advantages on a broader range of tasks where binary success feedback is delayed, noisy, or costly?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
