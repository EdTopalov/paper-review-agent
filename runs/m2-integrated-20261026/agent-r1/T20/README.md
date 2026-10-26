# T20: RAFT: Adapting Language Model to Domain Specific RAG

**agent · ok**

7 model calls · 5 reads · 19.59 s · $0.003154

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.73

RAFT is a practical fine-tuning recipe for in-domain RAG: train with question/document/answer examples that include irrelevant retrieved documents, sometimes omit the oracle document, and produce quoted reasoning answers. The paper reports improvements over several fine-tuning and RAG baselines across biomedical QA, multi-hop QA, and API-document tasks. Its main value is the targeted training setup and broad task demonstrations, while claims are bounded to a same-domain/document setting and the inspected evidence leaves some evaluation details unresolved.

- **strength**: The method directly trains for imperfect retrieval by mixing relevant evidence with distractors and withholding the oracle document on some examples.
  - Page 3 · citation: whitespace
  - Quote: "For (1 − P ) fraction of the questions (qi) in the dataset, we include no oracle document and only include distractor documents (dk)."

- **strength**: The reported benchmark table gives evidence of gains over the listed RAG and domain-specific fine-tuning baselines on several tasks, though not uniformly over every baseline and task.
  - Page 5 · citation: exact
  - Quote: "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"

- **limitation**: The work explicitly targets a restricted deployment setting rather than domain transfer to new documents at inference time.
  - Page 9 · citation: whitespace
  - Quote: "our paper studies a slightly opposite scenario where we only care about testing the LLM on the same set of documents."

- **uncertainty**: The pages inspected establish headline results but do not provide enough detail here to judge statistical variability or fully audit the evaluation protocol.
  - Page 4 · citation: whitespace
  - Quote: "We see that RAFT consistently and significantly outperforms the baselines."

Unresolved questions:

- How sensitive are the headline gains to random seeds, data composition, and the exact retrieval pipeline?
- How well does RAFT transfer to new documents or domains, outside the same-document setting?
- How much of the gain depends on generated chain-of-thought quality versus the distractor-aware training construction?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The method uses oracle documents alongside distractors for a portion of examples, and only distractors for the remainder (PDF p. 3).
- Observation 2: **supported** — Table 1 reports RAFT’s results against the listed baselines across five tasks, with gains on several metrics and exceptions such as Torch Hub, where DSF scores 84.94 versus RAFT’s 84.95, and PubMed, where DSF + RAG ties GPT-3.5 + RAG (PDF p. 5). The claim appropriately avoids saying every comparison is a substantial win.
- Observation 3: **supported** — The paper explicitly contrasts its setting with work testing on different domains or documents, stating that it focuses on the same set of documents (PDF p. 9).
- Observation 4: **overstated** — The cited statement on p. 4 asserts that RAFT significantly outperforms baselines, but the paper includes more than headline results: it describes datasets and baselines (PDF p. 4), provides benchmark results and a CoT ablation (PDF pp. 5–7), and examines training and test-time document variation (PDF pp. 6–8). Those reported details do not establish statistical variability, but saying the pages inspected do not provide enough detail to fully audit the protocol is broader than the evidence shown; this is an open question, not itself a demonstrated defect.

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: search_paper

Locate experimental results to assess evidence for RAFT's claimed performance gains.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "Results",
    "reason": "Locate experimental results to assess evidence for RAFT's claimed performance gains."
  },
  "observation": {
    "matches": [
      {
        "page": 4,
        "snippet": "AG (DSF + RAG): Equip a domain specific finetuned model with external knowledge using RAG. So, for the “knowledge” the model does not know, it can still refer to the context. 4.2. Results Using the above datasets and baselines, we evaluate our model RAFT and demonstrate the effectiveness of RAFT in Tab. 1. We see that RAFT consistently and significantly outperforms the baselines. Compared with the base Llama- 2 instruction-tuned model, RAFT with RAG does much better in terms of extracting information as well as being robust towards distractors. The gain can be as big as 35.25% on "
      },
      {
        "page": 6,
        "snippet": "sing the top-k documents obtained from the retriever - not to be confused with p. Our findings, detailed in Fig. 6, reveal that finetuning with only the oracle document frequently results in inferior per- formance compared to configurations that include a greater number of distractor documents. As we can see in the fig- ure, the better performance for Natural Questions is training with D∗ + 3D and it is D∗ + 1D documents with Hotpot QA. This insight has been particularly beneficial for our algorithm, RAFT . In our experiments, we typically employ a training setup consisting of one"
      },
      {
        "page": 7,
        "snippet": "RAFT: Adapting Language Model to Domain Specific RAG Table 2: Ablation on Chain-of-Thought: The numbers of RAFT and RAFT without CoT. Results on various datasets show that adding CoT can significantly improve the performance of the finetuned model. With a gain of 9.66% and 14.93% on the Hotpot QA and HuggingFace datasets respectively. PubMed HotpotQA HuggingFace Torch Hub TensorFlow Hub RAFT w.o CoT 68.30 25.62 59.07 86.56 83.21 RAFT 73.30 35.28 74.00 84.95 86.86 HotPot QA Question: What screenwriter with credits for “Evolution”[0/1879"
      },
      {
        "page": 7,
        "snippet": "ur experiments focused on as- sessing how models, trained with varying numbers of dis- tractor documents, respond to changes in the number of documents presented at test time. The results, illustrated in Fig. 6, confirm that the inclusion of distractor documents during training indeed makes the model more resilient to fluctuations in the number of docu- ments encountered during testing. This ability to maintain consistent performance despite variations in test-time doc- ument numbers further validates the robustness of our ap- proach, RAFT . This finding underscores the importance"
      },
      {
        "page": 8,
        "snippet": " Figure 5: How many golden documents to involve? We study the hyperparameter P % which indicates what fraction of the training data contains the oracle document(s) in its context. Results on NQ, TQA and HotpotQA suggest that mixing a fraction of data that does not have the oracle document in its context is helpful for in-domain RAG. 2 4 6 8 10 # T est Documents (T op-k) 0.22 0.24 0.26 0.28 0.30 0.32Final Accuracy Natural Questions Train D* Train D* + 1D Train D* + 2D Train D* + 3D 2 4 6 8 10 # T est Documents (T op-k) 0.125 0.150 0.175 0.200 0.225 0.250Final Accuracy Hotpot QA Tra"
      }
    ],
    "limit_reached": false
  }
}
```

</details>

### Step 2: read_pages

Inspect the main benchmark setup, results table, and stated evaluation details.

[Event 10](trace.jsonl#L10)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 4,
    "end": 5,
    "reason": "Inspect the main benchmark setup, results table, and stated evaluation details."
  },
  "observation": {
    "pages": [
      {
        "page": 4,
        "text": "RAFT: Adapting Language Model to Domain Specific RAG\ntion of a reasoning process, such as Chain-of-Thought, to\nexplain the provided answers.RAFT approach is similar:\nwe demonstrate that creating a full reasoning chain and in\naddition, clearly citing sources enhances the model’s accu-\nracy in answering questions. In Fig. 3, we illustrate this\nset-up. Generating the training data in this fashion, involves\npresenting the model with a question, context, and verified\nanswers, and then requesting it to form a reasoning chain\nthat appropriately references the original context.\nFor all the datasets in … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 5,
        "text": "RAFT: Adapting Language Model to Domain Specific RAG\nQuestion: The Oberoi family is part of a hotel company that has a head office in what\ncity?\ncontext: [The Oberoi family is an Indian family that is famous for its involvement in\nhotels, namely through The Oberoi Group]...[It is located in city center of Jakarta,\nnear Mega Kuningan, adjacent to the sister JW Marriott Hotel. It is operated by The\nRitz-Carlton Hotel Company. The complex has two towers that comprises a hotel and the\nAirlangga Apartment respectively]...[The Oberoi Group is a hotel company with its head\noffice in Delhi.]\nInstructi … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 3: search_paper

Check whether the paper explicitly discusses scope constraints or limitations.

[Event 15](trace.jsonl#L15)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "limitations",
    "reason": "Check whether the paper explicitly discusses scope constraints or limitations."
  },
  "observation": {
    "matches": [],
    "limit_reached": false,
    "hint": "Literal phrase not found. Try one keyword or a shorter exact phrase, or read pages."
  }
}
```

</details>

### Step 4: read_pages

Inspect the method and training-data construction to understand the distinctive contribution.

[Event 20](trace.jsonl#L20)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 2,
    "end": 3,
    "reason": "Inspect the method and training-data construction to understand the distinctive contribution."
  },
  "observation": {
    "pages": [
      {
        "page": 2,
        "text": "RAFT: Adapting Language Model to Domain Specific RAG\n“Open book”\nquery\n answer\n“Closed book”\nquery\n answer\nBake in Knowledge at Train TimeModel can use External Docs at Test\nRAFT (Proposed)\nquery\n answer\nTeach Model to use External Docs at Test\nFigure 1: How best to prepare for an Exam?(a) Fine-tuning based approaches implement \"studying\" by either directly\n\"memorizing\" the input documents or answering practice QA without referencing the documents. (b) Alternatively, in-\ncontext retrieval methods fail to leverage the learning opportunity afforded by the fixed domain and are equivalent to\ntakin … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 3,
        "text": "RAFT: Adapting Language Model to Domain Specific RAG\nFigure 2: Overview of our RAFT method. The top-left figure depicts our approach of adapting LLMs to reading solution\nfrom a set of positive and negative documents in contrast to standard RAG setup where models are trained based on the\nretriever outputs, which is a mixture of both memorization and reading. At test time, all methods follow the standard RAG\nsetting, provided with a top-k retrieved documents in the context.\nlowed by the key takeaways from our experiments. Then, we\nintroduce RAFT , a modified version of general instruction\ntuning … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 5: read_pages

Inspect later discussion and conclusion for scope caveats and whether the authors identify limitations.

[Event 25](trace.jsonl#L25)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 9,
    "end": 10,
    "reason": "Inspect later discussion and conclusion for scope caveats and whether the authors identify limitations."
  },
  "observation": {
    "pages": [
      {
        "page": 9,
        "text": "RAFT: Adapting Language Model to Domain Specific RAG\ntheir settings, at test time, the domain or documents can be\ndifferent than the training time; whereas our paper studies a\nslightly opposite scenario where we only care about testing\nthe LLM on the same set of documents.\n7. Conclusion\nRAFT is a training strategy designed to enhance the model’s\nperformance in answering questions within a specific do-\nmain, in \"open-book\" settings. This technique demonstrates\na fine-tuning recipe for LLMs for question-answering tasks\nbased on a selected collection of documents. We have pin-\npointed several cru … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 10,
        "text": "RAFT: Adapting Language Model to Domain Specific RAG\nJin, Q., Dhingra, B., Liu, Z., Cohen, W. W., and Lu, X.\nPubmedqa: A dataset for biomedical research question\nanswering. arXiv preprint arXiv:1909.06146, 2019.\nJoshi, M., Choi, E., Weld, D. S., and Zettlemoyer, L.\nTriviaqa: A large scale distantly supervised challenge\ndataset for reading comprehension. arXiv preprint\narXiv:1705.03551, 2017.\nKandpal, N., Wallace, E., and Raffel, C. Deduplicating\ntraining data mitigates privacy risks in language models.\nIn International Conference on Machine Learning , pp.\n10697–10707. PMLR, 2022.\nKhandelwal, U … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 6: submit_review · citation_validation_failed

Evidence covers the core training recipe, benchmark comparisons, and stated same-document scope; submit an assessment while noting evaluation details not inspected.

[Event 31](trace.jsonl#L31)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Evidence covers the core training recipe, benchmark comparisons, and stated same-document scope; submit an assessment while noting evaluation details not inspected.",
    "review": {
      "score": 0.73,
      "summary": "RAFT is a practical fine-tuning recipe for in-domain RAG: train with question/document/answer examples that include irrelevant retrieved documents, sometimes omit the oracle document, and produce quoted reasoning answers. The paper reports improvements over several fine-tuning and RAG baselines across biomedical QA, multi-hop QA, and API-document tasks. Its main value is the targeted training setup and broad task demonstrations, while claims are bounded to a same-domain/document setting and the inspected evidence leaves some evaluation details unresolved.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The method directly trains for imperfect retrieval by mixing relevant evidence with distractors and withholding the oracle document on some examples.",
          "page": 3,
          "quote": "For (1 − P ) fraction of the questions (qi) in the dataset, we include no oracle document and only include distractor documents (dk)."
        },
        {
          "kind": "strength",
          "claim": "The reported benchmark table gives evidence of gains over the listed RAG and domain-specific fine-tuning baselines on several tasks, though not uniformly over every baseline and task.",
          "page": 5,
          "quote": "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"
        },
        {
          "kind": "limitation",
          "claim": "The work explicitly targets a restricted deployment setting rather than domain transfer to new documents at inference time.",
          "page": 9,
          "quote": "our paper studies a slightly opposite scenario where we only care about testing the LLM on the same set of documents."
        },
        {
          "kind": "uncertainty",
          "claim": "The pages inspected establish headline results but do not provide enough detail here to judge statistical variability or fully audit the evaluation protocol.",
          "page": 4,
          "quote": "We design our experiments to study how well RAFT performs compared to various baselines."
        }
      ],
      "unresolved_questions": [
        "How sensitive are the headline gains to random seeds, data composition, and the exact retrieval pipeline?",
        "How well does RAFT transfer to new documents or domains, outside the same-document setting?",
        "How much of the gain depends on generated chain-of-thought quality versus the distractor-aware training construction?"
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
          5
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
        "quote_matches": false,
        "citation_verified": false,
        "matching_pages": [],
        "candidate_pages": [
          4
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

### Step 7: submit_review · accepted

Correct the invalid citation using exact language already observed on page 4 and submit the completed review.

[Event 37](trace.jsonl#L37)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Correct the invalid citation using exact language already observed on page 4 and submit the completed review.",
    "review": {
      "score": 0.73,
      "summary": "RAFT is a practical fine-tuning recipe for in-domain RAG: train with question/document/answer examples that include irrelevant retrieved documents, sometimes omit the oracle document, and produce quoted reasoning answers. The paper reports improvements over several fine-tuning and RAG baselines across biomedical QA, multi-hop QA, and API-document tasks. Its main value is the targeted training setup and broad task demonstrations, while claims are bounded to a same-domain/document setting and the inspected evidence leaves some evaluation details unresolved.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The method directly trains for imperfect retrieval by mixing relevant evidence with distractors and withholding the oracle document on some examples.",
          "page": 3,
          "quote": "For (1 − P ) fraction of the questions (qi) in the dataset, we include no oracle document and only include distractor documents (dk)."
        },
        {
          "kind": "strength",
          "claim": "The reported benchmark table gives evidence of gains over the listed RAG and domain-specific fine-tuning baselines on several tasks, though not uniformly over every baseline and task.",
          "page": 5,
          "quote": "RAFT (LLaMA2-7B) 73.30 35.28 74.00 84.95 86.86"
        },
        {
          "kind": "limitation",
          "claim": "The work explicitly targets a restricted deployment setting rather than domain transfer to new documents at inference time.",
          "page": 9,
          "quote": "our paper studies a slightly opposite scenario where we only care about testing the LLM on the same set of documents."
        },
        {
          "kind": "uncertainty",
          "claim": "The pages inspected establish headline results but do not provide enough detail here to judge statistical variability or fully audit the evaluation protocol.",
          "page": 4,
          "quote": "We see that RAFT consistently and significantly outperforms the baselines."
        }
      ],
      "unresolved_questions": [
        "How sensitive are the headline gains to random seeds, data composition, and the exact retrieval pipeline?",
        "How well does RAFT transfer to new documents or domains, outside the same-document setting?",
        "How much of the gain depends on generated chain-of-thought quality versus the distractor-aware training construction?"
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
          5
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
          4
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
