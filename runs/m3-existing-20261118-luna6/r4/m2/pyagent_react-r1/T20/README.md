# T20: RAFT: Adapting Language Model to Domain Specific RAG

**pyagent_react · ok**

6 model calls · 3 reads · 18.41 s · $0.002553

6 decisions · 5 tool calls · 46777 input tokens (34842 cached) · 1427 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

RAFT is a practical fine-tuning recipe for domain-specific, open-book QA: train on question–document contexts containing relevant and distractor documents, sometimes omit the oracle context, and use answers with reasoning and direct quotations. The reported results and ablations suggest this helps LLaMA-2-7B use retrieved context and tolerate distractors on the evaluated tasks. Its strongest claim is in-domain performance on the document collections studied, not generalization to new domains or collections.

- **strength**: The recipe distinguishes answer-bearing oracle documents from distractors and trains with both, targeting the ability to use context despite retrieval noise.
  - Page 3 · citation: whitespace
  - Quote: "We differentiate between two types of documents:"

- **strength**: The reported comparison shows sizable improvements over the listed baselines on several tasks, though results are not uniformly better on every column.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **strength**: The paper includes a CoT ablation with mixed results: gains on PubMed, HotpotQA, HuggingFace, and TensorFlow Hub, but a lower Torch Hub score.
  - Page 7 · citation: exact
  - Quote: "RAFT w.o CoT 68.30 25.62 59.07 86.56 83.21"

- **limitation**: The authors delimit their target to testing on the same document collection as training, so the evidence does not establish transfer to unseen collections.
  - Page 9 · citation: whitespace
  - Quote: "our paper studies a slightly opposite scenario where we only care about testing the LLM on the same set of documents."

Unresolved questions:

- How robust are the reported gains across random seeds, training-data construction choices, and evaluation runs? Those details and uncertainty estimates were not established by the excerpts inspected.
- How well does the approach transfer to new document collections, domains, or retrieval systems? The paper states a same-document scope; broader transfer remains unanswered.
- How much of the improvement comes from distractor training, oracle omission, quoted evidence, and reasoning together? A CoT ablation is reported, but component interactions were not established in the pages inspected.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the RAFT training recipe and evaluation setup. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Inspect quantitative results, ablations, and evaluation details. | read pages [5, 6, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 10}` | Review discussion, limitations, and reproducibility-related details. | read pages [8, 9, 10] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit an evidence-based assessment using the inspected method, results, and stated scope. | citation_validation_failed; #1: not_found | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Replace the failed method citation with a short exact quote from the inspected page. | review accepted | [event 30](trace.jsonl#L30) |
