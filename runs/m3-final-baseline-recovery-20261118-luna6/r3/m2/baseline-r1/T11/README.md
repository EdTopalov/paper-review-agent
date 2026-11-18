# T11: Executable Code Actions Elicit Better LLM Agents

**baseline · ok**

1 model calls · 0 reads · 7.67 s · $0.000633

1 decisions · 0 tool calls · 30099 input tokens (30096 cached) · 663 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes CodeAct, a multi-turn agent framework in which LLMs use executable Python as actions, and evaluates it against text and JSON action formats. It also contributes a 7k-trajectory instruction-tuning dataset and open-source CodeActAgent models. Results show advantages on several tool-use and agent benchmarks, though the strongest evidence comes from a small, purpose-built benchmark and the paper itself identifies practical safety and reliability concerns.

- **strength**: The comparison across 17 LLMs reports a consistent, measurable advantage for CodeAct on the authors’ complex tool-use benchmark, including higher success rates and fewer interaction turns for most evaluated models.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs), similar to the trend in §2.2."

- **strength**: The paper tests whether the training data contributes beyond the action framework: its ablation reports that CodeActInstruct and general conversation data both contribute to agent-task performance, while the latter helps preserve general-task performance.
  - Page 9 · citation: whitespace
  - Quote: "Both CodeActInstruct and general conversations contribute to agent tasks, while general conversations are essential to maintain performance on general tasks."

- **limitation**: M3ToolEval contains only 82 human-curated instances and uses manually crafted domain-specific tools, so the reported gains do not by themselves establish performance across broader or less curated environments.
  - Page 5 · citation: whitespace
  - Quote: "It contains 82 human-curated instances, spanning tasks including web browsing, finance, travel itinerary planning, science, and information processing."

- **uncertainty**: The paper acknowledges that executing generated code raises safety concerns, but the supplied evaluation does not resolve how robustly sandboxing contains unsafe behavior in deployment.
  - Page 10 · citation: whitespace
  - Quote: "highlighting the need for future work to design better safety mechanism to safeguard autonomous agents."

Unresolved questions:

- How do CodeAct’s benefits hold up on larger, independently constructed benchmarks and on environments with tools or tasks not designed around its evaluation setup?
- What sandbox protections, monitoring, and recovery mechanisms are needed to make arbitrary generated-code execution acceptably safe in practical deployments?
- What explains the LLaMA-2 CodeActAgent’s failure to improve on M3ToolEval, and would further controlled analyses distinguish pretraining artifacts from differences in backbone capability?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
