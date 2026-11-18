# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**pyagent_react · ok**

2 model calls · 1 reads · 17.96 s · $0.001019

2 decisions · 2 tool calls · 5736 input tokens (3996 cached) · 1524 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

τ-bench proposes a benchmark for language agents that interact with simulated users, use domain APIs, and follow domain-specific policies. Its database-state evaluator and pass^k metric address task success and consistency across repeated trials. The reported results suggest current agents struggle, making the benchmark useful for research. Assessment is provisional: I have not inspected the full methods, results, or limitations.

- **strength**: The benchmark targets a meaningful evaluation gap by combining user interaction, API tools, and domain policies.
  - Page 1 · citation: whitespace
  - Quote: "a benchmark emulating dynamic conversations between a user (simulated by language models) and a language agent provided with domain-specific API tools and policy guidelines."

- **strength**: The authors define pass^k to assess consistency across repeated trials, not just single-run success.
  - Page 4 · citation: whitespace
  - Quote: "we propose a new metric – pass^k (pass hat k), defined as the chance that all k i.i.d. task trials are successful, averaged across tasks."

- **uncertainty**: The abstract reports low success, but the inspected evidence does not establish how representative the tasks are or how well the simulated interactions and evaluation reflect real-world deployment.
  - Page 1 · citation: whitespace
  - Quote: "even state-of-the-art function calling agents (like gpt-4o) succeed on < 50% of the tasks"

Unresolved questions:

- How representative and challenging are the domains, tasks, policies, and simulated users?
- How sensitive are the results to simulator choices and sampling across repeated trials?
- What validation supports the evaluator’s rule-based judgments and the interpretation of pass^k as real-world reliability?
- Important inspection gap: evidence was limited to the supplied first page and search excerpts; I did not inspect the full methods, detailed experimental results, or limitations.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "pass^k"}` | Locate the benchmark metric definition and reported reliability results. | 8 matches on pages [1, 2, 4, 5, 6] | [event 6](trace.jsonl#L6) |
| 2 | submit_review `{"review": {"score": 0.68, "observations": 3}}` | Assess the benchmark’s stated contribution and metric, while acknowledging that detailed methods and experiments remain uninspected. | review accepted | [event 11](trace.jsonl#L11) |
