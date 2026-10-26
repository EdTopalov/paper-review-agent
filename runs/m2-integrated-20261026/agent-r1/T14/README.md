# T14: RULER: What's the Real Context Size of Your Long-Context Language Models?

**agent · ok**

4 model calls · 3 reads · 11.70 s · $0.001388

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.76

RULER broadens long-context evaluation beyond single-needle retrieval with configurable retrieval, multi-hop tracing, aggregation, and QA tasks. Its evaluations expose substantial performance degradation and failure modes in ten models, making a useful diagnostic benchmark contribution; the evidence remains tied to synthetic/proxy tasks and a limited model sample.

- **strength**: The benchmark deliberately tests multiple behaviors beyond simple retrieval using configurable task complexity.
  - Page 1 · citation: whitespace
  - Quote: "RULER contains four task categories to test behaviors (Ribeiro et al., 2020) beyond simple retrieval from context:"

- **strength**: Evaluation across ten models and 13 tasks finds degradation with longer contexts, revealing weaknesses not exposed by vanilla NIAH.
  - Page 7 · citation: whitespace
  - Quote: "Despite achieving nearly perfect performance on the passkey retrieval and the vanilla NIAH task (shown in Appendix E), all models exhibit large degradation in RULER as sequence length increases."

- **limitation**: Several task categories are explicitly proxies, so benchmark performance should not be equated with broad real-world understanding.
  - Page 5 · citation: whitespace
  - Quote: "In RULER , we introduce a new category as a proxy for summarization tasks where relevant information constitutes much larger portion of the context"

- **uncertainty**: The effective-length judgment depends on a particular baseline threshold and weighted scores on selected test configurations; sensitivity to other criteria is not established in the inspected results.
  - Page 6 · citation: whitespace
  - Quote: "We use the performance of Llama2-7b model at the 4K context length as the threshold."

Unresolved questions:

- How well do these synthetic and proxy tasks predict performance on diverse naturally occurring long-context workloads?
- Would the effective-length comparisons and model ordering remain similar under alternative thresholds, task mixes, and broader model coverage?
- The inspected pages do not include the full appendices, including task correlations and per-task results; how do those details qualify the aggregate findings?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes configurable sequence length and task complexity and four categories—retrieval, multi-hop tracing, aggregation, and QA—beyond simple retrieval (PDF pp. 1–5, 15).
- Observation 2: **supported** — The authors evaluate ten models on 13 tasks and report substantial degradation as sequence length increases; they contrast this with near-perfect passkey and vanilla NIAH results (PDF pp. 6–7, 21). The appendix does show some exceptions to near-perfect vanilla NIAH, but the observation does not claim every model is perfect.
- Observation 3: **supported** — Variable tracking is described as a minimal proxy for coreference-chain resolution, and aggregation is explicitly introduced as a proxy for summarization; the paper also states that RULER consists solely of synthetic tasks (PDF pp. 1–2, 5).
- Observation 4: **supported** — Effective length is defined using the Llama2-7B 4K performance threshold (PDF p. 6). The paper reports alternative weighted-average schemes for model rankings, but does not establish how effective-length judgments change under alternative thresholds (PDF pp. 6, 14–16).

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: search_paper

Locate the paper’s discussion of benchmark scope and limitations.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "limitations",
    "reason": "Locate the paper’s discussion of benchmark scope and limitations."
  },
  "observation": {
    "matches": [],
    "limit_reached": false,
    "hint": "Literal phrase not found. Try one keyword or a shorter exact phrase, or read pages."
  }
}
```

</details>

### Step 2: read_pages

Inspect benchmark construction and evaluation setup to assess evidence quality.

[Event 10](trace.jsonl#L10)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 5,
    "end": 7,
    "reason": "Inspect benchmark construction and evaluation setup to assess evidence quality."
  },
  "observation": {
    "pages": [
      {
        "page": 5,
        "text": "Preprint. Under review.\nWord types\n0\n10\n20\n30Word Freq.\nCWE\nCommon words\nUncommon words\nlog (Word rank)\n2\n4\n6\n8log (Word Freq.)\nFWE\n=1.5\n=2.0\n=2.5\n=3.0\nFigure 1: In aggregation tasks, we sample words from a vocabulary following the two distri-\nbutions above. The common words extraction (CWE) samples from uniform distributions.\nIn the frequent words extraction (FWE), the frequency of each word is determined by its\nrank in the vocabulary and the parameter α of Zeta distribution.\n3.2 Multi-hop Tracing: Variable Tracking (VT)\nEffective discourse comprehension (van Dijk & Kintsch, 1983) is continge … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 6,
        "text": "Preprint. Under review.\nModels Claimed\nLength\nEffective\nLength 4k 8k 16k 32k 64k 128k Avg. wAvg.\n(inc)\nwAvg.\n(dec)\nLlama2-7B (chat) 4k - 85.6\nGPT-4 128k 64k 96.6 96.3 95.2 93.2 87.0 81.2 91.6 89.0(1st) 94.1(1st)\nCommand-R (35B)128k 32k 93.8 93.3 92.4 89.5 84.9 76.0 88.3 85.5(2nd) 91.1(2nd)\nYi (34B) 200k 32k 93.3 92.2 91.3 87.5 83.2 77.3 87.5 84.8(3th) 90.1(3th)\nMixtral (8x7B) 32k 32k 94.9 92.1 92.5 85.9 72.4 44.5 80.4 72.8(4th) 87.9(4th)\nMistral (7B) 32k 16k 93.6 91.2 87.2 75.4 49.0 13.8 68.4 55.6(7th) 81.2(5th)\nChatGLM (6B) 128k 4k 87.8 83.4 78.6 69.9 56.0 42.0 69.6 62.0(6th) 77.2(6th)\nLWM (7 … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 7,
        "text": "Preprint. Under review.\nMain Results We include the results of ten long-context LMs in comparison with the\nLlama2-7B baseline in Table 3.6 The performance at a certain length is the average of all\n13 tasks in RULER . While these models all claim effective context of 32K tokens or greater,\nnone of them maintains performance above the Llama2-7B baseline at their claimed length,\nexcept for Mixtral, which achieves moderate performance on length doubling the claimed\n32K context size. Despite achieving nearly perfect performance on the passkey retrieval\nand the vanilla NIAH task (shown in Appendix E … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 3: read_pages

Review the paper’s discussion and conclusions for scope boundaries and benchmark claims.

[Event 15](trace.jsonl#L15)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 9,
    "end": 11,
    "reason": "Review the paper’s discussion and conclusions for scope boundaries and benchmark claims."
  },
  "observation": {
    "pages": [
      {
        "page": 9,
        "text": "Preprint. Under review.\n4k 8k 16k 32k 64k128k256k\nSequence Length\n0\n20\n40\n60\n80\n100Accuracy\nLength Comparison\nLWM-1M\nLWM-512K\nLWM-256K\nLWM-128K\n4k 8k 16k 32k 64k128k256k\nSequence Length\n0\n20\n40\n60\n80\n100Accuracy\nLength Comparison\nLWM-base-1M\nLWM-base-512K\nLWM-base-256K\nLWM-base-128K\nLWM-base-32K\n4k 8k 16k 32k 64k128k256k\nSequence Length\n0\n20\n40\n60\n80\n100Accuracy\nSize Comparison\nYi-34B-200K\nYi-9B-200K\nYi-6B-200K\n1k 2k 4k 8k\nSequence Length\n0\n20\n40\n60\n80\n100Accuracy\nArchitecture Comparison\nLlama2-7b\nRWKV-v5-7b\nMamba-2.8b-slimpj\nFigure 4: (Left & middle left): Comparison of LargeWorldModel (LWM)  … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 10,
        "text": "Preprint. Under review.\nReferences\nAI21. Introducing jamba: Ai21’s groundbreaking ssm-transformer model, 2024. URL\nhttps://www.ai21.com/blog/announcing-jamba.\nChenxin An, Shansan Gong, Ming Zhong, Mukai Li, Jun Zhang, Lingpeng Kong, and\nXipeng Qiu. L-eval: Instituting standardized evaluation for long context language models.\nIn ICLR, 2024.\nAnthropic. Long context prompting for Claude 2.1. Blog, 2023. URL https://www.\nanthropic.com/index/claude-2-1-prompting .\nAnthropic. Introducing the next generation of claude, 2024. URL https://www.anthropic.\ncom/news/claude-3-family.\nSimran Arora, Sabri Eyu … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 11,
        "text": "Preprint. Under review.\nDaniel Y. Fu et al. Simple hardware-efficient long convolutions for sequence modeling.\nICML, 2023b.\nYao Fu et al. Data engineering for scaling language models to 128k context.arXiv:2402.10171,\n2024.\nAlex Graves, Greg Wayne, and Ivo Danihelka. Neural Turing machines. arXiv:1410.5401,\n2014.\nAlbert Gu and Tri Dao. Mamba: Linear-time sequence modeling with selective state spaces.\narXiv:2312.00752, 2023.\nAlbert Gu, Karan Goel, and Christopher Re. Efficiently modeling long sequences with\nstructured state spaces. In ICLR, 2022.\nChi Han, Qifan Wang, Wenhan Xiong, Yu Chen, Heng  … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 4: submit_review · accepted

Evidence covers benchmark design, results, and conclusion; submit a balanced assessment with scope caveats.

[Event 20](trace.jsonl#L20)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Evidence covers benchmark design, results, and conclusion; submit a balanced assessment with scope caveats.",
    "review": {
      "score": 0.76,
      "summary": "RULER broadens long-context evaluation beyond single-needle retrieval with configurable retrieval, multi-hop tracing, aggregation, and QA tasks. Its evaluations expose substantial performance degradation and failure modes in ten models, making a useful diagnostic benchmark contribution; the evidence remains tied to synthetic/proxy tasks and a limited model sample.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The benchmark deliberately tests multiple behaviors beyond simple retrieval using configurable task complexity.",
          "page": 1,
          "quote": "RULER contains four task categories to test behaviors (Ribeiro et al., 2020) beyond simple retrieval from context:"
        },
        {
          "kind": "strength",
          "claim": "Evaluation across ten models and 13 tasks finds degradation with longer contexts, revealing weaknesses not exposed by vanilla NIAH.",
          "page": 7,
          "quote": "Despite achieving nearly perfect performance on the passkey retrieval and the vanilla NIAH task (shown in Appendix E), all models exhibit large degradation in RULER as sequence length increases."
        },
        {
          "kind": "limitation",
          "claim": "Several task categories are explicitly proxies, so benchmark performance should not be equated with broad real-world understanding.",
          "page": 5,
          "quote": "In RULER , we introduce a new category as a proxy for summarization tasks where relevant information constitutes much larger portion of the context"
        },
        {
          "kind": "uncertainty",
          "claim": "The effective-length judgment depends on a particular baseline threshold and weighted scores on selected test configurations; sensitivity to other criteria is not established in the inspected results.",
          "page": 6,
          "quote": "We use the performance of Llama2-7b model at the 4K context length as the threshold."
        }
      ],
      "unresolved_questions": [
        "How well do these synthetic and proxy tasks predict performance on diverse naturally occurring long-context workloads?",
        "Would the effective-length comparisons and model ordering remain similar under alternative thresholds, task mixes, and broader model coverage?",
        "The inspected pages do not include the full appendices, including task correlations and per-task results; how do those details qualify the aggregate findings?"
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
          1
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
          5
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
          6
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
