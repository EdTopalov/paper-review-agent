# T14: RULER: What's the Real Context Size of Your Long-Context Language Models?

**deliberative_review · ok**

7 model calls · 3 reads · 31.34 s · $0.007232

7 decisions · 4 tool calls · 48108 input tokens (1359 cached) · 2770 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

RULER extends needle-in-a-haystack evaluation with configurable retrieval, variable-tracking, aggregation, and QA tasks, and uses them to compare ten long-context models at multiple input lengths. The reported results show performance degradation as inputs grow and distinguish claimed context windows from effective performance under this benchmark. Its controlled synthetic tasks and benchmark-specific effective-length criterion support useful comparisons, but do not directly establish general long-context understanding.

- **strength**: The benchmark extends beyond single-needle retrieval to multi-step variable binding, with adjustable task complexity.
  - Page 5 · citation: whitespace
  - Quote: "The task complexity can be increased by adding more hops (i.e., the times of name binding) or more chains, similar to adding hard distractors in MK-NIAH."

- **strength**: The authors report that performance declines as input length increases across the evaluated models.
  - Page 6 · citation: whitespace
  - Quote: "We notice large performance degradation in all models as we increase input length in RULER ."

- **limitation**: The aggregation tasks are described as proxies for summarization and use synthetic word lists, so their results alone do not establish performance on natural summarization.
  - Page 5 · citation: exact
  - Quote: "we introduce a new category as a proxy for summarization tasks"

Unresolved questions:

- How sensitive are effective-length conclusions to the chosen Llama2-7B 4K threshold and to alternative task-averaging choices?
- How well do RULER scores predict performance on naturally occurring long-document tasks?
- Thirteen pages are uninspected and several observed pages are partial. The full discussion and limitations, detailed task-level results, and appendices—including the task-configuration and correlational-study details—remain unassessed.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect benchmark task definitions and scoring on later pages to verify that the proposed retrieval, multi-hop tracing, and aggregation tasks operationalize the claimed capabilities.; Check the model evaluation setup, results, and analysis pages to see whether evidence supports the reported context-length performance drops and 32K conclusions, including comparisons across tasks and models.; Inspect discussion and limitations, and note that only page 1 is currently available; ground any eventual observations in exact page-numbered quotes and explicitly disclose uninspected material. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [1, 3, 6, 7, 9, 10] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 8 matches on pages [6, 22, 23] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [4, 5, 6] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The page 6 quote in the second observation establishes the threshold used for effective length, but does not support the observation’s separate claim that cross-model results show substantial degradation. Replace it with a quote directly reporting the degradation, or narrow the claim to the threshold definition. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Replaced the page 6 observation quote with the paper’s direct statement about performance degradation, addressing the critic’s quotation-support concern. No score change was needed. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "Evaluation"}` | Locate evaluation section to inspect benchmark setup and supporting results beyond the abstract. | 8 matches on pages [1, 3, 6, 7, 9, 10] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "effective length"}` | Inspect evaluation methodology and counterevidence to support score and observations. | 8 matches on pages [6, 22, 23] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 4, "end": 6}` | Inspect benchmark task definitions and evaluation methodology/results, including counterevidence to claims about task validity and context-length performance. | read pages [4, 5, 6] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 3}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
