# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**pyagent_react · ok**

6 model calls · 4 reads · 14.70 s · $0.002187

6 decisions · 5 tool calls · 42814 input tokens (31190 cached) · 846 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

AGENTLESS presents a straightforward localization-then-repair pipeline that restricts LLM autonomy, samples candidate patches, filters by tests, and ranks by majority voting. Its results make a useful case that a comparatively simple, low-cost approach can be competitive on SWE-bench Lite. The manual issue classification and filtered Lite-S set add a benchmark-analysis contribution, though evidence is centered on one model and comparisons partly rely on reported results from other systems.

- **strength**: The paper gives a concrete, interpretable pipeline, and its repair process combines patch sampling, regression-test filtering, and normalized-patch voting.
  - Page 5 · citation: whitespace
  - Quote: "AGENTLESS uses a simple two phase approach to first localize and then repair the bug without relying on any agents for decision-making."

- **strength**: The reported Lite result is competitive and inexpensive, while the paper also reports per-component localization and repair analyses.
  - Page 7 · citation: exact
  - Quote: "AGENTLESS\n GPT-4o 82 (27.33%) $0.34 42,376 34.3% 51.0% 68.7%"

- **limitation**: The Lite-S comparison is not a fresh evaluation of commercial systems on the filtered set, limiting how directly its rankings can be interpreted.
  - Page 10 · citation: exact
  - Quote: "as we are not able to run commercial\ntools ourselves on the modified problems, we simply exclude the problematic problems in\nthe below evaluation."

- **uncertainty**: The inspected setup describes a single underlying model for AGENTLESS; it remains unclear how robust the approach is across different LLMs.
  - Page 6 · citation: exact
  - Quote: "We implement AGENTLESS using GPT-4o (gpt-4o-2024-05-13) [45]."

Unresolved questions:

- How well does the approach transfer to other LLMs, repositories, and software-engineering benchmarks?
- Would independently rerunning the baselines under the same evaluation setup alter the cost or performance comparisons?
- How reproducible and stable is the manual issue classification and the resulting Lite-S set?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the method and benchmark design. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 7, "end": 9}` | Inspect quantitative evaluation and benchmark results. | read pages [7, 8, 9] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 10, "end": 12}` | Inspect the revised benchmark and stated limitations. | read pages [10, 11, 12] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 5, "end": 6}` | Check evaluation protocol and implementation details. | read pages [5, 6] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Submit a balanced assessment grounded in the inspected method and evaluation pages. | review accepted | [event 30](trace.jsonl#L30) |
