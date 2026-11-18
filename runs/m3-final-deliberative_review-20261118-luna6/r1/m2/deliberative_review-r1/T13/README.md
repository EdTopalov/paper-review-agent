# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**deliberative_review · ok**

6 model calls · 3 reads · 24.96 s · $0.006358

6 decisions · 4 tool calls · 43399 input tokens (0 cached) · 1885 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

Self-RAG trains a language model to decide when to retrieve, generate with retrieved passages, and emit reflection tokens that assess passage relevance, support, and response utility. Its experiments report gains over several retrieval and non-retrieval baselines across six task settings, including factuality and citation metrics; the supplied pages also show meaningful ablations. The results support a substantial contribution, while the available evidence does not cover the complete paper or establish how robust the findings are beyond the reported settings.

- **strength**: The method is specified as a training and inference pipeline: reflection annotations are inserted into training outputs, and the generator is trained to predict them alongside task text.
  - Page 5 · citation: whitespace
  - Quote: "We train the generator model M by training on the curated corpus augmented with reflection tokens Dgen using the standard next token objective:"

- **strength**: The reported table covers closed-set, short-form, and long-form tasks, with measures including accuracy, FactScore, fluency, and citation precision and recall; Self-RAG leads many listed non-proprietary results.
  - Page 8 · citation: exact
  - Quote: "Table 2: Overall experiment results on six tasks."

- **limitation**: The ASQA ablation results are based on a sample of 150 instances, and some ablations are excluded there, limiting what those comparisons establish for that task.
  - Page 9 · citation: whitespace
  - Quote: "On ASQA, we evaluate models on sampled 150 instances and exclude ablations involving adaptive or no retrieval processes."

- **uncertainty**: The inspected material does not establish robustness across substantially different retrievers, training data, or evaluation settings; most of the paper, including appendices where further details are cited, was not inspected.
  - Page 7 · citation: whitespace
  - Quote: "For the retriever model R, we use off-the-shelf Contriever-MS MARCO (Izacard et al., 2022a) by default and retrieve up to ten documents for each input."

Unresolved questions:

- Do the uninspected sections and appendices report additional limitations, evaluation details, or results that change the assessment?
- How sensitive are the reported gains to the choice of critic and retriever, and to the quality of the reflection-token labels?
- How do the approach’s compute and inference costs compare with the evaluated baselines at comparable output quality?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the methods and training sections to verify how retrieval and reflection tokens are trained and used, and whether the described procedure supports the central adaptive-retrieval and self-critique claims.; Inspect the experiments, tables, and analysis for task coverage, baselines, quantitative support for quality/factuality claims, and any stated limitations; check whether apparent gaps in the abstract/introduction are addressed later.; Collect 2–4 short verbatim quotes with PDF page numbers from inspected pages, distinguish demonstrated weaknesses from open questions, and expli … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [2, 3] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [4, 5, 6] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [7, 8, 9] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: approve | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "training"}` | Locate methods/training evidence needed to assess how reflection tokens are trained and used. | 8 matches on pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 4, "end": 6}` | Inspect paper's methods/training sections for evidence on adaptive retrieval and reflection-token training. | read pages [4, 5, 6] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 7, "end": 9}` | Inspect experimental tasks and initial quantitative results to assess empirical support. | read pages [7, 8, 9] | [event 22](trace.jsonl#L22) |
| 6 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 34](trace.jsonl#L34) |
