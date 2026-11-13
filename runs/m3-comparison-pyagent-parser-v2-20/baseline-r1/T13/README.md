# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**baseline · ok**

1 model calls · 0 reads · 5.25 s · $0.003599

1 decisions · 0 tool calls · 27075 input tokens (0 cached) · 429 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

SELF-RAG trains a language model to decide when to retrieve, assess retrieved passages and generated segments with reflection tokens, and use those assessments to guide decoding. Across six tasks, the paper reports gains over many retrieval and non-retrieval baselines, including improved citation metrics on ASQA; its ablations and small human evaluation provide supporting, though not definitive, evidence.

- **strength**: The approach combines adaptive retrieval, passage relevance and support judgments, and controllable segment-level decoding in one trained model.
  - Page 4 · citation: not_found
  - Quote: "These reflection tokens signal the need for retrieval or confirm the output’s relevance, support, or completeness."

- **strength**: The reported results show broad task coverage and strong performance, with especially large citation-precision and recall differences against retrieval baselines on ASQA.
  - Page 8 · citation: not_found
  - Quote: "66.9 67.8\n70.3 71.3"

- **strength**: Ablations offer evidence that retrieval and reflection components matter, while the authors appropriately limit the ASQA ablation to a sample of 150 instances.
  - Page 9 · citation: whitespace
  - Quote: "On ASQA, we evaluate models on sampled 150 instances"

- **limitation**: The reported human check is small, and its S&P assessment excludes outputs marked irrelevant or unsupported, limiting what it establishes about overall factual reliability.
  - Page 10 · citation: not_found
  - Quote: "We sampled 50 samples from PopQA and Bio results."

Unresolved questions:

- How well do the gains and reflection-token judgments generalize to tasks, domains, retrieval corpora, and model families beyond those evaluated?
- Would the citation and factuality results hold under larger, independently annotated human evaluations that include outputs labeled irrelevant or unsupported?
- How sensitive are the main comparisons to the different retrieval sources and corpora used across tasks?
- The assessment here covers the supplied pages, including the main results and selected appendix material; detailed appendix evaluation settings, full result tables, and qualitative examples were not inspected in full.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
