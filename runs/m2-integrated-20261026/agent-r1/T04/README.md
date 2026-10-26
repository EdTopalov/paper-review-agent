# T04: AgentBench: Evaluating LLMs as Agents

**agent · ok**

6 model calls · 5 reads · 13.73 s · $0.003413

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

AgentBench offers a useful, broad interactive benchmark spanning eight environments and evaluates 25 LLMs, providing a shared testbed and evidence of substantial variation in agent performance. Its breadth and release are valuable, though claims about practical capability depend on heterogeneous tasks and evaluation procedures, several of which use constructed or automated judging. This assessment inspected the introduction, portions of the task protocols, and conclusion/results snippets rather than the complete paper.

- **strength**: The benchmark contributes breadth by combining newly created and adapted settings rather than evaluating agents in only one environment.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments, 5 of which are created in this paper for the first time"

- **strength**: The reported evaluation compares a substantial set of API and open models, with GPT-4 leading across most task datasets.
  - Page 14 · citation: whitespace
  - Quote: "gpt-4 presents the best performance on 7 out of 8 datasets in AgentBench"

- **limitation**: At least one task setting simplifies its underlying game, so results in that environment do not directly establish performance in the more complex original game.
  - Page 8 · citation: exact
  - Quote: "The original design of Aquawar could be too complicated for existing LLMs."

- **uncertainty**: Lateral-puzzle results rely on an automated GPT-3.5 host and judging procedures; the inspected passages do not establish how robust these measures are to evaluator errors or prompt choices.
  - Page 9 · citation: whitespace
  - Quote: "we first design an accurate LTP host system based on gpt-3.5-turbo for automatic game playing"

Unresolved questions:

- How stable are model rankings across repeated runs, prompt variants, and updates to API models?
- How sensitive are aggregate scores to the chosen weighting across environments and task-specific metrics?
- I inspected only selected pages and search excerpts, not all environment protocols, result analyses, or appendices; further claims about reproducibility, task validity, and detailed statistical uncertainty remain unassessed.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper says AgentBench has eight environments, five newly created and three recompiled from published datasets (PDF p. 2), supporting the stated breadth through both new and adapted settings.
- Observation 2: **supported** — The paper evaluates 25 API-based and open-source models (PDF pp. 1, 3), and reports GPT-4 as best on seven of eight datasets (PDF p. 14).
- Observation 3: **supported** — The authors explicitly describe Aquawar as simplified and say they made adjustments to accommodate current LLM performance, including limiting fish types and staging game logic (PDF pp. 8–9). The observation appropriately limits what this setting establishes about the original game.
- Observation 4: **supported** — The paper describes GPT-3.5-turbo as the automatic LTP host and uses GPT-3.5-turbo-based answer extraction and checking (PDF pp. 9–10, 30–33). It also reports that automatic evaluation can be more tolerant than human evaluation for some measures and says it plans to improve the host (PDF p. 30). Thus the qualified concern about evaluator robustness and prompt choices is warranted as an open question, not a demonstrated defect.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper's stated scope and limitations to assess interpretation of the benchmark results. | 1 matches on pages [2] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the benchmark motivation, environment design, and evaluation setup for evidence supporting its contribution. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Review benchmark evaluation methodology and reported model performance for supporting evidence and caveats. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 16, "end": 18}` | Inspect aggregate results and evaluation caveats to judge how strongly the paper's claims are supported. | read pages [16, 17, 18] | [event 20](trace.jsonl#L20) |
| 5 | search_paper `{"query": "GPT-4"}` | Find the main quantitative results table and its surrounding claims for direct evidence of empirical support. | 8 matches on pages [2, 3, 5, 14, 15] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Evidence reviewed covers benchmark scope, selected task protocols, and reported aggregate model results; submit an independent assessment with remaining evidence gaps noted. | review accepted | [event 31](trace.jsonl#L31) |
