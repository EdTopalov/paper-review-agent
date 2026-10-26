# T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering

**agent · ok**

5 model calls · 3 reads · 15.35 s · $0.002299

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.69

AlphaCodium presents a practical, test-driven multi-stage inference workflow for code generation: it builds problem reasoning and candidate tests, then iteratively runs and fixes code against public and generated tests. Reported gains across several models on CodeContests are substantial, though the evaluation is narrow and comparisons with prior systems are not fully controlled.

- **strength**: The central workflow makes concrete use of executable feedback and generated tests, rather than relying only on a direct prompt; this is a useful and clearly described inference-time contribution.
  - Page 3 · citation: whitespace
  - Quote: "repeatedly run and fix the generated code against input-output tests"

- **strength**: The paper reports consistent gains on both validation and test splits across the listed models, including a large GPT-4 validation-set increase.
  - Page 7 · citation: whitespace
  - Quote: "For GPT-4 on the validation set, for example, the pass@5 score improves from 19% to 44% - x2.3 improvement."

- **limitation**: The direct evaluation is on a small set of CodeContests problems, limiting confidence in generalization beyond this benchmark.
  - Page 3 · citation: whitespace
  - Quote: "which contain 107 and 165 problems, respectively."

- **uncertainty**: The reported comparisons to prior work have reproducibility and protocol-matching caveats acknowledged by the paper; these make the headline cross-system superiority less secure than the within-paper direct-prompt comparisons.
  - Page 7 · citation: exact
  - Quote: "There are subtleties when evaluating results."

Unresolved questions:

- How much of the improvement comes from individual components (generated tests, reflection, staged prompting, and iterative repair), versus their combination?
- How robust are the gains on benchmarks outside CodeContests and on additional model families?
- I inspected pages 1 and 3–8; detailed implementation/evaluation settings and appendices on failed methods were not fully examined, so some protocol and ablation details remain uncertain.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes a multi-stage flow that repeatedly runs and fixes code against public and AI-generated tests, with problem reflection and test generation as part of preprocessing (PDF pp. 1, 3–4).
- Observation 2: **supported** — Table 1 reports gains on both validation and test splits for DeepSeek-33B, GPT-3.5, and GPT-4; it also gives GPT-4 validation pass@5 as 19% versus 44% (PDF p. 7).
- Observation 3: **supported** — The evaluation uses 107 validation problems and 165 test problems, and the paper’s reported experiments are on CodeContests. The stated concern about confidence in generalization beyond this benchmark is a reasonable limitation (PDF p. 3).
- Observation 4: **supported** — The paper notes that prior systems did not release reproducible end-to-end solutions and identifies evaluation subtleties, including multiple solutions, tolerances, and timeouts. These caveats support qualifying cross-system comparisons, while the paper still reports superiority (PDF p. 7).

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: search_paper

Locate reported performance and evaluation details for the paper’s central result.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "44%",
    "reason": "Locate reported performance and evaluation details for the paper’s central result."
  },
  "observation": {
    "matches": [
      {
        "page": 1,
        "snippet": "ow con- sistently and significantly improves results. On the valida- tion set, for example, GPT-4 accuracy (pass@5) increased from 19% with a single well-designed direct prompt to 44% with the AlphaCodium flow. Many of the principles and best practices acquired in this work, we believe, are broadly ap- plicable to general code generation tasks. Full implementation is available at: https : / / github.com/Codium-ai/AlphaCodium 1. Introduction With a sparse reward signal, code generation tasks re- quire searching in the huge structured space of possible pro- grams. Correct soluti"
      },
      {
        "page": 2,
        "snippet": "his is true both for open-source models (DeepSeek [3]) and closed-source models (GPT [5]). For GPT-4 on the validation set, for example, the pass@5 ac- curacy improved from 19% to 44%. AlphaCodium also outperforms previous works, while having a significantly smaller computational budget - it achieves superior results over AlphaCode, for example, with four orders of magni- tude fewer LLM calls. We believe many of the principles and best practices used in this work broadly apply to general code generation tasks. In addition, we argue that utilizing harder and more 2"
      },
      {
        "page": 7,
        "snippet": "0% test Direct prompt 12% AlphaCodium 24% GPT-3.5 validation Direct prompt 15% AlphaCodium 25% test Direct prompt 8% AlphaCodium 17% GPT-4 validation Direct prompt 19% AlphaCodium 44% test Direct prompt 12% AlphaCodium 29% Table 1: Comparison of AlphaCodium flow results to di- rect prompt on various models. problem. As can be seen, AlphaCodium flow consistently and significantly improves the performance of LLMs on CodeContests problems. This is true both for open-source (DeepSeek) and close-source (GPT) models, and for both the validation and test sets. For GPT-4 on the valida"
      },
      {
        "page": 7,
        "snippet": "pen-source (DeepSeek) and close-source (GPT) models, and for both the validation and test sets. For GPT-4 on the validation set, for example, the pass@5 score improves from 19% to 44% - x2.3 improvement. 5.2. Comparison to previous works In Table 2 we compare AlphaCodium results to other methods from the literature. As can be seen, when com- paring AlphaCodium to CodeChain with the same model (GPT-3.5) and the same metric (pass@5), AlphaCodium consistently does better. When comparing AlphaCodium to AlphaCode work, we need to take into account that AlphaCode uses a different ge"
      },
      {
        "page": 7,
        "snippet": "odel set method score GPT-3.5 validation AlphaCodium (pass@5) 25% CodeChain (pass@5) 17% test AlphaCodium (pass@5) 17% CodeChain (pass@5) 14% GPT-4 validation AlphaCodium (pass@5) 44% AlphaCode AlphaCode (pass@10@1K) 17% AlphaCode (pass@10@100K) 24% GPT-4 test AlphaCodium (pass@5) 29% AlphaCode AlphaCode (pass@10@1K) 16% AlphaCode (pass@10@100K) 28% Table 2: Comparison of AlphaCodium to other works from the literature. ample - how to treat problems with multiple solutions, how to address tolerance issues, timeouts, and more. We com- pare to the numbers reported in the papers, "
      }
    ],
    "limit_reached": false
  }
}
```

</details>

### Step 2: read_pages

Inspect experimental setup, comparative results, and caveats to evaluate evidence.

[Event 10](trace.jsonl#L10)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 6,
    "end": 8,
    "reason": "Inspect experimental setup, comparative results, and caveats to evaluate evidence."
  },
  "observation": {
    "pages": [
      {
        "page": 6,
        "text": "...\nYour goal is to present possible solutions to the problem.\nMake sure that each solution fully addresses the problem goals, rules, and\nconstraints.\nThe output must be a YAML object equivalent to type $PossibleSolutions, according to\nthe following Pydantic definitions:\nclass Solution (BaseModel):\nname: str = Field(description=\"The name of the solution\")\ncontent: str = Field(description=\"A description of the solution\")\nwhy_it_works: str = Field(description=\"Why this solution is correct. Be specific \\\nand detailed regarding the problem rules and goals\")\ncomplexity: str = Field(description=\"The … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 7,
        "text": "model set method score\n(pass@5)\nDeepSeek\n-33B [3]\nvalidation Direct 7%\nAlphaCodium 20%\ntest Direct prompt 12%\nAlphaCodium 24%\nGPT-3.5\nvalidation Direct prompt 15%\nAlphaCodium 25%\ntest Direct prompt 8%\nAlphaCodium 17%\nGPT-4\nvalidation Direct prompt 19%\nAlphaCodium 44%\ntest Direct prompt 12%\nAlphaCodium 29%\nTable 1: Comparison of AlphaCodium flow results to di-\nrect prompt on various models.\nproblem. As can be seen, AlphaCodium flow consistently\nand significantly improves the performance of LLMs on\nCodeContests problems. This is true both for open-source\n(DeepSeek) and close-source (GPT) models, … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 8,
        "text": "dated variant that they did not release to the public. Accord-\ning to AlphaCode2 report: “AlphaCode2 requires about 100\nsamples to reach the level of performance of AlphaCode\nwith a million samples, making it over 10000× more sam-\nple efficient.” Hence both AlphaCode2 and AlphaCodium\nare four orders of magnitude more efficient than Alpha-\nCode, LLMs call-wise. But, AlphaCode2 utilized a modern\nfoundation model (Gemini-Pro) that was heavily fine-tuned\nspecifically for CodeContests competition, while Alpha-\nCodium uses general-purpose models as-is, and improves\ntheir performances without extra d … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 3: read_pages

Inspect method design and evaluation protocol for evidence on contribution and reproducibility.

[Event 15](trace.jsonl#L15)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 3,
    "end": 5,
    "reason": "Inspect method design and evaluation protocol for evidence on contribution and reproducibility."
  },
  "observation": {
    "pages": [
      {
        "page": 3,
        "text": "complicated benchmarks like CodeContests dataset will al-\nlow the community to better evaluate LLMs, compared to\nmore simplistic benchmarks, which are common today, like\nHumanEval [2].\n2. CodeContests Dataset\nCodeContests [8] is a challenging code generation\ndataset introduced by Google’s DeepMind, involving prob-\nlems curated from competitive programming platforms such\nas Codeforces [9]. The dataset contains 10K code problems\nthat can be used to train LLMs, as well as a validation and\ntest set to assess the ability of LLMs to solve challenging\ncode problems.\nIn this work, instead of training  … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 4,
        "text": "Mr. Chanek's city can be represented as a plane. He wants to build a\nhousing complex in the city. There are some telephone poles on the\nplane, which is represented by a grid a of size (n + 1) × (m + 1). There is a\ntelephone pole at (x, y) if a_{x, y} = 1.For each point (x, y), define S(x, y)\nas the square of the Euclidean distance between the nearest pole and (x,\ny). Formally, the square of the Euclidean distance between two points\n(x_1, y_1) and (x_2, y_2) is (x_2 - x_1)^2 + (y_2 - y_1)^2. To optimize the\nbuilding plan, the project supervisor asks you the sum of all S(x, y) for\neach 0 ≤ x ≤ n … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 5,
        "text": "3.3. Additional insights\nIn this section, we will offer additional insights and share\nintuitions about the proposed flow.\nFirstly, the flow relies on knowledge accumulation - try-\ning to progress from easy to hard, gaining knowledge and\ninsight along the way to help with the more difficult stages.\nFor example, the output of the first step,problem reflection,\ncan be utilized as prompt input to more difficult steps like\ngenerate possible solutions . The pre-processing phase’s\noutputs are used to aid the most challenging and critical\nphase, code iterations, where we try to generate code that\ncorr … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 4: submit_review · citation_validation_failed

Evidence covers the proposed flow, benchmark size, reported comparisons, and reproducibility caveat; submit a bounded assessment.

[Event 20](trace.jsonl#L20)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Evidence covers the proposed flow, benchmark size, reported comparisons, and reproducibility caveat; submit a bounded assessment.",
    "review": {
      "score": 0.69,
      "summary": "AlphaCodium presents a practical, test-driven multi-stage inference workflow for code generation: it builds problem reasoning and candidate tests, then iteratively runs and fixes code against public and generated tests. Reported gains across several models on CodeContests are substantial, though the evaluation is narrow and comparisons with prior systems are not fully controlled.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The central workflow makes concrete use of executable feedback and generated tests, rather than relying only on a direct prompt; this is a useful and clearly described inference-time contribution.",
          "page": 3,
          "quote": "repeatedly run and fix the generated code against input-output tests"
        },
        {
          "kind": "strength",
          "claim": "The paper reports consistent gains on both validation and test splits across the listed models, including a large GPT-4 validation-set increase.",
          "page": 7,
          "quote": "For GPT-4 on the validation set, for example, the pass@5 score improves from 19% to 44% - x2.3 improvement."
        },
        {
          "kind": "limitation",
          "claim": "The direct evaluation is on a small set of CodeContests problems, limiting confidence in generalization beyond this benchmark.",
          "page": 3,
          "quote": "the validation and test sets, which contain 107 and 165 problems, respectively."
        },
        {
          "kind": "uncertainty",
          "claim": "The reported comparisons to prior work have reproducibility and protocol-matching caveats acknowledged by the paper; these make the headline cross-system superiority less secure than the within-paper direct-prompt comparisons.",
          "page": 7,
          "quote": "There are subtleties when evaluating results."
        }
      ],
      "unresolved_questions": [
        "How much of the improvement comes from individual components (generated tests, reflection, staged prompting, and iterative repair), versus their combination?",
        "How robust are the gains on benchmarks outside CodeContests and on additional model families?",
        "I inspected pages 1 and 3–8; detailed implementation/evaluation settings and appendices on failed methods were not fully examined, so some protocol and ablation details remain uncertain."
      ]
    }
  },
  "observation": {
    "error": "citation_validation_failed",
    "citation_checks": [
      {
        "checker_version": "m2-citations-v2",
        "page_valid": true,
        "quote_nonempty": true,
        "quote_matches": true,
        "citation_verified": true,
        "matching_pages": [
          3
        ],
        "candidate_pages": [],
        "status": "whitespace",
        "observed": true
      },
      {
        "checker_version": "m2-citations-v2",
        "page_valid": true,
        "quote_nonempty": true,
        "quote_matches": true,
        "citation_verified": true,
        "matching_pages": [
          7
        ],
        "candidate_pages": [],
        "status": "whitespace",
        "observed": true
      },
      {
        "checker_version": "m2-citations-v2",
        "page_valid": true,
        "quote_nonempty": true,
        "quote_matches": false,
        "citation_verified": false,
        "matching_pages": [],
        "candidate_pages": [],
        "status": "not_found",
        "observed": false
      },
      {
        "checker_version": "m2-citations-v2",
        "page_valid": true,
        "quote_nonempty": true,
        "quote_matches": true,
        "citation_verified": true,
        "matching_pages": [
          7
        ],
        "candidate_pages": [],
        "status": "exact",
        "observed": true
      }
    ],
    "hint": "Copy exact quotes from observed pages, or read matching pages before resubmitting. Preserve case, mathematical notation, and ambiguous hyphens."
  }
}
```

</details>

### Step 5: submit_review · accepted

Correct the unsupported limitation quote with exact text observed on page 3 and resubmit the assessment.

[Event 25](trace.jsonl#L25)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Correct the unsupported limitation quote with exact text observed on page 3 and resubmit the assessment.",
    "review": {
      "score": 0.69,
      "summary": "AlphaCodium presents a practical, test-driven multi-stage inference workflow for code generation: it builds problem reasoning and candidate tests, then iteratively runs and fixes code against public and generated tests. Reported gains across several models on CodeContests are substantial, though the evaluation is narrow and comparisons with prior systems are not fully controlled.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The central workflow makes concrete use of executable feedback and generated tests, rather than relying only on a direct prompt; this is a useful and clearly described inference-time contribution.",
          "page": 3,
          "quote": "repeatedly run and fix the generated code against input-output tests"
        },
        {
          "kind": "strength",
          "claim": "The paper reports consistent gains on both validation and test splits across the listed models, including a large GPT-4 validation-set increase.",
          "page": 7,
          "quote": "For GPT-4 on the validation set, for example, the pass@5 score improves from 19% to 44% - x2.3 improvement."
        },
        {
          "kind": "limitation",
          "claim": "The direct evaluation is on a small set of CodeContests problems, limiting confidence in generalization beyond this benchmark.",
          "page": 3,
          "quote": "which contain 107 and 165 problems, respectively."
        },
        {
          "kind": "uncertainty",
          "claim": "The reported comparisons to prior work have reproducibility and protocol-matching caveats acknowledged by the paper; these make the headline cross-system superiority less secure than the within-paper direct-prompt comparisons.",
          "page": 7,
          "quote": "There are subtleties when evaluating results."
        }
      ],
      "unresolved_questions": [
        "How much of the improvement comes from individual components (generated tests, reflection, staged prompting, and iterative repair), versus their combination?",
        "How robust are the gains on benchmarks outside CodeContests and on additional model families?",
        "I inspected pages 1 and 3–8; detailed implementation/evaluation settings and appendices on failed methods were not fully examined, so some protocol and ablation details remain uncertain."
      ]
    }
  },
  "observation": {
    "accepted": true,
    "citation_checks": [
      {
        "checker_version": "m2-citations-v2",
        "page_valid": true,
        "quote_nonempty": true,
        "quote_matches": true,
        "citation_verified": true,
        "matching_pages": [
          3
        ],
        "candidate_pages": [],
        "status": "whitespace",
        "observed": true
      },
      {
        "checker_version": "m2-citations-v2",
        "page_valid": true,
        "quote_nonempty": true,
        "quote_matches": true,
        "citation_verified": true,
        "matching_pages": [
          7
        ],
        "candidate_pages": [],
        "status": "whitespace",
        "observed": true
      },
      {
        "checker_version": "m2-citations-v2",
        "page_valid": true,
        "quote_nonempty": true,
        "quote_matches": true,
        "citation_verified": true,
        "matching_pages": [
          3
        ],
        "candidate_pages": [],
        "status": "whitespace",
        "observed": true
      },
      {
        "checker_version": "m2-citations-v2",
        "page_valid": true,
        "quote_nonempty": true,
        "quote_matches": true,
        "citation_verified": true,
        "matching_pages": [
          7
        ],
        "candidate_pages": [],
        "status": "exact",
        "observed": true
      }
    ]
  }
}
```

</details>
