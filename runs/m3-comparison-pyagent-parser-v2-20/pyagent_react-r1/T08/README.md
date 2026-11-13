# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**pyagent_react · ok**

5 model calls · 2 reads · 19.93 s · $0.001867

5 decisions · 4 tool calls · 18931 input tokens (10651 cached) · 1452 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

τ-bench contributes a benchmark for evaluating language agents in simulated user-and-tool conversations under domain policies, with database-state goal checking and pass^k for consistency across trials. Its retail and airline tasks expose meaningful failures in task completion and rule following, supporting its value as a diagnostic benchmark. The paper also identifies limitations in user simulation and task curation, so its findings should not be treated as a complete measure of real-world agent reliability.

- **strength**: The benchmark proposes an explicit metric for assessing reliability across repeated trials.
  - Page 1 · citation: whitespace
  - Quote: "We also propose a new metric (pass^k) to evaluate the reliability of agent behavior over multiple trials."

- **strength**: The policy-removal comparison suggests domain complexity affects how much agents benefit from policy guidance.
  - Page 8 · citation: whitespace
  - Quote: "removing the policy hurts gpt-4o significantly (−22.4%)"

- **limitation**: The authors acknowledge possible user-simulator limitations in reasoning, calculation, memory, and alignment.
  - Page 9 · citation: exact
  - Quote: "the user simulation LM might have limited capacity at reasoning, calculation, long-"

- **limitation**: The authors note a potential task-curation bias and suggest other approaches for future work.
  - Page 9 · citation: whitespace
  - Quote: "Future work can investigate alternative ways of using LMs for improving data curation and user simulation."

Unresolved questions:

- How well do the simulated users and the two domains represent real users, policies, and operational environments beyond these benchmark tasks?
- How sensitive are agent comparisons to alternative user simulators and task-curation procedures?
- I inspected the abstract, search excerpts, and pages 8–9, not the full paper; benchmark-construction details and the broader experimental setup remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | search_paper `{"query": "pass^k"}` | Inspect the benchmark’s reliability metric and reported experimental evidence. | 8 matches on pages [1, 2, 4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 9}` | Inspect reported benchmark results and evaluation details. | read pages [8, 9] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Submit an evidence-based assessment using the inspected abstract, results, and stated limitations. | citation_validation_failed; #4: not_found | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Resubmit with short verbatim excerpts copied exactly from the observed pages. | review accepted | [event 27](trace.jsonl#L27) |
