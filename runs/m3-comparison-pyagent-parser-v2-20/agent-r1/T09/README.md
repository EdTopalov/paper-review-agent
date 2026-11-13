# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**agent · ok**

3 model calls · 2 reads · 8.28 s · $0.001453

3 decisions · 3 tool calls · 10962 input tokens (1475 cached) · 524 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

AGENTLESS makes a useful, interpretable case that a fixed localization-then-repair pipeline can compete with more elaborate LLM software agents. On SWE-bench Lite it reports 82 fixes (27.33%) at an average cost of $0.34, and contributes a manual classification of benchmark issues plus a filtered variant. The benchmark results support the approach on this evaluation, but do not establish broader superiority or isolate performance across alternative models and settings.

- **strength**: The paper presents a concrete, simple alternative to autonomous tool-using agents, with hierarchical code localization followed by candidate patch generation and selection.
  - Page 2 · citation: exact
  - Quote: "AGENTLESS follows a simple two phase process: localization and repair."

- **strength**: The reported repair ablation gives incremental evidence for multiple samples and test-based filtering, with full performance reported at 82 fixes.
  - Page 8 · citation: exact
  - Quote: "+ test filtering\n(full AGENTLESS) 82 (27.33%) $0.34"

- **strength**: The manual benchmark audit identifies concrete description-quality and solution-leakage concerns, motivating a more carefully filtered evaluation set.
  - Page 9 · citation: exact
  - Quote: "4.3% of issues contain the exact ground truth patch in the issue description"

- **limitation**: Localization is imperfect: the reported exact edit-location stage retains ground-truth locations in only about half of cases, a meaningful constraint on this pipeline.
  - Page 8 · citation: exact
  - Quote: "3. edit locations 50.8% 246 $0.05"

Unresolved questions:

- How robust are the comparative performance and cost claims across models, inference configurations, and benchmark versions?
- How reproducible and reliable are the manual classifications and the construction of SWE-bench Lite-S?
- I inspected pages 1–3 and 8–9 only; details elsewhere, including the complete evaluation protocol, comparisons, and Lite-S results, remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 3}` | Inspect method and benchmark setup to assess contribution and evidence. | read pages [2, 3] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 8, "end": 9}` | Review quantitative results and benchmark caveats for strength and limits. | read pages [8, 9] | [event 10](trace.jsonl#L10) |
| 3 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Evidence covers the proposed workflow, quantitative ablations, and benchmark audit; submit a balanced assessment while noting uninspected sections. | review accepted | [event 16](trace.jsonl#L16) |
