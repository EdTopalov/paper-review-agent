# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**agent · ok**

5 model calls · 4 reads · 11.27 s · $0.001595

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

WebArena contributes a self-hostable, dynamic web environment and 812-task benchmark for evaluating end-to-end natural-language web agents across diverse sites and tools. Its deterministic setup and programmatic completion checks make it useful for reproducible agent research; baseline performance and failure analysis illustrate the benchmark's difficulty, though the reported agents and evaluation provide only an initial view of capability.

- **strength**: The environment combines standalone reproducibility with realistic, populated applications and supports multiple observation/action modes.
  - Page 3 · citation: whitespace
  - Quote: "We achieve reproducibility by having the environment be standalone, not relying on live websites."

- **strength**: Evaluation checks intended task outcomes, including both information answers and intermediate execution state, rather than merely action prediction.
  - Page 8 · citation: exact
  - Quote: "We introduce two evaluation approaches."

- **strength**: The paper gives an empirical baseline and concrete failure analysis; the low success rate helps establish task difficulty, but is not itself evidence of agent progress.
  - Page 9 · citation: whitespace
  - Quote: "The reasoning agent powered by GPT-4 achieves a relatively modest end-to-end task success rate of 10.63%."

- **limitation**: The demonstrated agent comparison is narrow: text-only GPT-3.5/GPT-4 baselines with a 30-transition cap, so it does not establish performance across agent architectures or modalities.
  - Page 9 · citation: whitespace
  - Quote: "As part of our future research, we intend to explore the possibility of multi-modal agents that accept image-based observations and perform pixel-based actions."

Unresolved questions:

- How robust are the task annotations and outcome checks across the full benchmark, beyond the described annotation procedure?
- How do agent results change with repeated runs and alternative interaction budgets or observation modalities?
- I inspected pages 3–4 and 8–12 plus search snippets; I did not inspect the full appendix, task distribution details, or implementation/reproduction appendices, so those aspects remain uncertain.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes a standalone environment that avoids live websites and imports real-world data into functional applications (PDF pp. 3–4). It also supports multiple observation formats and different element-selection methods (PDF pp. 4–5).
- Observation 2: **supported** — Evaluation covers textual answers as well as programmatic checks of intermediate states and task outcomes (PDF pp. 7–8).
- Observation 3: **supported** — The paper reports baseline success rates and analyzes failure modes, including mistaken infeasibility judgments and observation errors (PDF pp. 9–10). The low rate supports the benchmark’s difficulty, not a claim of progress. There is a small inconsistency: Table 3 reports 10.59%, while the prose says 10.63% (PDF p. 9).
- Observation 4: **supported** — The evaluated agents are text-based GPT-3.5/GPT-4 baselines, with a 30-transition limit; the paper identifies image-based observations and pixel-based actions as future work (PDF p. 9). Thus these results do not establish performance across other architectures or modalities.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "task success"}` | Locate benchmark evaluation results to assess empirical support. | 7 matches on pages [1, 2, 9, 10, 12] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 4}` | Inspect task construction and environment design claims. | read pages [3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Read benchmark protocol, baseline results, and reported evaluation scope. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 11, "end": 12}` | Inspect discussion and explicit limitations to qualify benchmark conclusions. | read pages [11, 12] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Evidence covers environment construction, task evaluation, baseline results, and discussion; submit with limits of inspected pages noted. | review accepted | [event 25](trace.jsonl#L25) |
