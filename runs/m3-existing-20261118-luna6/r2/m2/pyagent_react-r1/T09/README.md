# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**pyagent_react · ok**

5 model calls · 3 reads · 18.65 s · $0.001848

5 decisions · 4 tool calls · 31856 input tokens (23065 cached) · 1038 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

AGENTLESS presents a deliberately simple, hierarchical localization-and-repair pipeline for repository-level bug fixing, with patch sampling, filtering, and ranking. Its evaluation reports competitive SWE-bench Lite performance at low cost, adds a manually classified filtered benchmark, and analyzes where the approach succeeds and struggles. The work is a useful, interpretable baseline and methodological challenge to the assumption that complex agents are necessary, though its benchmark comparisons and filtered evaluation leave important questions open.

- **strength**: The paper describes a concrete and interpretable pipeline, including hierarchical localization and candidate patch filtering and ranking.
  - Page 4 · citation: whitespace
  - Quote: "we perform a simple filtering to remove any patches with syntax errors and regression test failures, and use majority voting to rank the remaining patches."

- **strength**: The reported evaluation supports the approach’s usefulness: it resolves 82 of 300 issues at an average cost of $0.34, and component comparisons show gains from sampling and filtering.
  - Page 8 · citation: whitespace
  - Quote: "Finally, the fullAGENTLESS performance is achieved by further applying filtering to select only the patches which can successfully pass the existing regressions tests."

- **limitation**: The authors identify a weakness on problems without location clues: closed-source agent tools perform better, suggesting that the simple approach can struggle with harder localization.
  - Page 11 · citation: whitespace
  - Quote: "the closed-source agent tools perform better compared to AGENTLESS in the case where no location clue is provided."

- **uncertainty**: The filtered benchmark excludes problematic cases, but the authors could not rerun commercial tools on it; thus, the reported ranking on Lite-S is not a fresh, controlled comparison across all systems.
  - Page 10 · citation: whitespace
  - Quote: "as we are not able to run commercial tools ourselves on the modified problems, we simply exclude the problematic problems in the below evaluation."

Unresolved questions:

- How robust are comparisons when all approaches are run under matched models, prompts, budgets, and evaluation conditions?
- How reproducible and generalizable is the manually curated SWE-bench Lite-S classification and filtering?
- How would the pipeline perform on repositories or software engineering tasks beyond the inspected SWE-bench Lite evaluation? The inspected material covered pages 1–11 of 17; later sections and appendices remain uninspected.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the approach and benchmark setup. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 7, "end": 9}` | Inspect benchmark results and evaluation comparisons. | read pages [7, 8, 9] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 10, "end": 11}` | Inspect the cleaned benchmark and stated evaluation limitations. | read pages [10, 11] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Submit an evidence-based assessment from the abstract, method, and inspected evaluation pages. | review accepted | [event 25](trace.jsonl#L25) |
