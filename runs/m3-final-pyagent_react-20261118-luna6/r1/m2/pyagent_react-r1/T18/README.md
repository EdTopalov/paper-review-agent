# T18: Gorilla: Large Language Model Connected with Massive APIs

**pyagent_react · ok**

6 model calls · 4 reads · 19.76 s · $0.001874

6 decisions · 5 tool calls · 37523 input tokens (28181 cached) · 850 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.66

Gorilla pairs API-specific instruction fine-tuning with retrieval-aware training to generate calls for a sizable ML API benchmark. The paper offers comparative evaluations, retrieval ablations, and demonstrations of adaptation to changed documentation. Its results support the approach within this benchmark, but the benchmark’s synthetic instructions, API-call matching metric, and ML-only scope limit how broadly the findings establish practical API use.

- **strength**: The benchmark brings together APIs from three model hubs, with exhaustive coverage claimed for two sources and a documented selection rule for HuggingFace.
  - Page 2 · citation: whitespace
  - Quote: "We exhaustively include\nevery API call in TorchHub (94 API calls) and TensorHub (696 API calls); For HuggingFace, since the\nmodels come in a large number and lots of the models don’t have a specification, we choose the\nmost downloaded 20 models per task category"

- **strength**: The reported comparisons show Gorilla leading the zero-shot accuracy figures in all three benchmark groups, although the evaluation scope differs by group.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: The paper evaluates generated calls by matching API-call structure, rather than reporting execution success; this leaves runtime correctness unestablished by this metric.
  - Page 2 · citation: exact
  - Quote: "We adopt a common AST sub-tree matching technique to evaluate the\nfunctional correctness of the generated API."

- **uncertainty**: The HuggingFace baseline comparison is not fully like-for-like: other models are evaluated for domain selection, while Gorilla is evaluated differently. The effect on the headline comparison is unclear.
  - Page 7 · citation: exact
  - Quote: "for all the models except Gorilla, we only check if they can provide\nthe correct domain names."

Unresolved questions:

- How well does the approach transfer to APIs outside the ML model hubs and to multi-step API workflows?
- How do models perform on independently authored or real user requests, rather than synthetic instruction prompts?
- How often do generated calls execute successfully in realistic dependency and environment settings?
- How robust are the reported gains to other benchmark splits or API-level separation between training and test examples?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the paper’s method, benchmark construction, and evaluation setup. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 6, "end": 8}` | Inspect reported benchmark results, baselines, and evaluation details. | read pages [6, 7, 8] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "limitations"}` | Check the paper’s stated limitations and scope boundaries. | 3 matches on pages [2, 9, 13] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 9, "end": 10}` | Inspect stated limitations and the constraint-evaluation evidence. | read pages [9, 10] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.66, "observations": 4}}` | Submit an evidence-based assessment using observed method, results, and scope passages. | review accepted | [event 30](trace.jsonl#L30) |
