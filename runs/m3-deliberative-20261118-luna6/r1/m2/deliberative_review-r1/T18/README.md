# T18: Gorilla: Large Language Model Connected with Massive APIs

**deliberative_review · ok**

6 model calls · 3 reads · 24.57 s · $0.003355

6 decisions · 4 tool calls · 19113 input tokens (0 cached) · 1952 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.58

Gorilla combines fine-tuning with document retrieval to generate API calls and introduces APIBench, built from model-hub APIs. The supplied excerpts establish a focused contribution and a deliberately limited evaluation target, but do not provide enough of the methods or results to assess the strength of the central performance and adaptation claims.

- **strength**: The paper frames a combined training-and-retrieval approach and a benchmark spanning three model hubs.
  - Page 3 · citation: exact
  - Quote: "a information–retriever incorporated into the training and inference pipelines."

- **limitation**: The described AST evaluation is scoped to one API call, limiting what this metric establishes about more complex multi-call tool use.
  - Page 5 · citation: exact
  - Quote: "Since we only consider one API call in this paper"

- **uncertainty**: The abstract claims superiority to GPT-4, but the inspected excerpts do not show the quantitative results or enough protocol detail to verify the comparison.
  - Page 1 · citation: whitespace
  - Quote: "surpasses the performance of GPT-4 on writing API calls."

Unresolved questions:

- How are APIBench queries, documentation, and train/test splits constructed, and do they permit overlap or leakage relevant to the comparison?
- What do the evaluation tables show across APIBench categories, and how are accuracy and hallucination measured for each baseline?
- What test-time documentation changes are evaluated, and how broadly do those results support adaptation beyond the reported setting?
- This assessment uses only excerpts from pages 1–6, several of them truncated; pages 7–18 and substantial portions of the methods and results were not inspected.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the methods and dataset sections for how APIBench queries, API documentation, train/test splits, and model training are constructed; check for overlap or leakage that could affect the central comparison.; Inspect evaluation tables and protocols to verify the claimed performance advantage over GPT-4 and reduced hallucination, including baselines, metrics, and whether results cover all APIBench categories.; Inspect retrieval and test-time document-change experiments, plus discussion and limitations, to determine what adaptation is demonstrated and whether scope boundaries or cave … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 3 matches on pages [1, 2, 3] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 4 matches on pages [2, 3, 5, 6] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | 8 matches on pages [1, 2, 3, 4] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: approve | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "APIBench"}` | Locate the paper’s dataset, evaluation, and experiment sections to inspect the central evidence obligations. | 3 matches on pages [1, 2, 3] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "AST tree"}` | Locate evaluation protocol and results for the main performance claims. | 4 matches on pages [2, 3, 5, 6] | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "GPT-4"}` | Inspect evaluation results and counterevidence for the central performance claim. | 8 matches on pages [1, 2, 3, 4] | [event 22](trace.jsonl#L22) |
| 6 | submit_review `{"review": {"score": 0.58, "observations": 3}}` | Submit after the enforced critique and source validation. | review accepted | [event 34](trace.jsonl#L34) |
