# T20: RAFT: Adapting Language Model to Domain Specific RAG

**baseline · ok**

1 model calls · 0 reads · 10.70 s · $0.000553

1 decisions · 0 tool calls · 13497 input tokens (13494 cached) · 835 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

RAFT proposes a fine-tuning recipe for domain-specific RAG: train on questions and retrieved documents, including distractors, and generate answers with reasoning and quoted evidence. Results across several QA and API-document benchmarks suggest the approach can improve performance over the reported fine-tuning and RAG baselines, though the evidence is bounded by the paper’s in-domain setting and the details available in the supplied pages.

- **strength**: The core contribution is a concrete training-data strategy that exposes models to relevant and irrelevant retrieved documents, while sometimes omitting the oracle document.
  - Page 3 · citation: not_found
  - Quote: "For P fraction of the questions (qi) in the dataset, we retain the oracle document (d∗i ) along with distractor documents (dk−1)."

- **strength**: The reported benchmark results show substantial gains over domain-specific fine-tuning on some tasks, including HotpotQA and HuggingFace APIBench.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **limitation**: The authors explicitly scope the work to testing on the same document collection used during training, so the results do not establish transfer to new domains or document collections.
  - Page 9 · citation: whitespace
  - Quote: "our paper studies a slightly opposite scenario where we only care about testing the LLM on the same set of documents."

- **uncertainty**: The CoT ablation is not uniformly positive across the listed datasets: the reported Torch Hub score is higher without CoT. The supplied pages do not explain this variation.
  - Page 7 · citation: exact
  - Quote: "RAFT w.o CoT 68.30 25.62 59.07 86.56 83.21"

Unresolved questions:

- How sensitive are the benchmark gains to training-data construction, retrieval quality, and evaluation choices? The supplied pages do not provide enough detail to assess these factors fully.
- Would RAFT’s advantages persist when evaluated on document collections or domains not seen during fine-tuning?
- Why does CoT reduce the reported Torch Hub score, despite improving scores on several other datasets?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
