# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**deliberative_review · error**

8 model calls · 4 reads · 42.70 s · $0.006916

8 decisions · 5 tool calls · 40699 input tokens (0 cached) · 3684 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

Error: `{"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"}`

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the methods and experiment sections for prompt definitions, datasets, baselines, model settings, and whether comparisons support the headline claims across all ten datasets.; Check results, tables, and any robustness or error analyses for evidence behind the reported gains, especially the claimed comparison with 8-shot CoT and the diagnosis of Zero-shot-CoT errors.; Inspect limitations and discussion, while noting that only page 1 is currently available; avoid treating uninspected pages as evidence of missing support. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 1 matches on pages [5] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 1 matches on pages [5] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [2, 3, 4] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: investigate; Issues: The draft’s page 4 quotation is not verified as verbatim by the citation check; use a clearly matching span from the observed text. The page 2 quotation also has a hyphenation ambiguity, so replace it with an unambiguous exact span.; The draft reports an error diagnosis but does not flag a discrepancy in the observed source: page 1 describes Figure 1 as analyzing 46 incorrect GSM8K answers, while page 2 describes the cited percentages as coming from a sample of 100 arithmetic test examples. This needs qualification or targeted checking.; The available excer … | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | targeted_read | read pages [5, 6, 7] | [event 34](trace.jsonl#L34) · [event 39](trace.jsonl#L39) |
| 8 | revise | Draft revised; Changes: Updated the assessment after inspecting the main results and error-analysis tables. Replaced the previously questionable quotation with exact observed text and clarified the error-analysis denominator: the 100 sampled problems include 46 Zero-shot-CoT errors, whose reported categories sum to 46%. The concern that headline comparisons were unsupported is resolved by the newly observed tables; uncertainty about uninspected pages and generalization remains. | [event 40](trace.jsonl#L40) · [event 43](trace.jsonl#L43) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "experimental results"}` | Locate results pages to inspect evidence for the paper's claims. | 1 matches on pages [5] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "Experimental Results"}` | Inspect results and nearby experimental evidence for the stated dataset coverage and baseline comparisons. | 1 matches on pages [5] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 2, "end": 4}` | Inspect prompting method, dataset/model setup, and experimental design to substantiate the paper's central contribution. | read pages [2, 3, 4] | [event 22](trace.jsonl#L22) |
| 7 | read_pages `{"start": 5, "end": 7}` | Inspect main results and comparison settings for PS/PS+ evidence. | read pages [5, 6, 7] | [event 37](trace.jsonl#L37) |
| 8 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit after the enforced critique and source validation. | citation_validation_failed; #2: hyphenation_ambiguous (pages [5]); #3: not_found | [event 45](trace.jsonl#L45) |
| — | run_error | | {"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"} | [event 49](trace.jsonl#L49) |
