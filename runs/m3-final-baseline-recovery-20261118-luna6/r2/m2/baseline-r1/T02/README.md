# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**baseline · ok**

1 model calls · 0 reads · 9.08 s · $0.000508

1 decisions · 0 tool calls · 14416 input tokens (14413 cached) · 727 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

ReFlexion adds a natural-language reflection and working-memory loop to an LLM agent: after a failed trial, the agent receives binary success/failure feedback, reflects on its trajectory, and uses that reflection in a subsequent attempt. The paper reports improved cumulative task success over repeated trials on AlfWorld and HotPotQA, while also describing a WebShop evaluation with little improvement. The contribution is a simple, interpretable method for learning across trials without policy training, supported by promising but limited benchmark evidence.

- **strength**: The paper presents a concrete, broadly reusable mechanism: a heuristic can trigger reflection, and the resulting advice is retained as working memory for the next attempt.
  - Page 3 · citation: wrong_page
  - Quote: "Finally, we add the reflection to the agent’s memory, reset the environment, and start the next trial."

- **strength**: The AlfWorld results provide a sizable within-task improvement over the reported ReAct baseline across 134 environments, though they do not establish performance beyond this setup.
  - Page 5 · citation: normalized
  - Quote: "Given the ability to reflect, the agent used ReAct to solve 97% of the given environments in 12 trials"

- **limitation**: The HotPotQA result is reported inconsistently: the abstract gives 51%, while the results section gives 54%. This makes the headline figure unclear, although both accounts describe improvement over the baseline.
  - Page 6 · citation: exact
  - Quote: "Reﬂexion enabled the agent to successfully answer 54% of the questions from the dataset"

- **uncertainty**: The paper does not establish how robust these gains are to different models, prompts, or task samples. The supplied evaluation reports selected benchmark runs and does not provide uncertainty estimates in the inspected results.
  - Page 5 · citation: whitespace
  - Quote: "we ran the agent in 134 AlfWorld environments across six different tasks"

Unresolved questions:

- What accounts for the difference between the abstract’s 51% HotPotQA success rate and the 54% reported in the results section?
- How sensitive are the results to the reflection prompt, memory limit, heuristic thresholds, and choice of language model?
- Would the improvements persist across independent samples or runs, and how much do they depend on task-specific few-shot examples?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
