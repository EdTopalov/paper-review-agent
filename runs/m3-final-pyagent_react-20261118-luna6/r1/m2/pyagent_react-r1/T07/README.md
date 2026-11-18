# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**pyagent_react · ok**

5 model calls · 4 reads · 11.76 s · $0.002100

5 decisions · 5 tool calls · 37776 input tokens (26017 cached) · 741 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

OSWorld contributes a practical, extensible real-computer environment and a benchmark of open-ended tasks with task-specific execution-based evaluation. Its broad app and workflow coverage, substantial annotation and checking effort, and human/model comparison make it a useful research benchmark. Baselines expose a large performance gap, though the benchmark’s scope and validation leave open questions about representativeness and evaluator reliability.

- **strength**: The benchmark combines diverse real-computer tasks with task-specific setup and evaluation rather than relying only on fixed demonstrations.
  - Page 2 · citation: whitespace
  - Quote: "Each task example is based on real-world computer use cases experienced by real users"

- **strength**: The authors report extensive quality-control work, including independent attempts and multiple rounds of checks.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives, which we will leave to future work."

- **strength**: The reported baseline results show a substantial gap between tested agents and human participants on this benchmark.
  - Page 11 · citation: whitespace
  - Quote: "the success rate of the model is only 5.26% to 5.80% even with the strongest VLMs GPT-4V and Gemini-Pro-vision."

- **limitation**: The main benchmark is centered on Ubuntu and a selected set of applications; Windows examples are supplementary, and the paper reports remaining risk of evaluator errors.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives, which we will leave to future work."

Unresolved questions:

- How well do the task distribution and results generalize beyond the selected applications, Ubuntu-centered benchmark, and student participants?
- What are the evaluator false-positive and false-negative rates after the reported quality-control rounds?
- How would stronger agent methods or later models change the reported baseline gap?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 3}` | Inspect benchmark construction, task coverage, and evaluation design. | read pages [2, 3] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 10, "end": 12}` | Inspect benchmark evaluation results and human/model comparisons. | read pages [10, 11, 12] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 4, "end": 6}` | Inspect benchmark task sourcing, evaluation reliability, and human study methodology. | read pages [4, 5, 6] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 7, "end": 9}` | Inspect task annotation, benchmark scope, and human performance protocol. | read pages [7, 8, 9] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Evidence covers benchmark design, task quality checks, human evaluation, and baseline results. | review accepted | [event 26](trace.jsonl#L26) |
