# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**deliberative_review · error**

8 model calls · 3 reads · 36.59 s · $0.004803

8 decisions · 5 tool calls · 26442 input tokens (1565 cached) · 3376 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

Error: `{"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"}`

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the methods and results pages to verify the claimed gains over Zero-shot-CoT and other baselines: identify datasets, models, evaluation measures, and whether comparisons are supported across the stated tasks.; Check the paper’s prompting details, error analysis, and any ablations or robustness analyses to assess whether the proposed planning instructions plausibly address the stated failure modes, and whether support appears beyond the abstract and introduction excerpt.; Inspect discussion and conclusion for scope boundaries and limitations; note that only page 1 has been suppl … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 1 matches on pages [5] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 1 matches on pages [5] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | 8 matches on pages [5, 6, 18, 19, 20, 21, 22, 23] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The first observation’s quote is not verified against the supplied page text. Replace it with a verbatim span as represented in E1, preserving the source’s line-break hyphenation if needed.; Target: Revise the first observation’s page-1 quote to match E1 verbatim; retain the qualification that the broader results and analyses cannot be assessed from the partial excerpts. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Replaced the page-1 quotation with a verbatim span from E1, preserving its line-break hyphenation. Retained the score and the qualifications about incomplete evidence; the excerpts do not support a stronger conclusion. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |
| 8 | revise | Draft revised; Changes: Replaced the first observation’s unverified quote with an exact span from E1. Retained the qualification that broader results, analyses, and limitations cannot be assessed from the partial excerpts. | [event 42](trace.jsonl#L42) · [event 45](trace.jsonl#L45) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "experimental results"}` | Locate results and evaluation evidence for claims across datasets. | 1 matches on pages [5] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "Experimental Results"}` | Inspect main results to assess evidence supporting claimed gains and identify evaluation scope. | 1 matches on pages [5] | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "Table 2"}` | Inspect results evidence for task, model and baseline comparisons. | 8 matches on pages [5, 6, 18, 19, 20, 21, 22, 23] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.55, "observations": 4}}` | Submit after the enforced critique and source validation. | citation_validation_failed; #1: not_found; #2: not_found | [event 39](trace.jsonl#L39) |
| 8 | submit_review `{"review": {"score": 0.55, "observations": 4}}` | Submit after the enforced critique and source validation. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1]) | [event 47](trace.jsonl#L47) |
| — | run_error | | {"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"} | [event 51](trace.jsonl#L51) |
