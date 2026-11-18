# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**agent · ok**

6 model calls · 5 reads · 10.86 s · $0.001745

6 decisions · 6 tool calls · 20333 input tokens (9074 cached) · 531 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

WebArena contributes a self-hostable, reproducible web-agent benchmark spanning four operational website domains, utility tools, and knowledge resources, together with 812 natural-language tasks and functional evaluation. Its broad task formulation and evaluators are useful advances over action-sequence matching, and the reported low GPT-4 success rate makes the benchmark a meaningful challenge. The score is provisional because only pages 1–3 and 6–7 were inspected; agent comparisons, broader error analysis, and remaining limitations were not reviewed.

- **strength**: The benchmark evaluates outcomes rather than requiring a single reference action trace, supporting alternative valid ways to complete a task.
  - Page 2 · citation: exact
  - Quote: "We focus on evaluating the functional correctness of these tasks"

- **strength**: The work supplies a substantial collection of instantiated tasks, derived from a larger set of templates.
  - Page 7 · citation: exact
  - Quote: "In total, we curated 241 templates and 812 instantiated intents."

- **limitation**: Some information-seeking answers rely on an LM-based evaluator, so evaluation depends partly on that evaluator’s judgments.
  - Page 7 · citation: whitespace
  - Quote: "we usegpt-3.5-turbo-0613 to assess whether ˆa could entail each of the key concepts in a∗"

Unresolved questions:

- How robust and consistent are the language-model-based fuzzy-match judgments across varied answers?
- How do the agents compare across task categories, and what additional error analysis or limitations are reported on uninspected pages?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper’s stated limitations and scope boundaries. | 2 matches on pages [2, 11] | [event 5](trace.jsonl#L5) |
| 2 | search_paper `{"query": "10.59%"}` | Find benchmark evaluation results and reported agent performance. | 2 matches on pages [1, 2] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 2, "end": 3}` | Inspect benchmark design and task construction details for contribution and evidence. | read pages [2, 3] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "812"}` | Locate task benchmark scale and sampling or validation details. | 4 matches on pages [2, 5, 7, 12] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 6, "end": 7}` | Review task annotation methodology and benchmark evaluation design. | read pages [6, 7] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.78, "observations": 3}}` | The inspected pages establish the environment, task suite, methods, and one important evaluation caveat; submit a provisional evidence-based review. | review accepted | [event 31](trace.jsonl#L31) |
