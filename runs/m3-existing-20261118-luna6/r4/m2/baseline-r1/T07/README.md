# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**baseline · ok**

1 model calls · 0 reads · 8.83 s · $0.000725

1 decisions · 0 tool calls · 38684 input tokens (38681 cached) · 675 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

OSWorld contributes an interactive, VM-based desktop benchmark and reusable environment for evaluating computer agents on open-ended tasks across applications and interfaces. Its 369 Ubuntu tasks pair configurable starting states with task-specific execution-based evaluators; experiments document a large gap between the tested agents and human participants. The breadth of the task suite, infrastructure, and behavioral analyses make this a substantial benchmark contribution, while the evaluation and platform coverage remain bounded by the authors’ choices.

- **strength**: The benchmark combines realistic starting states with custom executable checks, supporting reproducible evaluation across varied task outcomes.
  - Page 7 · citation: not_found
  - Quote: "each example is carefully annotated with a natural language instruction, a setup configuration with corresponding files and setup actions for initialization of initial states upon our provided VM image, and a manually crafted evaluation script"

- **strength**: The reported results expose substantial deficiencies in the evaluated agents and include a human comparison.
  - Page 10 · citation: exact
  - Quote: "Human Performance 75.00% 71.79% 70.51% 73.47% 73.27% 72.36%"

- **limitation**: The main benchmark is concentrated on Ubuntu; Windows coverage is much smaller, and macOS is not represented in the task suite described here.
  - Page 6 · citation: not_found
  - Quote: "We introduce the OSWORLD benchmark, which encompasses 369 real computing tasks defined and executed on Ubuntu. Additionally, we provide a set of 43 tasks for Windows"

- **uncertainty**: The authors acknowledge that evaluator false positives and negatives may remain; the extent to which they affect reported success rates is not quantified in the inspected text.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives"

Unresolved questions:

- How robust are the benchmark’s task-specific evaluators to valid alternative solutions and edge cases beyond the quality-control trials described?
- How well would the findings generalize to broader operating-system and application coverage, including the claimed macOS environment support?
- How much do results change with newer agent models or different interaction budgets and prompting choices?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
