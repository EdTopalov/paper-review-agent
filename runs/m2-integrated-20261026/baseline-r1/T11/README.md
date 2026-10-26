# T11: Executable Code Actions Elicit Better LLM Agents

**baseline · ok**

1 model calls · 0 reads · 9.16 s · $0.004051

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.76

The paper proposes CodeAct, a general agent-action framework in which LLMs issue executable Python code and receive execution results as observations, and contributes a 7,139-trajectory instruction dataset plus fine-tuned open models. Its controlled comparisons and agent evaluations offer meaningful evidence that code actions can improve success and reduce interaction turns on complex tool-use tasks, while also exposing considerable variation across backbones and a narrow evaluation scope.

- **strength**: The multi-tool benchmark provides a direct comparison across action formats, with CodeAct leading on success rate and average turns for most tested models; for GPT-4-1106-preview, the reported success gain over the next-best format is substantial.
  - Page 5 · citation: whitespace
  - Quote: "achieves a 20.7% absolute improvement compared to the next best action format (text) while requiring2.1 fewer interaction turns on average."

- **strength**: The paper contributes both a multi-domain interaction dataset and an open-model evaluation, including out-of-domain tasks and general-capability measures. The results are not uniformly positive, which the authors acknowledge rather than masking.
  - Page 9 · citation: whitespace
  - Quote: "Surprisingly, no improvement is observed for the Llama-2 variant."

- **limitation**: The key complex-task benchmark is small and manually curated, and its reported success rates vary sharply by model family. This limits how broadly the headline advantage can be generalized from the presented evidence.
  - Page 5 · citation: exact
  - Quote: "It contains 82 human-curated instances"

- **uncertainty**: The study evaluates executable code in an interactive Python setting but does not establish deployment safety or robustness beyond that setup; the authors themselves identify sandbox escape as a concern. I inspected the supplied main text, tables, and appendices, but did not inspect external code or supplementary artifacts.
  - Page 10 · citation: whitespace
  - Quote: "in the worst scenario (e.g., in Sci-Fi movies), such an agent may potentially break free of the sandbox restriction"

Unresolved questions:

- How stable are the M3ToolEval results across repeated runs, alternative task samples, and different tool environments?
- Which execution restrictions and monitoring mechanisms are necessary to safely grant agents access to general-purpose Python packages and code execution?
- How much of CodeActAgent’s improvement is attributable to CodeActInstruct versus the larger general-conversation mixture and other training choices?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — On M3ToolEval, CodeAct has the highest success rate for 12 of 17 models and the lowest average turns for 12 of 17. For GPT-4-1106-preview, it improves success by 20.7 percentage points over text and uses 2.1 fewer turns (PDF p. 5).
- Observation 2: **supported** — The paper reports 7,139 trajectories across multiple domains and evaluates CodeActAgent on out-of-domain agent tasks and general-capability benchmarks. It also reports that the Llama-2 variant shows no M3ToolEval improvement (PDF pp. 7–9).
- Observation 3: **supported** — M3ToolEval comprises 82 human-curated instances (PDF p. 5). Its results differ markedly across model families, including a best open-source success rate of 13.4% versus 74.4% for the best closed-source model; the stated constraint on generalizing the headline advantage is a reasonable qualification (PDF p. 5).
- Observation 4: **supported** — The evaluation describes specific benchmarks and interaction setups, not deployment safety or robustness beyond them (PDF pp. 5, 9). The authors explicitly flag the possibility of escaping sandbox restrictions and call for future safety mechanisms (PDF p. 10).

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: final_answer

Returned the final assessment.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": "{\n  \"score\": 0.76,\n  \"summary\": \"The paper proposes CodeAct, a general agent-action framework in which LLMs issue executable Python code and receive execution results as observations, and contributes a 7,139-trajectory instruction dataset plus fine-tuned open models. Its controlled comparisons and agent evaluations offer meaningful evidence that code actions can improve success and reduce interaction turns on complex tool-use tasks, while also exposing considerable variation across backbones and a narrow evaluation scope.\",\n  \"observations\": [\n    {\n      \"kind\": \"strength\",\n      \"claim\": \"The multi-tool benchmark provides a direct comparison across action formats, with CodeAct leading on success rate and average turns for most tested models; for GPT-4-1106-preview, the reported success gain over the next-best format is substantial.\",\n      \"page\": 5,\n      \"quote\": \"achieves a 20.7% absolute improvement compared to the next best action format (text) while requiring2.1 fewer interaction turns on average.\"\n    },\n    {\n      \"kind\": \"strength\",\n      \"claim\": \"The paper contributes both a multi-domain interaction dataset and an open-model evaluation, including out-of-domain tasks and general-capability measures. The results are not uniformly positive, which the authors acknowledge rather than masking.\",\n      \"page\": 9,\n      \"quote\": \"Surprisingly, no improvement is observed for the Llama-2 variant.\"\n    },\n    {\n      \"kind\": \"limitation\",\n      \"claim\": \"The key complex-task benchmark is small and manually curated, and its reported success rates vary sharply by model family. This limits how broadly the headline advantage can be generalized from the presented evidence.\",\n      \"page\": 5,\n      \"quote\": \"It contains 82 human-curated instances\"\n    },\n    {\n      \"kind\": \"uncertainty\",\n      \"claim\": \"The study evaluates executable code in an interactive Python setting but does not establish deployment safety or robustness beyond that setup; the authors themselves identify sandbox escape as a concern. I inspected the supplied main text, tables, and appendices, but did not inspect external code or supplementary artifacts.\",\n      \"page\": 10,\n      \"quote\": \"in the worst scenario (e.g., in Sci-Fi movies), such an agent may potentially break free of the sandbox restriction\"\n    }\n  ],\n  \"unresolved_questions\": [\n    \"How stable are the M3ToolEval results across repeated runs, alternative task samples, and different tool environments?\",\n    \"Which execution restrictions and monitoring mechanisms are necessary to safely grant agents access to general-purpose Python packages and code execution?\",\n    \"How much of CodeActAgent’s improvement is attributable to CodeActInstruct versus the larger general-conversation mixture and other training choices?\"\n  ]\n}",
  "observation": {}
}
```

</details>
