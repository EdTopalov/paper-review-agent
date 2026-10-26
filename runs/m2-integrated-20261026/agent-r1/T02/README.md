# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**agent · ok**

4 model calls · 3 reads · 12.96 s · $0.001207

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.68

Reflexion adds a practical, training-free loop in which an LLM agent reflects on failed attempts and stores the resulting guidance in dynamic memory, using binary success feedback. The reported gains on AlfWorld and HotPotQA are promising, but evaluations are modest in scale and the approach does not improve meaningfully on WebShop, limiting the strength and breadth of the evidence.

- **strength**: The core design is simple and potentially broadly usable: reflection is stored between trials, while the reward signal is deliberately restricted to success or failure.
  - Page 4 · citation: whitespace
  - Quote: "By limiting the agent’s knowledge to a binary success status within an environment, we force the agent to make meaningful inferences about its performance without external input"

- **strength**: The AlfWorld result is substantial on the tested set and is framed as improvement through learning rather than merely retrying.
  - Page 5 · citation: whitespace
  - Quote: "the agent used ReAct to solve 97% of the given environments in 12 trials, failing to solve only 4 out of 134 tasks."

- **limitation**: The HotPotQA evaluation uses only 100 questions; reported gain over baseline is encouraging but does not establish broad generalization.
  - Page 6 · citation: exact
  - Quote: "We tested the base agent and Reﬂexion agent on a 100-question dataset."

- **limitation**: The authors report little benefit in WebShop and note that tool search quality can limit what reflection and planning can accomplish.
  - Page 10 · citation: whitespace
  - Quote: "The agent achieved a 33% → 34% accuracy improvement in the baseline run and a mere33% → 35% accuracy improvement in the Reﬂexion run"

Unresolved questions:

- How robust are the improvements across larger and more diverse task sets, model versions, and repeated runs?
- How much of the gains depends on prompt examples, trial budget, or the particular reflection heuristic?
- I inspected pages 4–6 and 9–11, not the full paper; detailed prompting, ablations, and other methodological particulars remain unassessed.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes adding reflections to working memory before resetting and trying again (PDF pp. 3–4), and explicitly constrains the agent to binary success/failure feedback (p. 4). Its discussion also presents the approach as broadly applicable, so “potentially” is appropriately qualified (pp. 7, 10).
- Observation 2: **supported** — The evaluation covers 134 AlfWorld environments, and reports solving 97% in 12 trials (PDF p. 5). The authors explicitly characterize the comparison as improved accuracy through self-improved learning rather than success by retry (p. 5).
- Observation 3: **supported** — The HotPotQA evaluation used 100 questions (PDF p. 6). The paper reports improvement over the baseline across trials, but this test size does not itself establish generalization to broader datasets; the assessment appropriately describes that as unestablished rather than as a demonstrated failure (pp. 6–7).
- Observation 4: **supported** — The paper reports only small WebShop gains after four trials and says the agent did not show helpful, intuitive reflections (PDF p. 10). It also notes that successful purchase outcomes may depend on search-engine result quality, which reflection cannot fully address (p. 10).

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: search_paper

Locate the paper’s explicit scope and limitations discussion.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "limitations",
    "reason": "Locate the paper’s explicit scope and limitations discussion."
  },
  "observation": {
    "matches": [
      {
        "page": 10,
        "snippet": " long. In those cases, Reﬂexion is needed to ensure that the query length does not exceed the maximum number of tokens while still discovering important information. 4.4 Limitations of Reﬂexion Reﬂexion relies on the emergent property of self-reﬂection that is present in several large language models. In this study, we used GPT-3.0 and GPT 3.5 to power a ReAct agent (Yao et al., 2023) to learn from its past mistakes. While Reﬂexion enabled the agent to discover new problem-solving techniques in AlfWorld decision-making tasks and HotPotQA knowledge-intensive tasks, we observed a shortc"
      },
      {
        "page": 10,
        "snippet": "e ReAct agents. In addition, we include an inconclusive attempt to improve performance on the WebShop benchmark and provide a discussion that highlights a few limitations of this approach. Reﬂexion is a highly applicable method to improve performance between trials on decision-making and knowledge-intensive tasks due to its sole dependence on a binary reward model. In the AlfWorld and HotPotQA experiments, we constrained the reward model to imitate environments in which informative reward models may be difﬁcult to design or compute. We encourage others to apply Reﬂexion to more comple"
      }
    ],
    "limit_reached": false
  }
}
```

</details>

### Step 2: read_pages

Inspect method and experimental results to assess novelty and evidential support.

[Event 10](trace.jsonl#L10)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 4,
    "end": 6,
    "reason": "Inspect method and experimental results to assess novelty and evidential support."
  },
  "observation": {
    "pages": [
      {
        "page": 4,
        "text": "pairs. Few-shot examples for AlfWorld and HotPotQA reﬂections can be found in A.1. To prevent\nthe agent from memorizing correct AlfWorld trajectories or HotPotQA answers, we do not grant\naccess to domain-speciﬁc solutions for the given problems. This approach encourages the agent to\ndevise creative and novel techniques for future attempts.\nSelf-reﬂection is modeled in the following equation:\nreflection =LLM(st,r t, [a0,o 0,...,a t,o t],mem )\nFinally, we add the reﬂection to the agent’s memory, reset the environment, and start the next trial.\n2.4 Reward model\nTypically, designing or training an … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 5,
        "text": "space in each state is not explicitly deﬁned, which allows the agent to have full expression in its next\nmoves. To avoid syntactic errors, we provide two domain-speciﬁc few-shot trajectories to the agent.\nSetup Following (Yao et al., 2023), we ran the agent in 134 AlfWorld environments across six\ndifferent tasks, including ﬁnding hidden objects (e.g., ﬁnding a spatula in a drawer), moving objects\n(e.g., moving a knife to the cutting board), and manipulating objects with other objects (e.g., chilling\na tomato in the fridge). To closely replicate baseline results, we used the same hand-selected  … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 6,
        "text": "matching between inferred answers and correct answers, but observed several cases of false positives\nand negatives that required further grading by a human, which rendered the retry process inefﬁcient\nand subjective.\nSetup To replicate results from the ReAct study (Yao et al., 2023), we prompted the agent with\nsix few-shot examples of successful trajectories. We also equipped the agent with a Wikipedia API to\nperform one of three actions at each time step: Search[entity], which returns the ﬁrst ﬁve sentences\nof the wiki page or a list of the ﬁve most similar wiki pages according to the entity; … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 3: read_pages

Read discussion, limitations, and concluding claims to calibrate scope and caveats.

[Event 15](trace.jsonl#L15)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 9,
    "end": 11,
    "reason": "Read discussion, limitations, and concluding claims to calibrate scope and caveats."
  },
  "observation": {
    "pages": [
      {
        "page": 9,
        "text": "Trial #1: Question: Grown-Ups starred the actor\nwho was best known for which role on \"’Allo\n’Allo!\"?\nThought 1: I need to search Grown-Ups and\n\"’Allo ’Allo!\", ﬁnd the actor who starred in\nGrown-Ups, then ﬁnd the role he was best known\nfor in \"’Allo ’Allo!\".\nAction 1: Search[Grown-Ups]\nObservation 1: Grown-Ups is a 1980 British\nBBC television ﬁlm devised and directed by\nMike Leigh. It stars Lesley Manville, Philip\nDavis, Brenda Blethyn, Janine Duvitski, Lindsay\nDuncan and Sam Kelly. It was edited by Robin\nSales and produced by Louis Marks for the BBC,\nand originally shown on BBC 2 on 28 Novembe … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 10,
        "text": "solved the task. Likewise, in other experiments, it is straightforward to design a binary reward model.\nFor code-writing tasks, the binary reward model can be a compilation or type-check attempt. In a\ncapture-the-ﬂag task, the possession status of the ﬂag could be the binary reward model. For other\ncases, an efﬁcient integration test could be written to assess the success status of the agent.\nAt its core, Reﬂexion is an approach designed to promote discovery for problem-solving LLM-agents\nthat may require several trials to solve given tasks, similar to the self-reﬂective learning methods\nof hu … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 11,
        "text": "Figure 6: Reﬂexion vs React performance on WebShop across 100 customer shopping requests.\n6 Reproducibility\nCode and log ﬁles for these experiments are available athttps://github.com/noahshinn024/\nreflexion.\nAcknowledgments and Disclosure of Funding\nA.G. acknowledge funding from National Science Foundation (MCB2027165) for partially supporting\nthis effort.\n11",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 4: submit_review · accepted

Evidence covers proposed binary-reward reflection method, benchmark results, and stated failure case; submit a balanced assessment while noting uninspected sections.

[Event 20](trace.jsonl#L20)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Evidence covers proposed binary-reward reflection method, benchmark results, and stated failure case; submit a balanced assessment while noting uninspected sections.",
    "review": {
      "score": 0.68,
      "summary": "Reflexion adds a practical, training-free loop in which an LLM agent reflects on failed attempts and stores the resulting guidance in dynamic memory, using binary success feedback. The reported gains on AlfWorld and HotPotQA are promising, but evaluations are modest in scale and the approach does not improve meaningfully on WebShop, limiting the strength and breadth of the evidence.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The core design is simple and potentially broadly usable: reflection is stored between trials, while the reward signal is deliberately restricted to success or failure.",
          "page": 4,
          "quote": "By limiting the agent’s knowledge to a binary success status within an environment, we force the agent to make meaningful inferences about its performance without external input"
        },
        {
          "kind": "strength",
          "claim": "The AlfWorld result is substantial on the tested set and is framed as improvement through learning rather than merely retrying.",
          "page": 5,
          "quote": "the agent used ReAct to solve 97% of the given environments in 12 trials, failing to solve only 4 out of 134 tasks."
        },
        {
          "kind": "limitation",
          "claim": "The HotPotQA evaluation uses only 100 questions; reported gain over baseline is encouraging but does not establish broad generalization.",
          "page": 6,
          "quote": "We tested the base agent and Reﬂexion agent on a 100-question dataset."
        },
        {
          "kind": "limitation",
          "claim": "The authors report little benefit in WebShop and note that tool search quality can limit what reflection and planning can accomplish.",
          "page": 10,
          "quote": "The agent achieved a 33% → 34% accuracy improvement in the baseline run and a mere33% → 35% accuracy improvement in the Reﬂexion run"
        }
      ],
      "unresolved_questions": [
        "How robust are the improvements across larger and more diverse task sets, model versions, and repeated runs?",
        "How much of the gains depends on prompt examples, trial budget, or the particular reflection heuristic?",
        "I inspected pages 4–6 and 9–11, not the full paper; detailed prompting, ablations, and other methodological particulars remain unassessed."
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
          4
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
          10
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
