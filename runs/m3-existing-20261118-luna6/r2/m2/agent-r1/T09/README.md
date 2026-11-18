# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**agent · ok**

6 model calls · 5 reads · 11.77 s · $0.002756

6 decisions · 6 tool calls · 35576 input tokens (17266 cached) · 626 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AGENTLESS presents a simple, interpretable localization-then-repair pipeline and demonstrates competitive repository-level issue resolution at low reported inference cost. Its contribution is both a practical baseline and a critique of benchmark quality, although comparisons rely partly on reported results for tools the authors could not rerun, and the evaluation is limited to SWE-bench Lite with GPT-4o.

- **strength**: The method is a clear hierarchical localization and patch-generation pipeline rather than an autonomous action-taking agent.
  - Page 5 · citation: exact
  - Quote: "AGENTLESS solves repository-level issues using a simple step-by-step procedure."

- **strength**: On the original benchmark, the reported solve rate and per-issue cost are competitive with open-source approaches.
  - Page 7 · citation: exact
  - Quote: "AGENTLESS\n GPT-4o 82 (27.33%) $0.34 42,376 34.3% 51.0% 68.7%"

- **strength**: The paper’s manual audit identifies problematic benchmark instances and evaluates a filtered 252-problem subset; Agentless reports 28.17% there.
  - Page 10 · citation: exact
  - Quote: "AGENTLESS\n GPT-4o 82 (27.33%) 5 71 (28.17%) 5"

- **limitation**: The modified-set comparison cannot directly validate commercial baselines on the filtered problems, limiting apples-to-apples inference.
  - Page 10 · citation: whitespace
  - Quote: "as we are not able to run commercial tools ourselves on the modified problems, we simply exclude the problematic problems in the below evaluation."

Unresolved questions:

- Would the comparative rankings persist if all systems were rerun under the same model, harness, and evaluation setup?
- How robust are the results across LLMs and repository-level benchmarks beyond SWE-bench Lite?
- I inspected the method, selected evaluation tables, and benchmark classification/filtering discussion, not the full paper’s appendices or all implementation details.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the authors’ stated limitations to assess scope. | 3 matches on pages [2, 3, 12] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 6}` | Inspect method and evaluation results supporting the contribution. | read pages [4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 7, "end": 8}` | Review benchmark comparisons and the filtered-set analysis. | read pages [7, 8] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "SWE-bench Lite-S"}` | Find filtered benchmark outcomes and caveats for balanced evaluation. | 8 matches on pages [3, 10, 11, 12] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 9, "end": 10}` | Inspect problem-labeling methodology and filtered benchmark claims. | read pages [9, 10] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence covers approach, benchmark results, filtering analysis, and key evaluation caveats; submit an evidence-based assessment. | review accepted | [event 31](trace.jsonl#L31) |
