# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**agent · ok**

4 model calls · 2 reads · 13.63 s · $0.001430

4 decisions · 4 tool calls · 13439 input tokens (5958 cached) · 896 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

WebArena contributes a self-hostable, multi-domain web environment and an 812-task benchmark evaluated by functional outcomes rather than exact action matching. It offers a useful testbed for long-horizon web agents, although the inspected pages establish the design rationale and headline challenge more directly than full empirical validation.

- **strength**: The paper combines functional websites, tools, and knowledge sources in a reproducible environment rather than relying on live sites.
  - Page 2 · citation: whitespace
  - Quote: "four fully operational, self-hosted web applications"

- **strength**: Task verification targets goal completion and accommodates alternative valid paths, a strong benchmark design choice.
  - Page 2 · citation: exact
  - Quote: "accommodates a range of potential valid paths to achieve the same goal"

- **strength**: The benchmark includes a substantial suite of long-horizon tasks; the reported best GPT-4 result illustrates task difficulty.
  - Page 2 · citation: whitespace
  - Quote: "we release a ready-to-use benchmark with 812 long-horizon web-based tasks"

- **limitation**: The inspected selection rationale is based on the authors’ browser histories and selects four categories, leaving representativeness beyond these categories unanswered, not demonstrated defective.
  - Page 3 · citation: whitespace
  - Quote: "we first conducted an analysis of approximately 200 examples from the authors’ actual web browser histories"

Unresolved questions:

- How are tasks authored and validated, and what evidence supports the reliability of their functional evaluators?
- What are the full agent comparisons, variability estimates, and failure analyses? Later experimental pages and appendices were not inspected, so these remain open rather than asserted deficiencies.
- How well does benchmark performance transfer to live websites or web tasks outside the four selected domains?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the authors’ explicit discussion of scope and limitations for a balanced assessment. | 2 matches on pages [2, 11] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark design, task construction, and evaluation evidence supporting the paper’s claims. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Evidence supports the benchmark’s core contribution and realism claims; submit a provisional assessment while explicitly noting that later experimental details were not inspected. | citation_validation_failed; #1: not_found | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Correct the first citation to match the exact observed wording and resubmit with evidence from the inspected pages. | review accepted | [event 22](trace.jsonl#L22) |
