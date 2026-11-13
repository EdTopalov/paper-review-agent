# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**baseline · ok**

1 model calls · 0 reads · 6.46 s · $0.004863

1 decisions · 0 tool calls · 36934 input tokens (0 cached) · 492 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

τ-bench introduces a benchmark for evaluating language agents in multi-turn interactions with simulated users and API tools under domain-specific policies. It contributes two customer-service domains, database-state-based task scoring, and pass^k to measure consistency across repeated stochastic trials. The reported baselines reveal substantial failures and declining reliability, while the paper also identifies limitations in user simulation, task curation, and evaluation scope.

- **strength**: The benchmark combines user interaction, tool use, policy following, and repeat-trial reliability in an evaluation design with explicit task outcomes.
  - Page 4 · citation: whitespace
  - Quote: "the final database is identical to the unique ground truth outcome database"

- **strength**: The experiments report a useful range of model performance and show a clear reliability drop across repeated trials, supporting the benchmark’s motivating concern.
  - Page 7 · citation: whitespace
  - Quote: "pass^8 drops to < 25%"

- **limitation**: The authors acknowledge that matching database state does not fully establish compliant behavior; the formal reward can miss policy violations such as acting without confirmation.
  - Page 4 · citation: whitespace
  - Quote: "r = 1 might be a necessary but not sufficient condition for a successful episode"

- **limitation**: The authors identify possible curation bias because task prompts were tuned using a particular GPT-4-turbo agent, which could influence the benchmark’s task distribution.
  - Page 9 · citation: not_found
  - Quote: "there is also some element of implicit bias during the task curation process"

Unresolved questions:

- How well do pass^k scores and task success transfer from the two synthetic customer-service domains and LM-simulated users to real users or other application domains?
- How much do baseline rankings and reliability estimates vary with user-simulator choice, model/API changes, or broader task sets?
- This assessment is based on the supplied paper pages; I did not inspect external code or run the benchmark, so implementation details and reproducibility are not independently assessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
