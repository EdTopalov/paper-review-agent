# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**baseline · ok**

1 model calls · 0 reads · 8.35 s · $0.000647

1 decisions · 0 tool calls · 27075 input tokens (27072 cached) · 752 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SELF-RAG trains a language model to decide when to retrieve, assess retrieved evidence and generated text with reflection tokens, and use those assessments to steer decoding. Its combination of adaptive retrieval, segment-level critique, and controllable inference is supported by evaluations across six tasks, including ablations and analyses of retrieval and citation trade-offs. The results are promising, though the paper’s critic labels are largely GPT-4-derived and the reported human evaluation is small.

- **strength**: The paper presents a coherent approach that combines retrieval decisions, evidence assessment, and generation-level critique, with reflection scores usable at inference time.
  - Page 6 · citation: not_found
  - Quote: "SELF-RAG tailors an LM with no additional training."

- **strength**: The reported results cover multiple task types and show strong performance against the listed baselines; the paper also includes component ablations rather than relying only on headline comparisons.
  - Page 8 · citation: not_found
  - Quote: "Our SELF -RAG also outperforms existing RAG in many tasks"

- **limitation**: The reflection labels depend substantially on GPT-4 judgments, and the paper’s manual check is limited to a small sample. This leaves the robustness of those labels beyond the reported checks unresolved.
  - Page 17 · citation: whitespace
  - Quote: "The authors of this paper manually assess randomly sampled 20 instances for each aspect"

- **uncertainty**: The reported human evaluation samples 50 outputs from two settings, so the paper leaves uncertainty about how reliably its support and plausibility findings extend to other tasks and broader samples.
  - Page 10 · citation: whitespace
  - Quote: "we sampled 50 samples from PopQA and Bio results"

Unresolved questions:

- How well do the critic’s reflection judgments generalize when assessed by larger, independent human evaluations, especially for usefulness and factual support?
- How sensitive are the reported gains to alternative retrievers, corpora, and evaluation settings beyond those tested?
- I assessed the supplied paper text and appendices, but did not independently reproduce experiments or verify results outside the paper.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
