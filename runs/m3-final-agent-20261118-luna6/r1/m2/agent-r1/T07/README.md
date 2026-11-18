# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**agent · ok**

6 model calls · 5 reads · 13.36 s · $0.002609

6 decisions · 6 tool calls · 30121 input tokens (12729 cached) · 653 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

OSWorld contributes an executable, extensible benchmark and virtualized environment for evaluating multimodal agents on open-ended computer tasks, with task-specific execution-based checks across real desktop applications. Its substantial task curation and comparative human/model evaluation make it useful for diagnosing current agent weaknesses; the reported model success rates remain low, and the initial benchmark is concentrated on Ubuntu and a defined application set.

- **strength**: The benchmark pairs task-specific setup with execution-based evaluation, supporting reproducible assessment of task completion rather than matching a single demonstration.
  - Page 7 · citation: whitespace
  - Quote: "a setup configuration with corresponding files and setup actions for initialization of initial states upon our provided VM image, and a manually crafted evaluation script to check if the task is successfully executed."

- **strength**: The paper reports broad task curation and repeated review of evaluation scripts, alongside substantial annotation effort.
  - Page 7 · citation: whitespace
  - Quote: "each example is further scrutinized and iterated upon by different individuals three times from the perspective of alignment with the instruction and correctness under different solutions."

- **limitation**: The core 369-task benchmark is defined on Ubuntu and concentrates on a representative but bounded application set; Windows examples are supplementary.
  - Page 6 · citation: whitespace
  - Quote: "We introduce the OSW ORLD benchmark, which encompasses 369 real computing tasks defined and executed on Ubuntu."

- **strength**: Baseline results and human comparison reveal a large performance gap, while performance varies substantially by task category.
  - Page 10 · citation: exact
  - Quote: "GPT-4 20.83% 3.58% 25.64% 26.53% 2.97% 12.24%"

Unresolved questions:

- How well do the task selection and hand-authored evaluators generalize to computer-use scenarios outside the selected applications and curated tasks?
- How robust are the reported model and human comparisons to variation across annotators, repeated trials, and interaction budgets?
- I inspected the environment and benchmark description and selected results, but not the full appendices, all qualitative analyses, or every experimental setting; those details could change confidence in reliability and breadth.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Find the authors' stated scope limitations to assess boundaries. | 3 matches on pages [6, 15, 23] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 4}` | Inspect benchmark construction and evaluation design supporting the contribution. | read pages [3, 4] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "12.24%"}` | Locate quantitative benchmark results and baseline performance. | 4 matches on pages [1, 2, 10, 11] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 6, "end": 7}` | Read limitations and benchmark task composition for scope and validity. | read pages [6, 7] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 10, "end": 11}` | Inspect empirical evaluation results and human comparison. | read pages [10, 11] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Evidence inspected covers benchmark design, dataset construction, limitations and baseline results; submit concise independent assessment. | review accepted | [event 31](trace.jsonl#L31) |
