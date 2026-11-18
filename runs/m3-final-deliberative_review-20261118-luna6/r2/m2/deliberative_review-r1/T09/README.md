# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**deliberative_review · ok**

7 model calls · 3 reads · 31.69 s · $0.005931

7 decisions · 4 tool calls · 37288 input tokens (1274 cached) · 2853 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

AGENTLESS presents a simple, hierarchical localization-and-repair workflow for repository-level software issues and evaluates it on SWE-bench Lite. The reported results make a useful case that a non-agentic approach can be competitive, while the paper also identifies problematic benchmark instances and proposes a filtered subset. The contribution is practically relevant, though the evidence available here does not establish the full breadth of its performance or the reliability of the benchmark reclassification.

- **strength**: The paper gives a concrete, interpretable workflow: hierarchical localization followed by patch generation, filtering, and voting.
  - Page 4 · citation: exact
  - Quote: "AGENTLESS addresses this by using a simple three-step hierarchical localization process:"

- **strength**: The evaluation uses a functional-correctness benchmark and reports a substantial result for the proposed method; the available excerpt does not include the full comparison table.
  - Page 6 · citation: whitespace
  - Quote: "We observe that AGENTLESS is able to solve 82 out of 300 problems (27.33%)."

- **limitation**: The authors rely on reported baseline results rather than rerunning all baseline tools, limiting direct comparability and verification.
  - Page 6 · citation: whitespace
  - Quote: "For baseline tools, we directly use the reported results either from the official leaderboard [29] or from the tool’s official paper/repository."

- **uncertainty**: The paper describes a 252-problem filtered subset, but the available excerpts do not establish how the issues were classified or how reliable those classifications are. This is an unresolved question, not an established defect.
  - Page 10 · citation: exact
  - Quote: "We refer to our subset of 252 problems as SWE-bench Lite-S."

Unresolved questions:

- How were problematic issues classified, and what checks or agreement measures support the labels?
- How robust are the reported solve-rate and cost comparisons when baselines are evaluated under matched conditions? The available excerpts do not show the complete results or cost table.
- What limitations or additional results appear in the uninspected pages and appendices? This assessment uses excerpts from pages 1, 3–6, and 10–12; pages 2, 7–9, and 13–17 were not inspected, and several inspected excerpts are partial.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the methods and evaluation pages for the localization/repair procedure, benchmark setup, and evidence supporting the claimed solve rate and cost; check what baselines and comparisons are actually reported.; Inspect the SWE-bench Lite-S construction and results for the criteria used to exclude issues, whether the revised evaluation supports the paper’s conclusions, and any caveats about manual classification.; Inspect limitations and remaining results/appendices for scope boundaries or additional evidence; currently only page 1 is available, so substantive claims and potential q … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [3, 10, 11, 12] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [4, 5, 6] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | invalid_page_range | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The page 10 quote in the Lite-S observation only identifies the 252-problem subset; it does not support the observation’s claim about manual classification. Cite a supplied passage that explicitly states the classification basis, or narrow the observation to what the quote establishes.; Target: Replace or narrow the Lite-S observation so its verbatim quote directly supports its claim about issue classification and the unresolved reliability question. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Narrowed the Lite-S observation and replaced its quote with one that directly supports the stated subset size. The supplied excerpts do not provide a verified quotation for the manual-classification procedure, so classification reliability remains an open question rather than a claimed defect. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "Lite-S"}` | Locate the paper's revised benchmark construction and results, then inspect relevant pages for evidence and caveats. | 8 matches on pages [3, 10, 11, 12] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 4, "end": 6}` | Inspect core Agentless method and evaluation evidence, including localization and repair details, to support an independent assessment. | read pages [4, 5, 6] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 7, "end": 10}` | Inspect actual performance/cost tables and benchmark Lite-S curation details and counterevidence. | invalid_page_range | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
