# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**agent · ok**

3 model calls · 2 reads · 7.32 s · $0.001845

3 decisions · 3 tool calls · 14251 input tokens (1539 cached) · 500 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

OSWorld contributes a broad, executable benchmark for computer-use agents, pairing real desktop environments with intermediate-state setup and task-specific execution-based evaluation. Its 369-task benchmark and baseline/human comparisons expose a substantial current capability gap, though the inspected material leaves important experimental details and evaluation validity uncertain.

- **strength**: The environment supports flexible real-computer interaction and executable assessment beyond isolated apps.
  - Page 2 · citation: whitespace
  - Quote: "This executable environment allows free-form raw keyboard and mouse control of real computer applications and supports initial task state configuration, execution-based evaluation, and interactive learning across mainstream operating systems (e.g., Ubuntu, Windows, macOS)."

- **strength**: The benchmark has substantial breadth and bespoke evaluation, with extensive construction and review effort.
  - Page 7 · citation: whitespace
  - Quote: "As a result, we implement nearly sample-specific executable evaluation scripts, resulting in a total of 134 unique evaluation functions for assessing functional correctness"

- **strength**: Human evaluation and agent baselines provide evidence of difficulty and a marked gap.
  - Page 9 · citation: whitespace
  - Quote: "the human performance on our tasks was approximately 72.36%"

- **limitation**: The authors acknowledge further quality-control work may be needed, so evaluation false positives/negatives remain a stated concern.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives, which we will leave to future work."

Unresolved questions:

- How robust are the hand-crafted task evaluators to alternate valid solutions and edge cases across all task types?
- What are the detailed baseline protocols, variability, and per-task results? The inspected pages do not include the full experimental section or its tables.
- How well does the curated task set generalize to broader user populations and real-world computer workflows?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark design and task construction to assess contribution and evaluation support. | read pages [2, 3, 4] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 7, "end": 9}` | Inspect benchmark composition and empirical results for evidence and caveats. | read pages [7, 8, 9] | [event 10](trace.jsonl#L10) |
| 3 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Evidence covers the environment, benchmark creation, empirical task results, and disclosed quality-control caveat; submit a provisional assessment noting uninspected experimental details. | review accepted | [event 16](trace.jsonl#L16) |
