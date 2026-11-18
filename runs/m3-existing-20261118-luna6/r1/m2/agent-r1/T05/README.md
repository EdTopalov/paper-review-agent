# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**agent · ok**

5 model calls · 4 reads · 10.74 s · $0.001608

5 decisions · 5 tool calls · 24355 input tokens (15019 cached) · 613 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

WebArena contributes a reproducible, self-hostable environment of functional websites and an 812-task benchmark evaluated by task outcome rather than action-sequence imitation. Baseline results establish a challenging starting point, while the paper’s authorship-derived site selection, constrained environment, and narrow baseline study bound what those results show.

- **strength**: The benchmark combines several website domains and supports multi-step interaction across tools and knowledge resources, with an explicit focus on reproducibility.
  - Page 2 · citation: whitespace
  - Quote: "We deliver the hosting services using Docker containers withgym-APIs [4], ensuring both the usability and the reproducibility ofWebArena."

- **strength**: Outcome-based evaluation checks whether tasks achieve their goals and can permit different valid execution paths; the authors describe annotation review procedures.
  - Page 8 · citation: whitespace
  - Quote: "These examples allow us to assess an agent’s ability to avoid making unfounded claims and its adherence to factual accuracy."

- **limitation**: Task categorization is grounded in roughly 200 examples from the authors’ own browser histories, leaving representativeness beyond that source as an open question.
  - Page 3 · citation: whitespace
  - Quote: "we first conducted an analysis of approximately 200 examples from the authors’ actual web browser histories."

- **uncertainty**: The reported baseline comparison is limited to text-based agents using two model versions and a 30-transition cap; results do not establish performance across other agent designs or observation modes.
  - Page 9 · citation: exact
  - Quote: "The maximum number of state transitions is set to 30."

Unresolved questions:

- How representative are the selected tasks and site data of web tasks outside the authors’ browser-history sample?
- How robust are the benchmark scores to alternative valid evaluation implementations, and to agents using screenshot or multimodal observations?
- I inspected pages 1–4, 8–10, and 17–19; other sections, including fuller task statistics and discussion of limitations, were not reviewed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "10.59%"}` | Locate reported benchmark results and evaluation evidence for the paper's central claims. | 2 matches on pages [1, 2] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark construction, task design, and evaluation setup to judge evidence and scope. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Inspect task benchmark and validation procedures, including task diversity and evaluation caveats. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 17, "end": 19}` | Check explicitly stated limitations and discussion of realism or benchmark generalizability. | read pages [17, 18, 19] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Evidence covers the environment and benchmark contribution, validation design, baseline results, and limited inspection of limitations; submit a qualified assessment. | review accepted | [event 25](trace.jsonl#L25) |
