# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**baseline · ok**

1 model calls · 0 reads · 8.94 s · $0.000747

1 decisions · 0 tool calls · 38684 input tokens (38681 cached) · 719 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

OSWorld contributes an executable, extensible desktop-computer environment and a 369-task Ubuntu benchmark with task-specific setup and execution-based evaluation, then uses it to expose substantial gaps between evaluated agents and human users. Its breadth and operational detail make it a useful research platform; the evidence is strongest as a benchmark and diagnostic study, with generalization and evaluation quality still open questions.

- **strength**: The benchmark’s task-specific setup and evaluation design supports diverse, stateful computer tasks, including workflows across applications.
  - Page 7 · citation: not_found
  - Quote: "each example is carefully annotated with a natural language instruction, a setup configuration with corresponding files and setup actions for initialization of initial states upon our provided VM image, and a manually crafted evaluation script to check if the task is successfully executed."

- **strength**: The reported baseline results provide a clear diagnostic of current agent limitations, and the human comparison offers a useful reference point.
  - Page 10 · citation: exact
  - Quote: "GPT-4 20.83% 3.58% 25.64% 26.53% 2.97% 12.24%"

- **limitation**: The authors acknowledge that benchmark quality control may not eliminate evaluator errors, which matters for interpreting success rates.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives, which we will leave to future work."

- **uncertainty**: The main benchmark is Ubuntu-based; the paper describes a smaller Windows set, while macOS support is discussed as an environment capability rather than evaluated benchmark coverage.
  - Page 6 · citation: not_found
  - Quote: "We create a benchmark suite of 369 real-world computer tasks on Ubuntu environment. Additionally, we provide a set of 43 tasks for Windows"

Unresolved questions:

- How stable are the reported task success rates under independent re-annotation or alternative evaluation scripts, especially for tasks where multiple valid outcomes are possible?
- How well do the benchmark’s task mix and results generalize to broader application ecosystems, operating systems, and users beyond the studied settings?
- Would stronger agent architectures or later model generations substantially change the reported performance gaps? The reported baselines establish a useful snapshot, but do not answer that longer-term question.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
