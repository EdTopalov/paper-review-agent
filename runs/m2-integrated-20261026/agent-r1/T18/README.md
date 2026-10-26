# T18: Gorilla: Large Language Model Connected with Massive APIs

**agent · ok**

5 model calls · 3 reads · 15.31 s · $0.001798

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.72

Gorilla combines APIBench, AST-based API-call evaluation, and retrieval-aware fine-tuning of LLaMA to improve API selection and call generation across several model hubs. Reported results are strong on the evaluated tasks, while also revealing substantial dependence on retrieval quality and a narrower empirical scope than the paper’s broad API ambitions.

- **strength**: The paper presents a useful end-to-end benchmark and training setup for API-call generation, with a held-out evaluation.
  - Page 6 · citation: whitespace
  - Quote: "We emphasize that we have maintained a holdout test set on which we report our findings."

- **strength**: On reported zero-shot results, Gorilla exceeds listed GPT baselines for all three hub datasets, though evaluation conventions differ by dataset.
  - Page 7 · citation: exact
  - Quote: "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"

- **limitation**: The HuggingFace evaluation uses a weaker correctness check for comparison models than for Gorilla, limiting direct cross-model comparability there.
  - Page 7 · citation: whitespace
  - Quote: "for all the models except Gorilla, we only check if they can provide the correct domain names."

- **limitation**: Practical retrieval remains a significant bottleneck: the authors report large accuracy drops when substituting evaluated retrievers for the oracle.
  - Page 7 · citation: whitespace
  - Quote: "using GPT-Index at evaluation results in 29.20% accuracy degradation, and using BM25 results in a 52.27% accuracy degradation."

Unresolved questions:

- How well do these results transfer to APIs outside the three hubs and to real user requests or executable multi-step tool workflows?
- How representative and reproducible are the benchmark examples, generated instructions, and reported gains across API versions and stronger retrieval systems?
- The inspected passages do not establish the robustness of adaptation to documentation changes beyond illustrated examples; what systematic test-time update evaluation was performed?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes APIBench, AST-based evaluation, Gorilla fine-tuning, and a held-out test set (PDF pp. 2–6). The appendix also reports the data splits (p. 13).
- Observation 2: **supported** — In the zero-shot results, Gorilla exceeds both listed GPT baselines on TorchHub, HuggingFace, and TensorFlow Hub. The paper explicitly notes that HuggingFace uses a different, less stringent check for comparison models (PDF p. 7).
- Observation 3: **supported** — The paper states that, for HuggingFace, models other than Gorilla are checked only for correct domain names, whereas TorchHub and TensorHub use AST-tree accuracy for all models (PDF pp. 6–7).
- Observation 4: **supported** — The paper reports 29.20% accuracy degradation with GPT-Index and 52.27% with BM25 when evaluating the retrieval-aware fine-tuned model, relative to the ground-truth retrieval setting (PDF pp. 7–8).

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: search_paper

Locate the paper’s evaluation section to assess evidence for its claims.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "evaluation",
    "reason": "Locate the paper’s evaluation section to assess evidence for its claims."
  },
  "observation": {
    "matches": [
      {
        "page": 3,
        "snippet": "otics has been explored to some extent [41, 1]. However, these works primarily aim at showcasing the potential of “prompting” LLMs rather than establishing a systematic method for evaluation and training (including fine-tuning). Our work, on the other hand, concentrates on systematic evaluation and building a pipeline for future use. LLMs for Program Synthesis Harnessing LLMs for program synthesis has historically been a challenging task [ 23, 7, 45, 16, 13, 20]. Researchers have proposed an array of strategies to prompt LLMs to perform better in coding tasks, including in-context le"
      },
      {
        "page": 3,
        "snippet": "ntial of “prompting” LLMs rather than establishing a systematic method for evaluation and training (including fine-tuning). Our work, on the other hand, concentrates on systematic evaluation and building a pipeline for future use. LLMs for Program Synthesis Harnessing LLMs for program synthesis has historically been a challenging task [ 23, 7, 45, 16, 13, 20]. Researchers have proposed an array of strategies to prompt LLMs to perform better in coding tasks, including in-context learning [ 44, 18, 7], task decomposition [17, 46], and self-debugging [8, 36]. Besides prompting, there ha"
      },
      {
        "page": 3,
        "snippet": "We then introduce Gorilla, a novel training paradigm with a information–retriever incorporated into the training and inference pipelines. Finally, we present our AST tree matching evaluation metric. 3.1 Dataset Collection To collect the dataset, we meticulously recorded all online model cards for HuggingFace’s “The Model Hub”, PyTorch Hub, and TensorFlow Hub Models. Throughout the rest of the paper, we call these HuggingFace, Torch Hub, and TensorFlow Hub respectively for brevity. API Documentation The HuggingFace platform hosts and servers about 203,681 models. However, many of them"
      },
      {
        "page": 6,
        "snippet": "has a subtree match. In the above example, the matching subtree is highlighted in brown, signifying that the API call is indeed correct. Pretrained=True is an optional argument. 4 Evaluation We carried out an array of experiments on our collected dataset, benchmarking our model Gorilla with other models, and exploring how different retrieval methods may impact the performance of the model in making API calls. We then demonstrate that Gorilla can easily adapt to test-time changes in API documentation. In addition, we assess Gorilla’s ability to reason about API calls under constraints"
      },
      {
        "page": 6,
        "snippet": "es, when a retriever is used, it is appended to the user’s prompt as follows:<user_prompt>Use this API documentation for reference: <retrieved_API_doc_JSON>. The dataset for these evaluations is detailed in Sec 3. We emphasize that we have maintained a holdout test set on which we report our findings. The holdout test set was created by dividing the self-instruct dataset’s instruction, API pairs into training and testing sets. 4.1 AST Accuracy on API call We first demonstrate the results for the AST accuracy for different models. We present the results in Tab. 1. We test each model f"
      },
      {
        "page": 7,
        "snippet": "ests quantitatively, that finetuning is better than retrieval, at-least in our scope. In addition, we found that finetuning without retriever and putting ground truth retriever in evaluation time rarely helps the performance: 0.88% worse in TensorHub and 0.97% better in HuggingFace. If we put BM25 or GPT-Index as retriever, results will be significantly dropped: 21.50% in Torch Hub and 47.57% in HuggingFace. The result illustrates that adding a non-optimal retriever at test time will sometime misguide the model and result in more errors. We will discuss an interesting ablation on how"
      },
      {
        "page": 7,
        "snippet": "he finetuning pipeline achieves significantly better results 12.37% better than training without retriever in Torch Hub and 23.46% better in HuggingFace. However, we found that at evaluation time, current retrievers still have a big gap between the ground truth retriever: using GPT-Index at evaluation results in 29.20% accuracy degradation, and using BM25 results in a 52.27% accuracy degradation. Nevertheless, we can still conclude that with a better retriever, finetuning 7"
      },
      {
        "page": 7,
        "snippet": "rch Hub and 23.46% better in HuggingFace. However, we found that at evaluation time, current retrievers still have a big gap between the ground truth retriever: using GPT-Index at evaluation results in 29.20% accuracy degradation, and using BM25 results in a 52.27% accuracy degradation. Nevertheless, we can still conclude that with a better retriever, finetuning 7"
      }
    ],
    "limit_reached": true
  }
}
```

</details>

### Step 2: read_pages

Inspect benchmark results and retrieval ablations, including exact passages for evidence.

[Event 10](trace.jsonl#L10)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 6,
    "end": 8,
    "reason": "Inspect benchmark results and retrieval ablations, including exact passages for evidence."
  },
  "observation": {
    "pages": [
      {
        "page": 6,
        "text": "torchutilshubTensormodel_zooloadrepo: pytorch/visionmodel: densenet121model: densenet161model: densenet201pretrained: Truepretrained: False\nrepo: huggingface/pytorch-transformers\ntorch.hub.load(’pytorch/vision:v0.10.0’,  ‘densenet121’, pretrained=True)\ntorchhubloadpytorch/visiondensenet121pretrained = True\nFigure 4: AST Sub-Tree Matching to evaluate API calls. On the left is an API call returned by Gorilla. We\nfirst build the associated API tree. We then compare this to our dataset, to see if the API dataset has a subtree\nmatch. In the above example, the matching subtree is highlighted in brow … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 7,
        "text": "LLAMA GPT-3.5 GPT-4 Claude Gorilla\nModel\n0\n20\n40\n60\n80\n100\nAccuracy\n14.51\n60.21 59.13 60.21 61.82\nT orch Hub with GPT-Retriever\nLLAMA GPT-3.5 GPT-4 Claude Gorilla\nModel\n0\n20\n40\n60\n80\n100\n10.17\n47.34 44.57 41.37 47.45\nHuggingFace with GPT-Retriever\nLLAMA GPT-3.5 GPT-4 Claude Gorilla\nModel\n0\n20\n40\n60\n80\n100\n15.62\n65.59\n43.94\n55.62\n64.96\nT ensorflow Hub with GPT-Retriever\nFigure 5: Accuracy with GPT-retriever.Gorilla outperforms on Torch Hub and Hugging-Face while matching\nperformance on Tensorflow Hub for all existing SoTA LLMs - closed source, and open source.\nsince the dataset is not exhaustiv … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 8,
        "text": "USER: I want to automatically remove the background from an input image <Retrieval: ..fcn_resnet101..>GORILLA:     api_call:         “torch.hub.load('pytorch/vision', 'fcn_resnet101', pretrained=True)”\nUSER: I want to automatically remove the background from an input image. <Retrieval: ..NVIDIA/DeepLearningExamples:torchhub..>GORILLA:    api_call:         “torch.hub.load(‘NVIDIA / DeepLearningExamples:torchhub ', 'fcn_resnet50', pretrained=True)”\nUSER: I want to automatically remove the background from an input image. <Retrieval:  ..fcn_resnet50..>GORILLA:     api_call:         “torch.hub.load … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 3: read_pages

Check how the API dataset was constructed to judge benchmark scope and support.

[Event 15](trace.jsonl#L15)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 3,
    "end": 3,
    "reason": "Check how the API dataset was constructed to judge benchmark scope and support."
  },
  "observation": {
    "pages": [
      {
        "page": 3,
        "text": "2 Related Work\nLarge Language Models Recent strides in the field of LLMs have renovated many downstream\ndomains [ 10, 40, 48, 47], not only in traditional natural language processing tasks but also in\nprogram synthesis. Many of these advances are achieved by augmenting pre-trained LLMs by\nprompting [44, 14] and instruction fine-tuning [11, 31, 43, 15]. Recent open-sourced models like\nLLaMa [40], Alpaca [38], and Vicuna [9] have furthered the understanding of LLMs and facilitated\ntheir experimentation. While our approach, Gorilla, incorporates techniques akin to those mentioned,\nits primary emp … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 4: submit_review · citation_validation_failed

Evidence covers the contribution, benchmark construction, measured performance, and an explicit retrieval caveat; submit a scoped assessment.

[Event 20](trace.jsonl#L20)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Evidence covers the contribution, benchmark construction, measured performance, and an explicit retrieval caveat; submit a scoped assessment.",
    "review": {
      "score": 0.72,
      "summary": "Gorilla combines APIBench, AST-based API-call evaluation, and retrieval-aware fine-tuning of LLaMA to improve API selection and call generation across several model hubs. The reported benchmark results show strong performance on the authors’ evaluated tasks, while also exposing substantial dependence on retrieval quality and a narrower empirical scope than the paper’s broad API ambitions.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The paper presents a useful end-to-end benchmark and training setup for API-call generation, and reports a held-out evaluation against several language-model baselines.",
          "page": 6,
          "quote": "We emphasize that we have maintained a holdout test set on which we report our findings."
        },
        {
          "kind": "strength",
          "claim": "On reported zero-shot results, Gorilla exceeds the listed GPT baselines for all three hub datasets, though evaluation conventions differ by dataset.",
          "page": 7,
          "quote": "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"
        },
        {
          "kind": "limitation",
          "claim": "The HuggingFace evaluation uses a weaker correctness check for comparison models than for Gorilla, limiting direct cross-model comparability there.",
          "page": 7,
          "quote": "for all the models except Gorilla, we only check if they can provide the correct domain names."
        },
        {
          "kind": "limitation",
          "claim": "Practical retrieval remains a significant bottleneck: the paper reports large accuracy drops when substituting evaluated retrievers for the oracle, so results do not establish robust performance with ordinary retrieval.",
          "page": 8,
          "quote": "using GPT-Index at evaluation results in 29.20% accuracy degradation, and using BM25 results in a 52.27% accuracy degradation."
        }
      ],
      "unresolved_questions": [
        "How well do these results transfer to APIs outside the three hubs and to real user requests or executable multi-step tool workflows?",
        "How representative and reproducible are the benchmark examples, generated instructions, and reported gains across API versions and stronger retrieval systems?",
        "The inspected passages do not establish the robustness of adaptation to documentation changes beyond the illustrated examples; what systematic test-time update evaluation was performed?"
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
          6
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
        "matching_pages": [
          7
        ],
        "candidate_pages": [],
        "status": "wrong_page",
        "observed": false
      }
    ],
    "hint": "Copy exact quotes from observed pages, or read matching pages before resubmitting. Preserve case, mathematical notation, and ambiguous hyphens."
  }
}
```

</details>

### Step 5: submit_review · accepted

Correct the citation page for the retrieval caveat using the observed page 7 text and finalize the assessment.

[Event 25](trace.jsonl#L25)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Correct the citation page for the retrieval caveat using the observed page 7 text and finalize the assessment.",
    "review": {
      "score": 0.72,
      "summary": "Gorilla combines APIBench, AST-based API-call evaluation, and retrieval-aware fine-tuning of LLaMA to improve API selection and call generation across several model hubs. Reported results are strong on the evaluated tasks, while also revealing substantial dependence on retrieval quality and a narrower empirical scope than the paper’s broad API ambitions.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The paper presents a useful end-to-end benchmark and training setup for API-call generation, with a held-out evaluation.",
          "page": 6,
          "quote": "We emphasize that we have maintained a holdout test set on which we report our findings."
        },
        {
          "kind": "strength",
          "claim": "On reported zero-shot results, Gorilla exceeds listed GPT baselines for all three hub datasets, though evaluation conventions differ by dataset.",
          "page": 7,
          "quote": "Gorilla (0-shot) 59.13 6.98 33.87 71.68 10.95 17.36 83.79 5.40 10.80"
        },
        {
          "kind": "limitation",
          "claim": "The HuggingFace evaluation uses a weaker correctness check for comparison models than for Gorilla, limiting direct cross-model comparability there.",
          "page": 7,
          "quote": "for all the models except Gorilla, we only check if they can provide the correct domain names."
        },
        {
          "kind": "limitation",
          "claim": "Practical retrieval remains a significant bottleneck: the authors report large accuracy drops when substituting evaluated retrievers for the oracle.",
          "page": 7,
          "quote": "using GPT-Index at evaluation results in 29.20% accuracy degradation, and using BM25 results in a 52.27% accuracy degradation."
        }
      ],
      "unresolved_questions": [
        "How well do these results transfer to APIs outside the three hubs and to real user requests or executable multi-step tool workflows?",
        "How representative and reproducible are the benchmark examples, generated instructions, and reported gains across API versions and stronger retrieval systems?",
        "The inspected passages do not establish the robustness of adaptation to documentation changes beyond illustrated examples; what systematic test-time update evaluation was performed?"
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
          6
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
          7
        ],
        "candidate_pages": [],
        "status": "whitespace",
        "observed": true
      }
    ]
  }
}
```

</details>
