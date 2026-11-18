# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**pyagent_react · ok**

5 model calls · 4 reads · 13.15 s · $0.001892

5 decisions · 5 tool calls · 36310 input tokens (26273 cached) · 751 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

WebArena contributes a self-hostable, interactive web environment and 812 high-level tasks spanning several common website domains, with outcome-oriented evaluation rather than action-sequence matching. Its functional validation and reproducibility make it a substantial platform for agent research. Baseline results establish a challenging reference point, though the experiments cover only a small set of text-based agents and the task/evaluation design leaves questions about broader representativeness and evaluator reliability.

- **strength**: The benchmark evaluates whether tasks achieve their intended outcomes, allowing alternative valid action paths instead of requiring a reference sequence.
  - Page 2 · citation: exact
  - Quote: "accommodates a range of potential valid paths to achieve the same goal"

- **strength**: The environment and benchmark have meaningful breadth: 812 tasks are spread across multiple site types, with cross-site tasks included.
  - Page 5 · citation: exact
  - Quote: "We provide a benchmark with 812 test examples"

- **limitation**: The task collection draws on author-led annotation and uses ChatGPT for inspiration, leaving representativeness and possible author/model influence as open questions.
  - Page 6 · citation: exact
  - Quote: "We additionally provided a prompt for the annotators to use to prompt ChatGPT 5 for inspiration."

- **uncertainty**: The reported baseline evidence is narrow: the paper tests two text-based prompting approaches with two model families, so results do not establish performance across other agent designs or observation modalities.
  - Page 9 · citation: exact
  - Quote: "We design two LLM-prompt-based web agents as our baselines"

Unresolved questions:

- How well do the author-curated intents represent the diversity and frequency of real users’ web tasks?
- How robust are the fuzzy-match evaluations that rely on a GPT-3.5 judge, including across paraphrases and judge errors?
- Would the conclusions about agent difficulty hold for visual observations, other action interfaces, or stronger and more varied agent architectures?
- I inspected the abstract, environment and task design, evaluation details, baseline setup, and selected results/error analysis; I did not inspect the appendices or the full task set, so deployment and annotation details remain uncertain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark construction and environment design. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect task benchmark design and evaluation criteria. | read pages [5, 6, 7] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 10, "end": 12}` | Inspect agent baselines and reported benchmark results. | read pages [10, 11, 12] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 8, "end": 9}` | Inspect agent configurations and quantitative evaluation setup. | read pages [8, 9] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Submit an evidence-based assessment after inspecting benchmark design, evaluation, and results. | review accepted | [event 26](trace.jsonl#L26) |
