# T20: RAFT: Adapting Language Model to Domain Specific RAG

**baseline · ok**

1 model calls · 0 reads · 9.10 s · $0.000511

1 decisions · 0 tool calls · 13497 input tokens (13494 cached) · 752 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.66

RAFT is a fine-tuning recipe for domain-specific, open-book question answering: train on questions with relevant and distractor documents, and sometimes omit the relevant document, while using answers that quote supporting text and explain the reasoning. The reported results are promising across several tasks, but the paper frames its target as in-domain use on the same document collection, so its evidence does not establish broader transfer.

- **strength**: The paper evaluates the method across medical QA, multi-hop Wikipedia QA, and API documentation, and reports gains over several fine-tuning and RAG baselines.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **strength**: The ablation provides evidence that reasoning-style training helps on some tasks, while also showing that the effect is not uniform: RAFT without CoT scores higher on Torch Hub.
  - Page 7 · citation: exact
  - Quote: "RAFT w.o CoT 68.30 25.62 59.07 86.56 83.21"

- **limitation**: The authors explicitly limit the study to testing on the same documents used in training; the results therefore do not establish generalization to new document collections.
  - Page 9 · citation: whitespace
  - Quote: "we only care about testing the LLM on the same set of documents."

Unresolved questions:

- How well does RAFT transfer when the test-time document collection differs from the training collection?
- How sensitive are the reported gains to the choice of training and test document sampling, retrieval quality, and answer-generation procedure?
- The inspected evidence covers the reported benchmark results and discussion, but does not establish whether the gains persist under broader deployment conditions or across additional model sizes.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
