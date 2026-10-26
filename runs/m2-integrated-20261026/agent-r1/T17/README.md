# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · error**

8 model calls · 4 reads · 25.93 s · $0.002977

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

Error: `{"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"}`

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: search_paper

Locate the paper’s evaluation findings to assess empirical support.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "experimental results",
    "reason": "Locate the paper’s evaluation findings to assess empirical support."
  },
  "observation": {
    "matches": [
      {
        "page": 5,
        "snippet": "papers, Wei et al. (2022b) and Zhang et al. (2022). Evaluation metrics wise, we follow Manual-CoT (Wei et al., 2022b) and report the ac- curacy of all methods across datasets. 4 Experimental Results 4.1 Main Results Arithmetic Reasoning. Table 2 reports the accu- racy comparison of our method and existing zero- shot and few-shot methods on the arithmetic rea- soning datasets. In the zero-shot setting, our PS+ prompting (i.e., PS prompting with more detailed instructions) consistently outperforms Zero-shot- CoT across all arithmetic reasoning datasets by a large margin. Speciﬁcally, PS+ prompti"
      }
    ],
    "limit_reached": false
  }
}
```

</details>

### Step 2: read_pages

Inspect method formulation and initial experimental comparisons.

[Event 10](trace.jsonl#L10)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 3,
    "end": 5,
    "reason": "Inspect method formulation and initial experimental comparisons."
  },
  "observation": {
    "pages": [
      {
        "page": 3,
        "text": "Figure 2: Example inputs and outputs of GPT-3 with (a) Zero-shot-CoT prompting, (b) Plan-and-Solve (PS)\nprompting, and (c) answer extraction prompting. While Zero-shot-CoT encourages LLMs to generate multi-step\nreasoning with “ Let’s think step by step ”, it may still generate wrong reasoning steps when the problem is com-\nplex. Unlike Zero-shot-CoT, PS prompting ﬁrst asks LLMs to devise a plan to solve the problem by generating a\nstep-by-step plan and carrying out the plan to ﬁnd the answer.\n• The templates should elicit LLMs to deter-\nmine subtasks and accomplish the subtasks.\n• The template … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 4,
        "text": "Figure 3: Example inputs and outputs of GPT-3 with (a) Plan-and-Solve (PS) Prompting and (b) Plan-and-Solve\nprompting with more detailed instructions (PS+ prompting). PS+ prompting greatly improves the quality of the\ngenerated reasoning process.\n2.2 Step 2: Prompting for Answer Extraction\nSimilar to Zero-shot-CoT, we devise another\nprompt in Step 2 to get the LLM to extract the\nﬁnal numerical answer from the reasoning text gen-\nerated in Step 1. This prompt includes the answer\nextraction instruction appended to ﬁrst prompt fol-\nlowed by the LLM generated reasoning text. This\nway, LLM is expect … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 5,
        "text": "Table 1: Details of datasets being evaluated. Math:\narithmetic reasoning. CS: commonsense reasoning.\nSym.: symbolic reasoning.\nDataset Domain # Samples Ave. words Answer\nMultiArith Math 600 31.8 Number\nAddSub Math 395 31.5 Number\nGSM8K Math 1319 46.9 Number\nAQUA Math 254 51.9 Option\nSingleEq Math 508 27.4 Number\nSV AMP Math 1000 31.8 Number\nCSQA CS 1221 27.8 Option\nStrategyQA CS 2290 9.6 Yes / No\nLast Letters Sym. 500 15.0 String\nCoin Flip Sym. 500 37.0 Yes / No\nstill heads up after it is ﬂipped or not ﬂipped based\non steps given in the questions. Table 1 shows\ndataset statistics.\n3.2 Zero-sho … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 3: read_pages

Check non-arithmetic results and reported study boundaries.

[Event 15](trace.jsonl#L15)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 6,
    "end": 7,
    "reason": "Check non-arithmetic results and reported study boundaries."
  },
  "observation": {
    "pages": [
      {
        "page": 6,
        "text": "Table 2: Accuracy comparison on six math reasoning datasets. The best and second best results are boldfaced and\nunderlined respectively. The best and second best results are boldfaced and underlined.\nSetting Method (GPT-3) MultiArith GSM8K AddSub AQuA SingleEq SV AMP Average\nZero-Shot\nCoT 83.8 56.4 85.3 38.9 88.1 69.9 70.4\nPoT 92.2 57.0 85.1 43.9 91.7 70.8 73.5\nPS (ours) 87.2 58.2 88.1 42.5 89.2 72.0 72.9\nPS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7\nFew-Shot Manual-CoT 93.6 58.4 91.6 48.4 93.5 80.3 77.6\nAuto-CoT 95.5 57.1 90.8 41.7 92.1 78.1 75.9\nTable 3: Accuracy on commonsense reasoning\ndat … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 7,
        "text": "Table 5: Performance comparison of trigger sentences measured on GSM8K and SV AMP datasets with\ntext-davinci-003 except for No. 2 ( code-davinci-002). (*1) means the trigger sentence used in\nZero-shot-CoT (Kojima et al., 2022). (*2) means the trigger sentence used in Zero-shot-PoT (Chen et al., 2022).\nNo. Trigger Setence GSM8K SV AMP\n1 Let’s think step by step. (*1) 56.4 69.9\n2\nimport math\nimport numpy as np\n# Question: example[’question’]\n# Answer this question by implementing a solver() function.\ndef solver():\n# Let’s write a Python program step by step, and then return the answer\n# Firstly, … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 4: read_pages

Inspect discussion and conclusions for stated scope or limitations.

[Event 20](trace.jsonl#L20)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 8,
    "end": 9,
    "reason": "Inspect discussion and conclusions for stated scope or limitations."
  },
  "observation": {
    "pages": [
      {
        "page": 8,
        "text": "CalculationStep Missing Semantic\nVariablesPlanSolution\n-0.41 -0.56 0.76\n-0.02 -0.83 0.7\n-0.42 0.076 0.24\n0.8\n0.6\n0.4\n0.2\n0.0\n0.2\n0.4\n0.6\nFigure 5: Correlation analysis of generated reasoning\nand error types of randomly sampled 100 data exam-\nples from GSM8K for Zero-shot-PS+.\n5 Related Work\n5.1 Reasoning in NLP\nIt is well known that complex reasoning prob-\nlems are challenging for NLP models, and such\nproblems include mathematical reasoning (Cobbe\net al., 2021; Patel et al., 2021; Ling et al., 2017;\nKoncel-Kedziorski et al., 2016) (requiring the abil-\nity to understand mathematical concepts, c … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 9,
        "text": "multiple arithmetic reasoning datasets. Overall, our\nresults suggest that (a) Zero-shot PS+ prompting\ncan generate high-quality reasoning process than\nZero-shot-CoT prompting, as the PS prompts pro-\nvide more detailed instructions guiding the LLMs\nto perform correct reasoning; (b) Zero-shot PS+\nprompting has the potential to outperform manual\nFew-shot CoT prompting, which hopefully will\nspark further development of new CoT prompting\napproaches to elicit reasoning in LLMs.\n7 Limitations\nThere are two limitations in this work. First, it takes\neffort to design the prompt to guide the LLMs gen-\ner … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 5: submit_review · citation_validation_failed

Evidence covers method, benchmark outcomes, error analysis, and the authors’ stated limitations.

[Event 25](trace.jsonl#L25)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Evidence covers method, benchmark outcomes, error analysis, and the authors’ stated limitations.",
    "review": {
      "score": 0.72,
      "summary": "The paper introduces Plan-and-Solve prompting, which explicitly asks an LLM to devise and execute a plan, with PS+ adding instructions about variables and calculations. On ten reasoning datasets, reported GPT-3 results generally improve over Zero-shot-CoT, and PS+ is competitive with few-shot CoT on arithmetic tasks. This is a useful, clearly scoped prompt-design contribution, though the evidence is centered on one model family and task benchmarks, and the authors acknowledge prompt sensitivity and persistent semantic errors.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The method is a simple, explicit zero-shot decomposition strategy, with PS+ extending it to encourage variable extraction and intermediate calculations.",
          "page": 3,
          "quote": "Our Zero-shot PS prompting method instead includes the instructions “ devise a plan ” and “ carry out the plan ”"
        },
        {
          "kind": "strength",
          "claim": "Reported gains span arithmetic, commonsense, and symbolic tasks, rather than relying on a single benchmark family.",
          "page": 6,
          "quote": "it consistently outperforms Zero-shot-CoT on CommonsenseQA (71.9% vs. 65.2%) and StrategyQA (65.4% vs. 63.8%) datasets."
        },
        {
          "kind": "limitation",
          "claim": "The authors state that prompts require careful design because GPT-3 is sensitive to wording; this is a practical constraint, not evidence the approach fails.",
          "page": 9,
          "quote": "The GPT-3 models are sensitive to the expressions in prompts, thus we need to carefully design the prompts."
        },
        {
          "kind": "limitation",
          "claim": "The approach does not resolve semantic misunderstanding, which the authors identify as remaining error type.",
          "page": 9,
          "quote": "the proposed plan-and-solve prompting can help address the calculation errors and missing-reasoning-step errors, but the semantic misunderstanding errors are still remain."
        }
      ],
      "unresolved_questions": [
        "How well does PS/PS+ transfer to model families beyond GPT-3 or to newer models?",
        "How robust are the results to alternate prompt formulations and evaluation settings?",
        "The inspected evidence is limited to selected method, results, and conclusion pages; detailed appendix results and full implementation details were not reviewed."
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
        "quote_matches": false,
        "citation_verified": true,
        "matching_pages": [
          6
        ],
        "candidate_pages": [],
        "status": "normalized",
        "observed": true
      },
      {
        "checker_version": "m2-citations-v2",
        "page_valid": true,
        "quote_nonempty": true,
        "quote_matches": true,
        "citation_verified": true,
        "matching_pages": [
          9
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
      }
    ],
    "hint": "Copy exact quotes from observed pages, or read matching pages before resubmitting. Preserve case, mathematical notation, and ambiguous hyphens."
  }
}
```

</details>

### Step 6: submit_review · citation_validation_failed

Correcting the citation that did not match the observed page text; retaining concise evidence-based assessment.

[Event 30](trace.jsonl#L30)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Correcting the citation that did not match the observed page text; retaining concise evidence-based assessment.",
    "review": {
      "score": 0.72,
      "summary": "The paper introduces Plan-and-Solve prompting, which asks an LLM to devise and execute a plan, with PS+ adding instructions about variables and calculations. On ten reasoning datasets, reported GPT-3 results generally improve over Zero-shot-CoT, and PS+ is competitive with few-shot CoT on arithmetic tasks. This is a useful, clearly scoped prompt-design contribution, though evidence is centered on one model family and task benchmarks; the authors acknowledge prompt sensitivity and persistent semantic errors.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The method is an explicit zero-shot decomposition strategy; PS+ expands the prompt with variable and calculation guidance.",
          "page": 3,
          "quote": "Our Zero-shot PS prompting method instead includes the instructions “ devise a plan ” and “ carry out the plan ”"
        },
        {
          "kind": "strength",
          "claim": "Reported results show improvements over Zero-shot-CoT on commonsense datasets.",
          "page": 6,
          "quote": "it consistently outperforms Zero-shot-CoT on CommonsenseQA (71.9% vs. 65.2%) and StrategyQA (65.4% vs. 63.8%) datasets."
        },
        {
          "kind": "limitation",
          "claim": "The authors describe prompt sensitivity as a practical constraint on designing the method.",
          "page": 9,
          "quote": "The GPT-3 models are sensitive to the expressions in prompts, thus we need to carefully design the prompts."
        },
        {
          "kind": "limitation",
          "claim": "The approach addresses some error types but leaves semantic misunderstanding errors unresolved.",
          "page": 9,
          "quote": "the proposed plan-and-solve prompting can help address the calculation errors and missing-reasoning- step errors, but the semantic misunderstanding errors are still remain."
        }
      ],
      "unresolved_questions": [
        "How well does PS/PS+ transfer to model families beyond GPT-3 or to newer models?",
        "How robust are results to alternate prompt formulations and evaluation settings?",
        "Inspection focused on method, selected results, and conclusion pages; detailed appendix results and full implementation details were not reviewed."
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
        "quote_matches": false,
        "citation_verified": true,
        "matching_pages": [
          6
        ],
        "candidate_pages": [],
        "status": "normalized",
        "observed": true
      },
      {
        "checker_version": "m2-citations-v2",
        "page_valid": true,
        "quote_nonempty": true,
        "quote_matches": true,
        "citation_verified": true,
        "matching_pages": [
          9
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
      }
    ],
    "hint": "Copy exact quotes from observed pages, or read matching pages before resubmitting. Preserve case, mathematical notation, and ambiguous hyphens."
  }
}
```

</details>

### Step 7: submit_review · citation_validation_failed

Submitting after correcting both quotes to exact observed page text.

[Event 35](trace.jsonl#L35)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Submitting after correcting both quotes to exact observed page text.",
    "review": {
      "score": 0.72,
      "summary": "The paper introduces Plan-and-Solve prompting, which asks an LLM to devise and execute a plan, with PS+ adding instructions about variables and calculations. On ten reasoning datasets, reported GPT-3 results generally improve over Zero-shot-CoT, and PS+ is competitive with few-shot CoT on arithmetic tasks. This is a useful, clearly scoped prompt-design contribution, though evidence is centered on one model family and task benchmarks; the authors acknowledge prompt sensitivity and persistent semantic errors.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The method is an explicit zero-shot decomposition strategy; PS+ expands the prompt with variable and calculation guidance.",
          "page": 3,
          "quote": "Our Zero-shot PS prompting method instead includes the instructions “ devise a plan ” and “ carry out the plan ”"
        },
        {
          "kind": "strength",
          "claim": "Reported results show improvements over Zero-shot-CoT on commonsense datasets.",
          "page": 6,
          "quote": "While PS+ prompting underperforms Few-Shot-CoT(Manual) on this problem, it consistently outperforms Zero-shot-CoT on CommonsenseQA (71.9% vs. 65.2%) and StrategyQA (65.4% vs. 63.8%) datasets."
        },
        {
          "kind": "limitation",
          "claim": "The authors describe prompt sensitivity as a practical constraint on designing the method.",
          "page": 9,
          "quote": "The GPT-3 models are sensitive to the expressions in prompts, thus we need to carefully design the prompts."
        },
        {
          "kind": "limitation",
          "claim": "The approach addresses some error types but leaves semantic misunderstanding errors unresolved.",
          "page": 9,
          "quote": "the proposed plan-and-solve prompting can help address the calculation errors and missing-reasoning-step errors, but the semantic misunderstanding errors are still remain."
        }
      ],
      "unresolved_questions": [
        "How well does PS/PS+ transfer to model families beyond GPT-3 or to newer models?",
        "How robust are results to alternate prompt formulations and evaluation settings?",
        "Inspection focused on method, selected results, and conclusion pages; detailed appendix results and full implementation details were not reviewed."
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
          9
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
      }
    ],
    "hint": "Copy exact quotes from observed pages, or read matching pages before resubmitting. Preserve case, mathematical notation, and ambiguous hyphens."
  }
}
```

</details>

### Step 8: submit_review · citation_validation_failed

Final attempt using only short exact excerpts copied verbatim from observed pages.

[Event 40](trace.jsonl#L40)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Final attempt using only short exact excerpts copied verbatim from observed pages.",
    "review": {
      "score": 0.72,
      "summary": "The paper proposes Plan-and-Solve prompting: ask an LLM to devise and carry out a plan, with PS+ adding calculation and variable-extraction guidance. Reported GPT-3 results across ten datasets generally improve over Zero-shot-CoT, including arithmetic, commonsense, and symbolic tasks. It is a useful prompt-design contribution with benchmark support, but its evidence is scoped to GPT-3 and the authors acknowledge prompt sensitivity and unresolved semantic errors.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The proposed prompt explicitly directs the model to plan and execute subtasks.",
          "page": 3,
          "quote": "“ devise a plan ” and “ carry out the plan ”"
        },
        {
          "kind": "strength",
          "claim": "The method is tested across multiple reasoning categories.",
          "page": 4,
          "quote": "The proposed method is evaluated on the ten benchmark datasets from three categories of reasoning problems:"
        },
        {
          "kind": "limitation",
          "claim": "The authors identify sensitivity to prompt wording as a design burden.",
          "page": 9,
          "quote": "The GPT-3 models are sensitive to the expressions in prompts"
        },
        {
          "kind": "limitation",
          "claim": "Semantic misunderstanding remains outside what the method resolves.",
          "page": 9,
          "quote": "the semantic misunderstanding errors are still remain."
        }
      ],
      "unresolved_questions": [
        "How well does the approach transfer beyond GPT-3?",
        "How robust are results to alternative prompt wording and evaluation settings?",
        "I inspected selected method, results, and conclusion pages, not the detailed appendix or full implementation details."
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
        "quote_matches": false,
        "citation_verified": false,
        "matching_pages": [],
        "candidate_pages": [
          4
        ],
        "status": "hyphenation_ambiguous",
        "observed": false
      },
      {
        "checker_version": "m2-citations-v2",
        "page_valid": true,
        "quote_nonempty": true,
        "quote_matches": true,
        "citation_verified": true,
        "matching_pages": [
          9
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
        "candidate_pages": [
          9
        ],
        "status": "hyphenation_ambiguous",
        "observed": false
      }
    ],
    "hint": "Copy exact quotes from observed pages, or read matching pages before resubmitting. Preserve case, mathematical notation, and ambiguous hyphens."
  }
}
```

</details>

- Event 43: **run_error** — {"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"}
