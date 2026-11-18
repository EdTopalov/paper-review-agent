# T14: RULER: What's the Real Context Size of Your Long-Context Language Models?

**agent · ok**

6 model calls · 5 reads · 10.58 s · $0.002992

6 decisions · 6 tool calls · 33765 input tokens (13491 cached) · 684 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

RULER broadens long-context evaluation beyond single-needle retrieval with configurable synthetic tasks for retrieval, multi-hop tracing, aggregation, and QA. Its evaluation of ten models plus targeted complexity analyses gives useful evidence that vanilla NIAH scores can overstate broader long-context performance; the benchmark is valuable as a controlled diagnostic, though synthetic-task coverage does not establish performance on realistic long-document use.

- **strength**: The benchmark deliberately tests capabilities and failure modes that a single-needle retrieval test misses, with configurable task complexity.
  - Page 3 · citation: whitespace
  - Quote: "RULER comprises tasks across four categories: retrieval, multi-hop tracing, aggregation, and question answering with all tasks configurable for varying length and complexity"

- **strength**: The evaluation reports substantial breadth across models, sequence lengths, and task configurations, and finds broad performance degradation.
  - Page 6 · citation: whitespace
  - Quote: "For each task, we evaluate each model with 500 examples generated for each length from the series (4k, 8k, 16k, 32k, 64k, 128k)"

- **limitation**: The authors explicitly frame the benchmark as synthetic; this bounds how directly its results transfer to natural long-context applications.
  - Page 9 · citation: exact
  - Quote: "We present RULER , a synthetic benchmark for evaluating long-context language models."

- **uncertainty**: The paper's detailed error analysis focuses on Yi-34B and does not establish that each identified failure mechanism generalizes across all evaluated models.
  - Page 7 · citation: whitespace
  - Quote: "We evaluate Yi-34B-200K, the 2nd best open-source model onRULER , with increased input lengths (up to 256K) on more complex tasks"

Unresolved questions:

- How well do RULER scores predict performance on realistic long-document tasks beyond the synthetic and adapted QA settings?
- Would the model rankings and effective-length conclusions persist under alternative threshold choices, evaluation prompts, or task-generation distributions?
- I inspected the benchmark/task description, main evaluation, error analysis, and conclusion, but not the appendices' full task configurations, correlation study, or per-task results.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper's stated scope limits to assess how its benchmark claims are bounded. | 0 matches | [event 5](trace.jsonl#L5) |
| 2 | search_paper `{"query": "Results"}` | Find the evaluation results section and inspect empirical support for the benchmark's claims. | 8 matches on pages [2, 6, 7, 9, 14] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 3, "end": 5}` | Inspect benchmark design and task definitions to evaluate novelty and construct validity. | read pages [3, 4, 5] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 6, "end": 8}` | Read main evaluation setup and outcome tables to judge empirical breadth and interpretation. | read pages [6, 7, 8] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 9, "end": 10}` | Check conclusion and reported benchmark caveats before finalizing the assessment. | read pages [9, 10] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | The benchmark design, evaluation setup, results, and conclusion have been inspected; submit a citation-supported assessment while noting scope uncertainty. | review accepted | [event 31](trace.jsonl#L31) |
