# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**agent · ok**

6 model calls · 5 reads · 15.29 s · $0.002624

6 decisions · 6 tool calls · 30443 input tokens (13207 cached) · 712 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.77

Self-RAG trains a language model to decide when to retrieve, generate text segments conditioned on retrieved passages, and emit reflection tokens that assess relevance, support, and utility. The tokens also guide inference-time selection and controllability. Across six task types, the paper reports strong results for 7B/13B models, including improved factuality and citation metrics, with ablations supporting the value of retrieval and critique components.

- **strength**: The method combines on-demand retrieval with segment-level critique and adjustable decoding, making retrieval and generation quality part of one trainable framework.
  - Page 2 · citation: whitespace
  - Quote: "SELF -RAG further enables a customizable decoding algorithm to satisfy hard or soft constraints, which are defined by reflection token predictions."

- **strength**: Evaluation spans closed-set classification/reasoning, short-form QA, and long-form generation; the table reports especially large citation precision and recall gains over the listed non-proprietary retrieval baselines.
  - Page 8 · citation: exact
  - Quote: "Our SELF -RAG 13 B 55.8 69.3 74.5 73.1 80.2 31.7 37.0 71.6 70.3 71.3"

- **limitation**: The evaluation is explicitly zero-shot and uses a particular 150k-pair training mixture, Llama2 base models, and a specified retriever; broader transfer across training regimes and model families is not established by the inspected evidence.
  - Page 7 · citation: whitespace
  - Quote: "In total, we use 150k instruction-output pairs."

- **uncertainty**: The paper describes ASQA citation evaluation alongside full-test-set evaluations elsewhere, but the inspected ablation analysis uses only a sampled subset for ASQA; how stable those ablation differences are on the full set remains unclear.
  - Page 9 · citation: whitespace
  - Quote: "On ASQA, we evaluate models on sampled 150 instances and exclude ablations involving adaptive or no retrieval processes."

Unresolved questions:

- How robust are the reported benefits across model families, retrieval corpora, and non-zero-shot settings?
- How reliably do the model-generated reflection tokens track independently verified relevance and evidential support?
- What are the runtime and computational costs relative to simpler retrieval-augmented baselines at matched output quality?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Experiments"}` | Locate the paper’s evaluation and reported results to assess empirical support. | 4 matches on pages [1, 3, 6] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect the method description and training setup to understand the core contribution and assumptions. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Check whether the authors explicitly state limitations or scope constraints. | 0 matches | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 6, "end": 7}` | Inspect evaluation design, datasets, and reported outcomes for evidence and scope. | read pages [6, 7] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 8, "end": 9}` | Review key comparative results and any reported analysis to judge strength and caveats of the evidence. | read pages [8, 9] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.77, "observations": 4}}` | Evidence inspected covers the framework, evaluation scope, main comparative results, and ablations; submit a qualified paper assessment. | review accepted | [event 31](trace.jsonl#L31) |
