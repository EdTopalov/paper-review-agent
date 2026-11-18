# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**pyagent_react · ok**

7 model calls · 4 reads · 17.13 s · $0.001986

7 decisions · 5 tool calls · 45012 input tokens (35267 cached) · 832 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

τ-bench introduces a modular benchmark for evaluating language agents in multi-turn user interaction while using domain APIs and following policy rules. Its two customer-service domains, state-based task evaluation, and pass^k reliability metric provide a useful, challenging evaluation setup, with comparisons across models and methods. The study is bounded by its small set of simplified domains and relies on LM-simulated users and manually curated tasks; the authors discuss these constraints directly.

- **strength**: The benchmark combines simulated user interaction, API use, and domain policies, addressing a broader task setting than single-turn tool use.
  - Page 2 · citation: whitespace
  - Quote: "τ-bench aims to unify both under realistic settings, while also testing how well agents can follow domain-specific policies in a consistent manner."

- **strength**: The paper operationalizes repeated-trial reliability with a metric suited to tasks where consistent success matters, and reports substantial degradation across trials.
  - Page 4 · citation: whitespace
  - Quote: "we propose a new metric – pass^k (pass hat k), defined as the chance that all k i.i.d. task trials are successful, averaged across tasks."

- **strength**: The benchmark includes a broad set of model comparisons and reports low success on the more challenging airline domain; the paper also analyzes failure types and policy removal.
  - Page 7 · citation: exact
  - Quote: "even gpt-4o solves only 35.2% of the tasks."

- **limitation**: The evaluated domains are simplified and limited to retail and airline; broader transfer to more complex application domains remains unestablished.
  - Page 5 · citation: whitespace
  - Quote: "We choose these two domains as they are relatively easy to synthesize data (e.g., products, prices, flights) and craft policies (e.g., product return, baggage allowance) based on common sense"

Unresolved questions:

- How well do pass^k results and agent rankings transfer to additional domains, less simplified policies, and interactions with real users?
- How sensitive are benchmark outcomes to the choice and behavior of the user-simulation model, beyond the limitations and example cases discussed by the authors?
- I inspected the abstract, benchmark description, construction, selected experiments, and the stated limitations; I did not inspect the appendices or full task-level results, so annotation details and per-task variance remain uncertain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark construction, evaluation, and task coverage. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 5, "end": 7}` | Inspect benchmark size, evaluation procedures, and reported experimental evidence. | read pages [5, 6, 7] | [event 19](trace.jsonl#L19) |
| 5 | search_paper `{"query": "Limitations"}` | Locate the authors’ stated scope limits and caveats. | 3 matches on pages [9, 12, 35] | [event 24](trace.jsonl#L24) |
| 6 | read_pages `{"start": 8, "end": 9}` | Review analysis caveats and the authors’ limitations discussion. | read pages [8, 9] | [event 29](trace.jsonl#L29) |
| 7 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Submit an evidence-based assessment of benchmark contribution, empirical support, and disclosed limitations. | review accepted | [event 34](trace.jsonl#L34) |
