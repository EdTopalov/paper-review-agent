# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**baseline · ok**

1 model calls · 0 reads · 5.53 s · $0.002287

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

WebArena contributes a self-hosted, interactive web environment and an 812-task benchmark for evaluating agents on realistic, multi-step web tasks. Its functional outcome checks and diverse applications make it a useful infrastructure contribution; the baseline results also expose substantial agent difficulties. Evidence is strongest for the environment and benchmark design, while the reported agent evaluation is limited in breadth.

- **strength**: The benchmark combines realistic natural-language tasks with outcome-oriented evaluation that can accept different valid action paths.
  - Page 2 · citation: whitespace
  - Quote: "This evaluation is not only more reliable [40, 5, 33] than comparing the vanilla action sequences"

- **strength**: The environment supports varied observations, multi-tab browsing, and interactive actions, offering a concrete platform for agent development.
  - Page 4 · citation: whitespace
  - Quote: "WebArena is the first web environment to consider multi-tab web-based tasks"

- **strength**: The authors report low baseline success and characterize specific failure patterns, giving the benchmark an initial diagnostic use beyond a headline score.
  - Page 10 · citation: not_found
  - Quote: "the agent erroneously identifies approximately 54.9% of feasible tasks (428 tasks) as impossible"

- **limitation**: The baseline evidence is narrow: the reported comparison covers two prompt styles and two model versions, with the direct agent evaluated only using GPT-3.5.
  - Page 9 · citation: exact
  - Quote: "Direct gpt-3.5 7.14"

Unresolved questions:

- How well do the benchmark tasks and site data represent web tasks beyond the four selected application categories and the authors’ browser-history analysis?
- How reliable and reproducible are the fuzzy-match judgments and task-specific programmatic evaluators across all benchmark items?
- How sensitive are the baseline success rates to prompt choices, sampling variability, and the 30-transition cap?
- This assessment is based on the supplied pages; I did not inspect additional supplementary materials beyond the included appendix excerpt.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes high-level natural-language tasks and functional-correctness checks that assess outcomes rather than matching action sequences, allowing alternative valid paths (PDF p. 2).
- Observation 2: **supported** — The environment supports observations as HTML, screenshots, or accessibility trees, includes multi-tab browsing and interactive actions, and is presented as a platform for agent development (PDF pp. 2, 4–5).
- Observation 3: **supported** — The authors report low success rates and analyze distinct failure patterns, including erroneous infeasibility judgments and observation-interpretation failures, giving the results diagnostic value (PDF pp. 9–11).
- Observation 4: **supported** — The results compare direct and reasoning prompt styles; the direct agent is reported with GPT-3.5, while the reasoning agent is reported with GPT-3.5 and GPT-4 (PDF p. 9).

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
