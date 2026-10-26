# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**agent · ok**

6 model calls · 4 reads · 16.38 s · $0.001718

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.76

SWE-bench contributes a substantial, realistic benchmark of issue-resolution tasks drawn from real GitHub repositories, framing code generation as repository-level engineering evaluated against tests. The reported baselines show difficulty for evaluated models, and the authors clearly identify Python-only coverage and test-based evaluation as scope limitations.

- **strength**: The benchmark grounds tasks in real GitHub issues and pull requests across multiple Python repositories.
  - Page 1 · citation: exact
  - Quote: "2,294 software engi-\nneering problems drawn from real GitHub issues and corresponding pull requests\nacross 12 popular Python repositories."

- **strength**: The paper reports low performance on the benchmark even with oracle retrieval, supporting its claim that these tasks challenge the tested models.
  - Page 1 · citation: exact
  - Quote: "Claude 2 and GPT-4 solve a mere4.8% and 1.7% of instances re-\nspectively, even when provided with an oracle retriever."

- **limitation**: The current task collection covers only Python, so generalization to other languages and domains remains unestablished.
  - Page 9 · citation: whitespace
  - Quote: "SWE-bench task instances are all in Python; we hope to ap-\nply SWE-bench’s task instance collection procedure to expand its coverage to more programming languages and domains."

- **limitation**: Execution-based tests alone do not guarantee that generated solutions are reliable.
  - Page 9 · citation: exact
  - Quote: "relying solely on this method is insufficient to guarantee reliable performance of\nmodel generations"

Unresolved questions:

- I did not inspect the benchmark-construction procedure or detailed experimental sections; how are issue/PR pairs filtered and test relevance validated, and how robust are headline results across model configurations?
- How well does benchmark success correlate with expert judgments of correctness, maintainability, and usefulness in real engineering work?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — Page 1 states that the 2,294 tasks come from real GitHub issues and corresponding pull requests across 12 Python repositories; page 2 describes those as user-submitted issues and solutions.
- Observation 2: **supported** — Pages 1–2 report low solve rates for Claude 2 and GPT-4 even with oracle retrieval, and page 5 reports Claude 2’s 4.8% oracle pass rate. This supports the qualified claim that the benchmark challenges the evaluated models.
- Observation 3: **supported** — Page 9 states that all task instances are in Python and presents expanding language and domain coverage as future work; generalization beyond the current collection is therefore unestablished.
- Observation 4: **supported** — Page 9 explicitly says relying solely on execution-based testing is insufficient to guarantee reliable model generations, noting that outputs can be less comprehensive, efficient, or readable than human-written solutions.

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: search_paper

Locate the paper’s stated scope boundaries and limitations for a balanced assessment.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "limitations",
    "reason": "Locate the paper’s stated scope boundaries and limitations for a balanced assessment."
  },
  "observation": {
    "matches": [
      {
        "page": 2,
        "snippet": "olve issues using over 100,000 tokens as context. We hope SWE-bench serves as a challenging software engineering benchmark that aids in better understand- ing of the abilities and limitations of LMs. 2 SWE- BENCH SWE-bench is a benchmark featuring GitHub issues from popular repositories that report bugs or request new features, and pull requests that make changes to the repository to resolve these issues. The task is to generate a pull request that addresses a given issue and passes tests related to the issue. 2.1 B ENCHMARK CONSTRUCTION GitHub is a rich data source for software devel"
      },
      {
        "page": 9,
        "snippet": "t provides a significantly more realistic and challenging arena to carry out future experiments towards augmenting LMs with software engineering tools and practices. 7 D ISCUSSION Limitations and future directions. SWE-bench task instances are all in Python; we hope to ap- ply SWE-bench’s task instance collection procedure to expand its coverage to more programming languages and domains. Second, our experiments aim to establish a baseline of the simplest and most straight-forward approaches for this task; we do not intend to constrain future methodologies to the same type of approach "
      }
    ],
    "limit_reached": false
  }
}
```

</details>

### Step 2: read_pages

Read discussion and limitations, plus nearby empirical findings, to evaluate scope and evidence.

[Event 10](trace.jsonl#L10)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 8,
    "end": 10,
    "reason": "Read discussion and limitations, plus nearby empirical findings, to evaluate scope and evidence."
  },
  "observation": {
    "pages": [
      {
        "page": 8,
        "text": "from SWE-Llama and summarize our overall findings, with in-depth analyses for the remaining\nexamples shown in Appendix F.\nGold  P a t ch\n      (self, section: str) -> List[str]: \n-         self. (_( ), self._consume_fields()) \n+         self._config.napoleon_use_param: \n+            \n+            fields = self. (multiple=True) \n+             self. (fields) \n+        : \n+            fields = self. () \n+            return self. (_( ), fields)\ndef\nreturn\nif\nreturn\nelse\n_parse_other_parameters_section\n_format_fields\n_consume_fields\n_format_docutils_params\n_consume_fields\n_format_fields\n'Other Para … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 9,
        "text": "one or a few skills, resulting in challenges that are typically too simple, pigeonhole the model into a\nreduced role, and do not provide models with the bandwidth to exercise their versatility or potentially\ndemonstrate new abilities (Srivastava et al., 2023). Consequently, a model’s performance on such\ntask conglomerations may not yield actionable, deep insights regarding its capabilities and how to\nimprove them (Schlangen, 2019; Mart ´ınez-Plumed et al., 2021; Bowman & Dahl, 2021). SWE-\nbench addresses these shortcomings, as our work demonstrates that it is significantly challenging,\npresent … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 10,
        "text": "8 E THICS STATEMENT\nSWE-bench is collected entirely from public repositories with licenses that permit software usage\nthat our contributions are in accordance with. Details of the licenses are included in Table 12.\nDuring the collection or evaluation processes, we do not collect information about GitHub users,\nand the SWE-bench task instances do not use GitHub data beyond what is offered via the public API\nand website. Our contributions do not involve any human subject participation; we do not perform\ncrowdsourcing or recruit human task workers for any part of SWE-bench, including its collecti … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 3: search_paper

Find the reported evaluation setup and headline results to substantiate the benchmark’s empirical contribution.

[Event 15](trace.jsonl#L15)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "oracle retriever",
    "reason": "Find the reported evaluation setup and headline results to substantiate the benchmark’s empirical contribution."
  },
  "observation": {
    "matches": [
      {
        "page": 1,
        "snippet": "odels and our fine-tuned model SWE-Llama can resolve only the simplest issues. Claude 2 and GPT-4 solve a mere4.8% and 1.7% of instances re- spectively, even when provided with an oracle retriever. Advances on SWE-bench represent steps towards LMs that are more practical, intelligent, and autonomous. 1 I NTRODUCTION Language models (LMs) are rapidly being deployed in commercial products such as chatbots and coding assistants. At the same time, existing benchmarks have become saturated (Kiela et al., 2021; Ott et al., 2022) and fail to capture the frontier of what state-of-the-art LMs can a"
      }
    ],
    "limit_reached": false
  }
}
```

</details>

### Step 4: submit_review · citation_validation_failed

Submit an evidence-based assessment using inspected abstract, discussion, and limitations pages; note evaluation details not inspected.

[Event 20](trace.jsonl#L20)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Submit an evidence-based assessment using inspected abstract, discussion, and limitations pages; note evaluation details not inspected.",
    "review": {
      "score": 0.76,
      "summary": "SWE-bench contributes a substantial, realistic benchmark of 2,294 issue-resolution tasks drawn from real GitHub repositories, reframing code generation as multi-file software engineering evaluated against tests. The paper’s baselines demonstrate that the task was difficult for the evaluated models, while the authors clearly delimit the benchmark’s Python-only scope and the limits of test-based evaluation.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The benchmark targets practical repository-level issue resolution rather than short, self-contained code generation, and connects issue descriptions to real codebases and tests.",
          "page": 1,
          "quote": "We therefore introduce SWE-bench, an evaluation framework including 2,294 software engineering problems drawn from real GitHub issues and corresponding pull requests across 12 popular Python repositories."
        },
        {
          "kind": "strength",
          "claim": "The reported baseline results show substantial difficulty for the tested models, including when given oracle retrieval.",
          "page": 1,
          "quote": "Claude 2 and GPT-4 solve a mere4.8% and 1.7% of instances respectively, even when provided with an oracle retriever."
        },
        {
          "kind": "limitation",
          "claim": "The benchmark’s present task collection is restricted to Python, limiting demonstrated coverage of other languages and domains.",
          "page": 9,
          "quote": "SWE-bench task instances are all in Python; we hope to apply SWE-bench’s task instance collection procedure to expand its coverage to more programming languages and domains."
        },
        {
          "kind": "limitation",
          "claim": "Passing execution-based tests does not by itself establish that generated patches are reliable or match human standards for quality.",
          "page": 9,
          "quote": "relying solely on this method is insufficient to guarantee reliable performance of model generations"
        }
      ],
      "unresolved_questions": [
        "I did not inspect the benchmark-construction procedure or detailed experimental sections; how are issue/PR pairs filtered and test relevance validated, and how robust are the headline results across model configurations?",
        "How well does benchmark success correlate with expert judgments of correctness, maintainability, and usefulness on real engineering work?"
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
        "quote_matches": false,
        "citation_verified": false,
        "matching_pages": [],
        "candidate_pages": [
          1
        ],
        "status": "hyphenation_ambiguous",
        "observed": false
      },
      {
        "checker_version": "m2-citations-v2",
        "page_valid": true,
        "quote_nonempty": true,
        "quote_matches": false,
        "citation_verified": false,
        "matching_pages": [],
        "candidate_pages": [
          1
        ],
        "status": "hyphenation_ambiguous",
        "observed": false
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
      }
    ],
    "hint": "Copy exact quotes from observed pages, or read matching pages before resubmitting. Preserve case, mathematical notation, and ambiguous hyphens."
  }
}
```

</details>

### Step 5: read_pages

Retrieve exact abstract wording for citation validation after the prior quote check flagged hyphenation ambiguity.

[Event 25](trace.jsonl#L25)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 1,
    "end": 1,
    "reason": "Retrieve exact abstract wording for citation validation after the prior quote check flagged hyphenation ambiguity."
  },
  "observation": {
    "pages": [
      {
        "page": 1,
        "text": "SWE- BENCH : C AN LANGUAGE MODELS RESOLVE\nREAL -WORLD GITHUB ISSUES ?\nCarlos E. Jimenez* 1,2 John Yang* 1,2 Alexander Wettig1,2\nShunyu Yao1,2 Kexin Pei3 Ofir Press1,2 Karthik Narasimhan1,2\n1Princeton University 2Princeton Language and Intelligence 3University of Chicago\nABSTRACT\nLanguage models have outpaced our ability to evaluate them effectively, but for\ntheir future development it is essential to study the frontier of their capabilities. We\nconsider real-world software engineering to be a rich, sustainable, and challeng-\ning testbed for evaluating the next generation of language models. We … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 6: submit_review · accepted

Resubmit with exact observed quotations, preserving the PDF’s hyphenation and spelling.

[Event 30](trace.jsonl#L30)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Resubmit with exact observed quotations, preserving the PDF’s hyphenation and spelling.",
    "review": {
      "score": 0.76,
      "summary": "SWE-bench contributes a substantial, realistic benchmark of issue-resolution tasks drawn from real GitHub repositories, framing code generation as repository-level engineering evaluated against tests. The reported baselines show difficulty for evaluated models, and the authors clearly identify Python-only coverage and test-based evaluation as scope limitations.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The benchmark grounds tasks in real GitHub issues and pull requests across multiple Python repositories.",
          "page": 1,
          "quote": "2,294 software engi-\nneering problems drawn from real GitHub issues and corresponding pull requests\nacross 12 popular Python repositories."
        },
        {
          "kind": "strength",
          "claim": "The paper reports low performance on the benchmark even with oracle retrieval, supporting its claim that these tasks challenge the tested models.",
          "page": 1,
          "quote": "Claude 2 and GPT-4 solve a mere4.8% and 1.7% of instances re-\nspectively, even when provided with an oracle retriever."
        },
        {
          "kind": "limitation",
          "claim": "The current task collection covers only Python, so generalization to other languages and domains remains unestablished.",
          "page": 9,
          "quote": "SWE-bench task instances are all in Python; we hope to ap-\nply SWE-bench’s task instance collection procedure to expand its coverage to more programming languages and domains."
        },
        {
          "kind": "limitation",
          "claim": "Execution-based tests alone do not guarantee that generated solutions are reliable.",
          "page": 9,
          "quote": "relying solely on this method is insufficient to guarantee reliable performance of\nmodel generations"
        }
      ],
      "unresolved_questions": [
        "I did not inspect the benchmark-construction procedure or detailed experimental sections; how are issue/PR pairs filtered and test relevance validated, and how robust are headline results across model configurations?",
        "How well does benchmark success correlate with expert judgments of correctness, maintainability, and usefulness in real engineering work?"
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
          1
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
          9
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
