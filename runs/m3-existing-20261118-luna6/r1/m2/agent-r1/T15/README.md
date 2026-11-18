# T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering

**agent · ok**

6 model calls · 4 reads · 14.80 s · $0.001943

6 decisions · 6 tool calls · 28944 input tokens (19949 cached) · 1276 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AlphaCodium is a test-driven, multi-stage inference workflow combining problem reflection, AI-generated tests, candidate solutions, and iterative code repair. On CodeContests it reports consistent gains over direct prompting across several models, including GPT-4 pass@5 rising from 19% to 44% on validation and 12% to 29% on test. The evidence supports a useful benchmark-specific contribution, while broad applicability and some comparisons remain less firmly established.

- **strength**: The paper offers a concrete inference-time workflow aimed at a distinctive weakness in code generation: validating and repairing against tests rather than relying on a single prompt.
  - Page 3 · citation: whitespace
  - Quote: "Two key elements for this code-oriented flow are (a) generating additional data in a pre-processing stage, such as self-reflection and public tests reasoning, to aid the iterative process, and (b) enrichment of the public tests with additional AI-generated tests."

- **strength**: Reported improvements are consistent across the listed model families and both validation and test sets.
  - Page 7 · citation: exact
  - Quote: "GPT-4\nvalidation Direct prompt 19%\nAlphaCodium 44%\ntest Direct prompt 12%\nAlphaCodium 29%"

- **limitation**: The demonstrated evaluation is restricted to CodeContests; transferring findings to general software engineering is proposed rather than demonstrated in the inspected evidence.
  - Page 3 · citation: whitespace
  - Quote: "In this work, instead of training a dedicated model, we focused on developing a code-oriented flow, that can be applied to any LLM pre-trained to support coding tasks, such as GPT [5] or DeepSeek [3]."

- **uncertainty**: Prior-work comparisons acknowledge evaluation subtleties and do not establish a controlled, reproducible head-to-head comparison in the inspected evidence.
  - Page 7 · citation: exact
  - Quote: "There are subtleties when evaluating results."

Unresolved questions:

- How much of the gain comes from individual flow components, and how sensitive is it to model/version, prompting choices, and inference budget?
- Do gains transfer to real-world software development tasks outside competitive programming?
- How stable are results across repeated runs and evaluation choices? The inspected excerpts do not provide uncertainty estimates or detailed run-level variation.
- I inspected pages 1–3 and 6–9; pages 4–5 were not inspected, so implementation and experimental details there may qualify this assessment.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the authors’ stated scope and limitations for assessment. | 0 matches | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect method details and experimental setup beyond the abstract. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 6, "end": 7}` | Review quantitative results and evaluation details supporting reported gains. | read pages [6, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 9}` | Check discussion of evaluation caveats, generalization, and remaining scope. | read pages [8, 9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | The inspected abstract, method, results, and conclusion support a balanced assessment; submit with explicit uncertainty about uninspected details. | citation_validation_failed; #4: not_found | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Resubmit with the exact observed sentence on page 7 for the comparison caveat. | review accepted | [event 30](trace.jsonl#L30) |
