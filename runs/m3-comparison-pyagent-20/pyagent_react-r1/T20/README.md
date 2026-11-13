# T20: RAFT: Adapting Language Model to Domain Specific RAG

**pyagent_react · ok**

4 model calls · 2 reads · 14.56 s · $0.002452

4 decisions · 4 tool calls · 25807 input tokens (12089 cached) · 1233 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

RAFT proposes training language models for in-domain RAG using questions, relevant and distractor documents, and answer explanations that cite source text. The reported evaluations and ablations provide useful evidence that this recipe can improve some RAG tasks and help models handle distractors, while also showing that effects vary by dataset. This is a substantial, practical contribution, though the inspected evidence leaves important questions about robustness and evaluation scope.

- **strength**: The approach directly trains for the test-time setting by combining relevant and irrelevant context, and its evaluations cover several task domains.
  - Page 3 · citation: whitespace
  - Quote: "We then fine-tune the language model using the standard supervised training (SFT) technique, training it to generate answers from the provided documents and questions."

- **strength**: The paper reports an ablation supporting the value of reasoning traces, with gains on some datasets but not uniformly across all reported metrics.
  - Page 7 · citation: whitespace
  - Quote: "With a gain of 9.66% and 14.93% on the Hotpot QA and HuggingFace datasets respectively."

- **limitation**: The paper itself reports that RAFT does not yield significant gains over DSF + RAG on PubMed QA, tempering the broad claim of consistent improvement.
  - Page 4 · citation: whitespace
  - Quote: "Note that for PubMed QA, since it is a binary yes/no question, we don’t observe significant gains when we compare our model with DSF + RAG."

- **uncertainty**: The paper reports dataset-dependent optimal training proportions, but the inspected evidence does not establish how stable those choices are across seeds or other settings.
  - Page 6 · citation: whitespace
  - Quote: "Our analysis reveals that the optimal proportion varies across datasets"

Unresolved questions:

- How sensitive are the reported improvements and selected training proportions to random seeds, data construction, and retriever quality?
- How well does the recipe transfer to domains or retrieval conditions beyond those evaluated?
- Inspection was limited to the initial page and pages 3–8; pages 2 and 9–11 were not inspected, so details there may qualify the assessment.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 3, "end": 5}` | Inspect the method details and reported evaluation evidence. | read pages [3, 4, 5] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 6, "end": 8}` | Inspect ablations, training configuration, and any stated evaluation caveats. | read pages [6, 7, 8] | [event 11](trace.jsonl#L11) |
| 3 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit an evidence-based assessment using the inspected abstract and pages 3–8. | citation_validation_failed; #4: hyphenation_ambiguous (pages [6]) | [event 17](trace.jsonl#L17) |
| 4 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Replace the ambiguous hyphenated citation with an exact observed phrase from page 6. | review accepted | [event 23](trace.jsonl#L23) |
