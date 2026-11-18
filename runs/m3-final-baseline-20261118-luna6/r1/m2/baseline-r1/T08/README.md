# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**baseline · ok**

1 model calls · 0 reads · 8.34 s · $0.000667

1 decisions · 0 tool calls · 36934 input tokens (36931 cached) · 594 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

τ-bench introduces a benchmark for evaluating language agents that must interact with simulated users and APIs while following domain policies. Its two customer-service domains pair annotated database outcomes with repeated trials and pass^k to assess both task completion and consistency. Results across a range of models and analyses of failures make a useful case that these settings challenge current agents, though evidence is bounded by the benchmark’s scope and evaluation design.

- **strength**: The benchmark’s modular setup and end-state evaluation provide a concrete, reproducible way to test dynamic user interaction and tool-mediated task completion.
  - Page 4 · citation: whitespace
  - Quote: "the final database is identical to the unique ground truth outcome database"

- **strength**: The experiments include multiple models, domains, and repeated-trial reliability results; the authors also analyze observed failure categories rather than reporting aggregate scores alone.
  - Page 7 · citation: whitespace
  - Quote: "pass^8 drops to < 25%"

- **limitation**: The rule-based reward does not itself verify every policy requirement, so a matching database outcome can miss an important process violation. This is a stated limitation of the measure, not evidence that the reported experiment is invalid.
  - Page 4 · citation: whitespace
  - Quote: "r = 1 might be a necessary but not sufficient condition for a successful episode"

- **uncertainty**: The evaluation covers two constructed customer-service domains, and the paper describes more complex domains as future work. How well the measured performance generalizes to other real-world settings is therefore unresolved by the supplied evidence.
  - Page 5 · citation: whitespace
  - Quote: "more advanced domains (e.g., medical, tax, or legal) with more complex data and rules can be studied"

Unresolved questions:

- How closely do the LM-simulated user behaviors and task distributions represent interactions with real users?
- Would rankings or pass^k trends persist with broader domains and alternative user simulators?
- How much do results change when success measures explicitly check policy compliance and conversation quality, rather than relying primarily on state comparison and required output substrings?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
