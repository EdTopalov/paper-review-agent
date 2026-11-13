# T11: Executable Code Actions Elicit Better LLM Agents

**baseline · ok**

1 model calls · 0 reads · 4.67 s · $0.004041

1 decisions · 0 tool calls · 30099 input tokens (0 cached) · 557 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes CodeAct, a general-purpose LLM-agent action interface in which agents execute Python code and receive environment feedback over multiple turns. It evaluates action formats on atomic API calls and a new multi-tool benchmark, then introduces a 7k-trajectory instruction-tuning dataset and CodeActAgent models. Results suggest advantages on complex tool-use tasks and show promising agent-task transfer, while also exposing substantial variability across model backbones.

- **strength**: The action-format comparison covers 17 models and multiple task settings; on the authors’ 82-instance benchmark, CodeAct has the highest success rate for 12 of 17 models and uses fewer turns for 12 of 17.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs)"

- **strength**: The paper goes beyond proposing an interface by releasing a substantial multi-domain interaction dataset and reporting agent and general-task evaluations, with ablations reported in the appendix.
  - Page 8 · citation: not_found
  - Quote: "Total 7,139 10,581,681 1482.24"

- **limitation**: The paper itself documents a major inconsistency in the fine-tuning results: the LLaMA-2-based agent shows no M3ToolEval improvement, whereas the Mistral-based agent improves. This limits claims of reliable gains across backbones.
  - Page 9 · citation: whitespace
  - Quote: "Surprisingly, no improvement is observed for the Llama-2 variant."

- **uncertainty**: The complex-task benchmark is small and manually curated; how robust its rankings are to broader task coverage or alternative task construction remains unclear. I inspected the main paper and selected appendix pages, not every prompt, instance, or implementation detail.
  - Page 5 · citation: exact
  - Quote: "It contains 82 human-curated instances"

Unresolved questions:

- How stable are the M3ToolEval action-format comparisons across larger and independently constructed task sets?
- Which factors explain the divergent fine-tuning outcomes between the LLaMA-2 and Mistral backbones, and do they generalize to other models?
- How should executable-code agents be sandboxed and permissioned in practical deployments, given the paper’s stated safety concern?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
