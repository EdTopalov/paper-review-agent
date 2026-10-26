# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**baseline · ok**

1 model calls · 0 reads · 7.22 s · $0.002584

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.69

The paper proposes Plan-and-Solve prompting, a zero-shot prompting strategy that asks an LLM to devise and execute a plan, with PS+ adding instructions to extract variables and attend to intermediate calculations. Tests on ten datasets report consistent improvements over Zero-shot-CoT, with particularly strong arithmetic results. The contribution is practical and supported by broad benchmark comparisons, though the evidence is limited to one GPT-3 engine and does not establish how reliably the gains generalize.

- **strength**: The evaluation spans arithmetic, commonsense, and symbolic reasoning, and reports gains over Zero-shot-CoT across the tested datasets.
  - Page 2 · citation: whitespace
  - Quote: "We evaluate our proposed prompting on six math reasoning datasets"

- **strength**: The math results show meaningful gains for PS+, including a higher average than the listed zero-shot baselines and Auto-CoT.
  - Page 6 · citation: exact
  - Quote: "PS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7"

- **limitation**: The authors explicitly identify prompt design and model sensitivity as a practical constraint on applying the method.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3 models are sensitive to the expressions in prompts, thus we need to carefully design the prompts."

- **uncertainty**: The reported evidence is specific to text-davinci-003 in the main experiments; whether the gains transfer to other model families remains unresolved.
  - Page 5 · citation: hyphenation_ambiguous
  - Quote: "We report the results using text-davinci-003 engine for GPT-3 in the main paper."

Unresolved questions:

- Do the observed gains persist across other model families, model sizes, and current prompting interfaces?
- How sensitive are results to prompt wording and selection, particularly given the reported prompt sensitivity?
- The inspected pages describe a 100-example error analysis but provide limited detail about annotation reliability; how stable are the reported error-category differences under independent annotation or repeated samples?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper evaluates ten datasets across arithmetic, commonsense, and symbolic reasoning (pp. 2, 4–5). It reports PS+ outperforming Zero-shot-CoT on all ten (pp. 5–6).
- Observation 2: **supported** — Table 2 reports PS+ at a 76.7 average, above the listed Zero-shot-CoT (70.4), PoT (73.5), PS (72.9), and Auto-CoT (75.9) averages (p. 6).
- Observation 3: **supported** — The limitations section explicitly says prompt design takes effort and GPT-3 models are sensitive to prompt expressions, requiring careful design (p. 9).
- Observation 4: **supported** — The main-paper experiments report results using text-davinci-003 (p. 5). The paper does not establish transfer to other model families, so that remains unresolved.

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: final_answer

Returned the final assessment.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": "{\n  \"score\": 0.69,\n  \"summary\": \"The paper proposes Plan-and-Solve prompting, a zero-shot prompting strategy that asks an LLM to devise and execute a plan, with PS+ adding instructions to extract variables and attend to intermediate calculations. Tests on ten datasets report consistent improvements over Zero-shot-CoT, with particularly strong arithmetic results. The contribution is practical and supported by broad benchmark comparisons, though the evidence is limited to one GPT-3 engine and does not establish how reliably the gains generalize.\",\n  \"observations\": [\n    {\n      \"kind\": \"strength\",\n      \"claim\": \"The evaluation spans arithmetic, commonsense, and symbolic reasoning, and reports gains over Zero-shot-CoT across the tested datasets.\",\n      \"page\": 2,\n      \"quote\": \"We evaluate our proposed prompting on six math reasoning datasets\"\n    },\n    {\n      \"kind\": \"strength\",\n      \"claim\": \"The math results show meaningful gains for PS+, including a higher average than the listed zero-shot baselines and Auto-CoT.\",\n      \"page\": 6,\n      \"quote\": \"PS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7\"\n    },\n    {\n      \"kind\": \"limitation\",\n      \"claim\": \"The authors explicitly identify prompt design and model sensitivity as a practical constraint on applying the method.\",\n      \"page\": 9,\n      \"quote\": \"The GPT-3 models are sensitive to the expressions in prompts, thus we need to carefully design the prompts.\"\n    },\n    {\n      \"kind\": \"uncertainty\",\n      \"claim\": \"The reported evidence is specific to text-davinci-003 in the main experiments; whether the gains transfer to other model families remains unresolved.\",\n      \"page\": 5,\n      \"quote\": \"We report the results using text-davinci-003 engine for GPT-3 in the main paper.\"\n    }\n  ],\n  \"unresolved_questions\": [\n    \"Do the observed gains persist across other model families, model sizes, and current prompting interfaces?\",\n    \"How sensitive are results to prompt wording and selection, particularly given the reported prompt sensitivity?\",\n    \"The inspected pages describe a 100-example error analysis but provide limited detail about annotation reliability; how stable are the reported error-category differences under independent annotation or repeated samples?\"\n  ]\n}",
  "observation": {}
}
```

</details>
