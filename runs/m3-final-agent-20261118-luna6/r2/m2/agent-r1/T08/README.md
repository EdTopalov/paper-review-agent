# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**agent · ok**

6 model calls · 5 reads · 11.80 s · $0.002430

6 decisions · 6 tool calls · 30804 input tokens (14919 cached) · 628 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.77

τ-bench introduces a modular benchmark for evaluating tool-using agents in multi-turn interaction with simulated users, domain APIs, and policy rules. It pairs end-state and response checks with a pass^k reliability measure, and reports substantial failures and inconsistency in tested agents across retail and airline tasks. The contribution is useful and well-motivated, though it is an initial customer-service benchmark whose simulator, curation, and success criteria have acknowledged limitations.

- **strength**: The benchmark combines user interaction, API use, and policy following, and reports concrete shortcomings in evaluated agents.
  - Page 2 · citation: whitespace
  - Quote: "even state-of-the-art LMs like gpt-4o achieve low task success rates (pass^1) using function calling (∼61% on τ-retail and ∼35% on τ-airline)."

- **strength**: The end-state reward and pass^k metric provide an operational way to evaluate task completion and consistency over stochastic conversations.
  - Page 4 · citation: whitespace
  - Quote: "pass^k (pass hat k), defined as the chance that all k i.i.d. task trials are successful, averaged across tasks."

- **limitation**: The paper explicitly recognizes that simulated users, annotation, and curation can constrain evaluation fidelity.
  - Page 9 · citation: whitespace
  - Quote: "There is also some element of implicit bias during the task curation process since we use the gpt-4-turbo FC agent to tune the user’s system prompt."

Unresolved questions:

- How well do these two customer-service domains and LM-simulated users represent interaction patterns in other real-world domains or with human users?
- How sensitive are the benchmark conclusions to alternative task curation, user simulators, and success checks beyond database state and required output substrings?
- I inspected the benchmark construction, reported findings, and discussion of limitations, but not the full experimental setup, all task examples, or appendices; those details could affect assessment of coverage and reproducibility.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Limitations"}` | Locate the authors' stated scope and limitations for a balanced assessment. | 3 matches on pages [9, 12, 35] | [event 5](trace.jsonl#L5) |
| 2 | search_paper `{"query": "pass^k"}` | Inspect the benchmark's reliability metric and empirical results. | 8 matches on pages [1, 2, 4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 2, "end": 4}` | Read benchmark design, evaluation choices, and metric definition directly. | read pages [2, 3, 4] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "simulated user"}` | Check discussion of simulation limitations and benchmark scope. | 4 matches on pages [2, 4, 9] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 8, "end": 9}` | Read empirical conclusions and explicit limitations before scoring. | read pages [8, 9] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.77, "observations": 3}}` | Evidence covers the benchmark design, reported results, and author-stated limitations; finalize an evidence-based score. | review accepted | [event 31](trace.jsonl#L31) |
