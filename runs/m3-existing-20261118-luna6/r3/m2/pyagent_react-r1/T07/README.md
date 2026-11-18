# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**pyagent_react · ok**

5 model calls · 4 reads · 14.00 s · $0.001814

5 decisions · 5 tool calls · 31660 input tokens (22104 cached) · 797 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

OSWorld contributes an executable, extensible computer-use environment and a 369-task benchmark spanning real desktop applications, operating-system actions, and cross-app workflows. It pairs task-specific initial states with execution-based evaluation and uses human and model evaluations to illustrate the difficulty of the benchmark. This is a substantial research resource; the inspected evidence supports its design and reported findings, while leaving uncertainty about evaluator reliability and broader generalization.

- **strength**: The benchmark operationalizes success through task-specific evaluation, supporting diverse workflows rather than requiring a single prescribed action sequence.
  - Page 5 · citation: whitespace
  - Quote: "The example-wise evaluation facilitates the diversity of tasks and reliable evaluation of complex, real-world, open-ended tasks."

- **strength**: The task collection has broad coverage and documents substantial annotation and review effort.
  - Page 7 · citation: whitespace
  - Quote: "Overall, it takes 9 computer science students (all student authors) over 3 months, consuming approximately 1800 man-hours"

- **strength**: The reported human/model performance gap and low baseline success provide evidence that the benchmark challenges the tested agents.
  - Page 10 · citation: exact
  - Quote: "Human Performance 75.00% 71.79% 70.51% 73.47% 73.27% 72.36%"

- **limitation**: The authors acknowledge that further scrutiny may be needed to reduce evaluation errors; this is a stated limitation, not proof that the reported evaluations are defective.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives, which we will leave to future work."

Unresolved questions:

- How reliably do the task-specific evaluators handle alternative valid solutions and edge cases across the full benchmark?
- How well do the reported results generalize beyond the tested operating systems, applications, task set, and baseline configurations?
- I inspected pages 1 and 3–11, not the full 51-page paper or its appendices; implementation details, additional experiments, and supplementary evidence remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "12.24%"}` | Locate the reported benchmark results and their context. | 4 matches on pages [1, 2, 10, 11] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 3, "end": 5}` | Inspect task construction and execution-based evaluation. | read pages [3, 4, 5] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 7, "end": 9}` | Inspect benchmark task coverage and the agent evaluation design. | read pages [7, 8, 9] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 10, "end": 11}` | Inspect baseline outcomes and stated analysis of agent performance. | read pages [10, 11] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Submit an evidence-based assessment using the inspected benchmark design, dataset, and results pages. | review accepted | [event 26](trace.jsonl#L26) |
