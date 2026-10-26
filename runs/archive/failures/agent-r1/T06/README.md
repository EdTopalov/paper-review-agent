# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**agent · ok**

5 model calls · 4 reads · 11.22 s · $0.001393

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SWE-bench introduces a substantial, realistic benchmark for repository-level software issue resolution, pairing real GitHub issues and codebase snapshots with execution-based tests. The careful filtering pipeline and challenging baseline evaluations make it a useful research contribution, though the evaluation is limited in scope and passing tests does not establish patch quality.

- **strength**: The benchmark operationalizes real-world repository-level issue resolution at useful scale, with filtering that checks issue-linked PRs and test behavior.
  - Page 2 · citation: no strict match
  - Quote: "Through these stages of filtering, the original 90,000 PRs are filtered down to the 2,294 task instances"

- **strength**: Results substantiate substantial difficulty for the tested models, including an oracle-context setting that offers relevant-file information.
  - Page 6 · citation: no strict match
  - Quote: "the best performing model, Claude 2, only achieves a mere 4.8% pass rate using the “oracle” retrieval context."

- **limitation**: The authors explicitly scope the data to Python and caution that execution-based testing alone cannot ensure solution quality.
  - Page 9 · citation: strict match
  - Quote: "relying solely on this method is insufficient to guarantee reliable performance of model generations"

- **uncertainty**: The paper reports baseline results across several models and retrieval conditions, but I did not inspect the full prompting and implementation appendices; the inspected pages do not settle how sensitive outcomes are to those choices.
  - Page 5 · citation: strict match
  - Quote: "there are only a few models that are currently suitable for SWE-bench"

Unresolved questions:

- How robust are task selection and measured resolution rates to the benchmark’s filtering and test-selection choices?
- How would strong tool-using agents and newer models perform under comparable, fully specified evaluation conditions?
- How often do test-passing generated patches meet human standards for correctness, maintainability, and completeness?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes 2,294 tasks drawn from real GitHub issues and merged PRs, filtered for issue resolution, test changes, and fail-to-pass test behavior (pp. 1–3, 15, 18–19). That supports the claim of realistic, useful-scale benchmark construction.
- Observation 2: **supported** — The paper reports low resolution rates, including Claude 2’s 4.8% with oracle retrieval (pp. 5–6). Oracle retrieval provides files edited by the reference patch, while the authors note it is less realistic and may omit needed context (p. 4).
- Observation 3: **supported** — The authors state that all benchmark instances are Python and that execution-based testing alone cannot guarantee reliable performance or capture qualities such as comprehensiveness, efficiency, and readability (p. 9).
- Observation 4: **supported** — This is carefully framed as an uncertainty about the inspected pages, not a claim that the paper lacks details. The paper supplies additional prompting and inference information in the appendices, including a prompt template and greedy-decoding setup (pp. 24–25); it also says prompt variations generally did not substantially affect performance, with stated exceptions (p. 25).

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "evaluation setup results SWE-bench Lite"}` | Locate benchmark construction and quantitative evaluation details. | 0 matches | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect benchmark construction methodology and dataset filtering details. | response recorded | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 6}` | Check model evaluation tables and supporting results. | response recorded | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 9, "end": 10}` | Inspect authors' stated limitations, threats, and benchmark caveats. | response recorded | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Evidence covers benchmark design, quantitative baseline results, and discussion limitations; submit a balanced assessment while noting uninspected methodological appendices. | review accepted | [event 25](trace.jsonl#L25) |
