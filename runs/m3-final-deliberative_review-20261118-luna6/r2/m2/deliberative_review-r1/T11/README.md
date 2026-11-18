# T11: Executable Code Actions Elicit Better LLM Agents

**deliberative_review · ok**

6 model calls · 3 reads · 20.27 s · $0.003663

6 decisions · 4 tool calls · 24097 input tokens (1344 cached) · 1630 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

The paper proposes CodeAct, using executable Python as a flexible action format for multi-turn LLM agents, and reports comparisons on tool-use benchmarks alongside an instruction-tuning dataset and agent model. The inspected excerpts suggest a promising contribution with positive benchmark results, but do not expose enough of the later evaluation to assess the dataset and model claims in depth.

- **strength**: The paper reports a broad comparison across 17 LLMs, with CodeAct winning on task success for most of them. This supports the central action-format claim, although the inspected excerpts do not provide the full experimental setup or results.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs)"

- **strength**: The work also contributes a 7k-interaction instruction-tuning dataset, with the stated focus on multi-turn agent-environment behavior. The excerpt describes its scope, but not the underlying data-quality evidence or full evaluation.
  - Page 3 · citation: whitespace
  - Quote: "CodeActInstruct consisting of 7k high-quality multi-turn interaction trajectories with CodeAct"

- **limitation**: The authors acknowledge a safety boundary associated with executing generated code. The inspected passage identifies sandbox escape as a potential risk and calls for safeguards; it does not establish that a sandbox escape occurred.
  - Page 10 · citation: whitespace
  - Quote: "such an agent may potentially break free of the sandbox restriction"

Unresolved questions:

- How were the benchmarks constructed and controlled, and how robust are the reported gains across task types and evaluation conditions?
- What detailed results support the claims that CodeActInstruct improves agent tasks without compromising general capability, and how broad is CodeActAgent’s out-of-domain evaluation?
- What execution restrictions and safety mechanisms are implemented, and how are they tested?
- Inspection was partial: 21 of 29 pages were uninspected, and several observed pages contain only partial excerpts. Conclusions about detailed methods, results, and limitations therefore remain provisional.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the benchmark and experimental sections for the evaluation setup, baselines, measured results, and whether they support the claimed CodeAct success-rate gains.; Check later sections for evidence behind claims about CodeActInstruct, retained general capability, and CodeActAgent, including evaluation scope and stated limitations.; Verify whether the paper discusses safety, execution constraints, or other boundaries of running generated code; currently only page 1 is available, so do not treat uninspected sections as absent. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [1, 2, 3, 5, 9] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 2 matches on pages [10] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | 8 matches on pages [1, 3, 4, 7] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: approve | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "success rate"}` | Find evaluation evidence and results for CodeAct and comparison baselines. | 8 matches on pages [1, 2, 3, 5, 9] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "sandbox"}` | Check the paper's discussion of code execution constraints and safety boundaries. | 2 matches on pages [10] | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "CodeActInstruct"}` | Investigate the later experimental evidence for the trained agent claims and evaluation scope. | 8 matches on pages [1, 3, 4, 7] | [event 22](trace.jsonl#L22) |
| 6 | submit_review `{"review": {"score": 0.68, "observations": 3}}` | Submit after the enforced critique and source validation. | review accepted | [event 34](trace.jsonl#L34) |
