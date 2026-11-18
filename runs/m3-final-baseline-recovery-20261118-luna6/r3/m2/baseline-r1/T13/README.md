# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**baseline · ok**

1 model calls · 0 reads · 5.72 s · $0.000512

1 decisions · 0 tool calls · 27075 input tokens (27072 cached) · 481 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

SELF-RAG trains a language model to decide when to retrieve, assess retrieved passages and generated segments with learned reflection tokens, and use those signals to select outputs at inference. The paper presents a substantial, integrated approach to adaptive retrieval and evidence-aware generation, with results across six tasks and analyses of ablations and inference-time trade-offs. The reported gains are strongest on several factuality and citation measures, though the evidence is limited by small human evaluations and reliance on GPT-4-generated supervision.

- **strength**: The method combines retrieval decisions, passage relevance and support checks, and utility judgments in a single model, with inference-time controls over those signals.
  - Page 4 · citation: wrong_page
  - Quote: "These reflection tokens (Table 1) signal the need for retrieval or confirm the output’s relevance, support, or completeness."

- **strength**: Evaluation spans six tasks and multiple outcome types; on ASQA, SELF-RAG reports much higher citation precision and recall than most listed baselines.
  - Page 8 · citation: not_found
  - Quote: "Our model shows significantly higher citation precision and recall than all models except ChatGPT."

- **limitation**: The human assessment is modest in scale: the paper samples 50 cases from PopQA and biography generation, limiting what it establishes about general reliability.
  - Page 10 · citation: whitespace
  - Quote: "we sampled 50 samples from PopQA and Bio results."

- **uncertainty**: The critic’s supervision is largely derived from GPT-4 judgments, and reported agreement with those judgments does not by itself establish accuracy against independent human labels at scale.
  - Page 5 · citation: not_found
  - Quote: "The critic achieves a higher than 90% agreement with GPT-4-based predictions on most reflection token categories."

Unresolved questions:

- How well do the reflection-token judgments and retrieval policy generalize when evaluated against larger, independently annotated human datasets, rather than GPT-4-derived labels?
- How robust are the reported benefits across different retrievers, corpora, and retrieval settings? The paper notes corpus-dump variation and leaves instruction-tuned or jointly trained retrieval for future work (page 20).
- I inspected the supplied main text and selected appendix material, but not every appendix detail or underlying evaluation artifact; uncertainty remains about sensitivity to prompt, decoding, and metric choices.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
