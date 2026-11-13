# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**pyagent_react · error**

5 model calls · 2 reads · 25.39 s · $0.002834

5 decisions · 5 tool calls · 32350 input tokens (19310 cached) · 2023 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

Error: `{"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"}`

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark construction, task validation, and evaluation methodology. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect model results, evaluation caveats, and stated limitations. | read pages [5, 6, 7] | [event 11](trace.jsonl#L11) |
| 3 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Submit an evidence-based assessment using the inspected benchmark and results pages. | citation_validation_failed; #2: wrong_page (pages [5]) | [event 17](trace.jsonl#L17) |
| 4 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Correct the GPT-4 subset citation to the page identified by validation. | citation_validation_failed; #2: wrong_page (pages [5]); #3: wrong_page (pages [6]) | [event 23](trace.jsonl#L23) |
| 5 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Replace unverified citations with exact excerpts from observed page 2. | citation_validation_failed; #3: wrong_page (pages [1]) | [event 29](trace.jsonl#L29) |
| — | run_error | | {"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"} | [event 33](trace.jsonl#L33) |
