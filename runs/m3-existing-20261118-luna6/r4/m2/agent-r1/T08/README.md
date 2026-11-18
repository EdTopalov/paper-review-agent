# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**agent · ok**

4 model calls · 3 reads · 10.66 s · $0.001438

4 decisions · 4 tool calls · 20305 input tokens (11802 cached) · 540 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

τ-bench contributes a modular benchmark for evaluating tool-using agents in multi-turn simulated user interactions under domain policies, with database-state evaluation and a pass^k reliability metric. Experiments across two customer-service domains show substantial baseline failures and inconsistency, making a useful empirical case for stronger interaction and rule-following methods.

- **strength**: The benchmark joins tool interaction, user dialogue, and domain policies, with explicit annotations for evaluating the final outcome.
  - Page 3 · citation: whitespace
  - Quote: "The agent interacts with both (1) databases (db) via API tools, and (2) a (simulated) user (user) to complete a task"

- **strength**: The paper proposes pass^k to measure consistency across repeated trials, and reports a notable reliability drop for the strongest tested retail agent.
  - Page 7 · citation: whitespace
  - Quote: "pass^8 drops to < 25%."

- **limitation**: The initial benchmark scope is deliberately narrow: two customer-service domains with simplified schemas, APIs, and rules.
  - Page 6 · citation: whitespace
  - Quote: "Each τ-bench domain’s data schemas, APIs, and rules are simplified compared to real-world domains"

- **uncertainty**: The reward combines exact database outcomes with required user-facing content; the paper itself notes that database success alone may not establish policy compliance. I inspected only the opening and pages 2–7, so later validation and broader methodological details remain unassessed.
  - Page 4 · citation: whitespace
  - Quote: "r = 1 might be a necessary but not sufficient condition for a successful episode"

Unresolved questions:

- How well do the simulated-user interactions and task outcomes correspond to real users and deployment settings?
- How much do the conclusions depend on the chosen domains, model configurations, and policy/task construction process?
- What validation or analysis in the uninspected remainder addresses reward fidelity and annotation quality?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "pass^k"}` | Locate the benchmark reliability results and metric definition. | 8 matches on pages [1, 2, 4, 5, 6] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark design, evaluation choices, and stated limitations. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Review dataset scope and experimental methodology/results for support and limitations. | read pages [5, 6, 7] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Evidence covers benchmark framing, construction, evaluation and core results; submit a scored assessment while noting uninspected sections. | review accepted | [event 20](trace.jsonl#L20) |
