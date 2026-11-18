# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**baseline · ok**

1 model calls · 0 reads · 12.09 s · $0.000486

1 decisions · 0 tool calls · 14416 input tokens (14413 cached) · 683 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.65

ReflExion adds a persistent, natural-language memory and LLM-generated reflection between trials to a language-model agent, using binary success feedback and simple failure heuristics rather than policy training. The paper reports improved cumulative task completion over ReAct on AlfWorld and HotPotQA, and discusses a largely unsuccessful WebShop evaluation. It is a useful, concrete demonstration of trial-to-trial adaptation, though the evidence is limited in scale and does not isolate reflection from other contributing factors.

- **strength**: The method is clearly described as a lightweight, model-agnostic addition to an existing agent loop, with memory updated after failure and the environment reset for another attempt.
  - Page 3 · citation: wrong_page
  - Quote: "Finally, we add the reflection to the agent’s memory, reset the environment, and start the next trial."

- **strength**: The AlfWorld evaluation reports a substantial cumulative gain over the ReAct baseline and includes a concrete trajectory illustrating how stored information can change a later attempt.
  - Page 5 · citation: normalized
  - Quote: "Given the ability to reflect, the agent used ReAct to solve 97% of the given environments in 12 trials"

- **limitation**: The HotPotQA headline results are inconsistent across the paper: the abstract gives 51%, while the results section reports 54%, and the reported improvement over baseline also differs. This makes the exact headline result unclear.
  - Page 6 · citation: normalized
  - Quote: "Reflexion enabled the agent to successfully answer 54% of the questions from the dataset"

- **uncertainty**: The reported evaluations cover 134 AlfWorld environments and 100 HotPotQA questions, but the inspected results do not establish how robust the gains are across different question or environment samples. Broader evaluation would clarify generality.
  - Page 6 · citation: normalized
  - Quote: "We tested the base agent and Reflexion agent on a 100-question dataset."

Unresolved questions:

- How much of the improvement depends on the reflection mechanism itself, versus repeated attempts, memory contents, prompting examples, or the specific trial and stopping rules?
- Would the reported gains hold across multiple random samples or runs, with uncertainty estimates and a broader range of tasks and models?
- What explains the discrepancy between the abstract’s HotPotQA result of 51% and the results section’s 54%?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
