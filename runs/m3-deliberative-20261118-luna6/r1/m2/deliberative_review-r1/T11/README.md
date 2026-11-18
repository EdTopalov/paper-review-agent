# T11: Executable Code Actions Elicit Better LLM Agents

**deliberative_review · ok**

7 model calls · 3 reads · 39.55 s · $0.009444

7 decisions · 4 tool calls · 62311 input tokens (0 cached) · 3330 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

CodeAct proposes executable Python as a flexible action format for LLM agents, enabling tool composition and multi-turn revision from execution feedback. The paper reports comparative results on API-Bank and an 82-instance multi-tool benchmark, and introduces CodeActInstruct and finetuned agents. The reported benchmark gains are promising, but the inspected evidence is incomplete, particularly for the finetuning and general-capability claims.

- **strength**: The multi-tool evaluation gives a concrete, though small, comparative test: it uses 82 curated instances and reports CodeAct as best for more models than either alternative. The setup and scope are stated.
  - Page 5 · citation: whitespace
  - Quote: "It contains 82 human-curated instances, spanning tasks including web browsing, finance, travel itinerary planning, science, and information processing."

- **strength**: The reported results support a qualified success-rate advantage on M3ToolEval, not a universal one: CodeAct led for 12 of 17 models, with exceptions also visible in the table.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs)"

- **limitation**: The results show that the format comparison does not entail strong absolute performance across models: the best open-source result is far below the strongest closed-source result. This qualifies practical generalization, rather than refuting the comparison.
  - Page 5 · citation: whitespace
  - Quote: "the best open-source model achieving 13.4% while the best closed-source model gpt-4-1106-preview 74.4%."

- **uncertainty**: The inspected excerpt states the finetuning claim but does not provide the relevant evaluation results, so I cannot verify the claimed gains or preservation of general capability. This is an inspection gap, not evidence that the paper lacks those results: 21 of its 29 pages are uninspected.
  - Page 7 · citation: whitespace
  - Quote: "improves CodeAct performances without hurting LLM’s general performance on a diverse suite of tasks (§3.2)."

Unresolved questions:

- How robust are the M3ToolEval comparisons to benchmark size, task composition, prompt and tool choices, and exact-match evaluation? The inspected excerpt describes 82 curated instances but does not establish these sensitivities.
- What do the detailed CodeActInstruct finetuning results show, including comparisons and evaluation conditions for agent tasks and general capability? The relevant pages were not inspected.
- How do execution safety, sandboxing, and resource constraints affect use of executable code in broader environments? This remains an open question, not a demonstrated defect in the inspected material.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the experimental results and benchmark/task setup to verify whether CodeAct’s claimed success-rate gains over alternative action formats are supported and measured comparably.; Check the methods and analysis for scope conditions or limitations that qualify the claims about dynamic code actions, tool composition, and self-debugging.; Review the CodeActInstruct and finetuning evaluations for evidence behind claims of improved agent tasks without compromised general capability; record that only page 1 is currently available and the remaining 28 pages are uninspected. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [1, 2, 3, 5, 9] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [4, 5] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [6, 7] (text truncated by tool) | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The draft notes that finetuning results are unavailable but does not explicitly acknowledge the inspection gap: 21 of the paper’s 29 pages are uninspected. Add that qualification so readers can distinguish an inspected absence from material not reviewed. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Made the inspection gap explicit: 21 of 29 pages are uninspected, so the unavailable finetuning results should not be read as absent from the paper. The supplied quotations and page numbers were verified; no score change was warranted. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "success rate"}` | Inspect experimental results and comparisons to assess the claimed CodeAct performance gains, and obtain page-specific quotations. | 8 matches on pages [1, 2, 3, 5, 9] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 4, "end": 5}` | Inspect experimental setup and reported results supporting comparative success-rate claims. | read pages [4, 5] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 6, "end": 7}` | Inspect implementation/evaluation qualifications and limitations following the reported benchmark results. | read pages [6, 7] (text truncated by tool) | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
