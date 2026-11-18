# T11: Executable Code Actions Elicit Better LLM Agents

**baseline · ok**

1 model calls · 0 reads · 6.78 s · $0.004033

1 decisions · 0 tool calls · 30099 input tokens (0 cached) · 541 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes CodeAct, a framework in which LLM agents use executable Python as their environment-facing action format, with observations and errors fed back across turns. It evaluates action formats on atomic API calls and a newly curated multi-tool benchmark, then trains CodeActAgent using 7k interaction trajectories plus general conversation data. Results support advantages on complex tool tasks and improved agent performance for the Mistral-based model, while also exposing substantial variation across backbones and limits in practical reliability.

- **strength**: The new M3ToolEval benchmark directly tests the paper’s central claim about composing multiple tools over turns; CodeAct leads on success rate for most evaluated models and often uses fewer turns.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs), similar to the trend in §2.2."

- **strength**: The authors provide evidence that curated interaction data can improve an open model on several agent and general-task measures, and include an ablation indicating that both interaction data and general conversations contribute.
  - Page 9 · citation: whitespace
  - Quote: "Both CodeActInstruct and general conversations contribute to agent tasks, while general conversations are essential to maintain performance on general tasks."

- **limitation**: The agent results are not uniform across backbones: the LLaMA-2 variant fails to improve on M3ToolEval, whereas the Mistral model does. The paper offers hypotheses rather than establishing the cause.
  - Page 9 · citation: whitespace
  - Quote: "Surprisingly, no improvement is observed for the Llama-2 variant."

- **limitation**: The complex-task benchmark is relatively small and manually curated, and the paper itself reports a large open/closed-model performance gap; conclusions about broad real-world performance should therefore remain bounded.
  - Page 5 · citation: whitespace
  - Quote: "It contains 82 human-curated instances, spanning tasks including web browsing, finance, travel itinerary planning, science, and information processing."

Unresolved questions:

- How robust are the M3ToolEval comparisons to benchmark size, task composition, and variation in manually authored tools and answer formats?
- What specifically explains the LLaMA-2/Mistral difference, and does the result persist across training seeds or alternative data mixtures?
- How do execution permissions, isolation, and safety checks affect reliability when CodeAct is deployed with access to real software packages or external systems?
- Inspection was limited to the supplied pages; detailed supplementary prompts, full evaluation protocols, and underlying interaction examples were not independently examined beyond the excerpts provided.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
