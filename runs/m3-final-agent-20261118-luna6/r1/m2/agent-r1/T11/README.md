# T11: Executable Code Actions Elicit Better LLM Agents

**agent · ok**

6 model calls · 5 reads · 11.93 s · $0.001866

6 decisions · 6 tool calls · 22938 input tokens (11306 cached) · 636 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

Introduces CodeAct, using executable Python as a multi-turn LLM-agent action space, and CodeActInstruct/CodeActAgent to support that interface. The paper reports gains over text/JSON baselines on complex tool tasks and promising fine-tuning results; it is a substantial systems-and-evaluation contribution, while practical safety and the breadth of evidence remain important boundaries.

- **strength**: Code actions enable iterative interaction and composition using existing programming constructs and packages, rather than a fixed action schema.
  - Page 2 · citation: whitespace
  - Quote: "code inherently supports control and data flow, allowing for the storage of intermediate results as variables for reuse and the composition of multiple tools"

- **strength**: On the authors’ curated complex-task benchmark, CodeAct reports improved success and fewer actions than baselines.
  - Page 3 · citation: whitespace
  - Quote: "CodeAct achieves up to a 20% absolute improvement over baselines on the success rate of solving the problems while requiring up to 30% fewer actions."

- **limitation**: Results for the tuned agent are not uniformly positive: the Llama-2 variant did not improve on M3ToolEval, and the evaluation includes overlap between training and MINT domains.
  - Page 9 · citation: whitespace
  - Quote: "Surprisingly, no improvement is observed for the Llama-2 variant."

- **limitation**: The paper identifies unresolved practical risks of autonomous code execution; this is a stated safety concern, not evidence that an escape occurred.
  - Page 10 · citation: exact
  - Quote: "future work to design better safety mechanism to safeguard autonomous agents."

Unresolved questions:

- How robust are the reported advantages across additional independently designed complex-task benchmarks and real-world deployment conditions?
- What sandbox and permission controls would reliably constrain executable actions, and how would safety trade-offs affect task performance?
- How sensitive are the fine-tuning gains to dataset construction and training choices? Inspection was limited to pages 1–3 and 9–10; detailed methods, tables, and appendices were not inspected.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "20%"}` | Locate reported evaluation results to assess empirical support. | 2 matches on pages [1, 3] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect benchmark design and comparison results for context and support. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "without compromising"}` | Find the reported fine-tuning evaluation and capability-retention evidence. | 2 matches on pages [1, 3] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "sandbox"}` | Check for explicit execution-safety constraints and stated scope boundaries. | 2 matches on pages [10] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 9, "end": 10}` | Read discussion and limitations to distinguish safety concerns from demonstrated shortcomings. | read pages [9, 10] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Evidence covers proposed action interface, benchmark results, evaluation caveat, and stated safety limitation; submit a balanced review. | review accepted | [event 31](trace.jsonl#L31) |
