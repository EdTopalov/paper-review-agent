# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**baseline · ok**

1 model calls · 0 reads · 6.59 s · $0.002139

1 decisions · 0 tool calls · 14416 input tokens (0 cached) · 674 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Refl exion (Reflexion) adds a language-model reflection step and persistent working memory between attempts, using binary success feedback and simple heuristics to trigger reflection. The paper reports improved performance over retrying with ReAct on AlfWorld and HotPotQA, while WebShop results are inconclusive. The approach is straightforward and potentially useful, but the evidence is limited to a small set of experiments and the reported HotPotQA numbers are inconsistent.

- **strength**: The paper presents a simple, model-agnostic idea: use feedback from a failed attempt to produce advice for a later attempt, rather than relying only on retries.
  - Page 4 · citation: normalized
  - Quote: "Finally, we add the reflection to the agent’s memory, reset the environment, and start the next trial."

- **strength**: On AlfWorld, the authors report substantial improvement over the ReAct baseline across repeated trials, with a stated 97% task success rate.
  - Page 5 · citation: exact
  - Quote: "the agent used ReAct to solve 97% of the given environments in 12 trials"

- **limitation**: The WebShop experiment does not establish a benefit: the authors report nearly unchanged performance and say the agent did not generate helpful reflections.
  - Page 10 · citation: whitespace
  - Quote: "The agent achieved a 33% → 34% accuracy improvement in the baseline run and a mere33% → 35% accuracy improvement in the Reﬂexion run"

- **uncertainty**: The HotPotQA results are reported inconsistently: the abstract gives 51%, while the results section gives 54%. This makes the precise reported endpoint unclear.
  - Page 1 · citation: exact
  - Quote: "We observe success rates of 97% and 51%, respectively"

Unresolved questions:

- How robust are the reported gains across more tasks, environments, and model choices? The experiments described here use 134 AlfWorld environments and a 100-question HotPotQA dataset.
- How much of the improvement depends on the reflection prompts, memory cap, and other experiment-specific choices, rather than the general reflection-and-memory mechanism?
- Which HotPotQA result is intended: the abstract's 51% or the results section's 54%?
- The assessment is limited to the supplied paper text and figures as transcribed; I have not independently checked the code, logs, or underlying benchmark results.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
