# T11: Executable Code Actions Elicit Better LLM Agents

**agent · ok**

6 model calls · 3 reads · 15.92 s · $0.002151

6 decisions · 6 tool calls · 39681 input tokens (29912 cached) · 1299 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

The paper proposes CodeAct, using executable Python as a unified action format for LLM agents, and evaluates it against text/JSON actions. Results on API-Bank and a curated multi-tool benchmark support gains in tool use; a 7k-interaction tuning dataset and finetuned agents demonstrate a route to adoption. The strongest contribution is evidence for code’s compositional control and data flow in complex tool-use settings, though the support is benchmark-scoped.

- **strength**: The framework supports combining tools and reusing intermediate outputs; the authors report substantial improvements on their curated complex-task benchmark.
  - Page 3 · citation: whitespace
  - Quote: "CodeAct achieves up to a 20% absolute improvement over baselines on the success rate of solving the problems while requiring up to 30% fewer actions."

- **strength**: A simpler evaluation largely removes the composition advantage and finds broadly competitive atomic tool-use performance across models.
  - Page 4 · citation: whitespace
  - Quote: "For most LLMs, CodeAct achieves comparable or better performance even in atomic actions (the simplistic tool use scenario) where its control and data flow strengths are ablated."

Unresolved questions:

- How robust are the gains on independently developed, real-world tool-use tasks and environments?
- How do execution safety and permission controls affect practical deployment of generated Python actions?
- I inspected pages 1–4 and 12–14, not the complete experimental sections or appendices; benchmark construction, statistical uncertainty, and tuning evaluation remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "20%"}` | Locate comparative evaluation results and their reported magnitude. | 2 matches on pages [1, 3] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect method, benchmarks, and evidence behind comparative performance claims. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 12, "end": 14}` | Check limitations and training-data evaluation claims to calibrate scope. | read pages [12, 13, 14] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.74, "observations": 3}}` | Evidence covers framing, benchmark comparison, and atomic-call evaluation; submit balanced paper assessment. | citation_validation_failed; #3: wrong_page (pages [4]) | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.74, "observations": 3}}` | Correct the third citation to a quote observed on page 3 and resubmit the assessment. | citation_validation_failed; #3: wrong_page (pages [4]) | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.74, "observations": 2}}` | Use only the two citations already validated and remove the mismatched third citation. | review accepted | [event 30](trace.jsonl#L30) |
