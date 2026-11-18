# T20: RAFT: Adapting Language Model to Domain Specific RAG

**baseline · ok**

1 model calls · 0 reads · 7.30 s · $0.000472

1 decisions · 0 tool calls · 13497 input tokens (13494 cached) · 674 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.65

RAFT is a fine-tuning recipe for domain-specific, open-book question answering: train on questions and retrieved documents that mix answer-bearing context with distractors, and sometimes omit the oracle document. The paper reports gains over several fine-tuning and RAG baselines across medical QA, multi-hop QA, and API benchmarks. The approach is simple and supported by ablations, though its stated scope is in-domain use and the supplied pages leave some evaluation and training details unclear.

- **strength**: The central training design explicitly addresses imperfect retrieval by combining oracle and distractor contexts, and sometimes training without the oracle context.
  - Page 3 · citation: not_found
  - Quote: "For P fraction of the questions (qi) in the dataset, we retain the oracle document (d∗i ) along with distractor documents"

- **strength**: The reported benchmark table shows RAFT outperforming the listed domain-specific fine-tuning baselines on most tasks, with PubMed performance close to DSF + RAG.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **limitation**: The authors delimit the intended setting to testing on the same document collection used for training, which narrows the scope of the generalization claim.
  - Page 9 · citation: whitespace
  - Quote: "our paper studies a slightly opposite scenario where we only care about testing the LLM on the same set of documents."

- **uncertainty**: The supplied pages report benchmark scores and describe dataset-specific choices of the oracle-context fraction, but do not provide enough detail here to assess run-to-run variability or statistical uncertainty.
  - Page 6 · citation: whitespace
  - Quote: "our findings challenge this assumption: incorporating a portion of the training data without the oracle document"

Unresolved questions:

- How sensitive are the reported gains to random seeds, training-data construction, and answer/reasoning generation choices?
- How well does RAFT transfer to new document collections or domains, given that the paper states its focus is testing on the same documents?
- What accounts for the reported dataset-to-dataset variation in the best fraction of training examples that include oracle documents?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
