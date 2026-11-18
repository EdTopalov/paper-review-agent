# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**agent · ok**

5 model calls · 4 reads · 12.41 s · $0.001259

5 decisions · 5 tool calls · 23131 input tokens (16725 cached) · 614 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.77

WebArena contributes a self-hostable, realistic multi-site web environment and an 812-task benchmark that evaluates functional outcomes rather than action-sequence imitation. Its initial agent results establish a useful challenging baseline, though the paper’s evidence is primarily environment and benchmark construction plus a small set of LLM baselines, not evidence that the environment fully predicts performance on live web tasks.

- **strength**: The benchmark targets diverse, long-horizon task execution across self-hosted web applications, tools, and knowledge resources, and checks task outcomes rather than requiring a single action path.
  - Page 2 · citation: exact
  - Quote: "We focus on evaluating the functional correctness of these tasks"

- **strength**: The evaluation pipeline has explicit annotation safeguards: information-seeking references receive duplicate annotation with a third adjudicator for disagreements, and programmatic checks are built from task executions.
  - Page 8 · citation: whitespace
  - Quote: "If the two annotators disagreed, a third annotator finalized the annotation."

- **limitation**: The selected site categories are grounded in a relatively small, author-derived sample of browsing histories; how representative that sample is remains an open question, not a demonstrated defect.
  - Page 3 · citation: whitespace
  - Quote: "analysis of approximately 200 examples from the authors’ actual web browser histories."

- **uncertainty**: The baseline evidence is narrow: the inspected results compare three prompt-based agents and report low completion rates, but do not establish whether these rates generalize to other agent architectures or observation modes.
  - Page 9 · citation: exact
  - Quote: "The end-to-end task success rate (%) onWebArena."

Unresolved questions:

- How well do benchmark rankings and success rates transfer to live websites or other web environments?
- How robust are the task labels and programmatic evaluators across valid but unanticipated solutions?
- What performance can agents achieve with multimodal observations, stronger exploration, or systematic failure recovery?
- I inspected pages 1–5, 8–9, and a keyword-search result; I did not inspect the full paper, including all dataset analyses and later discussion.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 3}` | Inspect benchmark design and task construction details on the following pages. | read pages [2, 3] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 8, "end": 9}` | Inspect task benchmark composition and validation methodology. | read pages [8, 9] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Check the paper’s stated limitations and scope boundaries before scoring. | 2 matches on pages [2, 11] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 4, "end": 5}` | Inspect benchmark scale and construction procedure to evaluate evidence and representativeness. | read pages [4, 5] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.77, "observations": 4}}` | Evidence covers the core environment, benchmark construction, and baseline results; submit a scoped assessment noting uninspected sections. | review accepted | [event 25](trace.jsonl#L25) |
