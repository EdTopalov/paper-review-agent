# T20: RAFT: Adapting Language Model to Domain Specific RAG

**deliberative_review · error**

8 model calls · 3 reads · 44.55 s · $0.012682

8 decisions · 5 tool calls · 84924 input tokens (0 cached) · 4152 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

Error: `{"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"}`

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the method and experimental pages to verify how RAFT constructs training examples, handles distractors, and compares against RAG and fine-tuning baselines.; Check results and analysis across the reported datasets, models, and metrics to assess whether the claimed improvements are supported and how broad they are.; Inspect limitations and remaining pages for qualifications or additional evidence; only page 1 is currently available, so avoid treating uninspected material as absent. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | read pages [2, 3, 4] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [5, 6, 7] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [8, 9, 10] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The fourth observation’s quotation is not verified against the supplied page text: it crosses a line-break hyphenation in “RAFT-\nperforms,” and the citation checker marks it unmatched. Replace it with a short verbatim span that matches page 4 exactly. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Replaced the unmatched page 4 quotation with a short exact span from that page. Retained the score and substantive assessment; no evidence warranted a score change. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |
| 8 | revise | Draft revised; Changes: Replaced the unmatched quotation in the uncertainty observation with the exact observed page 4 span “We design our experiments to study how well.” Retained the score and the existing scope and evidence qualifications. | [event 42](trace.jsonl#L42) · [event 45](trace.jsonl#L45) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect method and baseline setup, including exact page quotes. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Inspect reported results, ablations and sensitivity analysis to evaluate evidence and scope. | read pages [5, 6, 7] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 8, "end": 10}` | Inspect remaining discussion/conclusion and any stated limitations or further experimental qualifications before judging scope. | read pages [8, 9, 10] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit after the enforced critique and source validation. | citation_validation_failed; #1: not_found; #4: hyphenation_ambiguous (pages [4]) | [event 39](trace.jsonl#L39) |
| 8 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit after the enforced critique and source validation. | citation_validation_failed; #1: not_found | [event 47](trace.jsonl#L47) |
| — | run_error | | {"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"} | [event 51](trace.jsonl#L51) |
