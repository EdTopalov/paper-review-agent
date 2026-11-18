# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**pyagent_react · ok**

8 model calls · 4 reads · 31.08 s · $0.002959

8 decisions · 7 tool calls · 60347 input tokens (50237 cached) · 2387 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

WebArena contributes a self-hostable, multi-site web environment and an 812-task benchmark that evaluates task outcomes rather than requiring agents to match reference action sequences. Its realistic interaction design and reproducible setup are valuable for studying web agents, and baseline results demonstrate that the included long-horizon tasks challenge the tested systems. The evidence supports a substantial benchmark contribution, while the results characterize a narrow set of text-based baselines rather than the broader agent landscape.

- **strength**: The benchmark evaluates high-level natural-language commands as concrete web interactions and includes programmatic outcome validation.
  - Page 2 · citation: whitespace
  - Quote: "WebArena introduces a benchmark on interpreting high-level realistic natural language command to concrete web-based interactions."

- **strength**: The benchmark is sizeable and tasks are instantiated from templates, with coverage across multiple task types and sites.
  - Page 7 · citation: exact
  - Quote: "In total, we curated 241 templates and 812 instantiated intents."

- **limitation**: The reported baseline comparison is narrow: the paper describes two text-prompted agents, leaving multimodal and other approaches for future study.
  - Page 9 · citation: whitespace
  - Quote: "As part of our future research, we intend to explore the possibility of multi-modal agents that accept image-based observations and perform pixel-based actions."

- **uncertainty**: Some information-seeking judgments rely on an LM-based fuzzy-match evaluator; the inspected pages do not establish how robust its judgments are to evaluator errors.
  - Page 7 · citation: whitespace
  - Quote: "in this work, we usegpt-3.5-turbo-0613 to assess whether ˆa could entail each of the key concepts in a∗"

Unresolved questions:

- How well do task coverage and difficulty generalize beyond the authors’ browser-history analysis and the particular sites and user profiles selected?
- How sensitive are benchmark scores to evaluator errors for fuzzy-match tasks and to the choices made in programmatic task checks?
- How would agents using screenshots, different models, or approaches beyond the two reported prompt baselines perform?
- Inspection was limited to pages 1–11 and selected sections; the later error analysis and appendices were not reviewed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the environment design and benchmark construction. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Inspect task evaluation and agent results. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 5, "end": 7}` | Inspect task composition and benchmark annotation details. | read pages [5, 6, 7] | [event 20](trace.jsonl#L20) |
| 5 | search_paper `{"query": "limitations"}` | Check whether the paper states scope limitations. | 2 matches on pages [2, 11] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Submit an assessment grounded in the inspected environment, benchmark, and baseline pages. | citation_validation_failed; #1: not_found | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Replace the quote that failed validation with an exact excerpt from inspected page 3. | citation_validation_failed; #1: wrong_page (pages [2]) | [event 35](trace.jsonl#L35) |
| 8 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Use a quote validated against the inspected page 2 excerpt. | review accepted | [event 40](trace.jsonl#L40) |
