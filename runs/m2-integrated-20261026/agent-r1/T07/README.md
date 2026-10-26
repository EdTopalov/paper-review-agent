# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**agent · ok**

5 model calls · 3 reads · 14.69 s · $0.001710

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

OSWorld makes a substantial benchmark contribution by providing a controllable real-computer environment and diverse tasks with per-task executable evaluation, enabling assessment beyond browser-only or static-demonstration settings. Careful construction and human/baseline measurements make it useful, while empirical conclusions remain bounded by its Ubuntu-centered task suite and disclosed evaluation uncertainty.

- **strength**: The benchmark’s task coverage and execution-based setup support evaluation of multi-application workflows, with substantial annotation and quality-check effort.
  - Page 7 · citation: whitespace
  - Quote: "each example is further scrutinized and iterated upon by different individuals three times from the perspective of alignment with the instruction and correctness under different solutions"

- **strength**: Human evaluation establishes a meaningful capability gap on the benchmark.
  - Page 9 · citation: whitespace
  - Quote: "the human performance on our tasks was approximately 72.36%"

- **limitation**: The paper notes residual evaluator error risk despite extensive checks, relevant to interpreting execution-based scores.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives, which we will leave to future work."

- **limitation**: The primary task suite is Ubuntu-centered; Windows is supplementary in the inspected material.
  - Page 6 · citation: whitespace
  - Quote: "We introduce the OSW ORLD benchmark, which encompasses 369 real computing tasks defined and executed on Ubuntu."

Unresolved questions:

- How robust are success rates to alternative valid completion paths and evaluator edge cases across the full task suite?
- I inspected pages 1 and 6–10, but not the remaining methods, full ablations, or later discussion; what additional experimental details or limitations do those sections report?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper reports 101 multi-app workflow tasks among 369 Ubuntu tasks and describes substantial annotation effort, repeated cross-checking, and quality-control rounds (PDF pp. 6–8). The claim is appropriately scoped to the benchmark and its construction.
- Observation 2: **supported** — The human study reports 72.36% overall performance, compared with baseline agent success rates far below that level (PDF pp. 9–11). This supports a meaningful measured capability gap on this benchmark.
- Observation 3: **supported** — The authors explicitly state that further red-teaming could reduce false positives and negatives, leaving this for future work (PDF p. 8). This supports the qualified concern about residual evaluator error risk.
- Observation 4: **supported** — The paper identifies the 369-task main benchmark as defined and executed on Ubuntu and separately reports 43 Windows tasks (PDF p. 6). Calling the suite Ubuntu-centered and Windows supplementary is justified.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "human evaluation"}` | Locate evaluation results and human-performance evidence for assessing benchmark support. | 2 matches on pages [7, 9] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 6, "end": 7}` | Inspect benchmark construction, task composition, and validation procedures. | read pages [6, 7] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Inspect baseline results, benchmark human comparisons, and stated evaluation caveats. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Evidence covers benchmark design, quality checks, human comparison, and baseline results; submit a bounded assessment noting unread later analyses. | citation_validation_failed; #4: not_found | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Correct the Ubuntu-scope quotation to the exact observed wording and resubmit the review. | review accepted | [event 25](trace.jsonl#L25) |
