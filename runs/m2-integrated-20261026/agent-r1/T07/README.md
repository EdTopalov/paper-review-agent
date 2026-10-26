# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**agent · ok**

5 model calls · 3 reads · 14.69 s · $0.001710

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.78

OSWorld makes a substantial benchmark contribution by providing a controllable real-computer environment and diverse tasks with per-task executable evaluation, enabling assessment beyond browser-only or static-demonstration settings. Careful construction and human/baseline measurements make it useful, while empirical conclusions remain bounded by its Ubuntu-centered task suite and disclosed evaluation uncertainty.

- **strength**: The benchmark’s task coverage and execution-based setup support evaluation of multi-application workflows, with substantial annotation and quality-check effort.
  - Page 7 · citation: whitespace
  - Quote: "each example is further scrutinized and iterated upon by different individuals three times from the perspective of alignment with the instruction and correctness under different solutions"

- **strength**: Human evaluation establishes a meaningful capability gap on the benchmark.
  - Page 9 · citation: whitespace
  - Quote: "the human performance on our tasks was approximately 72.36%"

- **limitation**: The paper notes residual evaluator error risk despite extensive checks, relevant to interpreting execution-based scores.
  - Page 8 · citation: whitespace
  - Quote: "Further investment of time and a more red teaming could further reduce false positives and negatives, which we will leave to future work."

- **limitation**: The primary task suite is Ubuntu-centered; Windows is supplementary in the inspected material.
  - Page 6 · citation: whitespace
  - Quote: "We introduce the OSW ORLD benchmark, which encompasses 369 real computing tasks defined and executed on Ubuntu."

Unresolved questions:

- How robust are success rates to alternative valid completion paths and evaluator edge cases across the full task suite?
- I inspected pages 1 and 6–10, but not the remaining methods, full ablations, or later discussion; what additional experimental details or limitations do those sections report?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper reports 101 multi-app workflow tasks among 369 Ubuntu tasks and describes substantial annotation effort, repeated cross-checking, and quality-control rounds (PDF pp. 6–8). The claim is appropriately scoped to the benchmark and its construction.
- Observation 2: **supported** — The human study reports 72.36% overall performance, compared with baseline agent success rates far below that level (PDF pp. 9–11). This supports a meaningful measured capability gap on this benchmark.
- Observation 3: **supported** — The authors explicitly state that further red-teaming could reduce false positives and negatives, leaving this for future work (PDF p. 8). This supports the qualified concern about residual evaluator error risk.
- Observation 4: **supported** — The paper identifies the 369-task main benchmark as defined and executed on Ubuntu and separately reports 43 Windows tasks (PDF p. 6). Calling the suite Ubuntu-centered and Windows supplementary is justified.

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: search_paper

Locate evaluation results and human-performance evidence for assessing benchmark support.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "human evaluation",
    "reason": "Locate evaluation results and human-performance evidence for assessing benchmark support."
  },
  "observation": {
    "matches": [
      {
        "page": 7,
        "snippet": "struct it and add it to the function library of the environment. After completing each evaluation, the annotator conducts initial tests with self-designed test cases. Then, in the human evaluation and experiment running phases, each example is further scrutinized and iterated upon by different individuals three times from the perspective of alignment with the instruction and correctness under different solutions. As a result, we implement nearly sample-specific executable evaluation scripts, resulting in a total of 134 unique evaluation functions for assessing functional correctness—signif"
      },
      {
        "page": 9,
        "snippet": "me (s) Ours median: 111.94s WebArena median: 35.38s WebArena Ours 30 40 50 60 70 80 90Accuracy (%) Figure 4: Human operation time and accuracy on OSW ORLD and WebArena. We conduct human evaluations on each example in our dataset, with annotators being computer science major college students who possess ba- sic software usage skills but have not been ex- posed to the samples or software before. We recorded the time required to complete each ex- ample and whether their completion of the ex- ample was correct. For comparison, we also sampled 100 examples from WebArena [62] un- der the same ev"
      }
    ],
    "limit_reached": false
  }
}
```

</details>

### Step 2: read_pages

Inspect benchmark construction, task composition, and validation procedures.

[Event 10](trace.jsonl#L10)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 6,
    "end": 7,
    "reason": "Inspect benchmark construction, task composition, and validation procedures."
  },
  "observation": {
    "pages": [
      {
        "page": 6,
        "text": "Table 2: Some examples of the mouse and keyboard ac-\ntions A in OSW ORLD . See App. A.3 for the complete\nlist.\nFunction Description\nmoveTo(x, y) Moves the mouse to the specified coordinates.click(x, y) Clicks at the specified coordinates.write(‘text’) Types the specified text at the current cursor location.press(‘enter’) Presses the Enter key.hotkey(‘ctrl’, ‘c’)Performs the Ctrl+C hotkey combination (copy).scroll(200) Scrolls up by 200 units.scroll(-200) Scrolls down by 200 units.dragTo(x, y) Drags the mouse to the specified coordinates.keyDown(‘shift’)Holds down the Shift key.keyUp(‘shift’) R … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 7,
        "text": "for open-ended task creation within OSW ORLD . Each example is carefully annotated with a natural\nlanguage instruction, a setup configuration with corresponding files and setup actions for initialization\nof initial states upon our provided VM image, and a manually crafted evaluation script to check if\nthe task is successfully executed. We also adapt 43 tasks from the Ubuntu set for analytic usage\non Windows. Overall, it takes 9 computer science students (all student authors) over 3 months,\nconsuming approximately 1800 man-hours (650 hours on single-app tasks, 750 hours on workflow\ntasks and 40 … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 3: read_pages

Inspect baseline results, benchmark human comparisons, and stated evaluation caveats.

[Event 15](trace.jsonl#L15)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 8,
    "end": 10,
    "reason": "Inspect baseline results, benchmark human comparisons, and stated evaluation caveats."
  },
  "observation": {
    "pages": [
      {
        "page": 8,
        "text": "positives and negatives, etc.), and involves joint revisions and supplements. During experiments for\nhuman performance and baselines, we further fixed examples found to have issues, dedicating over\n400 man-hours for four rounds of checks. Further investment of time and a more red teaming could\nfurther reduce false positives and negatives, which we will leave to future work.\n3.3 Data Statistics\nTable 3: Key statistics in OSW ORLD .\nThe “Supp. tasks” refers to the Windows-\nbased tasks, that could only be used after\nactivation due to copyright restrictions.\nStatistic Number\nTotal tasks (Ubuntu) 3 … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 9,
        "text": "Table 4: Comparison of different environments for benchmarking digital agents. The columns\nindicate: whether they provide a controllable executable environment (Control. Exec. Env.), the\nease of adding new tasks involving arbitrary applications in open domains (Environment Scalability),\nsupport for multimodal agent evaluation (Multimodal Support), support for and inclusion of cross-app\ntasks (Cross-App), capability to start tasks from an intermediate initial state (Intermediate Init. State),\nand the number of execution-based evaluation functions (# Exec.-based Eval. Func.).\nSize\nControl.\nExec. … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 10,
        "text": "Table 5: Success rates of baseline LLM and VLM agents on OSW ORLD , grouped by task categories:\nOS, Office (LibreOffice Calc, Impress, Writer), Daily (Chrome, VLC Player, Thunderbird), Profes-\nsional (VS Code and GIMP) and Workflow (tasks involving multiple apps), for gaining insights from\ninterfaces and operation logic. See App. C.1 and C.5 for more details.\nInputs Model Success Rate (↑)\nOS Office Daily Profess. Workflow Overall\nA11y tree Mixtral-8x7B 12.5% 1.01% 4.79% 6.12% 0.09% 2.98%\nGPT-3.5 4.17% 4.43% 2.71% 0.00% 1.62% 2.69%\nGemini-Pro 4.17% 1.71% 3.99% 4.08% 0.63% 2.37%\nGPT-4 20.83% 3.5 … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 4: submit_review · citation_validation_failed

Evidence covers benchmark design, quality checks, human comparison, and baseline results; submit a bounded assessment noting unread later analyses.

[Event 20](trace.jsonl#L20)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Evidence covers benchmark design, quality checks, human comparison, and baseline results; submit a bounded assessment noting unread later analyses.",
    "review": {
      "score": 0.78,
      "summary": "OSWorld makes a substantial benchmark contribution by providing a controllable real-computer environment and a diverse task suite with per-task executable evaluation, enabling assessment beyond browser-only or static-demonstration settings. Its careful construction and human/baseline measurements make the benchmark useful, while the initial empirical results remain bounded by the benchmark’s Ubuntu-centered task coverage and disclosed evaluation uncertainty.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The benchmark’s task coverage and execution-based setup support evaluation of multi-application real-computer workflows, with substantial annotation and quality-check effort.",
          "page": 7,
          "quote": "each example is further scrutinized and iterated upon by different individuals three times from the perspective of alignment with the instruction and correctness under different solutions"
        },
        {
          "kind": "strength",
          "claim": "Human evaluation and model baselines establish a meaningful capability gap on the benchmark, rather than relying only on task counts or design claims.",
          "page": 9,
          "quote": "the human performance on our tasks was approximately 72.36%"
        },
        {
          "kind": "limitation",
          "claim": "The paper explicitly notes residual risk of evaluator errors despite extensive checks, a relevant limitation for interpreting execution-based scores.",
          "page": 8,
          "quote": "Further investment of time and a more red teaming could further reduce false positives and negatives, which we will leave to future work."
        },
        {
          "kind": "limitation",
          "claim": "The main benchmark is centered on Ubuntu; Windows is supplementary and macOS support is described as environment capability, not a comparably sized evaluated task set in the inspected pages.",
          "page": 6,
          "quote": "We introduce the OSWORLD benchmark, which encompasses 369 real computing tasks defined and executed on Ubuntu."
        }
      ],
      "unresolved_questions": [
        "How robust are the success rates to alternative correct completion paths and evaluator edge cases across the full task suite?",
        "I inspected pages 1 and 6–10, but not the remaining methods, full ablations, or later discussion; what additional experimental details or limitations do those sections report?"
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
          8
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

### Step 5: submit_review · accepted

Correct the Ubuntu-scope quotation to the exact observed wording and resubmit the review.

[Event 25](trace.jsonl#L25)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Correct the Ubuntu-scope quotation to the exact observed wording and resubmit the review.",
    "review": {
      "score": 0.78,
      "summary": "OSWorld makes a substantial benchmark contribution by providing a controllable real-computer environment and diverse tasks with per-task executable evaluation, enabling assessment beyond browser-only or static-demonstration settings. Careful construction and human/baseline measurements make it useful, while empirical conclusions remain bounded by its Ubuntu-centered task suite and disclosed evaluation uncertainty.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The benchmark’s task coverage and execution-based setup support evaluation of multi-application workflows, with substantial annotation and quality-check effort.",
          "page": 7,
          "quote": "each example is further scrutinized and iterated upon by different individuals three times from the perspective of alignment with the instruction and correctness under different solutions"
        },
        {
          "kind": "strength",
          "claim": "Human evaluation establishes a meaningful capability gap on the benchmark.",
          "page": 9,
          "quote": "the human performance on our tasks was approximately 72.36%"
        },
        {
          "kind": "limitation",
          "claim": "The paper notes residual evaluator error risk despite extensive checks, relevant to interpreting execution-based scores.",
          "page": 8,
          "quote": "Further investment of time and a more red teaming could further reduce false positives and negatives, which we will leave to future work."
        },
        {
          "kind": "limitation",
          "claim": "The primary task suite is Ubuntu-centered; Windows is supplementary in the inspected material.",
          "page": 6,
          "quote": "We introduce the OSW ORLD benchmark, which encompasses 369 real computing tasks defined and executed on Ubuntu."
        }
      ],
      "unresolved_questions": [
        "How robust are success rates to alternative valid completion paths and evaluator edge cases across the full task suite?",
        "I inspected pages 1 and 6–10, but not the remaining methods, full ablations, or later discussion; what additional experimental details or limitations do those sections report?"
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
          8
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
