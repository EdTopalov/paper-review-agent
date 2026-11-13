# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**baseline · ok**

1 model calls · 0 reads · 5.86 s · $0.002136

1 decisions · 0 tool calls · 14416 input tokens (0 cached) · 669 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

ReflExion adds a natural-language reflection and memory loop to an LLM agent: after a failed attempt, the agent reflects on its trajectory and carries advice into a retry. The paper reports gains on AlfWorld and HotPotQA, with a less successful WebShop attempt. The idea is simple and practically motivated, but the evidence is limited by the reported benchmark setups and an inconsistency in the HotPotQA results.

- **strength**: The method offers a straightforward way to use outcome feedback across trials without fine-tuning the agent, and the paper illustrates how reflection can change subsequent behavior.
  - Page 4 · citation: normalized
  - Quote: "Finally, we add the reflection to the agent’s memory, reset the environment, and start the next trial."

- **strength**: The AlfWorld evaluation reports a substantial cumulative improvement over repeated trials, while distinguishing learning from mere retries through a retry-only baseline.
  - Page 5 · citation: normalized
  - Quote: "Given the ability to reflect, the agent used ReAct to solve 97% of the given environments in 12 trials, failing to solve only 4 out of 134 tasks."

- **limitation**: The evaluation is bounded: the authors report a modest number of tasks and use a particular LLM and prompt setup, so the results do not establish how broadly the gains generalize.
  - Page 5 · citation: whitespace
  - Quote: "we ran the agent in 134 AlfWorld environments across six different tasks"

- **uncertainty**: The HotPotQA result is internally inconsistent: the abstract reports 51%, while the results section reports 54% and a 20-point advantage. The supplied text does not resolve which figure should be treated as the main result.
  - Page 6 · citation: whitespace
  - Quote: "Reﬂexion agent achieved 32% accuracy in the ﬁrst trials"

Unresolved questions:

- Which HotPotQA final accuracy and improvement over baseline are intended? The abstract states 51% and a 17-point gain, whereas the results section states 54% and a 20-point gain.
- How sensitive are the gains to the choice of base model, reflection prompts, and memory limit? The supplied evaluation uses specific prompt examples and a maximum of three stored reflections.
- Would the approach retain its benefits on broader task samples or tasks where success feedback is noisy or less directly measurable? The paper notes a weak WebShop result but does not establish how general that limitation is.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
