# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**baseline · ok**

1 model calls · 0 reads · 8.37 s · $0.004664

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.74

This paper introduces SWE-bench, a large-scale benchmark of 2,294 real GitHub issues paired with repository snapshots and test-based evaluation, and reports baseline results for proprietary models and fine-tuned SWE-Llama. Its main contribution is a realistic, executable evaluation setting for repository-level code editing; the evidence convincingly shows that the evaluated systems perform poorly under the study’s retrieval and prompting setups, while also exposing important evaluation and scope limitations.

- **strength**: The benchmark construction combines real issue/PR data with execution-based filters, including a fail-to-pass test criterion, giving tasks a concrete and reproducible success condition.
  - Page 2 · citation: not_found
  - Quote: "We filter out instances without at least one test where its status changes from a fail to pass"

- **strength**: The evaluation provides a useful baseline comparison and an informative retrieval-context analysis; the large gap between oracle and BM25 results illustrates how context selection affects measured performance.
  - Page 5 · citation: not_found
  - Quote: "Claude 2 only achieves a mere 4.8% pass rate using the “oracle” retrieval context."

- **limitation**: The reported baseline results are tied to constrained inference choices, including one greedy generation per task, and the paper itself frames its experiments as simple baselines rather than an exhaustive assessment of methods.
  - Page 24 · citation: exact
  - Quote: "we only generate a single patch file per instance."

- **limitation**: Passing the benchmark’s execution-based checks does not establish that generated changes are dependable or maintainable; the authors explicitly note this limitation of the evaluation criterion.
  - Page 9 · citation: whitespace
  - Quote: "relying solely on this method is insufficient to guarantee reliable performance of model generations"

Unresolved questions:

- How well do the benchmark’s test-derived success criteria track human judgments of correctness, maintainability, and whether an issue is fully resolved?
- How would results change under stronger interactive agents, iterative test-driven repair, or multiple samples per task, rather than the reported single-generation greedy setup?
- How representative are the selected, test-contributing issues of the broader range of software engineering work, especially beyond Python and the 12 selected repositories?
- I inspected the supplied paper pages, including the main evaluation and selected appendix details, but did not independently verify the released data, code, or experimental runs.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The construction filters require at least one test to change from fail to pass, and Appendix A.3 details how execution logs are compared (PDF pp. 2, 18–19). This supports the claim that tasks have a concrete, execution-based success condition; the paper also describes the task data and collection pipeline in enough detail to support the reproducibility qualification.
- Observation 2: **supported** — The paper compares BM25 and oracle retrieval and reports Claude 2 at 1.96% versus 4.8% resolved, explicitly discussing the importance of context selection (PDF pp. 5–6). That supports the retrieval-context analysis and the stated performance gap.
- Observation 3: **supported** — Appendix D.2 states that the authors generate a single patch per instance and use greedy decoding; the discussion says the experiments establish simple baselines and encourages other methods (PDF pp. 9, 24). The observation accurately characterizes the reported setup and the paper’s stated scope.
- Observation 4: **supported** — The paper explicitly cautions that execution-based testing alone does not guarantee reliable performance and notes that generated code may be less comprehensive, efficient, or readable than human-written solutions (PDF p. 9). This supports the limitation as stated.

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: final_answer

Returned the final assessment.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": "{\n  \"score\": 0.74,\n  \"summary\": \"This paper introduces SWE-bench, a large-scale benchmark of 2,294 real GitHub issues paired with repository snapshots and test-based evaluation, and reports baseline results for proprietary models and fine-tuned SWE-Llama. Its main contribution is a realistic, executable evaluation setting for repository-level code editing; the evidence convincingly shows that the evaluated systems perform poorly under the study’s retrieval and prompting setups, while also exposing important evaluation and scope limitations.\",\n  \"observations\": [\n    {\n      \"kind\": \"strength\",\n      \"claim\": \"The benchmark construction combines real issue/PR data with execution-based filters, including a fail-to-pass test criterion, giving tasks a concrete and reproducible success condition.\",\n      \"page\": 2,\n      \"quote\": \"We filter out instances without at least one test where its status changes from a fail to pass\"\n    },\n    {\n      \"kind\": \"strength\",\n      \"claim\": \"The evaluation provides a useful baseline comparison and an informative retrieval-context analysis; the large gap between oracle and BM25 results illustrates how context selection affects measured performance.\",\n      \"page\": 5,\n      \"quote\": \"Claude 2 only achieves a mere 4.8% pass rate using the “oracle” retrieval context.\"\n    },\n    {\n      \"kind\": \"limitation\",\n      \"claim\": \"The reported baseline results are tied to constrained inference choices, including one greedy generation per task, and the paper itself frames its experiments as simple baselines rather than an exhaustive assessment of methods.\",\n      \"page\": 24,\n      \"quote\": \"we only generate a single patch file per instance.\"\n    },\n    {\n      \"kind\": \"limitation\",\n      \"claim\": \"Passing the benchmark’s execution-based checks does not establish that generated changes are dependable or maintainable; the authors explicitly note this limitation of the evaluation criterion.\",\n      \"page\": 9,\n      \"quote\": \"relying solely on this method is insufficient to guarantee reliable performance of model generations\"\n    }\n  ],\n  \"unresolved_questions\": [\n    \"How well do the benchmark’s test-derived success criteria track human judgments of correctness, maintainability, and whether an issue is fully resolved?\",\n    \"How would results change under stronger interactive agents, iterative test-driven repair, or multiple samples per task, rather than the reported single-generation greedy setup?\",\n    \"How representative are the selected, test-contributing issues of the broader range of software engineering work, especially beyond Python and the 12 selected repositories?\",\n    \"I inspected the supplied paper pages, including the main evaluation and selected appendix details, but did not independently verify the released data, code, or experimental runs.\"\n  ]\n}",
  "observation": {}
}
```

</details>
