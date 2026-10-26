# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**agent · ok**

6 model calls · 5 reads · 13.88 s · $0.003218

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

AGENTLESS presents a deliberately simple repository-repair pipeline—hierarchical code localization followed by sampled patch generation, regression-test filtering, and majority voting—and shows that this design can perform competitively on SWE-bench Lite at low reported inference cost. Its useful additional contribution is a manual classification of benchmark problems and a filtered 252-problem variant, though comparative claims remain bounded by the benchmark and by reliance on reported baseline results.

- **strength**: The method is clearly specified as a practical two-stage system, and combines localization with patch selection rather than relying on autonomous tool-use planning.
  - Page 5 · citation: exact
  - Quote: "AGENTLESS solves repository-level issues using a simple step-by-step procedure."

- **strength**: On the original benchmark, the paper reports 82 resolved problems (27.33%) at $0.34 average cost; its ablations indicate gains from multi-sampling/voting and test filtering.
  - Page 8 · citation: whitespace
  - Quote: "Finally, the fullAGENTLESS performance is achieved by further applying filtering to select only the patches which can successfully pass the existing regressions tests."

- **strength**: The authors identify concrete benchmark-quality concerns and provide a filtered evaluation set; AGENTLESS resolves 71/252 (28.17%) there.
  - Page 10 · citation: exact
  - Quote: "We refer to our subset of 252 problems as SWE-bench Lite-S."

- **limitation**: Comparisons on the filtered set are not fully controlled: the authors could not rerun commercial systems on it, so their outcomes derive from excluding cases in prior reported results.
  - Page 10 · citation: whitespace
  - Quote: "as we are not able to run commercial tools ourselves on the modified problems, we simply exclude the problematic problems in the below evaluation."

Unresolved questions:

- How robust are the reported rankings and cost advantages across other repository-level benchmarks, model versions, and independently rerun baselines?
- Would the filtered Lite-S classifications and performance hold under independent annotation or a larger benchmark?
- I inspected the method, selected results and analysis pages, but not the full paper's appendices or implementation details; reproducibility and sensitivity beyond the reported setup remain uncertain.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes a two-phase localization-and-repair pipeline, with hierarchical localization and patch generation, filtering, and voting; it contrasts this with agent-based tool-use planning (PDF pp. 2–5).
- Observation 2: **supported** — The paper reports 82/300 resolved (27.33%) and $0.34 average cost (PDF pp. 6–7). Its ablation reports 70 fixes with one sample, 78 with multiple samples and majority voting, and 82 after test filtering (PDF p. 8).
- Observation 3: **supported** — The authors report a manual classification of SWE-bench Lite issues and define Lite-S as a 252-problem subset; Table 4 reports 71 resolved (28.17%) by AGENTLESS (PDF pp. 9–10).
- Observation 4: **supported** — The paper explicitly says it could not run commercial tools on the modified problems and instead excluded problematic cases from their prior results for the Lite-S evaluation (PDF p. 10).

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "SWE-bench Lite-S"}` | Locate the paper's evaluation setup and claims for assessing evidence. | 8 matches on pages [3, 10, 11, 12] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 6}` | Inspect method details and reported experimental evidence. | read pages [4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 7, "end": 10}` | Inspect result comparisons, cost evidence, and benchmark filtering rationale. | invalid_page_range | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 7, "end": 9}` | Read results and benchmark limitations to ground the assessment. | read pages [7, 8, 9] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 10, "end": 12}` | Check filtered benchmark results and stated limitations before final scoring. | read pages [10, 11, 12] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Evidence covers the method, benchmark performance, ablations, and filtered-set caveats; submit an independent paper assessment. | review accepted | [event 31](trace.jsonl#L31) |
