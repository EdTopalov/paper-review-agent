# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**agent · ok**

5 model calls · 4 reads · 11.27 s · $0.001595

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.78

WebArena contributes a self-hostable, dynamic web environment and 812-task benchmark for evaluating end-to-end natural-language web agents across diverse sites and tools. Its deterministic setup and programmatic completion checks make it useful for reproducible agent research; baseline performance and failure analysis illustrate the benchmark's difficulty, though the reported agents and evaluation provide only an initial view of capability.

- **strength**: The environment combines standalone reproducibility with realistic, populated applications and supports multiple observation/action modes.
  - Page 3 · citation: whitespace
  - Quote: "We achieve reproducibility by having the environment be standalone, not relying on live websites."

- **strength**: Evaluation checks intended task outcomes, including both information answers and intermediate execution state, rather than merely action prediction.
  - Page 8 · citation: exact
  - Quote: "We introduce two evaluation approaches."

- **strength**: The paper gives an empirical baseline and concrete failure analysis; the low success rate helps establish task difficulty, but is not itself evidence of agent progress.
  - Page 9 · citation: whitespace
  - Quote: "The reasoning agent powered by GPT-4 achieves a relatively modest end-to-end task success rate of 10.63%."

- **limitation**: The demonstrated agent comparison is narrow: text-only GPT-3.5/GPT-4 baselines with a 30-transition cap, so it does not establish performance across agent architectures or modalities.
  - Page 9 · citation: whitespace
  - Quote: "As part of our future research, we intend to explore the possibility of multi-modal agents that accept image-based observations and perform pixel-based actions."

Unresolved questions:

- How robust are the task annotations and outcome checks across the full benchmark, beyond the described annotation procedure?
- How do agent results change with repeated runs and alternative interaction budgets or observation modalities?
- I inspected pages 3–4 and 8–12 plus search snippets; I did not inspect the full appendix, task distribution details, or implementation/reproduction appendices, so those aspects remain uncertain.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes a standalone environment that avoids live websites and imports real-world data into functional applications (PDF pp. 3–4). It also supports multiple observation formats and different element-selection methods (PDF pp. 4–5).
- Observation 2: **supported** — Evaluation covers textual answers as well as programmatic checks of intermediate states and task outcomes (PDF pp. 7–8).
- Observation 3: **supported** — The paper reports baseline success rates and analyzes failure modes, including mistaken infeasibility judgments and observation errors (PDF pp. 9–10). The low rate supports the benchmark’s difficulty, not a claim of progress. There is a small inconsistency: Table 3 reports 10.59%, while the prose says 10.63% (PDF p. 9).
- Observation 4: **supported** — The evaluated agents are text-based GPT-3.5/GPT-4 baselines, with a 30-transition limit; the paper identifies image-based observations and pixel-based actions as future work (PDF p. 9). Thus these results do not establish performance across other architectures or modalities.

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: search_paper

Locate benchmark evaluation results to assess empirical support.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "task success",
    "reason": "Locate benchmark evaluation results to assess empirical support."
  },
  "observation": {
    "matches": [
      {
        "page": 1,
        "snippet": "rating recent techniques such as reasoning before acting. The results demonstrate that solving complex tasks is challenging: our best GPT-4-based agent only achieves an end-to-end task success rate of 10.59%. These results highlight the need for further development of robust agents, that current state-of-the-art LMs are far from perfect performance in these real-life tasks, and that WebArena can be used to measure such progress. Our code, data, environment reproduction resources, and video demonstrations are publicly available athttps://webarena.dev/. 1 Introduction Autonomous agents t"
      },
      {
        "page": 2,
        "snippet": "hion with powerful large language models (LLMs) such as GPT-3.5 and GPT-4. Experiment results show that the best GPT-4 agent performance is somewhat limited, with an end-to-end task success rate of 10.59%. We hypothesize that the limited performance of current LLMs stems from a lack of 2"
      },
      {
        "page": 9,
        "snippet": "Agent Model Success Rate Direct gpt-3.5 7.14 Reasoning gpt-3.5 7.38 Reasoning gpt-4 10.59 Table 3: The end-to-end task success rate (%) onWebArena. The direct agent directly predicts the next action given the observation, and the reasoning agent performs the reasoning on the observation, progress, and others before the action prediction. 4 Baseline Web Agents Prompts We design two LLM-prompt-based web agents as our baselines where the input observa- tions and the predicted actions are all in text: (1)Direct Agent: the ag"
      },
      {
        "page": 9,
        "snippet": "and hence warrant early termination. 5 Results 5.1 Main Results The main results are shown in Table 3. The reasoning agent powered by GPT-4 achieves a relatively modest end-to-end task success rate of 10.63%. When the same reasoning agent is powered by GPT-3.5, the success rate drops to 7.38%. Interestingly, the reasoning agent that explicitly engages in a reasoning process prior to providing the response does not exhibit a marked performance improvement when compared to its simpler counterpart that directly predicts the subsequent action without the intermediate reasoning step. The GP"
      },
      {
        "page": 10,
        "snippet": " Template Tasks derived from the same template typically share similar reasoning and planning procedures, albeit manifesting distinct executions and observations. We visualize the task success rate for templates with at least one successful completion in Figure 6. Of the 41 such templates, the GPT-4 agent manages to achieve a 100% task success rate on only one template, while GPT-3.5 agents do not achieve full task completion for any of the templates. In several cases, the agents are only able to complete one task variation among others. The discrepancy in performance arises from two r"
      },
      {
        "page": 10,
        "snippet": "rvations. We visualize the task success rate for templates with at least one successful completion in Figure 6. Of the 41 such templates, the GPT-4 agent manages to achieve a 100% task success rate on only one template, while GPT-3.5 agents do not achieve full task completion for any of the templates. In several cases, the agents are only able to complete one task variation among others. The discrepancy in performance arises from two reasons. First, the complexity of tasks can vary, even within the same template. For instance, the agent is able to correctly perform “F ork metaseq” whil"
      },
      {
        "page": 12,
        "snippet": "r tasks have been completed according to the desired objectives. When tested with the state-of-the-art GPT-4 language model, the best-performing agent achieved a modest end-to-end task success rate of 10.59Our error analysis suggests that while the agent could steer the interactions toward the task completion, there are several areas for improvement. Common errors include an overestimation of task infeasibility and an over-reliance on readily available context at the expense of necessary exploration. Additionally, the agent often fails to distinguish nuances in observations, leading to"
      }
    ],
    "limit_reached": false
  }
}
```

</details>

### Step 2: read_pages

Inspect task construction and environment design claims.

[Event 10](trace.jsonl#L10)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 3,
    "end": 4,
    "reason": "Inspect task construction and environment design claims."
  },
  "observation": {
    "pages": [
      {
        "page": 3,
        "text": "Search for museums  \nin Pittsburgh\nwebarena.wikipedia.com\nSearch for each art \nmuseum on the Map\nwebarena.openstreetmap.com\nRecord the optimized \nresults to the repo\nwebarena.gitlab.com\n…\nCreate an efficient itinerary to visit all Pittsburgh's art museums with minimal driving distance starting \nfrom CMU. Log the order in my “awesome-northeast-us-travel” repository\n“\n”\nFigure 2: A high-level task that can be fully executed inWebArena. Completing such tasks requires\nsophisticated, long-term planning and reasoning capability. To accomplish the goal stated at the\ntop, an agent needs to find out wh … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 4,
        "text": "<li> \n  <div> \n     <a href=\"...\"><img src=\"...\"></a> \n     <div class> \n        <a href=\"...\">Outdoor Patio …\n</a> \n        <div> \n              <span>Rating:</span> \n              <div> \n                 <span>82%</span> \n              </div> \n              <a href=“…#reviews\">12 \n<span>Reviews</span></a> \nwebarena.onestopshop.com\nwebarena.onestopshop.com\n[4] RootWebArea ‘Patio, Lawn ..’ \n  [1543] link 'Image' \n     [1547] img 'Image' \n  [1552] link 'Outdoor Patio..’ \n  [1549] LayoutTable '' \n      [1559] StaticText 'Rating:' \n      [1557] generic '82%' \n      [1567] link '12 Reviews' \n  [15 … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 3: read_pages

Read benchmark protocol, baseline results, and reported evaluation scope.

[Event 15](trace.jsonl#L15)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 8,
    "end": 10,
    "reason": "Read benchmark protocol, baseline results, and reported evaluation scope."
  },
  "observation": {
    "pages": [
      {
        "page": 8,
        "text": "Function ID Intent Eval Implementation\nrinfo(a∗, ˆa)\n1 Tell me the name of the customer who\nhas the most cancellations in the historyexact_match(ˆa, “Samantha Jones”)\n2 Find the customer name and\nemail with phone number 8015551212\nmust_include(ˆa, “Sean Miller”)\nmust_include(ˆa, “sean@gmail.com”)\n3 Compare walking and driving time\nfrom AMC Waterfront to Randyland\nfuzzy_match(ˆa, “Walking: 2h58min”)\nfuzzy_match(ˆa, “Driving: 21min”)\nrprog(s)\n4 Checkout merge requests\nassigned to me\nurl = locate_last_url(s)\nexact_match(URL, “gitlab.com/merge_\nrequests?assignee_username”\n=byteblaze”\n5 Post to ask … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 9,
        "text": "Agent Model Success Rate\nDirect gpt-3.5 7.14\nReasoning gpt-3.5 7.38\nReasoning gpt-4 10.59\nTable 3: The end-to-end task success rate (%) onWebArena. The direct agent directly predicts the\nnext action given the observation, and the reasoning agent performs the reasoning on the observation,\nprogress, and others before the action prediction.\n4 Baseline Web Agents\nPrompts We design two LLM-prompt-based web agents as our baselines where the input observa-\ntions and the predicted actions are all in text: (1)Direct Agent: the agent takes as input the observation\nand directly predict the next action. ( … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 10,
        "text": "0.2 0.4 0.6 0.8 1.0\nT ask Success Rate within a T emplate\n0\n5\n10\n15\n20\n25# T emplates\ngpt-3.5 direct\ngpt-3.5 reasoning\ngpt-4 reasoning\nFigure 6: Distribution of success rate\nwithin a template on templates with at\nleast one successful execution\n[2430] searchbox 'Search query' \n    [5172] StaticText 'DMV area'\n[2361] link 'Projects 0' \n[2365] link 'Users 1' \n[2070] heading \" We couldn't \nfind any projects matching \nFacebook\"\nFigure 7: Two examples where the GPT-4 agent failed,\nalong with their screenshot and the accessibility tree of\nthe relevant sections (grey). On the left, the agent fails\nto  … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 4: read_pages

Inspect discussion and explicit limitations to qualify benchmark conclusions.

[Event 20](trace.jsonl#L20)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 11,
    "end": 12,
    "reason": "Inspect discussion and explicit limitations to qualify benchmark conclusions."
  },
  "observation": {
    "pages": [
      {
        "page": 11,
        "text": "Benchmark Dynamic\nInteraction?\nRealistic\nEnvironment?\nDiverse\nHuman Tasks?\nFunctional\nCorrectness?\nMind2Web [7] ✗ ✓ ✓ ✗\nForm/QAWoB [27] ✗ ✓ ✓ ✗\nMiniWoB++ [21] ✓ ✗ ✗ ✓\nWebshop [37] ✓ ✗ ✗ ✓\nALFRED [29] ✓ ✗ ✗ ✓\nVirtualHome [25] ✗ ✗ ✓ ✗\nAndroidEnv [31] ✓ ✓ ✗ ✗\nWebArena ✓ ✓ ✓ ✓\nTable 4: The comparison between our benchmark and existing benchmarks on grounding natural\nlanguage instructions to concrete executions. Our benchmark is implemented in our fully interactable\nhighly-realistic environment. It features diverse tasks humans may encounter in their daily routines.\nWe design evaluation metrics to  … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 12,
        "text": "as well as the capacity to reconsider previous decisions. Moreover, it is crucial for LLMs to\ninclude built-in failure recovery and self-correction mechanisms to increase their robustness [28, 14].\nHowever, while these approaches have shown promise, their applications have largely been tested in\nrelatively simple settings. For instance, in environments where an erroneous action can be reversed\nby a singleundo command. However, actions in complex environments such asWebArena may not\nbe easily reversible. For example, canceling an incorrectly placed order requires navigating through a\nseries of  … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 5: submit_review · accepted

Evidence covers environment construction, task evaluation, baseline results, and discussion; submit with limits of inspected pages noted.

[Event 25](trace.jsonl#L25)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Evidence covers environment construction, task evaluation, baseline results, and discussion; submit with limits of inspected pages noted.",
    "review": {
      "score": 0.78,
      "summary": "WebArena contributes a self-hostable, dynamic web environment and 812-task benchmark for evaluating end-to-end natural-language web agents across diverse sites and tools. Its deterministic setup and programmatic completion checks make it useful for reproducible agent research; baseline performance and failure analysis illustrate the benchmark's difficulty, though the reported agents and evaluation provide only an initial view of capability.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The environment combines standalone reproducibility with realistic, populated applications and supports multiple observation/action modes.",
          "page": 3,
          "quote": "We achieve reproducibility by having the environment be standalone, not relying on live websites."
        },
        {
          "kind": "strength",
          "claim": "Evaluation checks intended task outcomes, including both information answers and intermediate execution state, rather than merely action prediction.",
          "page": 8,
          "quote": "We introduce two evaluation approaches."
        },
        {
          "kind": "strength",
          "claim": "The paper gives an empirical baseline and concrete failure analysis; the low success rate helps establish task difficulty, but is not itself evidence of agent progress.",
          "page": 9,
          "quote": "The reasoning agent powered by GPT-4 achieves a relatively modest end-to-end task success rate of 10.63%."
        },
        {
          "kind": "limitation",
          "claim": "The demonstrated agent comparison is narrow: text-only GPT-3.5/GPT-4 baselines with a 30-transition cap, so it does not establish performance across agent architectures or modalities.",
          "page": 9,
          "quote": "As part of our future research, we intend to explore the possibility of multi-modal agents that accept image-based observations and perform pixel-based actions."
        }
      ],
      "unresolved_questions": [
        "How robust are the task annotations and outcome checks across the full benchmark, beyond the described annotation procedure?",
        "How do agent results change with repeated runs and alternative interaction budgets or observation modalities?",
        "I inspected pages 3–4 and 8–12 plus search snippets; I did not inspect the full appendix, task distribution details, or implementation/reproduction appendices, so those aspects remain uncertain."
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
          9
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
