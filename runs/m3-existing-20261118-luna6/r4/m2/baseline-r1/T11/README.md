# T11: Executable Code Actions Elicit Better LLM Agents

**baseline · ok**

1 model calls · 0 reads · 7.56 s · $0.000595

1 decisions · 0 tool calls · 30099 input tokens (30096 cached) · 587 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

The paper proposes CodeAct, a framework in which LLM agents use executable Python as their environment-facing action format, with interpreter feedback enabling multi-turn revision. It evaluates action formats on atomic API calls and a new 82-task multi-tool benchmark, then introduces a 7k-trajectory tuning dataset and fine-tuned open models. Results are promising, especially for stronger models and the Mistral-based agent, but the benchmark is small and some claims about general practical capability rest on limited evidence.

- **strength**: The multi-tool comparison reports substantial gains for several models and fewer interaction turns, providing direct evidence for the proposed control/data-flow advantage on the authors’ benchmark.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs)"

- **strength**: The paper contributes both a curated interaction dataset and a trained agent, and evaluates the agent on in-domain, out-of-domain, and general tasks rather than only demonstrating the framework qualitatively.
  - Page 8 · citation: not_found
  - Quote: "Total 7,139 10,581,681 1482.24"

- **limitation**: M3ToolEval has only 82 human-curated instances, so its reported improvements do not by themselves establish broad coverage of complex tool-use settings.
  - Page 5 · citation: exact
  - Quote: "It contains 82 human-curated instances"

- **uncertainty**: The agent results are mixed: the LLaMA-2 variant shows no M3ToolEval improvement, and the authors offer possible explanations rather than identifying the cause. The provided pages do not resolve this anomaly.
  - Page 9 · citation: whitespace
  - Quote: "Surprisingly, no improvement is observed for the Llama-2 variant."

Unresolved questions:

- How robust are the action-format gains across larger and more diverse complex-task benchmarks, beyond the 82-instance M3ToolEval?
- What causes the LLaMA-2 CodeActAgent’s lack of M3ToolEval improvement, and can the proposed data-artifact explanation be tested?
- How do execution permissions, sandbox security, and failure containment affect CodeAct’s practical deployment? The paper flags sandbox escape as a concern but does not establish a safety evaluation in the inspected pages.
- This assessment is based on the supplied pages; supplementary sections are present, but their detailed contents and any additional experimental evidence were not fully inspected.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
