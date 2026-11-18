# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**baseline · ok**

1 model calls · 0 reads · 9.58 s · $0.000623

1 decisions · 0 tool calls · 27075 input tokens (27072 cached) · 704 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.77

SELF-RAG trains a language model to decide when to retrieve, assess retrieved passages and generated segments with reflection tokens, and use those assessments to guide decoding. Its experiments show promising gains over several retrieval-augmented and non-retrieval baselines, particularly in factuality and citation metrics, while demonstrating inference-time control over retrieval and output preferences. The evidence is substantial for the tested setup, though some supporting evaluations are small and the paper identifies retrieval quality as an open area.

- **strength**: The paper presents a coherent method combining adaptive retrieval, passage relevance and support judgments, and controllable segment-level decoding; it also reports broad comparisons and component ablations.
  - Page 6 · citation: not_found
  - Quote: "SELF -RAG tailors an LM with no additional training."

- **strength**: Results across six tasks include strong performance on multiple measures, and the paper reports particularly large citation-precision and recall gains over several retrieval baselines.
  - Page 8 · citation: exact
  - Quote: "Our SELF -RAG 13 B 55.8 69.3 74.5 73.1 80.2 31.7 37.0 71.6 70.3 71.3"

- **limitation**: The human assessment of generated outputs is limited in scale, so it offers only narrow evidence about human-perceived support and plausibility.
  - Page 10 · citation: whitespace
  - Quote: "we sampled 50 samples from PopQA and Bio results."

- **uncertainty**: The results rely on the selected retrievers and Wikipedia corpora; how much the framework’s gains depend on retrieval quality or transfer to stronger task-adapted retrieval remains unresolved.
  - Page 20 · citation: whitespace
  - Quote: "we leave exploring the effectivess of such appraoches for future work."

Unresolved questions:

- How robust are the reported gains across different retrievers, document collections, and retrieval-quality regimes?
- How well do reflection-token judgments and their decoding benefits hold up under larger, independently sampled human evaluations?
- How do retrieval costs and end-to-end latency compare with other approaches when accounting for adaptive retrieval, parallel passage processing, and segment-level beam search?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
