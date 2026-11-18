# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**agent · ok**

6 model calls · 5 reads · 12.27 s · $0.002629

6 decisions · 6 tool calls · 30425 input tokens (13201 cached) · 725 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AGENTLESS presents a simple hierarchical localization-then-repair method for repository-level software issues, challenging the assumption that complex autonomous agents are necessary. It reports competitive repair performance at low inference cost on SWE-bench Lite, provides component-level experiments and unique-fix analysis, and proposes a manually filtered benchmark subset. Its support is promising but bounded by the benchmark, reliance on reported baseline results, and its own exclusion of problematic items.

- **strength**: The approach reports strong performance for its simplicity and cost, and remains competitive on the authors' filtered subset.
  - Page 7 · citation: whitespace
  - Quote: "AGENTLESS GPT-4o 82 (27.33%) $0.34 42,376 34.3% 51.0% 68.7% 27.33% (82 / 300) on SWE-bench Lite."

- **strength**: The paper tests contributions of repair selection stages rather than relying only on aggregate results.
  - Page 8 · citation: exact
  - Quote: "single sample 70 (23.33%) $0.11\n+ multiple samples\n& maj. voting 78 (26.00%) $0.34\n+ test filtering\n(full AGENTLESS) 82 (27.33%) $0.34"

- **limitation**: The baseline comparison is partly indirect: the authors use published results, and note limited reproducibility and verification for closed systems.
  - Page 6 · citation: whitespace
  - Quote: "For baseline tools, we directly use the reported results either from the official leaderboard [29] or from the tool’s official paper/repository."

- **limitation**: The filtered evaluation cannot compare commercial tools under the modified benchmark because the authors did not run them there.
  - Page 10 · citation: whitespace
  - Quote: "However, as we are not able to run commercial tools ourselves on the modified problems, we simply exclude the problematic problems in the below evaluation."

Unresolved questions:

- Would independently rerunning the compared methods under a shared evaluation setup preserve the reported performance and cost advantage?
- How robust are the manually selected SWE-bench Lite-S exclusions to alternative classification decisions, and how would repaired benchmark issues affect conclusions?
- I inspected pages 1–3 via search excerpts and pages 6–8 and 10 directly; I did not inspect the full methods, all problem-classification details, or later discussion, so broader limitations and implementation specifics remain uncertain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper's stated scope limits for a balanced assessment. | 3 matches on pages [2, 3, 12] | [event 5](trace.jsonl#L5) |
| 2 | search_paper `{"query": "27.33%"}` | Find reported quantitative results and comparison details. | 7 matches on pages [1, 3, 6, 7, 8, 10] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 6, "end": 8}` | Inspect evaluation tables and ablation evidence on pages 6–8. | read pages [6, 7, 8] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "SWE-bench Lite-S"}` | Locate filtered benchmark results and the authors' rationale for dataset exclusions. | 8 matches on pages [3, 10, 11, 12] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 10, "end": 10}` | Inspect filtered benchmark description and reported comparison figures. | read pages [10] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | The observed abstract, evaluation, ablation, and filtered-benchmark pages provide enough evidence for a qualified review; remaining uncertainties are acknowledged. | review accepted | [event 31](trace.jsonl#L31) |
