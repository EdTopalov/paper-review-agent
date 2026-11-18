# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**agent · ok**

6 model calls · 5 reads · 11.58 s · $0.002914

6 decisions · 6 tool calls · 41841 input tokens (23095 cached) · 718 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

Reflexion presents a simple, model-agnostic trial-loop mechanism that stores verbal self-critiques and uses them to guide later attempts, with a heuristic trigger and binary success feedback. The reported AlfWorld and HotPotQA gains make the approach a useful demonstration of cross-trial improvement, but evidence is limited to selected benchmarks and models, and WebShop shows that reflection does not reliably overcome tool-quality bottlenecks.

- **strength**: The method is clearly specified as a practical addition to an existing agent, using trajectory history and binary outcome feedback to generate and retain reflection.
  - Page 4 · citation: exact
  - Quote: "Finally, we add the reﬂection to the agent’s memory, reset the environment, and start the next trial."

- **strength**: On AlfWorld, the paper reports improvement across trials over a substantial set of 134 tasks, while explicitly framing the result as evidence of learning rather than accuracy from retries alone.
  - Page 5 · citation: whitespace
  - Quote: "Given the ability to reﬂect, the agent used ReAct to solve 97% of the given environments in 12 trials, failing to solve only 4 out of 134 tasks."

- **limitation**: The WebShop result is a meaningful boundary to the positive findings: reflection barely improved accuracy, and the authors attribute failures partly to search-result quality rather than planning alone.
  - Page 10 · citation: whitespace
  - Quote: "The agent achieved a 33% → 34% accuracy improvement in the baseline run and a mere33% → 35% accuracy improvement in the Reﬂexion run"

- **uncertainty**: The experiments inspected use a small number of benchmark settings and GPT-3-series models; the inspected pages do not establish how robust results are across model families or broader tasks.
  - Page 10 · citation: whitespace
  - Quote: "In this study, we used GPT-3.0 and GPT 3.5 to power a ReAct agent (Yao et al., 2023) to learn from its past mistakes."

Unresolved questions:

- How stable are the gains across random seeds, alternative model families, and different prompt/example choices?
- How much of the improvement comes from persistent memory/reflection versus additional attempts and the task-specific heuristic?
- Can the approach improve tasks where success depends strongly on noisy or weak external tools, as the WebShop result raises?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the method and experimental setup/results on early pages to ground the assessment. | read pages [2, 3, 4] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 5, "end": 7}` | Review evaluation details and reported results for both benchmark settings. | read pages [5, 6, 7] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 9}` | Inspect discussion of limitations and implementation constraints to identify explicit scope boundaries. | read pages [8, 9] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "limitations"}` | Check whether the paper explicitly states limitations beyond the inspected discussion. | 2 matches on pages [10] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 10, "end": 10}` | Read the explicit limitations passage and identify any caveats affecting generalization. | read pages [10] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence covers the method, principal benchmark results, and explicit WebShop limitation; submit an independently grounded assessment. | review accepted | [event 31](trace.jsonl#L31) |
