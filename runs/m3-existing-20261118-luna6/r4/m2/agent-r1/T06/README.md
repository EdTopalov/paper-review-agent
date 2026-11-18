# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**agent · ok**

4 model calls · 3 reads · 8.60 s · $0.001463

4 decisions · 4 tool calls · 23536 input tokens (15228 cached) · 569 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SWE-bench contributes a large, execution-validated benchmark of real GitHub issue resolution, paired with baseline evaluations showing that the tested models solve few tasks even with reference-file retrieval. Its realistic repository-scale scope and refreshable construction pipeline make it valuable for evaluating software engineering capabilities, while its single-language coverage and test-based success criterion delimit what conclusions the benchmark supports.

- **strength**: The benchmark links real issues to merged fixes and filters candidates using tests that change from failing to passing, giving task outcomes an execution-based criterion.
  - Page 2 · citation: exact
  - Quote: "We also filter out instances that result in installation or runtime errors."

- **strength**: The input scale and multi-file edits extend beyond short, self-contained code generation tasks.
  - Page 3 · citation: whitespace
  - Quote: "SWE-bench’s reference solutions average editing 1.7 files, 3.0 functions, and 32.8 lines (added or removed)."

- **strength**: The reported baseline results make the benchmark’s difficulty concrete; the oracle setting is explicitly described as less realistic, so it is evidence of model capability under favorable localization rather than ordinary deployment performance.
  - Page 5 · citation: whitespace
  - Quote: "The best performing model, Claude 2, only achieves a mere 4.8% pass rate using the “oracle” retrieval context."

- **limitation**: The authors explicitly bound the study to Python and warn that passing tests alone cannot assure that model-generated changes are reliable or maintainable.
  - Page 9 · citation: normalized
  - Quote: "Lastly, while this work evaluates models using execution-based code testing, relying solely on this method is insufficient to guarantee reliable performance of model generations"

Unresolved questions:

- How representative are the selected popular Python repositories and their test-writing practices of software engineering tasks beyond this benchmark?
- Would broader human review or additional quality criteria change the interpretation of patches that pass the associated tests?
- I did not inspect the full appendices or all qualitative examples; details of filtering edge cases and model prompting remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark construction and task validation details to assess contribution and evidence. | read pages [2, 3, 4] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 5, "end": 7}` | Review evaluation results and interpret the empirical support for benchmark claims. | read pages [5, 6, 7] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 9, "end": 10}` | Inspect stated dataset and evaluation limitations and discussion of benchmark validity. | read pages [9, 10] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | The inspected benchmark construction, evaluation results, and limitations provide enough evidence for an independent assessment. | review accepted | [event 20](trace.jsonl#L20) |
