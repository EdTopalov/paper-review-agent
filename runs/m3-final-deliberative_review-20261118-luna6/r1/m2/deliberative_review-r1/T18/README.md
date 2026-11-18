# T18: Gorilla: Large Language Model Connected with Massive APIs

**deliberative_review · ok**

6 model calls · 3 reads · 25.62 s · $0.004451

6 decisions · 4 tool calls · 28145 input tokens (0 cached) · 1885 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Gorilla fine-tunes a LLaMA-based model to generate API calls and pairs it with retrieval over API documentation. On the reported HuggingFace, TorchHub, and TensorFlow Hub benchmark, Gorilla often outperforms the compared models without retrieval, and retrieval-aware training shows promise. The evidence is useful but limited to a narrow, one-call benchmark and AST-based evaluation; important parts of the paper, including the full dataset and adaptation analyses, were not inspected.

- **strength**: The reported zero-shot results show strong performance on the three evaluated API collections, including higher accuracy than GPT-4 in each collection, though the benchmark and metric are scoped.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: The evaluation is explicitly limited to one API call, and the paper uses AST matching against its collected dataset rather than testing execution or general semantic correctness.
  - Page 5 · citation: exact
  - Quote: "Since we only consider one API call in this paper,"

- **limitation**: Retrieval is not uniformly beneficial: the authors report substantial degradation with non-oracle retrievers in some settings, which constrains claims about practical retrieval-enabled performance.
  - Page 7 · citation: whitespace
  - Quote: "using GPT-Index at evaluation results in 29.20% accuracy degradation, and using BM25 results in a 52.27% accuracy degradation."

- **uncertainty**: The paper claims adaptation to documentation changes, but the inspected material does not include the detailed experiment or results needed to assess how broadly that finding holds.
  - Page 5 · citation: exact
  - Quote: "We demonstrate that this a) makes the LLM adapt to test-time\nchanges in API documentation"

Unresolved questions:

- How large and diverse is APIBench, and how independent are its generated instruction/API pairs across the training and test split? The available excerpts say the split is from those pairs but do not provide the full dataset-construction details.
- What are the detailed results and methodology for test-time documentation changes, constrained API requests, and hallucination reduction? Those sections were not available in the inspected excerpts.
- How well do the generated calls execute and satisfy user goals beyond matching selected AST nodes, and how does performance generalize to multi-step or broader real-world APIs?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the evaluation and results pages for how Gorilla is compared with GPT-4, including task coverage, metrics, and support for the claimed performance advantage.; Check the dataset and experimental setup for APIBench construction, training/test separation, and evaluation scope, to judge how far the results support broad API-use claims.; Inspect the retrieval and analysis sections, including limitations, for evidence of adaptation to documentation changes and reduced hallucination; note that only page 1 is currently available and 17 pages remain uninspected. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [4, 6, 7, 8] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | invalid_page_range | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [5, 6, 7] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: approve | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "Results"}` | Locate the evaluation/results evidence to assess comparisons and claims. | 8 matches on pages [4, 6, 7, 8] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 8}` | Inspect dataset construction, comparative evaluation, retrieval results, and counterevidence for paper assessment. | invalid_page_range | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 5, "end": 7}` | Inspect experiment setup, benchmark construction, and comparative results for evidence and counterevidence. | read pages [5, 6, 7] | [event 22](trace.jsonl#L22) |
| 6 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 34](trace.jsonl#L34) |
