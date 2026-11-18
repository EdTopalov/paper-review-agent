# T20: RAFT: Adapting Language Model to Domain Specific RAG

**pyagent_react · ok**

5 model calls · 2 reads · 17.31 s · $0.001614

5 decisions · 3 tool calls · 30282 input tokens (23274 cached) · 1012 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

RAFT trains a language model for domain-specific RAG using retrieved contexts that include relevant and distractor documents, with answers that quote supporting passages and provide reasoning. The paper reports gains over several fine-tuning and RAG baselines, and investigates the effects of reasoning supervision, oracle-context frequency, and varying numbers of retrieved documents.

- **strength**: The reported benchmark results show sizable gains over several baselines on some evaluated tasks, including HotpotQA and HuggingFace.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **strength**: The CoT ablation reports gains on several datasets, while also showing that the effect is not uniformly positive across all listed benchmarks.
  - Page 7 · citation: exact
  - Quote: "RAFT w.o CoT 68.30 25.62 59.07 86.56 83.21"

- **strength**: The paper examines how training with distractors relates to test-time retrieval variation, rather than evaluating only one fixed context count.
  - Page 8 · citation: whitespace
  - Quote: "We study how robust RAFT is to varying numbers of test-time documents that a retriever might provide."

- **uncertainty**: The inspected results do not establish how robust the reported gains are to evaluation variability or alternative data-generation choices; those details were not assessed in the passages inspected.
  - Page 4 · citation: whitespace
  - Quote: "For all the datasets in our experiments, we generate the answers using the technique described above."

Unresolved questions:

- How sensitive are the results to the choice and quality of generated reasoning traces and quoted evidence?
- Do the reported gains persist across additional domains, retrieval systems, and evaluation settings?
- What variability or statistical uncertainty accompanies the benchmark results?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 4, "end": 6}` | Inspect RAFT training design and reported evaluation results. | read pages [4, 5, 6] | [event 6](trace.jsonl#L6) |
| 2 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 7, "end": 8}` | Inspect additional generalization evidence and implementation details. | read pages [7, 8] | [event 15](trace.jsonl#L15) |
| 4 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit an evidence-based assessment from the abstract and inspected evaluation pages. | review accepted | [event 24](trace.jsonl#L24) |
