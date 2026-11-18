# T11: Executable Code Actions Elicit Better LLM Agents

**agent · ok**

5 model calls · 4 reads · 10.65 s · $0.001962

5 decisions · 5 tool calls · 29119 input tokens (17351 cached) · 667 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes CodeAct, using executable Python as a unified action interface for LLM agents, and supplies comparative tool-use results, a multi-turn instruction dataset, and fine-tuned agent models. The benchmark results support meaningful gains in the tested settings, particularly on complex tool composition, but the clearest new benchmark is small and zero-shot performance varies sharply by model; the paper itself identifies practical prototype limitations and safety concerns.

- **strength**: CodeAct has a concrete comparative advantage in the authors' multi-tool benchmark: 12 of 17 evaluated models have higher success with CodeAct, and the strongest reported result is substantially ahead of alternatives.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs), similar to the trend in §2.2."

- **limitation**: M3ToolEval is a modestly sized, human-curated benchmark, so evidence for broad complex-task generalization remains limited by the tested instance set and manually crafted tools.
  - Page 5 · citation: whitespace
  - Quote: "It contains 82 human-curated instances, spanning tasks including web browsing, finance, travel itinerary planning, science, and information processing."

- **strength**: The authors test their instruction-tuned models on both agent and general capability tasks, and report a caveat rather than claiming uniform gains: Mistral has slight MMLU degradation.
  - Page 9 · citation: whitespace
  - Quote: "except for a slight degradation on MMLU for CodeActAgent (Mistral, 7B)."

- **limitation**: The paper acknowledges prototype reliability and safety concerns arising from model hallucination and unrestricted code execution; these are important practical boundaries for deployment.
  - Page 10 · citation: exact
  - Quote: "CodeActAgent is an initial prototype of an autonomous agent and still has several practical limitations."

Unresolved questions:

- How robust are the benchmark advantages to larger and more diverse task sets, tool collections, and non-zero-shot prompting?
- What execution sandboxing and safety controls are needed for dependable real-world use, and how effective are they?
- I inspected the abstract, selected experimental and model-evaluation pages, and limitations, but not the full appendix or complete training/data-generation details; those could qualify reproducibility and generalization claims.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Check the paper's stated scope boundaries and limitations before scoring. | 3 matches on pages [10] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 4}` | Inspect experimental setup and comparative results supporting the central performance claim. | read pages [3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 9, "end": 10}` | Review evaluation details and the authors' explicit limitations for a balanced assessment. | read pages [9, 10] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 5, "end": 6}` | Inspect benchmark construction and results to judge strength and scope of the empirical comparison. | read pages [5, 6] (text truncated by tool) | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence covers core benchmark, model evaluation, and stated limitations; submit a balanced assessment while noting uninspected details. | review accepted | [event 25](trace.jsonl#L25) |
