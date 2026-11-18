# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**baseline · ok**

1 model calls · 0 reads · 7.84 s · $0.000727

1 decisions · 0 tool calls · 38684 input tokens (38681 cached) · 679 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

OSWorld contributes an executable, virtual-machine-based benchmark for open-ended computer tasks across desktop applications, interfaces, and workflows. Its 369 Ubuntu tasks include configured initial states and task-specific execution-based evaluators, and the paper evaluates a range of language and vision-language agents, finding a large gap between baseline and human success. The benchmark and infrastructure are substantial research resources; evidence is useful but bounded by the task set, evaluation design, and breadth of human and cross-platform studies.

- **strength**: The benchmark’s combination of intermediate task states, multi-application workflows, and custom executable evaluators supports a wider range of computer-use evaluation than static demonstrations.
  - Page 7 · citation: whitespace
  - Quote: "we implement nearly sample-specific executable evaluation scripts, resulting in a total of 134 unique evaluation functions"

- **strength**: The experiments provide a clear, consequential baseline result: tested agents perform far below the human participants on this task set.
  - Page 10 · citation: exact
  - Quote: "Human Performance 75.00% 71.79% 70.51% 73.47% 73.27% 72.36%"

- **limitation**: The paper identifies a genuine mismatch risk: task success can be recorded even when an agent violates a stated tool constraint, so evaluators may not always capture instruction fidelity.
  - Page 16 · citation: whitespace
  - Quote: "the agent used “ffmpeg” command to complete the video cropping, ignoring the “use GIMP” requirement in the instructions."

- **uncertainty**: The reported human comparison is informative, but the evidence does not establish how representative it is of broader computer users; participants are described as students with basic software skills, and the paper notes substantial remaining quality-control risk.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives, which we will leave to future work."

Unresolved questions:

- How often do task-specific evaluators accept outcomes that satisfy a narrow state check but fail to honor the full user instruction, and how consistently are such cases caught in review?
- How robust are the human-versus-agent comparisons across larger and more diverse participant groups?
- How well do the benchmark’s tasks and evaluation methods generalize beyond the Ubuntu task set, given the much smaller Windows set and the absence of a macOS benchmark in the described evaluation?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
