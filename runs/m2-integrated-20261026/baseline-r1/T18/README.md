# T18: Gorilla: Large Language Model Connected with Massive APIs

**baseline · ok**

1 model calls · 0 reads · 8.24 s · $0.002545

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.66

Gorilla combines API-focused instruction fine-tuning with retrieval-aware training and introduces APIBench to study model selection and API-call generation across three ML model hubs. Its results show strong performance on the benchmark, including reduced API hallucination in several settings, while highlighting that retrieval quality can materially affect outcomes. The contribution is useful and empirically supported within a narrow, mostly ML-API scope; the evaluation measures API identification more directly than whether generated calls work in practice.

- **strength**: The benchmark spans multiple model hubs and includes documented collection and instruction-generation procedures, making the work a concrete resource as well as a model study.
  - Page 4 · citation: exact
  - Quote: "Dataset curation: 1,645 API calls."

- **strength**: On the reported benchmark, Gorilla’s zero-shot accuracy is substantially higher than the compared models on HuggingFace and TensorFlow Hub; the results also show that retrieval outcomes vary with the retriever.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: The evaluation primarily checks API identity and selected arguments rather than whether the generated code executes successfully or achieves the requested task.
  - Page 13 · citation: whitespace
  - Quote: "We de-prioritize this as we haven’t tested the execution result of the code."

- **uncertainty**: The paper reports a holdout split of instruction–API pairs, but it is unclear whether evaluation on unseen instructions for APIs also tests generalization to APIs absent from training. The HuggingFace comparison additionally uses a different success criterion for most baselines.
  - Page 7 · citation: wrong_page
  - Quote: "The holdout test set was created by dividing the self-instruct dataset’s instruction, API pairs into training and testing sets."

Unresolved questions:

- How well does Gorilla generalize to APIs, documentation formats, and domains outside the selected ML hubs, particularly when APIs are not represented in fine-tuning data?
- How often do the generated calls execute correctly and satisfy the user’s task, beyond matching the benchmark’s API and argument criteria?
- How sensitive are the reported results to the instruction-generation process and to the differing HuggingFace evaluation criteria across Gorilla and the other models?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes collecting API documentation from Torch Hub, TensorFlow Hub, and HuggingFace, and explains the filtering and GPT-4 self-instruct procedure used to create instruction–API pairs (pp. 2–4). The appendix adds dataset and task details (p. 13).
- Observation 2: **supported** — Table 1 reports Gorilla’s zero-shot accuracy as 71.68 on HuggingFace and 83.79 on TensorFlow Hub, higher than the listed comparison models; the table also shows different outcomes across retriever settings (p. 7).
- Observation 3: **supported** — The evaluation matches API calls and selected arguments using AST subtrees, rather than testing whether the generated code executes or completes the requested task (pp. 5–6). The appendix explicitly says execution results were not tested (p. 13).
- Observation 4: **supported** — The paper says the holdout set was made by splitting instruction–API pairs, but does not specify whether APIs themselves were held out, leaving API-level generalization unclear (p. 6; see also the split details on p. 13). It also explicitly states that for HuggingFace, all models except Gorilla are evaluated only for correct domain names, unlike the AST-based evaluation applied to Torch Hub and TensorFlow Hub (p. 7).

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: final_answer

Returned the final assessment.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": "{\n  \"score\": 0.66,\n  \"summary\": \"Gorilla combines API-focused instruction fine-tuning with retrieval-aware training and introduces APIBench to study model selection and API-call generation across three ML model hubs. Its results show strong performance on the benchmark, including reduced API hallucination in several settings, while highlighting that retrieval quality can materially affect outcomes. The contribution is useful and empirically supported within a narrow, mostly ML-API scope; the evaluation measures API identification more directly than whether generated calls work in practice.\",\n  \"observations\": [\n    {\n      \"kind\": \"strength\",\n      \"claim\": \"The benchmark spans multiple model hubs and includes documented collection and instruction-generation procedures, making the work a concrete resource as well as a model study.\",\n      \"page\": 4,\n      \"quote\": \"Dataset curation: 1,645 API calls.\"\n    },\n    {\n      \"kind\": \"strength\",\n      \"claim\": \"On the reported benchmark, Gorilla’s zero-shot accuracy is substantially higher than the compared models on HuggingFace and TensorFlow Hub; the results also show that retrieval outcomes vary with the retriever.\",\n      \"page\": 7,\n      \"quote\": \"Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80\"\n    },\n    {\n      \"kind\": \"limitation\",\n      \"claim\": \"The evaluation primarily checks API identity and selected arguments rather than whether the generated code executes successfully or achieves the requested task.\",\n      \"page\": 13,\n      \"quote\": \"We de-prioritize this as we haven’t tested the execution result of the code.\"\n    },\n    {\n      \"kind\": \"uncertainty\",\n      \"claim\": \"The paper reports a holdout split of instruction–API pairs, but it is unclear whether evaluation on unseen instructions for APIs also tests generalization to APIs absent from training. The HuggingFace comparison additionally uses a different success criterion for most baselines.\",\n      \"page\": 7,\n      \"quote\": \"The holdout test set was created by dividing the self-instruct dataset’s instruction, API pairs into training and testing sets.\"\n    }\n  ],\n  \"unresolved_questions\": [\n    \"How well does Gorilla generalize to APIs, documentation formats, and domains outside the selected ML hubs, particularly when APIs are not represented in fine-tuning data?\",\n    \"How often do the generated calls execute correctly and satisfy the user’s task, beyond matching the benchmark’s API and argument criteria?\",\n    \"How sensitive are the reported results to the instruction-generation process and to the differing HuggingFace evaluation criteria across Gorilla and the other models?\"\n  ]\n}",
  "observation": {}
}
```

</details>
