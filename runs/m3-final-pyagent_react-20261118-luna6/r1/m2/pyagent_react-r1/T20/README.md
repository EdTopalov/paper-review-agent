# T20: RAFT: Adapting Language Model to Domain Specific RAG

**pyagent_react · ok**

7 model calls · 4 reads · 24.47 s · $0.001842

7 decisions · 6 tool calls · 41082 input tokens (34604 cached) · 1373 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.66

RAFT trains language models for domain-specific retrieval-augmented question answering using question/context/answer examples that include oracle and distractor documents, with cited reasoning in the answer. Across several biomedical, QA, and API-document benchmarks, the paper reports gains over standard domain fine-tuning and RAG baselines. The approach is a practical adaptation recipe, though the inspected evidence leaves questions about how broadly the reported comparisons support its claims.

- **strength**: The recipe explicitly trains on relevant and irrelevant retrieved context, targeting the practical challenge of ignoring distractors.
  - Page 3 · citation: whitespace
  - Quote: "we include no oracle document and only include distractor documents (dk)."

- **strength**: The reported benchmark results show RAFT ahead of several listed baselines on the displayed datasets, including HotpotQA and HuggingFace.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **limitation**: The paper reports that the best oracle-context proportion differs across datasets, so this training choice is not shown to have one universal setting.
  - Page 6 · citation: exact
  - Quote: "the optimal proportion varies across datasets"

- **uncertainty**: The inspected results establish evaluation on a mix of QA, API, and biomedical tasks, but do not resolve how well the recipe transfers to other domains or retrieval conditions.
  - Page 4 · citation: whitespace
  - Quote: "We selected these datasets to represent both popular and diverse domains including Wikipedia, Coding/API documents, and question-answering on medical documents."

Unresolved questions:

- How sensitive are the reported gains to dataset construction and answer-generation choices, beyond the CoT and oracle-proportion analyses inspected?
- How well does RAFT transfer to domains or retriever behaviors not represented by the evaluated datasets?
- I inspected the abstract and selected pages on method, datasets, results, and training analyses, not the full paper; details in uninspected passages could affect these questions.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 3}` | Inspect the RAFT training recipe and evaluation setup. | read pages [2, 3] | [event 6](trace.jsonl#L6) |
| 2 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 5, "end": 6}` | Inspect benchmark results and comparison evidence. | read pages [5, 6] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "limitations"}` | Check the paper's stated scope boundaries and limitations. | 0 matches | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 4, "end": 4}` | Inspect dataset, model, and evaluation details behind reported results. | read pages [4] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.66, "observations": 4}}` | Submit a balanced assessment using observed method, benchmark, and training-analysis evidence. | citation_validation_failed; #3: not_found | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.66, "observations": 4}}` | Correct the oracle-proportion citation to an exact observed phrase. | review accepted | [event 35](trace.jsonl#L35) |
