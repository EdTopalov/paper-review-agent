# T18: Gorilla: Large Language Model Connected with Massive APIs

**baseline · ok**

1 model calls · 0 reads · 10.76 s · $0.000486

1 decisions · 0 tool calls · 17424 input tokens (17421 cached) · 623 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Gorilla presents an API-calling benchmark built from ML model hubs and a retrieval-aware fine-tuning approach for a LLaMA-7B model. On the reported benchmark, fine-tuned Gorilla improves API identification over several prompted LLM baselines and can use retrieved documentation to respond to API changes. The work is useful and clearly evaluated within its chosen setting, but its conclusions are bounded by synthetic instructions, ML-focused APIs, and a correctness metric that primarily checks API identity and selected arguments.

- **strength**: The paper contributes a concrete benchmark and systematic comparisons across API sources and retrieval settings; it also reports that retrieval is not uniformly helpful.
  - Page 6 · citation: not_found
  - Quote: "We have maintained a holdout test set on which we report our findings."

- **limitation**: The central accuracy metric does not establish that generated calls execute successfully or produce the intended behavior; the paper explicitly leaves execution testing for future work.
  - Page 13 · citation: whitespace
  - Quote: "We de-prioritize this as we haven’t tested the execution result of the code."

- **limitation**: Evaluation is not fully comparable across API sources: for HuggingFace, most baselines are checked only for the correct domain, while Gorilla is evaluated against API calls.
  - Page 7 · citation: whitespace
  - Quote: "for all the models except Gorilla, we only check if they can provide the correct domain names."

Unresolved questions:

- How well do the reported gains transfer to real user queries and API catalogs beyond the selected ML hubs, given that instruction-answer pairs are synthetically generated?
- How often do generated calls execute correctly and satisfy the user’s task when evaluated end to end, rather than by AST matching?
- What is the impact of splitting instruction-API pairs into train and test sets while examples share the same underlying APIs?
- This assessment is based on the supplied paper text and figures; I did not inspect supplementary material beyond the included pages or independently verify the reported experiments.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
