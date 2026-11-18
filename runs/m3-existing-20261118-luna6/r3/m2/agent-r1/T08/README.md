# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**agent · ok**

8 model calls · 4 reads · 20.97 s · $0.003087

8 decisions · 8 tool calls · 68980 input tokens (56248 cached) · 1917 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

τ-bench contributes a concrete evaluation framework for agents that must converse with users, call domain APIs, and follow policies. Its database-state scoring and pass^k reliability measure expose weaknesses in tested agents, while simulated users and narrow, manually curated domains limit direct transfer to deployment.

- **strength**: The benchmark combines interactive user simulation, API-backed state, domain policies, and annotated task outcomes, enabling evaluation beyond single-turn tool calls.
  - Page 3 · citation: whitespace
  - Quote: "The agent interacts with both (1) databases (db) via API tools, and (2) a (simulated) user (user) to complete a task"

- **strength**: The proposed pass^k metric captures consistency across repeated stochastic conversations, complementing average success.
  - Page 4 · citation: whitespace
  - Quote: "defined as the chance that all k i.i.d. task trials are successful, averaged across tasks."

- **strength**: Experiments report meaningful policy sensitivity, with a significant reported effect in the airline domain.
  - Page 8 · citation: exact
  - Quote: "removing the policy hurts gpt-4o significantly"

- **limitation**: The authors identify prompt tuning with a single agent as a possible source of curation bias, a scope concern rather than demonstrated invalidity.
  - Page 9 · citation: whitespace
  - Quote: "some element of implicit bias during the task curation process"

Unresolved questions:

- How well do the two manually simplified domains and simulated users predict performance with diverse real users and operational systems?
- How sensitive are agent rankings and pass^k estimates to user-simulator choice, sampling settings, and alternative policy-compliance evaluators?
- I inspected pages 1, 3–5, and 8–9; detailed model comparisons and portions of the methodology and appendices remain uninspected.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "pass^k"}` | Locate the benchmark metric definition and reported reliability results. | 8 matches on pages [1, 2, 4, 5, 6] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 5}` | Inspect evaluation design, metric formulation, and benchmark construction details. | read pages [3, 4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Inspect empirical benchmark results and stated limitations for support and scope. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Evidence covers benchmark design, metric, empirical outcomes, and authors' stated limitations; submit independent assessment. | citation_validation_failed; #4: not_found | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 9, "end": 9}` | Verify an exact limitation quote on the cited discussion page. | read pages [9] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Submit corrected exact citation after verifying limitation text; assessment is otherwise supported by observed pages. | citation_validation_failed; #4: not_found | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Resubmit with exact quotation copied from the observed page text and otherwise retained findings. | citation_validation_failed; #4: not_found | [event 35](trace.jsonl#L35) |
| 8 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Submit final review with verified verbatim quotes from observed pages, correcting the limitation quote to an exact continuous span. | review accepted | [event 40](trace.jsonl#L40) |
