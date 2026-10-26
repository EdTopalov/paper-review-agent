# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**agent · ok**

5 model calls · 4 reads · 11.22 s · $0.001393

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.78

SWE-bench introduces a substantial, realistic benchmark for repository-level software issue resolution, pairing real GitHub issues and codebase snapshots with execution-based tests. The careful filtering pipeline and challenging baseline evaluations make it a useful research contribution, though the evaluation is limited in scope and passing tests does not establish patch quality.

- **strength**: The benchmark operationalizes real-world repository-level issue resolution at useful scale, with filtering that checks issue-linked PRs and test behavior.
  - Page 2 · citation: no strict match
  - Quote: "Through these stages of filtering, the original 90,000 PRs are filtered down to the 2,294 task instances"

- **strength**: Results substantiate substantial difficulty for the tested models, including an oracle-context setting that offers relevant-file information.
  - Page 6 · citation: no strict match
  - Quote: "the best performing model, Claude 2, only achieves a mere 4.8% pass rate using the “oracle” retrieval context."

- **limitation**: The authors explicitly scope the data to Python and caution that execution-based testing alone cannot ensure solution quality.
  - Page 9 · citation: strict match
  - Quote: "relying solely on this method is insufficient to guarantee reliable performance of model generations"

- **uncertainty**: The paper reports baseline results across several models and retrieval conditions, but I did not inspect the full prompting and implementation appendices; the inspected pages do not settle how sensitive outcomes are to those choices.
  - Page 5 · citation: strict match
  - Quote: "there are only a few models that are currently suitable for SWE-bench"

Unresolved questions:

- How robust are task selection and measured resolution rates to the benchmark’s filtering and test-selection choices?
- How would strong tool-using agents and newer models perform under comparable, fully specified evaluation conditions?
- How often do test-passing generated patches meet human standards for correctness, maintainability, and completeness?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes 2,294 tasks drawn from real GitHub issues and merged PRs, filtered for issue resolution, test changes, and fail-to-pass test behavior (pp. 1–3, 15, 18–19). That supports the claim of realistic, useful-scale benchmark construction.
- Observation 2: **supported** — The paper reports low resolution rates, including Claude 2’s 4.8% with oracle retrieval (pp. 5–6). Oracle retrieval provides files edited by the reference patch, while the authors note it is less realistic and may omit needed context (p. 4).
- Observation 3: **supported** — The authors state that all benchmark instances are Python and that execution-based testing alone cannot guarantee reliable performance or capture qualities such as comprehensiveness, efficiency, and readability (p. 9).
- Observation 4: **supported** — This is carefully framed as an uncertainty about the inspected pages, not a claim that the paper lacks details. The paper supplies additional prompting and inference information in the appendices, including a prompt template and greedy-decoding setup (pp. 24–25); it also says prompt variations generally did not substantially affect performance, with stated exceptions (p. 25).

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: search_paper

Locate benchmark construction and quantitative evaluation details.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "evaluation setup results SWE-bench Lite",
    "reason": "Locate benchmark construction and quantitative evaluation details."
  },
  "observation": {
    "matches": [],
    "limit_reached": false
  }
}
```

</details>

### Step 2: read_pages

Inspect benchmark construction methodology and dataset filtering details.

[Event 10](trace.jsonl#L10)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 2,
    "end": 3,
    "reason": "Inspect benchmark construction methodology and dataset filtering details."
  },
  "observation": {
    "start": 2,
    "end": 3,
    "text": "=== PDF PAGE 2 ===\nIn the real world, software engineering is not as simple. Fixing a bug might involve navigating a\nlarge repository, understanding the interplay between functions in different files, or spotting a small\nerror in convoluted code. Inspired by this, we introduce SWE-bench, a benchmark that evaluates\nLMs in a realistic software engineering setting. As shown in Figure 1, models are tasked to resolve\nissues (typically a bug report or a feature request) submitted to popular GitHub repositories. Each\ntask requires generating a patch describing changes to apply to the existing codebas … [preview; full text in trace]",
    "truncated": false
  }
}
```

</details>

### Step 3: read_pages

Check model evaluation tables and supporting results.

[Event 15](trace.jsonl#L15)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 5,
    "end": 6,
    "reason": "Check model evaluation tables and supporting results."
  },
  "observation": {
    "start": 5,
    "end": 6,
    "text": "=== PDF PAGE 5 ===\nWe compare the BM25 retrieval results against the “oracle” retrieval setting in Table 3, where we see\nthat BM25 retrieves a superset of the oracle files in about 40% of instances with the 27,000 token\ncontext limit but only also excludes all of the oracle files in over half of instances.\n4.2 I NPUT FORMAT\nOnce the retrieved files are selected using one of the two methods above, we construct the input\nto the model consisting of task instructions, the issue text, retrieved files and documentation, and\nfinally an example patch file and prompt for generating the patch file. Exam … [preview; full text in trace]",
    "truncated": false
  }
}
```

</details>

### Step 4: read_pages

Inspect authors' stated limitations, threats, and benchmark caveats.

[Event 20](trace.jsonl#L20)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 9,
    "end": 10,
    "reason": "Inspect authors' stated limitations, threats, and benchmark caveats."
  },
  "observation": {
    "start": 9,
    "end": 10,
    "text": "=== PDF PAGE 9 ===\none or a few skills, resulting in challenges that are typically too simple, pigeonhole the model into a\nreduced role, and do not provide models with the bandwidth to exercise their versatility or potentially\ndemonstrate new abilities (Srivastava et al., 2023). Consequently, a model’s performance on such\ntask conglomerations may not yield actionable, deep insights regarding its capabilities and how to\nimprove them (Schlangen, 2019; Mart ´ınez-Plumed et al., 2021; Bowman & Dahl, 2021). SWE-\nbench addresses these shortcomings, as our work demonstrates that it is significantly c … [preview; full text in trace]",
    "truncated": false
  }
}
```

</details>

### Step 5: submit_review · accepted

Evidence covers benchmark design, quantitative baseline results, and discussion limitations; submit a balanced assessment while noting uninspected methodological appendices.

[Event 25](trace.jsonl#L25)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Evidence covers benchmark design, quantitative baseline results, and discussion limitations; submit a balanced assessment while noting uninspected methodological appendices.",
    "review": {
      "score": 0.78,
      "summary": "SWE-bench introduces a substantial, realistic benchmark for repository-level software issue resolution, pairing real GitHub issues and codebase snapshots with execution-based tests. The careful filtering pipeline and challenging baseline evaluations make it a useful research contribution, though the evaluation is limited in scope and passing tests does not establish patch quality.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The benchmark operationalizes real-world repository-level issue resolution at useful scale, with filtering that checks issue-linked PRs and test behavior.",
          "page": 2,
          "quote": "Through these stages of filtering, the original 90,000 PRs are filtered down to the 2,294 task instances"
        },
        {
          "kind": "strength",
          "claim": "Results substantiate substantial difficulty for the tested models, including an oracle-context setting that offers relevant-file information.",
          "page": 6,
          "quote": "the best performing model, Claude 2, only achieves a mere 4.8% pass rate using the “oracle” retrieval context."
        },
        {
          "kind": "limitation",
          "claim": "The authors explicitly scope the data to Python and caution that execution-based testing alone cannot ensure solution quality.",
          "page": 9,
          "quote": "relying solely on this method is insufficient to guarantee reliable performance of model generations"
        },
        {
          "kind": "uncertainty",
          "claim": "The paper reports baseline results across several models and retrieval conditions, but I did not inspect the full prompting and implementation appendices; the inspected pages do not settle how sensitive outcomes are to those choices.",
          "page": 5,
          "quote": "there are only a few models that are currently suitable for SWE-bench"
        }
      ],
      "unresolved_questions": [
        "How robust are task selection and measured resolution rates to the benchmark’s filtering and test-selection choices?",
        "How would strong tool-using agents and newer models perform under comparable, fully specified evaluation conditions?",
        "How often do test-passing generated patches meet human standards for correctness, maintainability, and completeness?"
      ]
    }
  },
  "observation": {
    "accepted": true
  }
}
```

</details>
