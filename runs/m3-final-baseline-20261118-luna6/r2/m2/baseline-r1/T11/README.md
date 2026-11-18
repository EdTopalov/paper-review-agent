# T11: Executable Code Actions Elicit Better LLM Agents

**baseline · ok**

1 model calls · 0 reads · 6.21 s · $0.000570

1 decisions · 0 tool calls · 30099 input tokens (30096 cached) · 537 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

The paper proposes CodeAct, a multi-turn agent framework in which executable Python is the action format, and contributes a 7k-trajectory instruction-tuning dataset plus fine-tuned Llama-2- and Mistral-based agents. Its experiments offer encouraging evidence that code actions can improve task success and reduce interaction turns on a small multi-tool benchmark, while the trained agent improves on several agent evaluations. The core idea is practically motivated and supported by broad model comparisons, but the benchmark is small and curated, results vary by backbone, and the paper itself identifies unresolved safety and reliability concerns.

- **strength**: The paper evaluates action formats across 17 models and reports a clear CodeAct advantage on its multi-tool benchmark, including fewer turns for many evaluated models.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs)"

- **strength**: The authors release a substantial multi-domain training dataset and evaluate models on both agent-oriented and general tasks, including an ablation of the data mixture.
  - Page 8 · citation: not_found
  - Quote: "Total 7,139 10,581,681 1482.24"

- **limitation**: M3ToolEval has only 82 human-curated instances, which limits how confidently its measured gains establish broad performance across complex tool-use settings.
  - Page 5 · citation: exact
  - Quote: "It contains 82 human-curated instances"

- **uncertainty**: Safe deployment of unrestricted code execution remains unresolved; the paper flags sandbox escape as a possibility but does not establish what protections or threat model suffice in practice.
  - Page 10 · citation: whitespace
  - Quote: "the need for future work to design better safety mechanism to safeguard autonomous agents."

Unresolved questions:

- How robust are CodeAct's gains on larger, independently constructed benchmarks and tasks outside the paper's hand-crafted tool sets?
- What sandboxing, permission, and monitoring mechanisms are necessary for practical deployment of agents that can execute arbitrary code?
- Which aspects of the training mixture or backbone explain the Llama-2 and Mistral performance differences, and how consistently do these findings transfer to other models?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
