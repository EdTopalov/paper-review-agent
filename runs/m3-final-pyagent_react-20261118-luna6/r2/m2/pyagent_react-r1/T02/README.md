# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**pyagent_react · ok**

7 model calls · 5 reads · 20.08 s · $0.003092

7 decisions · 7 tool calls · 48212 input tokens (31841 cached) · 1456 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Reflexion adds a memory-and-reflection loop to an LLM agent: after failure, the agent reflects on its trajectory and binary reward, stores a reflection, and retries. The paper offers promising demonstrations that this can improve performance across trials in AlfWorld and HotPotQA, with an informative negative result in WebShop. The idea is clear and practically motivated, but the inspected evidence is benchmark-specific and does not establish broad, controlled generality.

- **strength**: The method is concrete and relatively simple: a heuristic triggers reflection, which is stored for a subsequent trial. This makes the proposed mechanism understandable and applicable to an existing agent approach.
  - Page 3 · citation: whitespace
  - Quote: "In this study, we do not learn a policy over a state space."

- **strength**: In AlfWorld, the authors report substantial improvement over the initial attempt and distinguish learning across trials from simply retrying.
  - Page 5 · citation: exact
  - Quote: "the agent used ReAct to solve 97% of the given environments in 12 trials"

- **strength**: The HotPotQA comparison is useful evidence that reflection can help beyond the interactive household setting, while specifying the evaluation size and baseline behavior.
  - Page 6 · citation: whitespace
  - Quote: "the Reﬂexion agent achieved 32% accuracy in the ﬁrst trials"

- **limitation**: The paper reports a weak WebShop outcome and attributes it partly to tool-result quality, showing that improved reasoning and reflection do not necessarily overcome external bottlenecks.
  - Page 10 · citation: whitespace
  - Quote: "The agent achieved a 33% → 34% accuracy improvement in the baseline run and a mere33% → 35% accuracy improvement in the Reﬂexion run"

Unresolved questions:

- How robust are the gains across additional models, tasks, and repeated evaluation runs? The inspected results do not establish that breadth.
- How much of the gains depends on the particular prompts, heuristics, and reflection examples, compared with the memory-and-reflection mechanism itself?
- I inspected pages 3–11, including the method, benchmark results, discussion, and limitations; I did not inspect pages 1–2 or 12–17, including the appendices, so details such as the full prompts and any additional evidence remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 3, "end": 5}` | Inspect the proposed reflection loop and benchmark evaluation details. | read pages [3, 4, 5] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 6, "end": 7}` | Inspect HotPotQA results and the authors’ interpretation of the evaluation. | read pages [6, 7] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 8, "end": 9}` | Inspect stated limitations and further experimental qualifications. | read pages [8, 9] | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "single model"}` | Check whether the paper discusses model and evaluation scope limitations. | 0 matches | [event 21](trace.jsonl#L21) |
| 5 | read_pages `{"start": 10, "end": 11}` | Inspect closing discussion for explicit scope limits and future questions. | read pages [10, 11] | [event 26](trace.jsonl#L26) |
| 6 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit an assessment grounded in the inspected method, results, and limitations pages. | citation_validation_failed; #1: not_found | [event 32](trace.jsonl#L32) |
| 7 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Resubmit with the first observation quoting exact text from inspected page 3. | review accepted | [event 38](trace.jsonl#L38) |
