# T18: Gorilla: Large Language Model Connected with Massive APIs

**deliberative_review · ok**

11 model calls · 4 reads · 68.02 s · $0.009535

11 decisions · 6 tool calls · 51442 input tokens (1302 cached) · 6536 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Gorilla combines fine-tuning and retrieval for API-call generation and introduces APIBench, covering APIs from three ML model hubs. Reported results show strong performance in several benchmark settings, alongside substantial sensitivity to retrieval quality. The evidence supports a useful contribution in this domain, but does not establish broad generalization beyond it. Inspection was incomplete: 7 of 18 pages were observed, and pages 2, 3, and 5 were only partially available.

- **strength**: On APIBench, Gorilla’s reported zero-shot overall accuracy exceeds the listed alternatives across all three hubs. This supports performance on this benchmark, not general performance beyond it.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: The reported results show substantial dependence on retrieval quality: using non-oracle retrievers can reduce accuracy relative to the oracle setting. Retrieval quality is therefore an important condition on the reported performance.
  - Page 7 · citation: whitespace
  - Quote: "using GPT-Index at evaluation results in 29.20% accuracy degradation, and using BM25 results in a 52.27% accuracy degradation."

- **uncertainty**: The paper illustrates adaptation to changed model versions and registries, but the observed material gives examples rather than quantified evidence across a broader range of documentation changes.
  - Page 8 · citation: whitespace
  - Quote: "The second column demonstrates changes in model upgrading FCN’s ResNet–50 backbone to ResNet–101."

- **limitation**: The authors explicitly scope the benchmark to ML APIs and flag a potential bias concern. This is an acknowledged scope boundary, not evidence that the benchmark results are invalid.
  - Page 9 · citation: exact
  - Quote: "With the goal of wanting to have a challenging dataset, we chose ML APIs"

Unresolved questions:

- How representative are the HuggingFace APIs and generated instruction-answer pairs, and how was their quality checked?
- How robust is adaptation to documentation changes beyond the examples shown, and how do retrieval errors affect real API use?
- What additional methodological or evaluation details appear on the 11 uninspected pages, including pages not represented by the supplied excerpts?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the method and training-data pages to determine how Gorilla is trained and how APIBench is constructed, including whether the benchmark supports the claimed breadth and validity.; Inspect experimental results and evaluation details, especially comparisons with GPT-4 and tests of retrieval, documentation/version changes, and hallucination; verify what the reported evidence establishes and under what conditions.; Inspect discussion and limitations for stated scope boundaries, and note that only page 1 is currently available so observations requiring evidence from other pages cann … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 3 matches on pages [1, 2, 3] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 1 matches on pages [3] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | 1 matches on pages [5] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: investigate; Issues: The draft appropriately discloses that most pages are uninspected, but assigns an absolute score before examining the experimental evidence central to the paper’s claimed contribution. The abstract’s performance claims alone do not establish how strongly the work is supported.; Target: What do the experimental-results pages report about Gorilla’s comparisons with GPT-4, retrieval and documentation-change tests, and hallucination outcomes, including the evaluation conditions and quantitative results? | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | targeted_read | read pages [7, 8, 9] | [event 34](trace.jsonl#L34) · [event 39](trace.jsonl#L39) |
| 8 | revise | invalid_phase_output; unobserved_ledger_reference; ValueError | [event 40](trace.jsonl#L40) · [event 43](trace.jsonl#L43) |
| 9 | revise | invalid_phase_output; unobserved_ledger_reference; ValueError | [event 44](trace.jsonl#L44) · [event 47](trace.jsonl#L47) |
| 10 | revise | Draft revised; Changes: Updated the assessment after considering the observed results pages: the quantitative APIBench findings support a stronger score than the earlier evidence-only draft. The score remains qualified by the benchmark-specific scope, the reported sensitivity to retrieval quality, the illustrative nature of the observed documentation-change evidence, and incomplete page coverage. The critic’s concern about scoring before reviewing results is addressed; no claim is made that the excerpts establish broad external validity. | [event 48](trace.jsonl#L48) · [event 51](trace.jsonl#L51) |
| 11 | revise | Draft revised; Changes: Updated the retrieval observation’s page citation to page 7, where the exact quoted sentence appears. The critic’s concern that the experimental evidence had not been inspected is addressed by the supplied results excerpts; the assessment now reflects their reported comparisons and conditions while retaining uncertainty about uninspected material. I did not change the score because the inspected evidence supports the existing assessment. | [event 56](trace.jsonl#L56) · [event 59](trace.jsonl#L59) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "APIBench"}` | Inspect benchmark construction and evidence beyond the supplied abstract page. | 3 matches on pages [1, 2, 3] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "AST tree matching"}` | Inspect evaluation and experimental evidence beyond the partial first pages, including comparisons and retrieval claims. | 1 matches on pages [3] | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "AST matching"}` | Inspect benchmark evaluation evidence and results supporting the paper's claims. | 1 matches on pages [5] | [event 22](trace.jsonl#L22) |
| 7 | read_pages `{"start": 7, "end": 9}` | Inspect experimental results for GPT-4 comparison, retrieval changes, and hallucination evidence. | read pages [7, 8, 9] | [event 37](trace.jsonl#L37) |
| 10 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit after the enforced critique and source validation. | citation_validation_failed; #2: wrong_page (pages [7]) | [event 53](trace.jsonl#L53) |
| 11 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 61](trace.jsonl#L61) |
