# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**agent · ok**

8 model calls · 4 reads · 27.54 s · $0.002865

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.78

τ-bench contributes a modular benchmark for tool agents in simulated multi-turn user interactions under domain policies, using database-state goals and pass^k to measure repeatability. Experiments across multiple models reveal substantial weaknesses in the tested setting. The evidence is useful, but simplified customer-service domains and simulated users limit real-world generalization.

- **strength**: The benchmark provides objective end-state assessment alongside user interaction and tool use.
  - Page 2 · citation: whitespace
  - Quote: "Our evaluation scheme compares the database state at the end of each episode with the ground truth expected state."

- **strength**: Repeated-trial evaluation reveals that reliability falls substantially even for the best-performing tested model.
  - Page 7 · citation: whitespace
  - Quote: "pass^8 drops to < 25%."

- **strength**: The ablation directly removes policy context to test its contribution.
  - Page 8 · citation: whitespace
  - Quote: "we perform an ablation study by remov- ing the domain policy from the FC agent system prompt."

- **limitation**: The benchmark intentionally simplifies its domains relative to real-world settings, limiting external validity.
  - Page 6 · citation: whitespace
  - Quote: "Each τ-bench domain’s data schemas, APIs, and rules are simplified compared to real-world domains"

Unresolved questions:

- How well do simulated users and database-state success correspond to real-user satisfaction and expert judgments?
- Do results generalize to domains beyond retail and airline, and to newer models and agent designs?
- I inspected pages 1–8 only; later discussion, appendices, and detailed task-level evidence remain unreviewed.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The benchmark evaluates tool-mediated conversations with a simulated user and compares the final database state with a ground-truth outcome; the reward also checks required information in user-facing responses (pp. 2, 4).
- Observation 2: **supported** — The paper reports that for the best-performing tested model, gpt-4o, pass^8 in retail drops below 25% (p. 7).
- Observation 3: **supported** — The authors explicitly remove the domain policy from the function-calling agent’s system prompt and report the resulting pass^1 changes (p. 8).
- Observation 4: **supported** — The paper states that the domains’ schemas, APIs, and rules are simplified relative to real-world domains, and presents this as a benchmark characteristic relevant to generalization (p. 6).

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: search_paper

Inspect the benchmark’s reliability metric and experimental evidence.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "pass^k",
    "reason": "Inspect the benchmark’s reliability metric and experimental evidence."
  },
  "observation": {
    "matches": [
      {
        "page": 1,
        "snippet": ". We employ an efficient and faithful evaluation process that compares the database state at the end of a conversation with the annotated goal state. We also propose a new metric (pass^k) to evaluate the reliability of agent behavior over multiple trials. Our experiments show that even state-of-the-art function calling agents (like gpt-4o) succeed on < 50% of the tasks, and are quite inconsistent (pass^8 < 25% in retail). Our findings point to the need for methods that can improve the ability of agents to act consistently and follow rules reliably. 1 Introduction There is increas"
      },
      {
        "page": 2,
        "snippet": "variation in the conversation itself, since the user may pose the same request in different ways that result in the same end state of the database. We also introduce the metric of pass^k, which measures the consistency and robustness of the agent across k i.i.d. trials. Our experiments reveal that agents built with simple LM constructs (like function calling or ReAct) perform poorly, highlighting the need for more sophisticated agent architectures. For instance, even state-of-the-art LMs like gpt-4o achieve low task success rates (pass^1) using function calling (∼61% on τ-retail "
      },
      {
        "page": 4,
        "snippet": "he policy. Nevertheless, our proposed rule-based reward is fast to compute and faithful, and already poses significant challenges for current models and methods as we show in § 5. Pass^k metric. For tasks like code generation with good verification techniques (unit tests), the community has defined the pass@k (pass at k) metric as the chance that at least one out ofk i.i.d. task trials is successful, which captures the trend of agents enabling discovery of solutions with scaling of inference-time compute [5]. For real-world agent tasks requiring reliability and consistency like c"
      },
      {
        "page": 4,
        "snippet": "iscovery of solutions with scaling of inference-time compute [5]. For real-world agent tasks requiring reliability and consistency like customer service, we propose a new metric – pass^k (pass hat k), defined as the chance that all k i.i.d. task trials are successful, averaged across tasks. Therefore, if a task is run for n trials and c of 4"
      },
      {
        "page": 5,
        "snippet": "PI tools 7 write, 8 non-write 6 write, 7 non-write Tasks 115 50 Table 1: Key statistics from τ-retail and τ-airline. those trials end up successful (r = 1), unbiased estimates for pass^k and pass@k would be: pass^k = Etask \u0014\u0012c k \u0013 \u0012n k \u0013\u0015 , pass@k = 1 − Etask \u0014\u0012n − c k \u0013 \u0012n k \u0013\u0015 . In our case, for the same task, the user prompt and database transitions are the same, with just the LM sampling of the user and agent messages generating sufficient stochasticity. Thus, pass^k can capture the reliability of the agent at handling variations in conversations with the same underlying sema"
      },
      {
        "page": 5,
        "snippet": "e 6 write, 7 non-write Tasks 115 50 Table 1: Key statistics from τ-retail and τ-airline. those trials end up successful (r = 1), unbiased estimates for pass^k and pass@k would be: pass^k = Etask \u0014\u0012c k \u0013 \u0012n k \u0013\u0015 , pass@k = 1 − Etask \u0014\u0012n − c k \u0013 \u0012n k \u0013\u0015 . In our case, for the same task, the user prompt and database transitions are the same, with just the LM sampling of the user and agent messages generating sufficient stochasticity. Thus, pass^k can capture the reliability of the agent at handling variations in conversations with the same underlying semantics while adhering to the "
      },
      {
        "page": 5,
        "snippet": "case, for the same task, the user prompt and database transitions are the same, with just the LM sampling of the user and agent messages generating sufficient stochasticity. Thus, pass^k can capture the reliability of the agent at handling variations in conversations with the same underlying semantics while adhering to the domain policies and rules. By default, we report the average reward across tasks, pass^1=pass@1=E[r] = E[c/n], as the main metric for comparing agents. 4 Benchmark Construction τ-bench defines domain-agnostic environment and user simulation classes shared by va"
      },
      {
        "page": 6,
        "snippet": "ometimes creative tasks (see § A, § C.2, § D.2). Importantly, we trade off quantity for quality — as § 5 shows, running a small set of high-quality tasks for multiple trials (with pass^k metric) can reliably reveal rich insights into different models, methods, and research challenges. Faithful rule-based evaluation. Real-world agents are hard to evaluate as the trajectory can be extremely diverse for the same task, and success criteria are multi-faceted. As a result, it often requires human evaluation, e.g., end users to judge task resolution and domain experts to judge rule foll"
      }
    ],
    "limit_reached": true
  }
}
```

</details>

### Step 2: read_pages

Read the benchmark’s design and stated scope beyond the abstract.

[Event 10](trace.jsonl#L10)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 2,
    "end": 3,
    "reason": "Read the benchmark’s design and stated scope beyond the abstract."
  },
  "observation": {
    "pages": [
      {
        "page": 2,
        "text": "You are mia_li_2017, and want to change the your \nmost recent reservation to fly to SF instead of LA on \nthe same day. If change is not possible, you want the \nagent to cancel and rebook … You are concise.\nUser instruction as system prompt\nUser\nCurrent time is 2024-5-15 15:00:00 EST. \n-Basic economy cannot be modified. \n-Basic economy cannot be cancelled after 24 hours \nof booking… (more rules omitted)Agent\nDomain policy as system prompt\nTools\nget_user_details book_reservation\ncancel_reservation update_reservation_flights\n……\n(a) τ-bench setup (b) Example trajectory in τ-airline\nChange flight\ng … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 3,
        "text": "ToolBench [22] and MetaTool [11] test tool use/function calling in multiple programming languages\nand propose various methods for evaluating the accuracy of function calls. ToolEmu [ 16] uses\nlanguage models themselves to emulate the execution of tools, with a focus on exposing potential\nsafety risks when LM agents fail to use tools correctly. However, all these works only contain a\nsingle-step user interaction, where the human interacting with the agent provides an initial instruction\ncontaining all the required information. In contrast, our benchmark focuses on a more realistic setting\nwhere … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 3: read_pages

Check benchmark size, construction choices, and evaluation caveats.

[Event 15](trace.jsonl#L15)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 5,
    "end": 6,
    "reason": "Check benchmark size, construction choices, and evaluation caveats."
  },
  "observation": {
    "pages": [
      {
        "page": 5,
        "text": "τ -retail τ -airline\nDatabases 500 users, 50 products, 1,000 orders 500 users, 300 flights, 2,000 reservations\nAPI tools 7 write, 8 non-write 6 write, 7 non-write\nTasks 115 50\nTable 1: Key statistics from τ-retail and τ-airline.\nthose trials end up successful (r = 1), unbiased estimates for pass^k and pass@k would be:\npass^k = Etask\n\u0014\u0012c\nk\n\u0013\u001e\u0012n\nk\n\u0013\u0015\n, pass@k = 1 − Etask\n\u0014\u0012n − c\nk\n\u0013\u001e\u0012n\nk\n\u0013\u0015\n.\nIn our case, for the same task, the user prompt and database transitions are the same, with just the\nLM sampling of the user and agent messages generating sufficient stochasticity. Thus, pass^k can\ncapture  … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 6,
        "text": "type. These constraints simplify task and API design, and challenge agents to follow domain-specific\nrules, and inform and collect complete information from users before taking actions.\nτ -airline. Here, the agent has to help users book, modify, or cancel flight reservations, or provide\nrefunds. We construct 300 flights between 20 US cities with realistic durations and prices, and\nAPI tools to query direct or one-stop flights. The domain policy is more complex than τ-retail,\nwith ad-hoc constraints about combining payment methods, checked bag allowance, flight changes\nand cancellations, etc. T … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 4: read_pages

Inspect reported results and whether evaluation reliability is characterized.

[Event 20](trace.jsonl#L20)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 7,
    "end": 8,
    "reason": "Inspect reported results and whether evaluation reliability is characterized."
  },
  "observation": {
    "pages": [
      {
        "page": 7,
        "text": "Model retail airline avg\ngpt-4o 61.2 35.2 48.2\ngpt-4-turbo 57.7 32.4 45.1\ngpt-4-32k 56.5 33.0 44.8\ngpt-3.5-turbo 20.0 10.8 15.4\nclaude-3-opus 44.2 34.7 39.5\nclaude-3-sonnet 26.3 27.6 27.0\nclaude-3-haiku 19.0 14.4 16.7\ngemini-1.5-pro 21.7 14.0 17.9\ngemini-1.5-flash 17.4 26.0 21.7\nmistral-large 30.7 22.4 26.6\nmixtral-8x22b 17.7 31.6 24.7\nmeta-llama-3-70B 14.8 14.4 14.6\nTable 2: Pass^1 across models via function call-\ning, except Llama-3 via text-ReAct. Average is\nweighted by domains, not by tasks.\ngpt-4o gpt-4-turbo gpt-4-32k gpt-3.5-turbo\n0\n20\n40\n60 FC\nReAct\nAct\nFigure 3: pass^1 across models/m … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 8,
        "text": "wants to exchange a lamp for a less bright one and prefers\nan AC adapter over battery or USB power source. The agent fails to reason over the complex inventory\nof lamps and find the unique option given such a preference. Weaker models and methods struggle\nwith even more basic failures such as hallucinating arguments — for example, while gpt-4o FC\nagent only makes 0.46 tool calls with non-existent user/product/order/item IDs per τ-retail task,\ngpt-3.5-turbo FC / Act agents make 2.08 / 6.34, respectively.\nFor “wrong info”, agents omit user-required information (e.g., the user asks for a tracking … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 5: submit_review · citation_validation_failed

Submit an evidence-grounded assessment based on the abstract and inspected benchmark, methods, and results pages.

[Event 25](trace.jsonl#L25)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Submit an evidence-grounded assessment based on the abstract and inspected benchmark, methods, and results pages.",
    "review": {
      "score": 0.78,
      "summary": "τ-bench contributes a modular benchmark for evaluating tool-using agents in simulated multi-turn user interactions under domain policies, with database-state goal evaluation and pass^k for repeatability. Its two domains and broad model comparisons expose substantial gaps in current agents; the evidence is meaningful for this benchmark setting, while its simplified customer-service domains and LM-simulated users constrain real-world generalization.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The benchmark combines user interaction, API tools, policy adherence, and objective end-state evaluation, with manually validated task construction.",
          "page": 2,
          "quote": "Our evaluation scheme compares the database state at the end of each episode with the ground truth expected state."
        },
        {
          "kind": "strength",
          "claim": "pass^k makes consistency across repeated stochastic interactions explicit; reported results reveal sharp reliability decline.",
          "page": 7,
          "quote": "pass^8 drops to < 25%."
        },
        {
          "kind": "strength",
          "claim": "The experiments cover multiple proprietary and open models, and provide failure analysis and a policy-removal ablation rather than only aggregate scores.",
          "page": 8,
          "quote": "removing the domain policy from the FC agent system prompt."
        },
        {
          "kind": "limitation",
          "claim": "The benchmark’s initial domain coverage is deliberately narrow and simplified, so claims about deployment in real-world domains remain an extrapolation.",
          "page": 6,
          "quote": "Each τ-bench domain’s data schemas, APIs, and rules are simplified compared to real-world domains"
        }
      ],
      "unresolved_questions": [
        "How well do the simulated users and database-state success criteria track real-user satisfaction and expert judgments in deployment?",
        "Do findings generalize to domains beyond retail and airline, or to agents and models developed after the reported experiments?",
        "I inspected pages 1–8 only; later discussion, appendices, and detailed task-level evidence were not reviewed."
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
        "candidate_pages": [
          8
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
          6
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

### Step 6: submit_review · citation_validation_failed

Correct the failed quote using an exact verbatim passage from inspected page 8 and resubmit.

[Event 30](trace.jsonl#L30)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Correct the failed quote using an exact verbatim passage from inspected page 8 and resubmit.",
    "review": {
      "score": 0.78,
      "summary": "τ-bench contributes a modular benchmark for evaluating tool-using agents in simulated multi-turn user interactions under domain policies, with database-state goal evaluation and pass^k for repeatability. Its two domains and broad model comparisons expose substantial gaps in current agents; evidence is meaningful for this benchmark setting, while simplified customer-service domains and LM-simulated users constrain real-world generalization.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The benchmark combines user interaction, API tools, policy adherence, and objective end-state evaluation, with manually validated task construction.",
          "page": 2,
          "quote": "Our evaluation scheme compares the database state at the end of each episode with the ground truth expected state."
        },
        {
          "kind": "strength",
          "claim": "pass^k makes consistency across repeated stochastic interactions explicit; reported results reveal sharp reliability decline.",
          "page": 7,
          "quote": "pass^8 drops to < 25%."
        },
        {
          "kind": "strength",
          "claim": "The experiments include a policy-removal ablation, showing that policy information affects results differently across domains and models.",
          "page": 8,
          "quote": "removing the domain policy from the FC agent system prompt."
        },
        {
          "kind": "limitation",
          "claim": "The benchmark’s initial domain coverage is deliberately narrow and simplified, so claims about deployment in real-world domains remain an extrapolation.",
          "page": 6,
          "quote": "Each τ-bench domain’s data schemas, APIs, and rules are simplified compared to real-world domains"
        }
      ],
      "unresolved_questions": [
        "How well do the simulated users and database-state success criteria track real-user satisfaction and expert judgments in deployment?",
        "Do findings generalize to domains beyond retail and airline, or to agents and models developed after the reported experiments?",
        "I inspected pages 1–8 only; later discussion, appendices, and detailed task-level evidence were not reviewed."
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
        "candidate_pages": [
          8
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
          6
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

### Step 7: submit_review · citation_validation_failed

Use an unambiguous exact citation from the inspected page 8 and finalize the assessment.

[Event 35](trace.jsonl#L35)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Use an unambiguous exact citation from the inspected page 8 and finalize the assessment.",
    "review": {
      "score": 0.78,
      "summary": "τ-bench contributes a modular benchmark for tool agents in simulated multi-turn user interactions under domain policies, using database-state goals and pass^k to measure repeatability. Experiments across multiple models reveal substantial weaknesses in the tested setting. The evidence is useful, but simplified customer-service domains and simulated users limit real-world generalization.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The benchmark provides objective end-state assessment alongside user interaction and tool use.",
          "page": 2,
          "quote": "compares the database state at the end of each episode with the ground truth expected state."
        },
        {
          "kind": "strength",
          "claim": "Repeated-trial evaluation reveals that reliability falls substantially even for the best-performing tested model.",
          "page": 7,
          "quote": "pass^8 drops to < 25%."
        },
        {
          "kind": "strength",
          "claim": "The policy-removal ablation shows measurable effects of policy context, especially in airline tasks.",
          "page": 8,
          "quote": "removing the domain policy from the FC agent system prompt."
        },
        {
          "kind": "limitation",
          "claim": "The benchmark intentionally simplifies its domains relative to real-world settings, limiting external validity.",
          "page": 6,
          "quote": "rules are simplified compared to real-world domains"
        }
      ],
      "unresolved_questions": [
        "How well do simulated users and database-state success correspond to real-user satisfaction and expert judgments?",
        "Do results generalize to domains beyond retail and airline, and to newer models and agent designs?",
        "I inspected pages 1–8 only; later discussion, appendices, and detailed task-level evidence remain unreviewed."
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
        "candidate_pages": [
          8
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
          6
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

### Step 8: submit_review · accepted

Finalize with observations supported by exact unambiguous quotes from inspected pages.

[Event 40](trace.jsonl#L40)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Finalize with observations supported by exact unambiguous quotes from inspected pages.",
    "review": {
      "score": 0.78,
      "summary": "τ-bench contributes a modular benchmark for tool agents in simulated multi-turn user interactions under domain policies, using database-state goals and pass^k to measure repeatability. Experiments across multiple models reveal substantial weaknesses in the tested setting. The evidence is useful, but simplified customer-service domains and simulated users limit real-world generalization.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The benchmark provides objective end-state assessment alongside user interaction and tool use.",
          "page": 2,
          "quote": "Our evaluation scheme compares the database state at the end of each episode with the ground truth expected state."
        },
        {
          "kind": "strength",
          "claim": "Repeated-trial evaluation reveals that reliability falls substantially even for the best-performing tested model.",
          "page": 7,
          "quote": "pass^8 drops to < 25%."
        },
        {
          "kind": "strength",
          "claim": "The ablation directly removes policy context to test its contribution.",
          "page": 8,
          "quote": "we perform an ablation study by remov- ing the domain policy from the FC agent system prompt."
        },
        {
          "kind": "limitation",
          "claim": "The benchmark intentionally simplifies its domains relative to real-world settings, limiting external validity.",
          "page": 6,
          "quote": "Each τ-bench domain’s data schemas, APIs, and rules are simplified compared to real-world domains"
        }
      ],
      "unresolved_questions": [
        "How well do simulated users and database-state success correspond to real-user satisfaction and expert judgments?",
        "Do results generalize to domains beyond retail and airline, and to newer models and agent designs?",
        "I inspected pages 1–8 only; later discussion, appendices, and detailed task-level evidence remain unreviewed."
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
