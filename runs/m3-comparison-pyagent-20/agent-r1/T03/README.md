# T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**agent · ok**

3 model calls · 2 reads · 8.73 s · $0.001035

3 decisions · 3 tool calls · 7829 input tokens (1250 cached) · 420 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.67

AutoGen presents a general framework for composing customizable LLM, tool, and human agents through flexible conversations, illustrated across varied application patterns. Its practical integration and human participation are meaningful contributions, but the inspected empirical evidence is narrow and mostly illustrative rather than a broad evaluation of framework-level benefits.

- **strength**: The paper frames AutoGen as general infrastructure, with conversation patterns spanning static and dynamic configurations and support for execution and human participation.
  - Page 8 · citation: exact
  - Quote: "Infrastructure ✓ ✗ ✓ ✗ ✗"

- **strength**: The application section covers several distinct use cases, and the math evaluation uses explicit comparison systems and repeated trials on two problems.
  - Page 9 · citation: exact
  - Quote: "We compare AutoGen with the following LLM-based agent systems."

- **limitation**: The inspected autonomous math evaluation is very small, limiting how much it can establish about comparative performance.
  - Page 10 · citation: whitespace
  - Quote: "We use two level-5 problems from the MATH dataset for the qualitative evaluation and test on each problem for 3 times."

Unresolved questions:

- How do the other application demonstrations perform under systematic, comparable evaluation?
- How robust are the framework's benefits across larger task sets, different LLM backends, and varied human/tool configurations?
- The assessment inspected pages 8–10 and search snippets, not the complete report; claims and limitations elsewhere may change this evaluation.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper's explicit scope or limitations discussion for a balanced assessment. | 7 matches on pages [3, 4, 7, 15, 20, 24] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 8, "end": 10}` | Inspect the framework's core design and evidence/examples to assess technical contribution and support. | read pages [8, 9, 10] | [event 10](trace.jsonl#L10) |
| 3 | submit_review `{"review": {"score": 0.67, "observations": 3}}` | The framework design and a concrete application evaluation have been inspected; submit a provisional evidence-based reading-club assessment while noting the narrow evaluation inspected. | review accepted | [event 16](trace.jsonl#L16) |
