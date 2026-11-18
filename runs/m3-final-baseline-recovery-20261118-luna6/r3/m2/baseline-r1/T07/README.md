# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**baseline · ok**

1 model calls · 0 reads · 6.74 s · $0.000695

1 decisions · 0 tool calls · 38684 input tokens (38681 cached) · 616 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

OSWorld contributes an executable desktop-computer environment and a 369-task Ubuntu benchmark with configurable initial states and task-specific execution-based evaluation, then uses it to assess language- and vision-language-model agents. Its broad task coverage and evaluation infrastructure are substantial contributions; baseline results document a large gap between the tested agents and humans, while the paper also identifies limits in benchmark quality assurance and scope.

- **strength**: The benchmark combines real computer interaction, varied tasks, and task-specific execution-based evaluation rather than relying only on static demonstrations.
  - Page 2 · citation: not_found
  - Quote: "Each task example is based on real-world computer use cases and often requires interactions with multiple applications and interfaces."

- **strength**: The evaluation demonstrates a substantial performance gap for the tested agents on this benchmark, with human performance providing a useful reference.
  - Page 10 · citation: exact
  - Quote: "Human Performance 75.00% 71.79% 70.51% 73.47% 73.27% 72.36%"

- **limitation**: The authors acknowledge that annotation and quality-control work may not have eliminated false positives and negatives, which could affect measured task success.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives, which we will leave to future work."

- **limitation**: The main benchmark is centered on Ubuntu, with Windows coverage smaller and restricted; the paper also explains why macOS is not included in the benchmark.
  - Page 26 · citation: whitespace
  - Quote: "we select Ubuntu, the most representative Linux desktop OS, as the foundation for the main part of our benchmark intended for public use."

Unresolved questions:

- How robust are the task-specific evaluation scripts to valid alternative solutions and edge cases beyond the repeated checks described by the authors?
- How well do results generalize to operating systems, applications, and hardware configurations beyond the Ubuntu-centered benchmark and its smaller Windows set?
- How would newer agent systems perform under the same task suite and evaluation protocol?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
