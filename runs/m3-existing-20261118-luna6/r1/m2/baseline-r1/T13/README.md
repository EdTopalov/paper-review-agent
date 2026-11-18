# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**baseline · ok**

1 model calls · 0 reads · 5.78 s · $0.003624

1 decisions · 0 tool calls · 27075 input tokens (0 cached) · 479 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.77

SELF-RAG trains a language model to decide when to retrieve, assess retrieved passages and generated segments with learned reflection tokens, and use those assessments to guide decoding. Across six task settings, the paper reports gains over many retrieval and non-retrieval baselines, notably for factuality and citation precision/recall, while also showing that retrieval frequency and output preferences can be adjusted at inference time.

- **strength**: The method integrates retrieval decisions, passage relevance, support judgments, and utility estimates into a single model and uses them in segment-level decoding, rather than treating retrieval as unconditional context injection.
  - Page 4 · citation: not_found
  - Quote: "SELF -RAG processes multiple passages in parallel and uses its own generated reflection tokens to enforce soft constraints"

- **strength**: The reported benchmark results are broad and include a particularly large citation advantage on ASQA over retrieval-augmented non-proprietary baselines.
  - Page 8 · citation: whitespace
  - Quote: "our model shows significantly higher citation precision and recall than all models except ChatGPT."

- **strength**: Ablations provide evidence that both training components and inference choices matter, though the ASQA subset is small and some retrieval ablations are excluded there.
  - Page 9 · citation: whitespace
  - Quote: "On ASQA, we evaluate models on sampled 150 instances"

- **limitation**: The reflection supervision is distilled from GPT-4, with the paper’s manual agreement check based on only 20 sampled instances per category; the approach therefore depends on potentially noisy model-generated judgments.
  - Page 17 · citation: whitespace
  - Quote: "The authors of this paper manually assess randomly sampled 20 instances for each aspect"

Unresolved questions:

- How robust are the gains across random seeds, broader domains, and substantially larger or differently composed evaluation sets? The inspected results do not report uncertainty estimates or multiple-run variability.
- How do reflection-token errors affect downstream retrieval and selection when the model encounters unfamiliar queries or poor-quality evidence? The paper reports agreement checks and a small human evaluation, but I did not inspect the detailed appendix examples beyond those supplied.
- What are the practical latency and compute costs of parallel passage processing and segment-level beam search relative to simpler RAG systems? The paper describes efficiency measures, but the inspected pages do not give a direct end-to-end cost comparison.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
