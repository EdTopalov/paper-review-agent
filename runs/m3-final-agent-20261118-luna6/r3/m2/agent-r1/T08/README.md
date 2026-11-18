# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**agent · ok**

6 model calls · 4 reads · 15.42 s · $0.002338

6 decisions · 6 tool calls · 45138 input tokens (33268 cached) · 1080 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

τ-bench introduces a modular benchmark for evaluating agents in simulated user conversations involving domain policies and API tools, with database-state-based task scoring and pass^k for repeated-trial reliability. Experiments across retail and airline tasks show substantial failures and inconsistency among tested agents. The contribution is useful and well evidenced within its deliberately simplified customer-service scope, while simulator and curation validity remain important caveats.

- **strength**: The benchmark combines interactive user simulation, APIs, domain policies, and objective database-state scoring, providing an evaluation setup for capabilities not captured by single-turn tool calls.
  - Page 3 · citation: exact
  - Quote: "the agent has to interact with human users to gather information and authorization."

- **strength**: Repeated-trial reliability is an explicit contribution, and the reported model results show meaningful performance gaps and instability.
  - Page 7 · citation: whitespace
  - Quote: "Even for the best-performing gpt-4o function calling agent which has a > 60% average task success, pass^8 drops to < 25%."

- **limitation**: Domain coverage is intentionally restricted to two simplified customer-service domains; the authors identify more complex domains as future scope.
  - Page 5 · citation: whitespace
  - Quote: "For more capable agents in the future, more advanced domains (e.g., medical, tax, or legal) with more complex data and rules can be studied."

- **limitation**: The paper acknowledges simulator weaknesses and possible curation bias, which constrain how directly benchmark outcomes generalize to real users and domains.
  - Page 9 · citation: whitespace
  - Quote: "some element of implicit bias during the task curation process since we use the gpt-4-turbo FC agent to tune the user’s system prompt."

Unresolved questions:

- How well do benchmark outcomes predict performance with real human users and production systems?
- How sensitive are rankings and pass^k estimates to alternative user simulators, task curation procedures, and expanded domains?
- I inspected pages 1–9, not the appendices or the remaining paper; detailed task-level validation and full experimental protocols remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "pass^k"}` | Locate the benchmark's evaluation definition and empirical results. | 8 matches on pages [1, 2, 4, 5, 6] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark design, reward validation, and metric rationale. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Review benchmark task coverage and experimental setup/limitations. | read pages [5, 6, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 9}` | Inspect authors' stated limitations and broader validity discussion. | read pages [8, 9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Evidence covers benchmark construction, evaluation, results, and stated limitations; submit independent assessment. | citation_validation_failed; #4: not_found | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Correct the final limitation citation using exact text observed on page 9. | review accepted | [event 30](trace.jsonl#L30) |
