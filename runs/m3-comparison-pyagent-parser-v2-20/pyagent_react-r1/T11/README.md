# T11: Executable Code Actions Elicit Better LLM Agents

**pyagent_react · ok**

4 model calls · 2 reads · 17.56 s · $0.001626

4 decisions · 3 tool calls · 14832 input tokens (5309 cached) · 765 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

The paper proposes using executable Python code as a unified action format for LLM agents, enabling tool composition and iterative execution with feedback. It supports the proposal with comparisons across 17 LLMs and introduces a benchmark for multi-tool tasks; it also describes an instruction dataset and a fine-tuned agent. The inspected evidence is strongest for the benchmark results. I inspected the abstract and pages 4–5, not the full paper’s dataset construction, training, or broader agent evaluation, so those claims remain less assessed here.

- **strength**: The multi-turn benchmark compares CodeAct with JSON and text across 17 models and reports CodeAct as the most successful format for most of them, with fewer turns for most as well.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs)"

- **strength**: The benchmark targets complex tool composition and reports a substantial best-model gap over the next-best format, while also exposing large differences between model groups.
  - Page 5 · citation: whitespace
  - Quote: "achieves a 20.7% absolute improvement compared to the next best action format (text) while requiring2.1 fewer interaction turns on average."

- **limitation**: M3ToolEval is a compact, manually curated benchmark, which limits how broadly its results alone can establish performance across task distributions.
  - Page 5 · citation: exact
  - Quote: "It contains 82 human-curated instances"

- **uncertainty**: The benchmark’s success metric uses exact-match answers, and the tested setup is zero-shot; how sensitive the relative results are to alternative answer validation or demonstrations is unresolved in the inspected pages.
  - Page 5 · citation: exact
  - Quote: "match the ground-truth solutions"

Unresolved questions:

- How robust are CodeAct’s gains on larger or independently constructed task sets and under different prompting or demonstration conditions?
- How do the CodeActInstruct data and fine-tuning affect the agent’s results and general capabilities? Those sections were not inspected.
- What safety and reliability controls govern execution of generated code in the proposed agent? This was not established by the inspected pages.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | search_paper `{"query": "success rate"}` | Locate quantitative comparisons supporting the paper’s main performance claim. | 8 matches on pages [1, 2, 3, 5, 9] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 4, "end": 5}` | Inspect benchmark design and reported comparisons for evidence and scope. | read pages [4, 5] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Submit an evidence-based assessment from the abstract and inspected benchmark pages, noting uninspected sections. | review accepted | [event 21](trace.jsonl#L21) |
