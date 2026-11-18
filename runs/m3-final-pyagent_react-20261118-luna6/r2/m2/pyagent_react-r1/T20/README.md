# T20: RAFT: Adapting Language Model to Domain Specific RAG

**pyagent_react · ok**

7 model calls · 4 reads · 14.05 s · $0.001853

7 decisions · 5 tool calls · 40083 input tokens (30634 cached) · 732 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

RAFT proposes a supervised fine-tuning recipe for domain-specific, open-book QA: train on questions with relevant and distractor documents, sometimes omit the oracle document, and use answers with quoted evidence and reasoning. Results across biomedical QA, HotpotQA, and API documentation show useful gains over several baselines, with ablations on reasoning and document mixtures. Its scope is deliberately in-domain; evidence does not establish comparable benefit when test documents differ from training documents.

- **strength**: The training recipe explicitly models imperfect retrieval by mixing oracle and distractor documents and sometimes omitting the oracle, targeting the open-book inference setting.
  - Page 3 · citation: whitespace
  - Quote: "For (1 − P ) fraction of the questions (qi) in the dataset, we include no oracle document and only include distractor documents (dk)."

- **strength**: The reported benchmark table shows gains over DSF + RAG on several tasks, but not uniformly: PubMed is tied and Torch Hub is nearly tied with DSF.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **strength**: The CoT ablation supports a benefit on some datasets, while results are mixed: RAFT without CoT scores higher on Torch Hub.
  - Page 7 · citation: exact
  - Quote: "RAFT w.o CoT 68.30 25.62 59.07 86.56 83.21"

- **limitation**: The paper expressly limits its central setting to testing on the same documents as training, so its evidence does not establish cross-document generalization.
  - Page 9 · citation: whitespace
  - Quote: "our paper studies a slightly opposite scenario where we only care about testing the LLM on the same set of documents."

Unresolved questions:

- How well does the recipe transfer to test documents or domains that differ from those used for training?
- How sensitive are the results to choices of base model, training-data construction, and retrieval quality beyond the reported setups?
- What are the computational costs and reproducibility details for generating reasoning-and-quotation training targets? The inspected pages do not resolve these points.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 2, "end": 4}` | Inspect the method and experimental setup. | read pages [2, 3, 4] | [event 14](trace.jsonl#L14) |
| 4 | read_pages `{"start": 5, "end": 6}` | Inspect quantitative results and ablation evidence. | read pages [5, 6] | [event 19](trace.jsonl#L19) |
| 5 | search_paper `{"query": "limitations"}` | Check whether the paper explicitly states scope limits. | 0 matches | [event 24](trace.jsonl#L24) |
| 6 | read_pages `{"start": 7, "end": 9}` | Inspect generalization results and discussion. | read pages [7, 8, 9] | [event 29](trace.jsonl#L29) |
| 7 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Submit a balanced assessment grounded in the inspected method, results, and stated scope. | review accepted | [event 34](trace.jsonl#L34) |
