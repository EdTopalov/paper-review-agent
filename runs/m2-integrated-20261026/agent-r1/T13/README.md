# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**agent · ok**

5 model calls · 4 reads · 12.22 s · $0.001657

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.76

Self-RAG trains language models to decide when to retrieve, assess retrieved evidence and generated segments with reflection tokens, and use those signals for controllable decoding. Across six tasks, its reported results and ablations provide substantial evidence of gains over several retrieval and non-retrieval baselines, especially in factuality and citation measures, though evidence is scoped to particular models, datasets, and evaluation choices.

- **strength**: The framework integrates on-demand retrieval, tokenized critique, and customizable decoding, rather than treating retrieval as a fixed input step.
  - Page 2 · citation: whitespace
  - Quote: "our inference-time algorithm enables us to (1) flexibly adjust retrieval frequency for different downstream applications and (2) customize models’ behaviors to user preferences"

- **strength**: The reported results show competitive or leading performance across varied tasks, including large citation-precision and recall results on ASQA relative to listed retrieval baselines.
  - Page 8 · citation: exact
  - Quote: "Our SELF -RAG 13 B 55.8 69.3 74.5 73.1 80.2 31.7 37.0 71.6 70.3 71.3"

- **strength**: Ablations test multiple components and report deterioration when retrieval or critique is removed, or when only the top passage is used.
  - Page 9 · citation: whitespace
  - Quote: "Using the top passages regardless of their relevance (Retrieve top 1) as in conventional RAG approaches causes a large drop in PopQA and ASQA"

- **limitation**: The evaluation relies partly on previously reported results where implementations were unavailable, limiting direct comparability and independent verification within this study.
  - Page 7 · citation: exact
  - Quote: "We report numbers using the results reported in the paper as the implementations are not available."

Unresolved questions:

- How robust are the reported gains across additional model families, retrievers, and datasets beyond the evaluated setup?
- How do the reflection-token labels and critic supervision affect reliability when the proprietary-LM-generated supervision is imperfect?
- I inspected pages 1–3 and 7–9, not the remaining paper; training details, further analyses, and stated limitations elsewhere may qualify this assessment.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — Page 2 describes on-demand retrieval, reflection tokens for critique, and inference-time decoding that adjusts retrieval frequency and user-preference tradeoffs.
- Observation 2: **supported** — Page 8 reports results across six tasks and shows ASQA citation precision and recall of 70.3 and 71.3 for Self-RAG 13B. The text says these exceed all listed models except ChatGPT, and Self-RAG exceeds ChatGPT on citation precision.
- Observation 3: **supported** — Pages 9–10 describe training and inference ablations, including removing the retriever, critic, retrieval, or ISSUP, and using only the top passage. The paper reports performance drops for several of these comparisons, including top-1 retrieval on PopQA and ASQA.
- Observation 4: **supported** — Page 7 states that results for some baselines are taken from their papers because implementations were unavailable, supporting the qualified comparability and independent-verification limitation.

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: search_paper

Locate the evaluation setup to assess how the paper supports its claimed gains.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "Experimental Setup",
    "reason": "Locate the evaluation setup to assess how the paper supports its claimed gains."
  },
  "observation": {
    "matches": [],
    "limit_reached": false,
    "hint": "Literal phrase not found. Try one keyword or a shorter exact phrase, or read pages."
  }
}
```

</details>

### Step 2: search_paper

Find reported experiment results for evaluating the evidence behind the abstract's performance claims.

[Event 10](trace.jsonl#L10)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "Results",
    "reason": "Find reported experiment results for evaluating the evidence behind the abstract's performance claims."
  },
  "observation": {
    "matches": [
      {
        "page": 2,
        "snippet": "er preferences by leveraging reflection tokens through segment-level beam search using the weighted linear sum of the reflection token probabilities as segment score. Empirical results on six tasks, including reasoning and long-form generation, demonstrate that SELF - RAG significantly outperforms pre-trained and instruction-tuned LLMs that have more parameters and widely adopted RAG approaches with higher citation accuracy. In particular, SELF -RAG outperforms retrieval-augmented ChatGPT on four tasks, Llama2-chat (Touvron et al., 2023) and Alpaca (Dubois et al., 2023) on all tas"
      },
      {
        "page": 7,
        "snippet": "se the author-provided top 5 documents by GTR-XXL (Ni et al., 2022) across all baselines for a fair comparison. 5https://github.com/princeton-nlp/ALCE 6We report numbers using the results reported in the paper as the implementations are not available. 7"
      },
      {
        "page": 8,
        "snippet": "Preprint. Table 2: Overall experiment results on six tasks. Bold numbers indicate the best performance among non-proprietary models, and gray-colored bold text indicates the best proprietary model when they outperforms all non-proprietary models. ∗ indicates concurrent or recent results reported by concurrent work. – indicates numbers that are not reported by the original papers or are not applicable. Models are sorted based on scale. FS, em"
      },
      {
        "page": 8,
        "snippet": "ce among non-proprietary models, and gray-colored bold text indicates the best proprietary model when they outperforms all non-proprietary models. ∗ indicates concurrent or recent results reported by concurrent work. – indicates numbers that are not reported by the original papers or are not applicable. Models are sorted based on scale. FS, em, rg, mau, prec, rec denote FactScore (factuality); str-em, rouge (correctness); MAUVE (fluency); citation precision and recall, respectively. Short-form Closed-set Long-form generations (with citations) PopQA TQA Pub ARC Bio ASQA LM (acc) (a"
      },
      {
        "page": 8,
        "snippet": "6 2.0 3.8 Our SELF -RAG 7B 54.9 66.4 72.4 67.3 81.2 30.0 35.7 74.3 66.9 67.8 Our SELF -RAG 13 B 55.8 69.3 74.5 73.1 80.2 31.7 37.0 71.6 70.3 71.3 5 R ESULTS AND ANALYSIS 5.1 M AIN RESULTS Comparison against baselines without retrieval. Table 2 (top) presents the baselines without retrieval. Our SELF -RAG (bottom two rows) demonstrates a substantial performance advantage over supervised fine-tuned LLMs in all tasks and even outperforms ChatGPT in PubHealth, PopQA, biography generations, and ASQA (Rouge and MAUVE). Our approach also significantly outperforms a concurrent method that"
      },
      {
        "page": 9,
        "snippet": "pQA, PubHealth, and ASQA. On ASQA, we evaluate models on sampled 150 instances and exclude ablations involving adaptive or no retrieval processes. We show in Table 3a the ablation results. The top part of the table shows results for training ablations, and the bottom part is for inference ablations. We see that all components play important roles. We also observe a large performance gap between SELF -R AG and No Retriever or Critic baselines across tasks, indicating that training an LM with those models largely contributes to the performance gain of SELF -RAG. Using the top passag"
      },
      {
        "page": 9,
        "snippet": "luate models on sampled 150 instances and exclude ablations involving adaptive or no retrieval processes. We show in Table 3a the ablation results. The top part of the table shows results for training ablations, and the bottom part is for inference ablations. We see that all components play important roles. We also observe a large performance gap between SELF -R AG and No Retriever or Critic baselines across tasks, indicating that training an LM with those models largely contributes to the performance gain of SELF -RAG. Using the top passages regardless of their relevance (Retriev"
      },
      {
        "page": 9,
        "snippet": " the top passages regardless of their relevance (Retrieve top 1) as in conventional RAG approaches causes a large drop in PopQA and ASQA, and removing ISSUP during the beam search results hurts performance on ASQA. This demonstrates the effectiveness of SELF -RAG’s capabilities of carefully selecting generations based fine-grained multiple criterion, instead of naively using all of the top passages from the retrieval model or solely depending on relevance scores. Effects of inference-time customization. One key benefit of our proposed framework is that it enables us to control how"
      }
    ],
    "limit_reached": true
  }
}
```

</details>

### Step 3: read_pages

Inspect evaluation comparisons and ablation analysis to judge empirical support and caveats.

[Event 15](trace.jsonl#L15)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 7,
    "end": 9,
    "reason": "Inspect evaluation comparisons and ablation analysis to judge empirical support and caveats."
  },
  "observation": {
    "pages": [
      {
        "page": 7,
        "text": "Preprint.\nChallenge; Clark et al. 2018). We use accuracy as an evaluation metric and report on the test set. We\naggregate the answer probabilities of target classes for both of these datasets (Appendix Section B.2).\nShort-form generations tasks include two open-domain question answering (QA) datasets,\nPopQA (Mallen et al., 2023) and TriviaQA-unfiltered (Joshi et al., 2017), where systems need\nto answer arbitrary questions about factual knowledge. For PopQA, we use the long-tail subset,\nconsisting of 1,399 rare entity queries whose monthly Wikipedia page views are less than 100. As the\nTriviaQA … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 8,
        "text": "Preprint.\nTable 2: Overall experiment results on six tasks. Bold numbers indicate the best performance among\nnon-proprietary models, and gray-colored bold text indicates the best proprietary model when\nthey outperforms all non-proprietary models. ∗ indicates concurrent or recent results reported by\nconcurrent work. – indicates numbers that are not reported by the original papers or are not applicable.\nModels are sorted based on scale. FS, em, rg, mau, prec, rec denote FactScore (factuality); str-em,\nrouge (correctness); MAUVE (fluency); citation precision and recall, respectively.\nShort-form C … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 9,
        "text": "Preprint.\nPQA Med AS\n(acc) (acc) (em)\nSELF -RAG (50k) 45.5 73.5 32.1\nTraining\nNo Retriever R 43.6 67.8 31.0\nNo Critic C 42.6 72.0 18.1\nTest\nNo retrieval 24.7 73.0 –\nHard constraints 28.3 72.6 –\nRetrieve top1 41.8 73.1 28.6\nRemove ISSUP 44.1 73.2 30.6\n(a) Ablation\n1 2\n70.0\n70.5Precision\n1 2\nWeight for IsSupport\n90\n95Mauve\n (b) Customization\n0.0 0.2 0.4 0.6\n0.98\n0.99\n0.99\n1.00Accuracy\nPubHealth\n0.0 0.2 0.4 0.6\nRetrieval Threshold\n0.6\n0.8\n1.0Accuracy\nPopQA\n0.0\n0.5\n1.0\nFrequency\n0.25\n0.50\n0.75\n1.00\nFrequency\n (c) Retrieval\nFigure 3: Analysis on SELF -R AG: (a) Ablation studies for key components o … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 4: read_pages

Inspect the framework description and training signal to assess novelty and methodological substance.

[Event 20](trace.jsonl#L20)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 2,
    "end": 3,
    "reason": "Inspect the framework description and training signal to assess novelty and methodological substance."
  },
  "observation": {
    "pages": [
      {
        "page": 2,
        "text": "Preprint.\nStep 1: Retrieve K documents\nCalifornia was named after a ﬁctional \nisland in a Spanish book. \nPrompt How did US states get their names? \nUS states got their names from a variety of \nsources. Eleven states are named after an \nindividual person (e.g, California was named \nafter Christopher Columbus). Some states \nincluding Texas and Utah, are named after \nNative American tribe.\nRetrieval-Augmented Generation (RAG) Ours: Self-reﬂective Retrieval-Augmented Generation (Self-RAG) \nPopular names by states. In Texas, \nEmma is a popular baby name. \nOf the ﬁfty states, eleven are named \nafter … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 3,
        "text": "Preprint.\nof retrieved passages prepended to input, or pre-train a retriever and LM jointly, followed by few-\nshot fine-tuning on task datasets (Izacard et al., 2022b). While prior work often retrieves only\nonce at the beginning, Jiang et al. (2023) propose to adaptively retrieve passages for generation\non top of a proprietary LLM or Schick et al. (2023) train an LM to generate API calls for named\nentities. Yet, the improved task performance of such approaches often comes at the expense of\nruntime efficiency (Mallen et al., 2023), robustness to irrelevant context (Shi et al., 2023), and lack o … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 5: submit_review · accepted

Evidence covers method, benchmark setup, results, and ablations; submit a provisional assessment while noting inspection gaps.

[Event 25](trace.jsonl#L25)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Evidence covers method, benchmark setup, results, and ablations; submit a provisional assessment while noting inspection gaps.",
    "review": {
      "score": 0.76,
      "summary": "Self-RAG trains language models to decide when to retrieve, assess retrieved evidence and generated segments with reflection tokens, and use those signals for controllable decoding. Across six tasks, its reported results and ablations provide substantial evidence of gains over several retrieval and non-retrieval baselines, especially in factuality and citation measures, though evidence is scoped to particular models, datasets, and evaluation choices.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The framework integrates on-demand retrieval, tokenized critique, and customizable decoding, rather than treating retrieval as a fixed input step.",
          "page": 2,
          "quote": "our inference-time algorithm enables us to (1) flexibly adjust retrieval frequency for different downstream applications and (2) customize models’ behaviors to user preferences"
        },
        {
          "kind": "strength",
          "claim": "The reported results show competitive or leading performance across varied tasks, including large citation-precision and recall results on ASQA relative to listed retrieval baselines.",
          "page": 8,
          "quote": "Our SELF -RAG 13 B 55.8 69.3 74.5 73.1 80.2 31.7 37.0 71.6 70.3 71.3"
        },
        {
          "kind": "strength",
          "claim": "Ablations test multiple components and report deterioration when retrieval or critique is removed, or when only the top passage is used.",
          "page": 9,
          "quote": "Using the top passages regardless of their relevance (Retrieve top 1) as in conventional RAG approaches causes a large drop in PopQA and ASQA"
        },
        {
          "kind": "limitation",
          "claim": "The evaluation relies partly on previously reported results where implementations were unavailable, limiting direct comparability and independent verification within this study.",
          "page": 7,
          "quote": "We report numbers using the results reported in the paper as the implementations are not available."
        }
      ],
      "unresolved_questions": [
        "How robust are the reported gains across additional model families, retrievers, and datasets beyond the evaluated setup?",
        "How do the reflection-token labels and critic supervision affect reliability when the proprietary-LM-generated supervision is imperfect?",
        "I inspected pages 1–3 and 7–9, not the remaining paper; training details, further analyses, and stated limitations elsewhere may qualify this assessment."
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
          2
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
          8
        ],
        "candidate_pages": [],
        "status": "exact",
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
