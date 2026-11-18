# T20: RAFT: Adapting Language Model to Domain Specific RAG

**baseline · ok**

1 model calls · 0 reads · 9.78 s · $0.000501

1 decisions · 0 tool calls · 13497 input tokens (13494 cached) · 731 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

RAFT is a fine-tuning recipe for in-domain, open-book question answering: training examples combine questions, relevant and distractor documents, and answers with quoted evidence and reasoning; some examples omit the relevant document. The paper reports improvements over several fine-tuning and RAG baselines, and studies the effects of reasoning traces, relevant-document frequency, and distractor counts. The contribution is practical and supported by multiple evaluations, but its stated focus on testing against the same document collection limits the scope of the generalization claims.

- **strength**: The paper gives a clear, actionable training setup that explicitly prepares models to handle retrieved distractors and sometimes missing relevant context.
  - Page 3 · citation: whitespace
  - Quote: "For (1 − P ) fraction of the questions (qi) in the dataset, we include no oracle document and only include distractor documents (dk)."

- **strength**: The paper reports evaluations across several domains and an ablation suggesting that reasoning traces can help, though the effect varies by dataset.
  - Page 7 · citation: whitespace
  - Quote: "Results on various datasets show that adding CoT can significantly improve the performance of the finetuned model."

- **limitation**: The stated evaluation scope is in-domain: the paper distinguishes its setting from work that tests on different domains or documents, so broader transfer is not established.
  - Page 9 · citation: whitespace
  - Quote: "our paper studies a slightly opposite scenario where we only care about testing the LLM on the same set of documents."

- **uncertainty**: The supplied paper pages report headline comparisons and selected ablations, but do not make the training and evaluation procedure sufficiently detailed here to assess reproducibility or the robustness of the reported gains. This is an evidence gap, not a demonstrated defect.
  - Page 4 · citation: hyphenation_ambiguous
  - Quote: "We design our experiments to study how well RAFT performs compared to various baselines."

Unresolved questions:

- How sensitive are the reported gains to the choice of retrieved passages, distractor construction, and answer/reasoning generation process?
- Would the recipe transfer to document collections or domains not seen during fine-tuning, given the paper's explicitly same-document evaluation scope?
- How stable are the reported differences across training runs, and what are the corresponding uncertainty estimates?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
