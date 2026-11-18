# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · error**

8 model calls · 5 reads · 19.68 s · $0.003011

8 decisions · 8 tool calls · 50193 input tokens (34497 cached) · 1458 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

Error: `{"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"}`

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "experimental results"}` | Locate reported evaluation results and dataset evidence. | 1 matches on pages [5] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect main evaluation tables and experimental setup. | read pages [5, 6, 7] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 1, "end": 1}` | Review paper framing, stated contributions, and motivation. | read pages [1] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "limitations"}` | Check whether the authors explicitly state scope limitations. | 2 matches on pages [9] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 9, "end": 9}` | Inspect authors’ explicit limitations and stated scope. | read pages [9] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence inspected covers framing, main result tables, and explicit limitations; submit a balanced review. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1, 2]); #2: not_found; #3: hyphenation_ambiguous (pages [9]) | [event 31](trace.jsonl#L31) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the failed citations using exact wording observed in the supplied page excerpts. | citation_validation_failed; #1: not_found; #2: wrong_page (pages [5]) | [event 37](trace.jsonl#L37) |
| 8 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Fix remaining quote/page mismatches with exact observed lines from pages 1 and 6. | citation_validation_failed; #1: not_found; #2: not_found | [event 43](trace.jsonl#L43) |
| — | run_error | | {"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"} | [event 46](trace.jsonl#L46) |
