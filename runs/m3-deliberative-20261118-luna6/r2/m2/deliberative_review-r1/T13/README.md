# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**deliberative_review · error**

8 model calls · 4 reads · 32.39 s · $0.005309

8 decisions · 4 tool calls · 33303 input tokens (1507 cached) · 2664 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

Error: `{"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"}`

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the method and training sections to verify how retrieval and reflection tokens are trained and used, and whether the procedure supports the claimed on-demand retrieval and self-critique.; Inspect the experiments and tables for the claimed gains across QA, reasoning, fact verification, factuality, and citation accuracy; check baselines, evaluation setup, and whether results support the breadth of the abstract’s claims.; Inspect limitations, ablations, and later discussion for scope boundaries or qualifications; only page 1 is currently available, so do not treat uninspected mate … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [2, 3] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 0 matches | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | 0 matches | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: investigate; Issues: The third observation’s quote is not verified as verbatim in the supplied page text; the citation checker reports no match. Replace it with a verified short span before using it.; The score and overall contribution assessment remain provisional: the archive covers only page 1 and partial excerpts from pages 2–3, leaving the method details, experimental evidence, and limitations uninspected. The draft acknowledges this gap, so it should not be treated as evidence that the reported gains are unsupported.; Target: In the uninspected experiments and tables, wha … | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | targeted_read | read pages [10, 11, 12] | [event 34](trace.jsonl#L34) · [event 39](trace.jsonl#L39) |
| 8 | revise | invalid_phase_output; unobserved_ledger_reference; ValueError | [event 40](trace.jsonl#L40) · [event 43](trace.jsonl#L43) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "training"}` | Locate method and training details relevant to reflection-token supervision and retrieval behavior. | 8 matches on pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Find the paper's explicit scope limits and discussion, then inspect primary evidence. | 0 matches | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "Limitations"}` | Locate stated scope limitations and discussion to assess qualifications. | 0 matches | [event 22](trace.jsonl#L22) |
| 7 | read_pages `{"start": 10, "end": 12}` | Inspect experiment tables and comparisons across the claimed task types. | read pages [10, 11, 12] | [event 37](trace.jsonl#L37) |
| — | run_error | | {"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"} | [event 45](trace.jsonl#L45) |
