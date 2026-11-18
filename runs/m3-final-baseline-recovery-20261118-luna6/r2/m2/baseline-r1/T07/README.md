# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**baseline · ok**

1 model calls · 0 reads · 9.72 s · $0.000750

1 decisions · 0 tool calls · 38684 input tokens (38681 cached) · 725 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

OSWorld contributes an executable, VM-based environment and a 369-task benchmark for evaluating computer-use agents across desktop and web apps, operating-system tasks, and multi-app workflows. Its main value is the combination of realistic interaction, task-specific initial states, and execution-based evaluation; baseline results also document a large gap between the tested agents and human participants. This assessment uses only the supplied PDF and does not independently verify the released environment, task data, or evaluation scripts.

- **strength**: The benchmark’s execution-based, task-specific evaluation and intermediate-state setup make it a useful platform for testing varied computer tasks beyond static action prediction.
  - Page 7 · citation: not_found
  - Quote: "each example is carefully annotated with a natural language instruction, a setup configuration with corresponding files and setup actions for initialization of initial states"

- **strength**: The reported evaluations provide evidence that the tested agents remain far below human performance, including on multi-app workflows.
  - Page 10 · citation: exact
  - Quote: "Human Performance 75.00% 71.79% 70.51% 73.47% 73.27% 72.36%"

- **limitation**: The authors acknowledge that annotation and checking do not eliminate evaluation errors; residual false positives and negatives could affect measured performance.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives"

Unresolved questions:

- How much do baseline success rates change under repeated runs or updated model versions, especially given the paper notes that some evaluated models are closed-source and their results may change over time?
- How robust are the task-specific evaluators to valid alternative solutions and edge cases beyond the checks performed by the authors?
- The main benchmark is Ubuntu-based, with a smaller Windows set and no macOS benchmark in the supplied paper; how well do its task mix and findings transfer to other operating systems and application ecosystems?
- The paper identifies safety assessment as an open problem. What practical measures can detect harmful side effects that are unrelated to the task’s completion criteria?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
