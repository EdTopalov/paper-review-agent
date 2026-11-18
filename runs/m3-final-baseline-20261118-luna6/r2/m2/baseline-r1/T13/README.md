# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**baseline · ok**

1 model calls · 0 reads · 7.95 s · $0.000644

1 decisions · 0 tool calls · 27075 input tokens (27072 cached) · 745 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SELF-RAG trains a language model to decide when to retrieve, assess retrieved passages and generated segments with reflection tokens, and use those assessments to guide decoding. The paper presents a coherent training-and-inference framework and reports gains over multiple retrieval and non-retrieval baselines, including stronger citation metrics on a long-form QA task. The results are promising, though the paper’s own evaluation describes a limited set of tasks and a small human study.

- **strength**: The framework integrates on-demand retrieval, passage relevance and support judgments, and controllable segment selection in one model, rather than treating retrieval as an unconditional preprocessing step.
  - Page 4 · citation: wrong_page
  - Quote: "SELF -RAG dynamically decides when to retrieve text passages by predicting Retrieve ."

- **strength**: The main results provide evidence across several task types, and the table reports strong citation precision and recall for SELF-RAG on ASQA relative to the listed non-proprietary baselines.
  - Page 8 · citation: exact
  - Quote: "Our SELF -RAG 13 B 55.8 69.3 74.5 73.1 80.2 31.7 37.0 71.6 70.3 71.3"

- **limitation**: The evidence for human alignment of reflection judgments is narrow: the reported human assessment samples only 20 instances per aspect for the GPT-4 labels, and the later output evaluation samples 50 examples each from PopQA and biography generation.
  - Page 17 · citation: whitespace
  - Quote: "The authors of this paper manually assess randomly sampled 20 instances for each aspect"

- **uncertainty**: It remains unclear how reliably the approach transfers beyond the selected tasks, datasets, and retrieval setup; the paper identifies these evaluations as covering six tasks, but the supplied evidence does not establish broader deployment performance.
  - Page 7 · citation: wrong_page
  - Quote: "We conduct evaluations of our SELF -RAG and diverse baselines on a range of downstream tasks"

Unresolved questions:

- How does SELF-RAG perform with retrievers or document collections substantially different from the ones used here, and how sensitive are results to corpus freshness?
- How closely do the learned relevance and support judgments match independent human assessments at larger scale, especially for long-form outputs?
- How do the quality gains trade off against inference cost when retrieval, parallel passage processing, and segment-level beam search are used?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
