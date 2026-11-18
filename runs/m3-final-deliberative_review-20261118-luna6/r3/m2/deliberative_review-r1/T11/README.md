# T11: Executable Code Actions Elicit Better LLM Agents

**deliberative_review · ok**

9 model calls · 4 reads · 44.29 s · $0.009538

9 decisions · 6 tool calls · 60083 input tokens (1344 cached) · 4391 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

The paper proposes CodeAct, using executable Python as a flexible, interactive action format for LLM agents, and evaluates it against text and JSON. It reports improvements on complex tool-use tasks and introduces a 7,139-trajectory instruction dataset and fine-tuned agents. The inspected evidence supports a promising contribution, but does not establish broad real-world effectiveness; substantial parts of the evaluation and limitations remain uninspected.

- **strength**: On M3ToolEval, the paper reports higher task success for 12 of 17 models, supporting a majority-model advantage on this benchmark.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs)"

- **strength**: The paper also reports fewer average turns for a majority of evaluated models on M3ToolEval.
  - Page 5 · citation: whitespace
  - Quote: "using CodeAct requires a lower average number of turns (12 out of 17 evaluated LLMs)"

- **limitation**: The atomic API-call table shows CodeAct is not uniformly best: this CodeLlama example scores higher with text actions than CodeAct. This qualifies, rather than negates, the broader results.
  - Page 5 · citation: exact
  - Quote: "CodeLlama-7b-Instruct-hf12.5 12.0 17.0"

- **strength**: The dataset is designed around four agent-use cases and draws on five existing datasets. Table 5 reports improvements on some agent tasks, but the LLaMA-2 variant has 0.0 on M3ToolEval, so gains are not universal.
  - Page 7 · citation: exact
  - Quote: "We consider four main use cases in agent-environment interaction and repurpose five existing datasets"

Unresolved questions:

- How representative and difficult is M3ToolEval, and how sensitive are its outcomes to task construction and evaluation procedures?
- What complete evidence supports preservation of general capability across the reported evaluations? Table 5 provides some results, but full training and evaluation details were not inspected.
- What execution safeguards constrain generated code, and what are their practical effects? Execution details and most of the limitations discussion were not available in the inspected excerpts.
- Important inspection gap: 18 of 29 pages were uninspected, and several available page excerpts are partial.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the evaluation sections and tables to verify whether CodeAct’s claimed success-rate gains are supported across the reported models, benchmarks, and baselines, and note the evaluation scope.; Inspect the dataset, fine-tuning, and capability-retention evidence for CodeActInstruct and CodeActAgent, including the basis for the claims about improved agent tasks and preserved general capability.; Inspect the paper’s discussion of limitations and execution setup to distinguish stated scope boundaries from unresolved questions; only page 1 is currently available, so do not infer findin … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 3 matches on pages [10] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 7 matches on pages [1, 4, 5, 12, 16] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | 8 matches on pages [2, 4, 5, 8, 9, 16] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: investigate; Issues: The first observation claims CodeAct uses fewer turns for a majority of models, but its quote supports only the success-rate claim. The source archive contains a separate supporting excerpt (E15), so this is a citation-support mismatch rather than evidence that the claim is false.; The dataset, fine-tuning, and capability-retention evidence required by C2 remains largely uninspected. The draft appropriately flags this gap, but targeted inspection is needed to assess a central contribution before approving the assessment.; Target: On the uninspected pages, w … | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | targeted_read | read pages [6, 7, 8] (text truncated by tool) | [event 34](trace.jsonl#L34) · [event 39](trace.jsonl#L39) |
| 8 | revise | Draft revised; Changes: Addressed the critic’s citation concern by separating the M3ToolEval success-rate and fewer-turn claims and using the distinct available excerpts. The follow-up inspection supports a more specific account of CodeActInstruct’s data composition and Table 5’s results; it also shows a mixed pattern rather than universal gains. The score reflects these added details without treating incomplete inspection as evidence of a defect. | [event 40](trace.jsonl#L40) · [event 43](trace.jsonl#L43) |
| 9 | revise | Draft revised; Changes: Added the separate observed quotation supporting the fewer-turn claim and replaced the unsupported dataset quotation with an exact excerpt from page 7. The critic's concern about missing dataset and fine-tuning evidence is addressed with the available excerpts; substantial methodology and evaluation details remain uninspected, so uncertainty is retained. | [event 48](trace.jsonl#L48) · [event 51](trace.jsonl#L51) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "limitations"}` | Locate stated scope limitations and related discussion as part of assessing evidence and execution setup. | 3 matches on pages [10] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "API-Bank"}` | Locate evaluation results/tables and inspect evidence for claimed CodeAct gains. | 7 matches on pages [1, 4, 5, 12, 16] | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "M3ToolEval"}` | Inspect reported multi-turn evaluation results and benchmark scope to assess claimed gains. | 8 matches on pages [2, 4, 5, 8, 9, 16] | [event 22](trace.jsonl#L22) |
| 7 | read_pages `{"start": 6, "end": 8}` | Inspect dataset and fine-tuning results for the requested evidence. | read pages [6, 7, 8] (text truncated by tool) | [event 37](trace.jsonl#L37) |
| 8 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit after the enforced critique and source validation. | citation_validation_failed; #3: not_found | [event 45](trace.jsonl#L45) |
| 9 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 53](trace.jsonl#L53) |
