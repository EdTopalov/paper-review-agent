# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**baseline · ok**

1 model calls · 0 reads · 6.98 s · $0.000659

1 decisions · 0 tool calls · 36934 input tokens (36931 cached) · 579 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

τ-bench introduces a benchmark for evaluating tool-using agents in multi-turn interactions with simulated users, domain policies, and database APIs. Its end-state evaluation and pass^k metric make task success and consistency measurable across repeated trials. Experiments across two customer-service domains show substantial failures among tested agents, while the paper also identifies limits in user simulation, task curation, and domain coverage.

- **strength**: The benchmark combines user interaction, tool use, policy following, and a state-based measure of task completion, addressing a concrete evaluation need.
  - Page 4 · citation: whitespace
  - Quote: "the final database is identical to the unique ground truth outcome database"

- **strength**: Repeated-trial evaluation provides evidence about consistency, not only average success; the reported results show a clear decline in reliability as trials accumulate.
  - Page 7 · citation: whitespace
  - Quote: "pass^8 drops to < 25%"

- **limitation**: The authors acknowledge that user-simulator behavior and benchmark curation can affect evaluation validity, including ambiguities and bias from tuning instructions against a particular agent.
  - Page 9 · citation: not_found
  - Quote: "there is also some element of implicit bias during the task curation process"

- **uncertainty**: The demonstrated domains are customer service retail and airline tasks; how well the benchmark design and measured challenges generalize to other real-world domains remains unresolved.
  - Page 5 · citation: exact
  - Quote: "we modularly construct two domains, τ-retail and τ-airline."

Unresolved questions:

- How closely do the simulated users’ utterances and behavior match interactions with real users, and would conclusions about agent reliability persist with human participants?
- How sensitive are model rankings and pass^k results to changes in user-simulator model, sampling settings, and task curation?
- Do the benchmark’s state-based outcomes and policy checks capture important interaction failures that do not change database state?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
