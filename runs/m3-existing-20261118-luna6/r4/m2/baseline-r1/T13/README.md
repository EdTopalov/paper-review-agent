# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**baseline · ok**

1 model calls · 0 reads · 10.56 s · $0.000694

1 decisions · 0 tool calls · 27075 input tokens (27072 cached) · 845 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

SELF-RAG trains a language model to decide when to retrieve, assess retrieved passages and generated claims with reflection tokens, and use those assessments to guide decoding. The paper presents a coherent method and reports gains across six tasks, including citation metrics and ablations. The evidence is promising, but the human evaluation is small and the reflection judgments are substantially built from GPT-4-generated labels. This assessment is based on the supplied pages; it does not independently verify results or inspect material beyond them.

- **strength**: The method combines on-demand retrieval with passage relevance, support, and usefulness judgments, and uses the resulting reflection tokens to guide generation and selection.
  - Page 4 · citation: wrong_page
  - Quote: "These reflection tokens (Table 1) signal the need for retrieval or confirm the output’s relevance, support, or completeness."

- **strength**: The reported results show competitive performance across varied tasks; the 13B model has strong reported results on both closed-set tasks and citation metrics.
  - Page 8 · citation: exact
  - Quote: "Our SELF -RAG 13 B 55.8 69.3 74.5 73.1 80.2 31.7 37.0 71.6 70.3 71.3"

- **limitation**: The human assessment is explicitly small, so it offers limited evidence about the reliability of outputs and reflection-token judgments beyond the sampled cases.
  - Page 10 · citation: whitespace
  - Quote: "We conduct small human evaluations on SELF -RAG outputs, as well as the reliability of predicted reflection tokens."

- **uncertainty**: The supplied evidence does not establish how well the approach generalizes to broader tasks, retrieval setups, or independently judged reflection labels; the paper reports evaluations on six tasks and largely uses GPT-4-derived supervision.
  - Page 5 · citation: not_found
  - Quote: "The critic model is, in part, supervised on a dataset of input, output, and corresponding reflection tokens collected by prompting a propriety LM (i.e., GPT-4; OpenAI 2023)."

Unresolved questions:

- How robust are the reflection-token predictions and downstream gains when supervision is produced or evaluated by annotators independent of GPT-4?
- Do the reported advantages persist across other retrieval corpora, retrievers, and task distributions?
- How do inference latency and retrieval costs compare with conventional RAG in practical deployment settings?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
