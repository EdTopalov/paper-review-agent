# T11: Executable Code Actions Elicit Better LLM Agents

**baseline · ok**

1 model calls · 0 reads · 6.96 s · $0.000568

1 decisions · 0 tool calls · 30099 input tokens (30096 cached) · 534 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes CodeAct, a general-purpose LLM-agent framework that uses executable Python as the action interface, allowing tool composition and multi-turn revision from execution feedback. It also introduces a 7,139-trajectory instruction-tuning dataset and evaluates CodeAct across tool-use formats and agent tasks, reporting advantages on complex tasks and improved results for its Mistral-based agent. The work offers a coherent framework, benchmark, data, and model, though its complex-task benchmark is small and performance gains are not consistent across backbones.

- **strength**: The main empirical comparison includes 17 models and finds CodeAct most often has the best success rate and uses fewer turns on the authors’ 82-instance benchmark.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs)"

- **strength**: The paper contributes both a multi-domain interaction dataset and an open-source agent trained to use the proposed action interface.
  - Page 8 · citation: whitespace
  - Quote: "The statistics of the resulting dataset CodeActInstruct are shown in Tab. 4."

- **limitation**: The central complex-task benchmark has only 82 human-curated instances, making the breadth and reliability of its measured gains uncertain.
  - Page 5 · citation: exact
  - Quote: "It contains 82 human-curated instances"

- **uncertainty**: The agent’s improvements vary by backbone: the LLaMA-2 variant does not improve on M3ToolEval, while the Mistral variant does. The paper offers possible explanations but does not resolve the cause.
  - Page 9 · citation: whitespace
  - Quote: "Surprisingly, no improvement is observed for the Llama-2 variant."

Unresolved questions:

- How robust are the M3ToolEval results to a larger and more varied set of tasks, and to evaluation beyond exact-match answers?
- Which factors explain the different M3ToolEval outcomes for the LLaMA-2- and Mistral-based agents?
- How does CodeAct perform in deployments where executing generated code poses safety or reliability risks? The paper acknowledges sandbox concerns but does not establish a mitigation.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
