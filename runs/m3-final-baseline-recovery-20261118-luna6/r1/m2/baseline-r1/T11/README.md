# T11: Executable Code Actions Elicit Better LLM Agents

**baseline · ok**

1 model calls · 0 reads · 7.07 s · $0.000586

1 decisions · 0 tool calls · 30099 input tokens (30096 cached) · 569 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes CodeAct, a framework in which LLM agents use executable Python as their environment-facing action format, with a multi-turn interpreter loop that returns execution results and errors as observations. It evaluates action formats on atomic API calls and an 82-instance multi-tool benchmark, then introduces a 7k-trajectory instruction-tuning dataset and fine-tuned open-source agents. Results support gains on several complex tool-use evaluations, but the evidence is bounded by small, curated benchmarks and uneven results across model backbones.

- **strength**: The multi-tool benchmark compares code, JSON, and text under a shared evaluation setup; CodeAct has the highest success rate for 12 of 17 tested models and generally uses fewer turns.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs)"

- **strength**: The authors provide an open-source training contribution and report substantial gains for the Mistral-based agent on both in- and out-of-domain MINT tasks relative to the listed open-source baselines.
  - Page 9 · citation: whitespace
  - Quote: "CodeActAgent (both variants) perform better than all evaluated open-source LLMs on both the in-domain and out-of-domain subsets of MINT."

- **limitation**: The paper explicitly identifies hallucination as a practical limitation, including agents imagining variable contents without checking execution results.
  - Page 10 · citation: whitespace
  - Quote: "it may suffer from hallucination commonly seen in LLMs (e.g., imagine the content of a variable without actually printing it out)"

- **uncertainty**: The benchmark evidence is limited in scale and domain coverage: M3ToolEval contains 82 human-curated instances. How robust the reported format advantage is on larger, independently constructed task sets remains unresolved.
  - Page 5 · citation: exact
  - Quote: "It contains 82 human-curated instances"

Unresolved questions:

- How would CodeAct compare on larger benchmarks with broader task and tool coverage, and with evaluation that reduces dependence on exact-match answers?
- What explains the strong backbone-dependent differences, including the LLaMA-2 CodeActAgent's lack of improvement on M3ToolEval?
- How do execution cost, security controls, and failure rates change when agents use a real Python interpreter and broader package access?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
