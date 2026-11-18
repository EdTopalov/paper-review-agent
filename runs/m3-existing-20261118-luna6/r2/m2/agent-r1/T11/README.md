# T11: Executable Code Actions Elicit Better LLM Agents

**agent · ok**

6 model calls · 5 reads · 11.00 s · $0.003575

6 decisions · 6 tool calls · 46219 input tokens (21859 cached) · 661 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes CodeAct, using executable Python as a unified, multi-turn action format for LLM agents, and supports its advantages with API-calling and multi-tool evaluations across 17 LLMs. It also releases a 7k-trajectory instruction dataset and fine-tuned agents. The evidence is promising, especially for complex tool composition, but M3ToolEval is a compact, human-curated benchmark and performance is highly model-dependent.

- **strength**: Across tested LLMs, CodeAct often improves task success and reduces interaction turns on the new complex-tool benchmark.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs), similar to the trend in §2.2."

- **strength**: The work complements the action-format proposal with a dataset and model evaluation, including out-of-domain text-action tasks.
  - Page 9 · citation: whitespace
  - Quote: "Both CodeActInstruct and general conversations contribute to agent tasks, while general conversations are essential to maintain performance on general tasks."

- **limitation**: The central complex-task evaluation is based on only 82 curated instances with manually crafted tools, limiting how broadly its results establish real-world generality.
  - Page 5 · citation: whitespace
  - Quote: "It contains 82 human-curated instances, spanning tasks including web browsing, finance, travel itinerary planning, science, and information processing."

- **limitation**: The authors explicitly acknowledge practical reliability and execution-safety concerns for the prototype.
  - Page 10 · citation: whitespace
  - Quote: "For example, it may suffer from hallucination commonly seen in LLMs (e.g., imagine the content of a variable without actually printing it out), suggesting the need for subsequent alignment"

Unresolved questions:

- How robust are the comparative gains on larger, independently constructed benchmarks and less hand-crafted tool environments?
- What execution sandbox and safety guarantees are needed for deploying agents that can freely run generated code?
- I inspected the abstract, method/results pages, model evaluation, and limitations, but not the full appendix, prompting details, or all benchmark tables; those may affect reproducibility and interpretation of individual comparisons.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "20%"}` | Locate reported benchmark results to assess empirical support. | 2 matches on pages [1, 3] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect method, benchmark construction, and result pages for substantiation. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 6}` | Review dataset and agent training evidence, including evaluation protocol. | read pages [5, 6] (text truncated by tool) | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "safe"}` | Check whether execution safety or sandbox constraints are discussed as scope limitations. | 2 matches on pages [10] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 9, "end": 10}` | Inspect authors' stated limitations and safety boundary before scoring. | read pages [9, 10] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence inspected covers core method, comparative results, and stated limitations; submit independent assessment. | review accepted | [event 31](trace.jsonl#L31) |
