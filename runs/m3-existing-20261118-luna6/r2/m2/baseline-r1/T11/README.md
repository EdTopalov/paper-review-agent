# T11: Executable Code Actions Elicit Better LLM Agents

**baseline · ok**

1 model calls · 0 reads · 6.59 s · $0.000577

1 decisions · 0 tool calls · 30099 input tokens (30096 cached) · 552 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

The paper proposes CodeAct, a multi-turn agent framework in which LLMs use executable Python as a unified action format, and introduces a 7,139-trajectory instruction-tuning dataset and fine-tuned agents. Its experiments suggest that code actions can improve success and reduce interactions on compositional tool tasks, while fine-tuning improves several agent benchmarks for a Mistral-based model. The contribution is practical and supported by broad model comparisons, but the central complex-task benchmark is small and curated, and results are not uniformly favorable across backbones.

- **strength**: The paper evaluates action formats across 17 models and reports a clear advantage for CodeAct on its 82-instance multi-tool benchmark: it is best on success rate for 12 models and on interaction turns for 12.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs)"

- **strength**: The work goes beyond proposing an action format: it releases a substantial multi-domain interaction dataset and evaluates fine-tuned open models on both agent and general tasks.
  - Page 8 · citation: exact
  - Quote: "Total 7,139 10 ,581,681 1482 .24"

- **limitation**: The main complex-task evaluation is based on only 82 human-curated instances, so its breadth and representativeness for real-world tasks remain uncertain.
  - Page 5 · citation: exact
  - Quote: "It contains 82 human-curated instances"

- **uncertainty**: The agent fine-tuning gains vary substantially by backbone: the LLaMA-2 variant shows no M3ToolEval improvement, whereas Mistral does. The paper offers possible explanations, but their causes are not established.
  - Page 9 · citation: whitespace
  - Quote: "Surprisingly, no improvement is observed for the Llama-2 variant."

Unresolved questions:

- How well do the action-format results hold on larger, independently constructed compositional-tool benchmarks and beyond the manually curated tool sets?
- Which training-mixture or backbone factors explain the divergent M3ToolEval outcomes for LLaMA-2 and Mistral?
- What safety and reliability controls are needed for unrestricted package access and code execution in practical deployments?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
