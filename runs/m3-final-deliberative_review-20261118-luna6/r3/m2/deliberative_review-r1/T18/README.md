# T18: Gorilla: Large Language Model Connected with Massive APIs

**deliberative_review · ok**

8 model calls · 4 reads · 36.04 s · $0.006008

8 decisions · 5 tool calls · 35997 input tokens (1302 cached) · 3342 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

Gorilla combines fine-tuning with retrieval-aware training and inference to select API calls, and introduces APIBench with an AST-based evaluation. The observed results show that retrieval quality materially affects accuracy and give a qualitative example of adapting to documentation changes. The contribution is useful and focused, though the available evidence does not fully establish the breadth of its headline claims.

- **strength**: APIBench spans three model hubs and includes exhaustive coverage of the two smaller collections; the observed excerpt does not show the complete collection methodology.
  - Page 2 · citation: whitespace
  - Quote: "We exhaustively include every API call in TorchHub (94 API calls) and TensorHub (696 API calls)"

- **strength**: AST subtree matching provides a concrete task-specific measure of API-call correctness, but the observed material does not establish how well it captures broader tool-use behavior.
  - Page 2 · citation: whitespace
  - Quote: "We adopt a common AST sub-tree matching technique to evaluate the functional correctness of the generated API."

- **limitation**: Performance is materially sensitive to test-time retrieval quality: the reported settings show substantial accuracy degradation with non-oracle retrievers relative to the ground-truth retriever.
  - Page 7 · citation: whitespace
  - Quote: "using GPT-Index at evaluation results in 29.20% accuracy degradation, and using BM25 results in a 52.27% accuracy degradation."

- **uncertainty**: The paper illustrates adaptation to changed APIs and registries, but the observed discussion and figure do not quantify performance or establish generalization beyond the examples shown.
  - Page 8 · citation: exact
  - Quote: "Figure 6: Gorilla’s retriever–aware training enables it to react to changes in the APIs."

Unresolved questions:

- How do the complete results quantify Gorilla’s performance against GPT-4 and other baselines across the benchmark, including uncertainty or variation across test examples?
- How is adaptation to changing documentation evaluated beyond the Figure 6 examples, and how well does it generalize beyond the reported API hubs and single-call setting?
- What further evaluation qualifications or limitations appear in the eight uninspected pages?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the methods and evaluation pages for how APIBench is constructed and how Gorilla, GPT-4, and other baselines are compared; verify that the reported evidence supports the central performance claims.; Inspect results and examples, including retrieval and changing-document evaluations, for measured accuracy and hallucination outcomes, and check whether the claims are bounded by stated settings or limitations elsewhere in the paper.; Because only page 1 is currently available, inspect additional pages before assessing support or gaps; collect short verbatim, page-numbered quotes fo … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 3 matches on pages [1, 2, 3] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 4 matches on pages [2, 3, 5, 6] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | 8 matches on pages [4, 6, 7, 8] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: investigate; Issues: The draft appropriately qualifies its conclusions, but the central performance comparison and the changing-document evaluation remain unverified in the partial excerpts. A targeted read is warranted before settling the score.; Target: Inspect the remaining results pages for the complete Gorilla-versus-baseline tables and the changing-document evaluation: what settings and metrics are reported, and what limitations or qualifications accompany those results? | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | targeted_read | read pages [8, 9, 10] | [event 34](trace.jsonl#L34) · [event 39](trace.jsonl#L39) |
| 8 | revise | Draft revised; Changes: Updated the retrieval and adaptation assessments to incorporate the page 8 figure and discussion, and the page 9 constraint results. The figure supports an example of API-change adaptation but not a quantitative generalization claim, so the uncertainty remains. The available evidence still does not include the complete main comparison tables; no score change is warranted. | [event 40](trace.jsonl#L40) · [event 43](trace.jsonl#L43) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "APIBench"}` | Locate evaluation and dataset construction evidence needed to assess the paper's central claims. | 3 matches on pages [1, 2, 3] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "AST tree"}` | Locate evaluation methodology and results so claims can be judged from paper evidence. | 4 matches on pages [2, 3, 5, 6] | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "results"}` | Inspect reported comparisons, quantitative outcomes, and counterevidence to the central performance claims. | 8 matches on pages [4, 6, 7, 8] | [event 22](trace.jsonl#L22) |
| 7 | read_pages `{"start": 8, "end": 10}` | Inspect changing-document results and qualifications. | read pages [8, 9, 10] | [event 37](trace.jsonl#L37) |
| 8 | submit_review `{"review": {"score": 0.62, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 45](trace.jsonl#L45) |
