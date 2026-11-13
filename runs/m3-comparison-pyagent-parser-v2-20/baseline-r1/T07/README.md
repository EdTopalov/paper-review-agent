# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**baseline · ok**

1 model calls · 0 reads · 8.36 s · $0.005129

1 decisions · 0 tool calls · 38684 input tokens (0 cached) · 587 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

OSWorld contributes a controllable virtualized desktop environment and a 369-task Ubuntu benchmark with task-specific initial-state setup and execution-based evaluation, plus a smaller Windows set. Its baseline study documents a large gap between tested agents and human task completion and analyzes several GUI-agent failure modes. The work is a substantial benchmark and infrastructure contribution; its broad claims should be read alongside its constrained task coverage and the authors’ acknowledged evaluation-quality risks.

- **strength**: The benchmark combines diverse interactive tasks with per-task setup and execution-based evaluation, including tasks spanning multiple applications.
  - Page 7 · citation: not_found
  - Quote: "each example is carefully annotated with a natural language instruction, a setup configuration with corresponding files and setup actions for initialization of initial states upon our provided VM image, and a manually crafted evaluation script to check if the task is successfully executed."

- **strength**: The evaluation reports a marked performance gap between the tested agents and human participants, and examines performance across task categories.
  - Page 10 · citation: exact
  - Quote: "Human Performance 75.00% 71.79% 70.51% 73.47% 73.27% 72.36%"

- **limitation**: The main benchmark is Ubuntu-centered and limited to selected applications; the Windows set is smaller and has access restrictions, so broad cross-platform coverage is not demonstrated by the main results.
  - Page 6 · citation: not_found
  - Quote: "We create a benchmark suite of 369 real-world computer tasks on Ubuntu environment. Additionally, we provide a set of 43 tasks for Windows built on OSWorld environment."

- **uncertainty**: The authors acknowledge possible false positives and negatives in task quality, leaving uncertainty about the reliability of all benchmark evaluations despite repeated checks.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives, which we will leave to future work."

Unresolved questions:

- How often do the custom evaluators accept alternative valid solutions or reject correct completions across the full task set, and how does that affect reported success rates?
- How well do the benchmark tasks and agent-performance findings generalize to broader software ecosystems and the macOS environment, which is discussed as unsupported for copyright reasons?
- The provided excerpts do not include the full appendix’s detailed setup and evaluation procedures or the complete discussion of human-study protocol; how sensitive are outcomes to evaluator and participant variation?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
