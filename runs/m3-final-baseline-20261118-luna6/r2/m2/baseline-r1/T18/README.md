# T18: Gorilla: Large Language Model Connected with Massive APIs

**baseline · ok**

1 model calls · 0 reads · 8.94 s · $0.000541

1 decisions · 0 tool calls · 17424 input tokens (17421 cached) · 732 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Gorilla combines instruction fine-tuning of a LLaMA-7B model with API-document retrieval, and introduces APIBench for evaluating API selection and call generation across three ML model hubs. Its reported results show strong gains over zero-shot baseline models on several benchmark settings and suggest that retrieval-aware training can help adapt calls to changed documentation. The work offers a useful benchmark and pipeline, but its evaluation is largely based on matching API-call syntax to dataset entries rather than executing calls or verifying task outcomes. The supplied pages do not include enough detail to assess statistical uncertainty or the robustness of the documentation-change demonstrations.

- **strength**: The paper reports substantial zero-shot gains for Gorilla on the three benchmark collections, especially HuggingFace and TensorFlow Hub, against the evaluated baselines.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: The correctness measure identifies calls through AST matching to dataset entries; the paper itself notes that execution results are not tested. Thus, the reported accuracy does not establish that generated calls run successfully or complete the requested task.
  - Page 5 · citation: exact
  - Quote: "we adopt the AST tree-matching strategy"

- **uncertainty**: The documentation-change evidence is presented through examples, but the inspected pages do not show a quantitative evaluation across a broader set of changes. How often does retrieval-aware training generalize to novel updates rather than the illustrated cases?
  - Page 8 · citation: whitespace
  - Quote: "This includes alterations such as upgrading the FCN’s ResNet-50 backbone to ResNet-101"

- **limitation**: The dataset’s HuggingFace coverage is intentionally restricted to selected models, and the paper says this makes evaluation for other models a domain-name choice rather than exact API matching. This limits how broadly the headline results generalize across that hub.
  - Page 7 · citation: whitespace
  - Quote: "for all the models except Gorilla, we only check if they can provide the correct domain names"

Unresolved questions:

- How well do the reported gains hold when generated API calls are executed and evaluated for task success, including dependency, argument, and environment failures?
- How robust are the results to alternative train/test splits, different synthetic instruction generations, and a wider range of real user requests?
- Can retrieval remain effective when documentation changes are substantial or when the retriever returns irrelevant or conflicting documents?
- The inspected pages do not provide uncertainty estimates for the reported benchmark results; how sensitive are the model comparisons to sampling and evaluation variation?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
