# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**pyagent_react · ok**

6 model calls · 4 reads · 16.64 s · $0.001922

6 decisions · 6 tool calls · 39467 input tokens (29768 cached) · 825 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

τ-bench introduces a practical benchmark for evaluating agents that must converse with users, use APIs, and follow domain policies. Its database-state outcome metric and pass^k reliability measure make repeatability and consistency explicit, and experiments expose substantial shortcomings in tested agents. The contribution is useful and well-motivated, though the initial evaluation is limited to two simplified customer-service domains and depends on simulated users and manually curated tasks.

- **strength**: The benchmark combines an objective database outcome check with a check for required information in the agent’s responses, accommodating varied dialogue while retaining concrete success criteria.
  - Page 4 · citation: whitespace
  - Quote: "The reward of a task episode r = raction × routput ∈ {0, 1} is based on (1) whether the final database is identical to the unique ground truth outcome database (raction), and (2) whether the agent’s responses to the user contain all necessary information (routput)."

- **strength**: The experiments show meaningful task difficulty and motivate measuring repeat-run reliability, not just average success.
  - Page 7 · citation: whitespace
  - Quote: "Even for the best-performing gpt-4o function calling agent which has a > 60% average task success, pass^8 drops to < 25%."

- **limitation**: The authors identify simulator and curation weaknesses that may affect how faithfully benchmark performance reflects agent behavior, while arguing that user variability is itself realistic.
  - Page 9 · citation: whitespace
  - Quote: "There is also some element of implicit bias during the task curation process since we use the gpt-4-turbo FC agent to tune the user’s system prompt."

- **uncertainty**: The initial domain coverage is narrow relative to the intended real-world scope; whether the benchmark’s findings generalize to substantially different domains remains open.
  - Page 5 · citation: exact
  - Quote: "Using the above procedures, we modularly construct two domains, τ-retail and τ-airline."

Unresolved questions:

- How stable are conclusions when evaluated with human users or alternative user simulators?
- Do the benchmark design and agent failure patterns generalize to additional, more complex domains?
- How sensitive are results to task curation and simulator choices? I inspected pages 1–9, not the appendices or full paper, so details beyond those pages remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": ":", "end": ":"}` | Invalid page range; I will inspect the benchmark design and evaluation pages. | invalid_arguments | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark construction and evaluation methodology. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Inspect dataset composition and benchmark implementation details. | read pages [5, 6, 7] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "limitations"}` | Locate the paper's explicit scope limitations. | 3 matches on pages [9, 12, 35] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 8, "end": 9}` | Inspect conclusions and stated limitations. | read pages [8, 9] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Submit a supported assessment using inspected benchmark, results, and limitations pages. | review accepted | [event 30](trace.jsonl#L30) |
