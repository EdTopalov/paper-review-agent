# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**pyagent_react · ok**

6 model calls · 4 reads · 25.28 s · $0.002647

6 decisions · 6 tool calls · 49469 input tokens (38247 cached) · 1725 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

τ-bench introduces a benchmark for evaluating tool-using agents in simulated multi-turn user interactions under domain-specific policies. Its main contributions are database-state evaluation and pass^k, a measure of success consistency across repeated trials. Results across two customer-service domains show substantial baseline failure and declining reliability across trials. This is a useful evaluation contribution, while its synthetic domain scope and LM-simulated users bound what the results establish.

- **strength**: The database-state reward offers a concrete evaluation target for varied dialogue trajectories, while the paper recognizes that it does not capture every policy violation.
  - Page 4 · citation: whitespace
  - Quote: "the final database is identical to the unique ground truth outcome database"

- **strength**: The experiments support the benchmark’s ability to expose low task success and inconsistency across repeated trials.
  - Page 7 · citation: whitespace
  - Quote: "pass^8 drops to < 25%."

- **limitation**: The authors note that task annotation is difficult, requiring domain expertise. This is a stated scope concern, not evidence that the annotations are defective.
  - Page 9 · citation: whitespace
  - Quote: "The manual annotation process for the benchmark is difficult"

- **limitation**: The evaluation covers two deliberately simplified customer-service domains; the paper presents more complex domains as future work, so results do not establish performance across real-world sectors generally.
  - Page 5 · citation: whitespace
  - Quote: "more advanced domains (e.g., medical, tax, or legal) with more complex data and rules can be studied."

Unresolved questions:

- How well do benchmark scores predict agent performance with real users and operational tools, rather than LM-simulated users and synthetic databases?
- How robust are the findings to alternative task-construction procedures and broader domain coverage?
- I inspected the abstract, benchmark description, selected experimental results, and discussion of limitations, but not the appendices’ full task examples, all experimental details, or implementation; these may clarify annotation reliability and evaluation edge cases.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark construction and task design. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect benchmark scope and task statistics. | read pages [5, 6, 7] | [event 11](trace.jsonl#L11) |
| 3 | search_paper `{"query": "limitations"}` | Locate the authors’ explicit scope caveats. | 3 matches on pages [9, 12, 35] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 8, "end": 9}` | Inspect interpretation of failures and stated limitations. | read pages [8, 9] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Submit an evidence-based assessment from the inspected benchmark, results, and limitation pages. | citation_validation_failed; #3: not_found | [event 26](trace.jsonl#L26) |
| 6 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Replace the failed quotation with a short exact excerpt from the inspected discussion page. | review accepted | [event 31](trace.jsonl#L31) |
