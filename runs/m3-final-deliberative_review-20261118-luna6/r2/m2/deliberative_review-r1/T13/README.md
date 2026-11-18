# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**deliberative_review · ok**

7 model calls · 3 reads · 30.53 s · $0.008108

7 decisions · 4 tool calls · 54772 input tokens (1507 cached) · 2889 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

Self-RAG trains a language model to decide when retrieval is useful, generate with retrieved passages, and emit reflection tokens assessing relevance, support, and usefulness. Results across several task types and component ablations provide meaningful evidence for the approach, including strong ASQA citation metrics. Its feedback depends partly on critic labels distilled from GPT-4, and the inspected results do not establish how well the method generalizes beyond the evaluated settings.

- **strength**: The paper describes a training and inference scheme in which the generator learns task outputs alongside reflection tokens, using critic-generated labels prepared offline.
  - Page 5 · citation: exact
  - Quote: "M learns to predict the target output as well as the reflection tokens."

- **strength**: The reported table shows strong results across several tasks. On ASQA, the 13B model reports higher citation precision and recall than the listed non-proprietary baselines.
  - Page 8 · citation: exact
  - Quote: "Our SELF -RAG 13 B 55.8 69.3 74.5 73.1 80.2 31.7 37.0 71.6 70.3 71.3"

- **limitation**: ASQA ablations are bounded in scope: they use a 150-instance sample and omit adaptive- or no-retrieval ablations. This limits what those ablations establish, but does not demonstrate a defect in the method.
  - Page 9 · citation: whitespace
  - Quote: "On ASQA, we evaluate models on sampled 150 instances and exclude ablations involving adaptive or no retrieval processes."

- **uncertainty**: The critic’s reflection labels are distilled partly from GPT-4 predictions; the inspected pages do not establish robustness to errors or biases in those labels.
  - Page 5 · citation: whitespace
  - Quote: "We create supervised data by prompting GPT-4 to generate reflection tokens and then distill their knowledge into an in-houseC."

Unresolved questions:

- How robust are results to errors in critic-generated reflection labels and to changes in the retrieval corpus or retriever?
- How well do the reported gains generalize beyond the selected models, datasets, and inference settings?
- Inspection covered supplied excerpts for pages 1–9 of 30. The remaining pages, including any further analysis or dedicated limitations discussion, were not inspected.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the methods and training sections for how retrieval and reflection tokens are trained and used, and whether the described procedure supports the claimed adaptive retrieval and self-critique.; Inspect the experimental setup and results across the reported task types, checking baselines, metrics, and evidence for gains in accuracy, factuality, and citation quality.; Check limitations, ablations, and analysis elsewhere in the paper for qualifications or missing support; currently only page 1 is available, so do not treat uninspected pages as evidence of absence. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [2, 3] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [4, 5, 6] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [7, 8, 9] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The fourth observation’s quotation is not verbatim in the cited page. Replace it with the exact sentence from page 5, such as “We create supervised data by prompting GPT-4 to generate reflection tokens and then distill their knowledge into an in-houseC.”; Target: Correct the page 5 quotation in the fourth observation; retain the qualification that robustness to critic-label errors is unresolved rather than demonstrated defective. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Corrected the page 5 quotation to match the observed text. Retained the label-robustness concern as an unresolved question, not a demonstrated defect; no score change was warranted. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "Training"}` | Investigate the training procedure for retrieval and reflection tokens, one of the explicit evidence obligations. | 8 matches on pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 4, "end": 6}` | Inspect method and training details on reflection tokens and adaptive retrieval. | read pages [4, 5, 6] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 7, "end": 9}` | Inspect experimental setup and results for evidence and counterevidence on reported performance. | read pages [7, 8, 9] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
