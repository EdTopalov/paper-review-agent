# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**pyagent_react · ok**

6 model calls · 4 reads · 19.04 s · $0.001896

6 decisions · 5 tool calls · 39289 input tokens (30257 cached) · 929 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

WebArena contributes a self-hostable, interactive web environment and a benchmark of 812 high-level tasks with functional correctness checks. Its multi-site workflows and reproducible setup provide a useful testbed for autonomous agents, and baseline results expose substantial task-completion challenges. The inspected evidence supports the benchmark’s practical value, while leaving questions about representativeness and evaluation robustness open.

- **strength**: The standalone environment is designed to support reproducible comparisons while retaining functional web interactions.
  - Page 3 · citation: whitespace
  - Quote: "We achieve reproducibility by having the environment be standalone, not relying on live websites."

- **strength**: The benchmark spans many instantiated tasks and uses distinct evaluation approaches for answer-oriented and state-changing tasks.
  - Page 7 · citation: exact
  - Quote: "In total, we curated 241 templates and 812 instantiated intents."

- **strength**: The baseline results demonstrate that the tested agents struggle with the benchmark; they are useful evidence of difficulty, not proof that all current agents do so.
  - Page 9 · citation: exact
  - Quote: "The end-to-end task success rate (%) onWebArena."

- **limitation**: The reported GPT-4 success rate is inconsistent within the paper: Table 3 reports 10.59%, while the prose reports 10.63%. This is a demonstrated reporting discrepancy; its effect on the broader conclusion is unclear.
  - Page 9 · citation: whitespace
  - Quote: "achieves a relatively modest end-to-end task success rate of 10.63%."

Unresolved questions:

- How well do tasks based on the authors’ browsing histories and annotator-created templates represent the wider range of everyday web tasks?
- How robust are the reported success rates to model sampling variability and the language-model-based fuzzy-match evaluator?
- I inspected pages 3–12, including selected benchmark and results sections, but not the full appendix or the remaining paper; details there could refine assessment of task coverage, annotation validation, and reproducibility.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 3, "end": 5}` | Inspect the environment design and benchmark task construction. | read pages [3, 4, 5] | [event 6](trace.jsonl#L6) |
| 2 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 6, "end": 8}` | Inspect task annotation, benchmark composition, and correctness evaluation. | read pages [6, 7, 8] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 10, "end": 12}` | Inspect evaluated agent performance and the authors' analysis of failure modes. | read pages [10, 11, 12] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 9, "end": 9}` | Check the reported benchmark scores and experimental protocol. | read pages [9] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit a review grounded in the inspected environment, evaluation, and results pages. | review accepted | [event 30](trace.jsonl#L30) |
