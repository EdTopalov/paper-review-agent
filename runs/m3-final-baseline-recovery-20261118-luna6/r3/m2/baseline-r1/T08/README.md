# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**baseline · ok**

1 model calls · 0 reads · 7.59 s · $0.000676

1 decisions · 0 tool calls · 36934 input tokens (36931 cached) · 612 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

τ-bench introduces a benchmark for evaluating tool-using agents in multi-turn interactions with simulated users, domain policies, and database APIs. It contributes two customer-service domains, end-state-based task evaluation, and pass^k to measure consistency across repeated trials. Baseline experiments show substantial failures in task completion and reliability, while the paper also identifies important limits of its simulator and evaluation.

- **strength**: The benchmark combines user interaction, API use, and domain-specific rule following, and evaluates task outcomes against annotated database states.
  - Page 4 · citation: whitespace
  - Quote: "the final database is identical to the unique ground truth outcome database"

- **strength**: The repeated-trial reliability metric adds a useful evaluation perspective beyond average single-trial success, and the experiments demonstrate a marked consistency gap.
  - Page 7 · citation: whitespace
  - Quote: "pass^8 drops to < 25%"

- **limitation**: The authors acknowledge that simulator behavior and task curation can affect validity, including instruction ambiguity, limited user-model capability, and possible bias from tuning tasks against one agent.
  - Page 9 · citation: not_found
  - Quote: "there is also some element of implicit bias during the task curation process since we use the gpt-4-turbo FC agent to tune the user’s system prompt."

- **uncertainty**: Database-state matching does not by itself establish that every policy requirement was followed; the paper explicitly notes that an episode can receive reward 1 despite a policy violation. The inspected results do not establish how often this gap affects reported scores.
  - Page 4 · citation: whitespace
  - Quote: "r = 1 might be a necessary but not sufficient condition for a successful episode"

Unresolved questions:

- How well do benchmark results and pass^k rankings generalize to real users, whose behavior may differ from the LM simulator?
- How often do database-state successes conceal policy violations, and how would adding rule-following checks change the reported results?
- How robust are the task annotations and outcome uniqueness beyond the manual validation process described?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
