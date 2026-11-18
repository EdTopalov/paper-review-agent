# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**agent · ok**

5 model calls · 3 reads · 13.22 s · $0.002045

5 decisions · 5 tool calls · 30690 input tokens (19803 cached) · 1003 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

τ-bench contributes a benchmark for evaluating tool-using agents in simulated multi-turn user interactions under domain policies, with task success judged from target database outcomes and a proposed pass^k measure of consistency. Its two customer-service domains and model comparisons reveal substantial weaknesses in current agents, while its small, deliberately simplified domain scope limits claims about real-world deployment.

- **strength**: The benchmark combines simulated user interaction, APIs, policy guidance, and an end-state measure in a coherent task design.
  - Page 2 · citation: whitespace
  - Quote: "Our evaluation scheme compares the database state at the end of each episode with the ground truth expected state."

- **strength**: The authors report manual task validation and demonstrate broad performance gaps, including low success on airline tasks.
  - Page 5 · citation: whitespace
  - Quote: "we run each τ-retail task with > 40 gpt-4-turbo trials and check all tasks with zero or low success rates"

- **limitation**: The first release is limited to two domains whose databases, APIs, and rules are simplified; findings therefore do not establish performance in more consequential or varied sectors.
  - Page 6 · citation: whitespace
  - Quote: "Each τ-bench domain’s data schemas, APIs, and rules are simplified compared to real-world domains"

- **uncertainty**: The inspected material describes simulated users and rule-based rewards, but does not establish how well their behavior and success criteria represent real customers or service outcomes; later validation sections were not inspected.
  - Page 3 · citation: whitespace
  - Quote: "We use a language model (gpt-4-0613) to simulate a human user interacting with the agent."

Unresolved questions:

- How well do the simulated user distributions and annotated goals align with real customer interactions and expert judgments?
- Do the benchmark’s results generalize to additional domains, stronger agent architectures, or models beyond the tested baselines?
- What validation or limitations are reported in the uninspected later sections, including appendices?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "pass^k"}` | Locate the benchmark reliability metric and supporting results. | 8 matches on pages [1, 2, 4, 5, 6] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark design, task scope, evaluation and reliability metric. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Check dataset scale, curation claims and evaluation caveats. | read pages [5, 6, 7] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Evidence covers benchmark design, curation, scale, and experimental results; submit assessment while noting uninspected later sections. | citation_validation_failed; #1: not_found | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Correct the unverifiable quote using an exact observed benchmark-design excerpt, then finalize. | review accepted | [event 25](trace.jsonl#L25) |
