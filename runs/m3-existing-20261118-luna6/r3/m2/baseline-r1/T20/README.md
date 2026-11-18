# T20: RAFT: Adapting Language Model to Domain Specific RAG

**baseline · ok**

1 model calls · 0 reads · 10.16 s · $0.000510

1 decisions · 0 tool calls · 13497 input tokens (13494 cached) · 750 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

RAFT is a simple training recipe for domain-specific open-book QA: fine-tune on questions paired with relevant and distractor documents, sometimes omit the relevant document, and train answers to include reasoning and quotations. The reported experiments show substantial gains over several fine-tuning and RAG baselines on selected QA and API-document tasks. Its evidence is promising but bounded: the paper explicitly targets evaluation on the same document collection used for training, and the supplied results leave some important setup and generalization questions open.

- **strength**: The recipe directly trains models to use relevant context while contending with distractors, matching the paper’s stated target setting.
  - Page 3 · citation: whitespace
  - Quote: "we prepare the training data such that each data point contains a question (Q), a set of documents (Dk), and a corresponding Chain-of-though style answer ( A∗) generated from one of the document (D∗)."

- **strength**: The reported benchmark results include meaningful gains over the listed baselines on several tasks, though results vary by dataset and metric.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **limitation**: The authors define the work’s scope as same-document-set evaluation, so the reported evidence does not establish transfer to new document collections.
  - Page 9 · citation: whitespace
  - Quote: "our paper studies a slightly opposite scenario where we only care about testing the LLM on the same set of documents."

- **uncertainty**: The supplied results do not make the exact experimental setup fully clear: the main table labels the RAFT row without an explicit RAG suffix, while the surrounding discussion describes RAFT with RAG. The provided pages also do not expose full numerical values for the plotted sensitivity analyses.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B)"

Unresolved questions:

- How well does RAFT transfer to new document collections, rather than the training document set?
- What retrieval, training, and evaluation details account for the difference between the table’s RAFT label and the text’s descriptions of RAFT with RAG?
- How sensitive are the reported gains to the source and quality of generated reasoning and quotations, beyond the CoT ablation shown?
- Assessment is limited to the supplied pages (1–11); the sensitivity plots are not provided as full numerical tables, limiting scrutiny of those results.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
