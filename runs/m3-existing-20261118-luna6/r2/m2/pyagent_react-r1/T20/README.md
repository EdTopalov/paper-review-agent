# T20: RAFT: Adapting Language Model to Domain Specific RAG

**pyagent_react · ok**

5 model calls · 3 reads · 14.35 s · $0.001804

5 decisions · 4 tool calls · 30820 input tokens (21411 cached) · 829 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

RAFT is a practical fine-tuning recipe for domain-specific open-book QA: train with relevant and distractor documents, sometimes omit the oracle context, and provide quoted reasoning targets. The reported benchmark comparisons and CoT ablation offer useful evidence of gains, though the inspected results do not establish broad generalization beyond the paper’s fixed-document setting.

- **strength**: The method explicitly trains models to handle imperfect retrieval, including distractors and examples without oracle context.
  - Page 3 · citation: whitespace
  - Quote: "For (1 − P ) fraction of the questions (qi) in the dataset, we include no oracle document and only include distractor documents (dk)."

- **strength**: The reported comparison shows RAFT scoring above the listed DSF + RAG baseline on several benchmarks, while PubMed is tied; this is evidence of benefit but not uniform superiority over every baseline.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **strength**: The paper reports a CoT ablation, with RAFT improving HotpotQA and HuggingFace over the version without CoT, but the inspected table shows lower scores on Torch Hub.
  - Page 7 · citation: exact
  - Quote: "RAFT w.o CoT 68.30 25.62 59.07 86.56 83.21"

- **limitation**: The paper distinguishes its target setting from RAG that tests on documents different from training; this is an explicit scope boundary, limiting claims about out-of-domain transfer.
  - Page 9 · citation: whitespace
  - Quote: "our paper studies a slightly opposite scenario where we only care about testing the LLM on the same set of documents."

Unresolved questions:

- How sensitive are the gains to training-data construction, compute, and choices of model beyond the reported setup?
- Would RAFT retain its advantages when test documents differ from the training collection, or under substantially different retrieval errors?
- I inspected pages 1–9, including selected method and results passages; I did not inspect pages 10–11 or the complete experimental setup, so details such as statistical variability and all implementation choices remain uncertain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect RAFT's training method and reported evaluation evidence. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Check quantitative results, ablations, and stated evaluation qualifications. | read pages [5, 6, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 9}` | Inspect the paper's conclusion, limitations, and remaining scope boundaries. | read pages [8, 9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit an evidence-based assessment using the inspected method, results, ablation, and scope statements. | review accepted | [event 25](trace.jsonl#L25) |
