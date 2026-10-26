# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**baseline · ok**

1 model calls · 0 reads · 6.22 s · $0.003656

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SELF-RAG trains a language model to decide when to retrieve, assess retrieved passages and generated claims with reflection tokens, and use those signals to select outputs at inference. Across six task settings, the reported results and ablations provide substantial evidence that this approach can improve factuality, task performance, and citation quality over several retrieval and non-retrieval baselines, while enabling inference-time trade-offs.

- **strength**: The method combines adaptive retrieval, passage relevance and support judgments, and controllable segment-level decoding in one trained generator. The paper reports gains on multiple tasks, not only question answering.
  - Page 4 · citation: wrong_page
  - Quote: "These reflection tokens (Table 1) signal the need for retrieval or confirm the output’s relevance, support, or completeness."

- **strength**: The reported comparison is broad, including six tasks, multiple model types, and diverse metrics; SELF-RAG leads among non-proprietary models in the presented table, though not on every metric against proprietary systems.
  - Page 8 · citation: whitespace
  - Quote: "our SELF -RAG also outperforms existing RAG in many tasks, obtaining the best performance among non-proprietary LM-based models on all tasks."

- **strength**: Ablations provide evidence that retrieval and critique components contribute to outcomes, and the inference analysis demonstrates a factuality–fluency trade-off rather than implying a universally optimal setting.
  - Page 9 · citation: whitespace
  - Quote: "Using the top passages regardless of their relevance (Retrieve top 1) as in conventional RAG approaches causes a large drop in PopQA and ASQA"

- **limitation**: The authors acknowledge that citations can still fail to support generated text, so reflection-based assessment does not guarantee verifiability. The human evaluation is also small: 50 samples from two result sets, as described on page 10.
  - Page 11 · citation: exact
  - Quote: "it can still generate outputs that are not fully supported by the citations."

Unresolved questions:

- How robust are the gains across different retrievers, corpora, domains, languages, and deployment conditions beyond the evaluated settings? The paper identifies retriever adaptation as future work (page 20).
- How reliably do the learned reflection judgments track human assessments on a larger and more diverse evaluation, especially for usefulness and support? The reported human study samples 50 cases from PopQA and biography generation (page 10).
- What are the end-to-end latency and compute costs of parallel passage processing and segment-level beam search relative to conventional RAG? I inspected the supplied pages but did not find a quantitative runtime comparison.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes retrieval-on-demand, relevance/support/usefulness critique tokens, and inference-time control through segment-level beam search (pp. 3–6). Its evaluations span six tasks, including reasoning and long-form generation (pp. 7–8).
- Observation 2: **supported** — Table 2 reports six task settings and varied metrics, and the authors state SELF-RAG has the best performance among non-proprietary LM-based models on all tasks, while noting proprietary-model exceptions on particular metrics (p. 8).
- Observation 3: **supported** — The ablation results compare training and inference components, including removing the critic and using the top passage regardless of relevance (p. 9). The inference analyses vary support-token weights and retrieval thresholds, reporting effects on citation precision, MAUVE, retrieval frequency, and accuracy rather than claiming one setting is universally best (pp. 9–10).
- Observation 4: **supported** — The authors explicitly acknowledge that outputs may not be fully supported by citations (p. 11). The human evaluation sampled 50 PopQA and biography-generation cases (p. 10), and the appendix includes examples where predictions are unsupported or only partially supported (p. 24).

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
