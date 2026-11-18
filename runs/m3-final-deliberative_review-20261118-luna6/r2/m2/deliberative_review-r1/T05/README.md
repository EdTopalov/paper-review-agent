# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**deliberative_review · ok**

7 model calls · 3 reads · 33.10 s · $0.006614

7 decisions · 4 tool calls · 43106 input tokens (1235 cached) · 2755 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

WebArena contributes a reproducible, multi-site web environment and a benchmark of 812 instantiated, multi-step tasks spanning information seeking, navigation, and content operations. Its task-specific evaluation and baseline results make it a useful testbed; the reported low success rates indicate that the tested agents struggle on this benchmark, though the experimental evidence is limited to a small set of text-based baselines.

- **strength**: The benchmark has substantial task coverage and includes several kinds of web work, including tasks that require navigating across multiple pages.
  - Page 7 · citation: exact
  - Quote: "In total, we curated 241 templates and 812 instantiated intents."

- **strength**: The authors report double annotation for each information-seeking question, with a third annotator resolving disagreements.
  - Page 8 · citation: whitespace
  - Quote: "To ensure consistency and accuracy, each question was annotated twice."

- **uncertainty**: The baseline results indicate difficulty for the tested agents, but the GPT-4 success rate is inconsistent across the table and results prose: the table reports 10.59%, while the prose reports 10.63%. The observed experiments cover text-input agents and two model families.
  - Page 9 · citation: exact
  - Quote: "Reasoning gpt-4 10.59"

Unresolved questions:

- How well do the benchmark tasks and simulated websites generalize to live websites and tasks not authored from the included templates?
- How sensitive are results to the GPT-3.5-based fuzzy-match evaluator, agent configuration, and other task-level scoring choices?
- What further limitations or caveats are discussed in the uninspected pages? Coverage here is partial: 14 pages were uninspected, including much of the discussion and appendices.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the benchmark and environment-design pages for the number and diversity of tasks, how tasks and success criteria were constructed, and whether realism and reproducibility claims are supported.; Inspect the experimental setup and results pages to verify the reported 10.59% success rate, agent comparisons, evaluation procedure, and evidence supporting the claim that tasks are challenging.; Inspect limitations and discussion elsewhere in the paper for scope boundaries or caveats; only page 1 is currently observed, so do not treat uninspected material as absent. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | read pages [4, 5, 6] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 4 matches on pages [1, 2, 9, 12] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [7, 8, 9] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: Observation 2’s quote supports the double-annotation claim, but not its additional claim that evaluation combines answer checks with programmatic execution-state checks. Narrow the observation to what the quote demonstrates, or use a quote that supports the evaluation-method claim.; Target: Revise observation 2 so its claim is supported by its cited quote on page 8. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Narrowed observation 2 to the double-annotation claim directly supported by its page-8 quotation. Retained the score and the rate discrepancy, and preserved uncertainty about uninspected material. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | read_pages `{"start": 4, "end": 6}` | Inspect environment and benchmark construction evidence for realism, task count, diversity, and success criteria. | read pages [4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "10.59"}` | Inspect experimental results and comparisons to support or qualify the benchmark's reported agent performance. | 4 matches on pages [1, 2, 9, 12] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 7, "end": 9}` | Inspect task evaluation methodology and baseline experimental results to address benchmark and evidence obligations. | read pages [7, 8, 9] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 3}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
