# T19: A Survey on Large Language Model based Autonomous Agents

**agent · ok**

6 model calls · 4 reads · 16.47 s · $0.001970

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.69

This survey organizes the emerging LLM-based autonomous-agent literature around construction, applications, and evaluation, and proposes a four-module framework spanning profile, memory, planning, and action. Its value is primarily structured synthesis and agenda-setting rather than new empirical validation; its broad coverage is useful, while taxonomy coverage and the surveyed literature's early-stage evaluation remain relevant constraints.

- **strength**: The four-part framework offers a compact organizing structure and connects modular architecture to much of the prior work.
  - Page 2 · citation: whitespace
  - Quote: "By disabling one or more modules, the majority of previous studies can be viewed as specific examples of this framework."

- **strength**: The survey treats evaluation as a distinct topic and summarizes multiple complementary approaches.
  - Page 21 · citation: exact
  - Quote: "objective evaluation provides crucial insights complementing human assessment."

- **limitation**: The authors explicitly characterize the field as early-stage and identify substantial unresolved problems, limiting how conclusive the survey's synthesized picture can be.
  - Page 22 · citation: exact
  - Quote: "this field is still at its initial stage, and many challenges exist on its development road."

- **uncertainty**: The article acknowledges that existing objective evaluation approaches do not measure general capabilities fully; how to reconcile and validate measures across domains remains unresolved in the inspected material.
  - Page 21 · citation: whitespace
  - Quote: "While current techniques have limitations in measuring general capabilities, objective evaluation provides crucial insights complementing human assessment."

Unresolved questions:

- How comprehensive and reproducible was the literature-selection process, and what criteria determined which studies entered the survey?
- How well does the proposed framework classify agent designs that combine or blur the module boundaries?
- I inspected the introduction/framework, evaluation pages, and challenges/conclusion area, not the survey's full application sections or all cited studies; do those sections reveal coverage gaps or stronger comparative analysis?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper defines four modules—profile, memory, planning, and action—and says that disabling modules lets the majority of prior studies be viewed within the framework (PDF pp. 2–3). This supports the claim that it is a compact organizing structure connected to much prior work.
- Observation 2: **supported** — Evaluation is treated in a dedicated section, distinguishing subjective and objective evaluation and discussing multiple methods, metrics, strategies, and benchmarks (PDF pp. 19–21). The cited statement also explicitly presents objective evaluation as complementary to human assessment (PDF p. 21).
- Observation 3: **supported** — The authors explicitly call the field “still at its initial stage” and state that many challenges remain, then discuss those challenges in detail (PDF pp. 22–23).
- Observation 4: **overstated** — The paper says current techniques have limitations in measuring general capabilities and calls for continued progress in evaluation methodology (PDF p. 21), supporting the general concern. But it does not specifically establish that measures across domains need to be reconciled or validated; that part is a plausible open question rather than a demonstrated unresolved defect.

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: search_paper

Locate the survey's framework discussion to assess its synthesis contribution.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "unified framework",
    "reason": "Locate the survey's framework discussion to assess its synthesis contribution."
  },
  "observation": {
    "matches": [
      {
        "page": 1,
        "snippet": " systematic review of the field of autonomous agents from a holistic perspective. More specifically, our focus lies in the construction of LLM-based agents, for which we propose a unified framework that encompasses a majority of the previous work. Additionally, we provide a summary of the various applications of LLM-based AI agents in the domains of social science, natural science, and engineering. Lastly, we discuss the commonly employed evaluation strategies for LLM-based AI agents. Based on the previous studies, we also present several challenges and future directions in this field. To k"
      },
      {
        "page": 2,
        "snippet": "lly, we organize our survey based on three aspects including the construction, application, and evaluation of LLM-based autonomous agents. For the agent construction, we present a unified framework composed of four components, that is, a profile module to represent agent attributes, a memory module to store historical information, a planning module to strategize future actions, and an action module to execute the planned decisions. By disabling one or more modules, the majority of previous studies can be viewed as specific examples of this framework. After introducing the typical agent modu"
      },
      {
        "page": 3,
        "snippet": "of the architecture. Within the context of architectural design, we contribute a systematic synthesis of existing research, culminating in a comprehensive unified framework. As for the second aspect, we summarize three commonly employed strategies including (1) learning from examples, where the model is fine-tuned based on curated datasets, (2) learning from environment feedback, leveraging real-time interactions and observations, and (3) learning from human feedback, capitalizing on human expertise and intervention for refinement. 2.1 Agent Architecture Design Rece"
      },
      {
        "page": 3,
        "snippet": ". To bridge this gap, previous work has developed a number of modules to inspire and enhance the capabilities of LLMs for building autonomous agents. In this section, we propose a unified framework to summarize the architectures proposed in the previous work*. In specific, the overall structure of our framework is illustrated Figure 2, which is composed of a profiling module, a memory module, a planning module, and an action module. The purpose of the profiling module is to identify the role of the agent. The memory and planning modules place the agent into a dynamic environment, enabling i"
      },
      {
        "page": 4,
        "snippet": "hTools ØDatabase ØLists Øwithout Tools ØExploration Ørecollection Øinteraction ØEnvironments ØInternal States ActionSpace ØFeedback ØExternal Tools ØNew Actions ØHuman Figure 2: A unified framework for the architecture design of LLM-based autonomous AI agent. information, which indicates the personalities of the agents, and social information, which describes the relationships between agents. The choice of information to profile the agent is largely determined by the specific application scenarios. For instance, if the study focuses on user social behaviors, social profile information becom"
      }
    ],
    "limit_reached": false
  }
}
```

</details>

### Step 2: read_pages

Read the survey's stated scope and framework details, with page numbers for evidence.

[Event 10](trace.jsonl#L10)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 2,
    "end": 4,
    "reason": "Read the survey's stated scope and framework details, with page numbers for evidence."
  },
  "observation": {
    "pages": [
      {
        "page": 2,
        "text": "2021-1 2022-1 2023-2 2023-4 2023-6 2023-8\nTime（Year-Month）\nNumberofPapers（cumulated）\nSayCan \n2022-4\nWebGPT\n2021-12\nAtlas\n2022-8\nReact\n2022-10\nDECKARD2023-1\nToolformer\n2023-2\nAutoGPT\n2023-3\nHuggingGPT\n2023-3\nBMTools\n2023-3\nGenerative Agent\n2023-4\nBabyGPT\n2023-4\nAgentGPT\n2023-4\nSuperAGI\n2023-5\nGITM\n2023-5\nVoyager 2023-5\nRecAgent 2023-6\nCO-LLM\n2023-7\nChatDev 2023-7\nToolBehch\n2023-7\nMetaGPT\n2023-8\nAgentSims 2023-8\nXlang 2023-8\nTool Agent\nSimulation Agent\nGeneral Agent\nDomain Agent\nCAMEL\n2023-3\nTALM\n2022-5\nFigure 1: Illustration of the growth trend on the field of LLM-based autonomous agents.\nIn re … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 3,
        "text": "of the architecture. Within the context of architectural design, we contribute a systematic synthesis of\nexisting research, culminating in a comprehensive unified framework. As for the second aspect, we\nsummarize three commonly employed strategies including (1) learning from examples, where the\nmodel is fine-tuned based on curated datasets, (2) learning from environment feedback, leveraging\nreal-time interactions and observations, and (3) learning from human feedback, capitalizing on human\nexpertise and intervention for refinement.\n2.1 Agent Architecture Design\nRecent advancements in Language  … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 4,
        "text": "ØDemographicInformation\nØPersonalityInformation\nØSocialInformation\nØHandcraftingMethod\nØGPT-GeneratedMethod\nØDatasetAlignmentMethod\nProfile ActionMemory Planning\nØDialogue\nØTask Completion\nØMemory Read\nØMemory Write\nØMemory Reflection\nØLong-term Memory\nØShort-term Memory\nØLanguages\nØEmbeddings \nØEnvironmentFeedback\nØHuman Feedback\nØModel Feedback\nØSubgoal Decomposition\nØMulti-path Thought\nØExternal Planner\nGenerationStrategy\nProfileContents\nMemoryOperation\nMemoryStructure\nMemoryFormats\nPlanningw/oFeedback\nPlanningw/Feedback\nActionTarget\nActionStrategy\nActionInfluence\nØwithTools\nØDatabase\nØList … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 3: search_paper

Find the paper's explicit limitations or challenges to represent scope boundaries accurately.

[Event 15](trace.jsonl#L15)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "limitations",
    "reason": "Find the paper's explicit limitations or challenges to represent scope boundaries accurately."
  },
  "observation": {
    "matches": [
      {
        "page": 3,
        "snippet": "have demonstrated their potential to accomplish a wide range of tasks. However, only based on LLMs, it is hard to effectively realize an autonomous agent due to their architecture limitations. To bridge this gap, previous work has developed a number of modules to inspire and enhance the capabilities of LLMs for building autonomous agents. In this section, we propose a unified framework to summarize the architectures proposed in the previous work*. In specific, the overall structure of our framework is illustrated Figure 2, which is composed of a profiling module, a memory module, a pl"
      },
      {
        "page": 15,
        "snippet": "g new research methods to the field of computational social science research. However, the application of LLM-based agent on social computing still presents several challenges and limitations [ 163, 6]. Two primary concerns are bias and toxicity, as LLMs are trained from real-world datasets, which makes them susceptible to inherent biases, discrimination content, and unfairness. When LLM is introduced, it may produce biased information, which is further taken to train LLM, leading to the amplification of bias. Causality and interpretability pose another challenge, particularly in the "
      },
      {
        "page": 21,
        "snippet": "dies. A diverse toolbox of objective techniques has emerged targeted at different competencies, from environmental simula- tion to social evaluation. While current techniques have limitations in measuring general capabilities, objective evaluation provides crucial insights complementing human assessment. Continued progress in objective evaluation benchmarks and methodology will further advance the development and understanding of LLM-based autonomous agents. In the above sections, we introduce both subjective and objective evaluation strategies for LLM-based autonomous agents. The eva"
      },
      {
        "page": 22,
        "snippet": "uating LLMs, addressing what to evaluate, where to evaluate, and how to assess their performance in downstream tasks and societal impact. [ 13] also discusses the capabilities and limitations of LLMs in various downstream tasks. The aforementioned research encompasses various aspects of large models, including training, application, and evaluation. However, prior to this paper, no work has specifically focused on the rapidly emerging and highly promising field of LLM-based Agents. In this study, we have compiled 100 relevant works on LLM-based Agents, covering their construction, appl"
      }
    ],
    "limit_reached": false
  }
}
```

</details>

### Step 4: read_pages

Inspect evaluation synthesis, future challenges, and survey conclusions for evidence and limitations.

[Event 20](trace.jsonl#L20)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 21,
    "end": 23,
    "reason": "Inspect evaluation synthesis, future challenges, and survey conclusions for evidence and limitations."
  },
  "observation": {
    "pages": [
      {
        "page": 21,
        "text": "Strategies: Based on the methods employed for evaluation, we can identify several common strategies:\n(1) Environmental simulation: In this method, the agents are assessed in immersive 3D environments\nsuch as games and interactive fiction using metrics for task success and human similarity, which\nincorporate factors like trajectories, language usage, and completed objectives [16, 156, 161, 151,\n133, 99, 137, 85, 149, 155]. This showcases the agents’ practical abilities in real-world scenarios. (2)\nIsolated reasoning: In this method, the researchers concentrate on fundamental cognitive abilities … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 22,
        "text": "5 Related Surveys\nWith the vigorous development of large language models, numerous comprehensive surveys have\nemerged, providing detailed insights into various aspects. [ 157] extensively introduces the back-\nground, main findings, and mainstream technologies of LLMs, encompassing a vast array of existing\nworks. On the other hand, [ 148] primarily focus on the applications of LLMs in various downstream\ntasks and the challenges associated with their deployment. Aligning LLMs with human intelligence\nis an active area of research to address concerns such as biases and illusions. [ 136] have compi … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 23,
        "text": "similar behaviors in real-world society. Inspired by the above case, maybe an important problem for\nagent-based simulation is how to conduct generalized human alignment, that is, for different purposes\nand applications, the agent should be able to align with diverse human values. However, existing\npowerful LLMs including ChatGPT and GPT-4 are mostly aligned with unified human values. Thus,\nan interesting direction is how to “realign” these models by designing proper prompting strategies.\n6.3 Prompt Robustness\nTo ensure rational behavior in agents, designers often incorporate additional modules … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 5: submit_review · citation_validation_failed

Evidence covers the framework, survey scope, evaluation synthesis, and challenges; submit a provisional assessment while noting inspected sections.

[Event 25](trace.jsonl#L25)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Evidence covers the framework, survey scope, evaluation synthesis, and challenges; submit a provisional assessment while noting inspected sections.",
    "review": {
      "score": 0.69,
      "summary": "This survey organizes the emerging LLM-based autonomous-agent literature around construction, applications, and evaluation, and proposes a four-module framework spanning profile, memory, planning, and action. Its value is primarily structured synthesis and agenda-setting rather than new empirical validation; its broad coverage is useful, while taxonomy coverage and the surveyed literature's early-stage evaluation remain relevant constraints.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The four-part framework offers a compact organizing structure and connects modular architecture to much of the prior work.",
          "page": 2,
          "quote": "By disabling one or more modules, the majority of previous studies can be viewed as specific examples of this framework."
        },
        {
          "kind": "strength",
          "claim": "The survey treats evaluation as a distinct topic and summarizes multiple complementary approaches rather than a single metric family.",
          "page": 21,
          "quote": "A diverse toolbox of objective techniques has emerged targeted at different competencies, from environmental simulation to social evaluation."
        },
        {
          "kind": "limitation",
          "claim": "The authors explicitly characterize the field as early-stage and identify substantial unresolved problems, limiting how conclusive the survey's synthesized picture can be.",
          "page": 22,
          "quote": "this field is still at its initial stage, and many challenges exist on its development road."
        },
        {
          "kind": "uncertainty",
          "claim": "The article acknowledges that existing objective evaluation approaches do not measure general capabilities fully; how to reconcile and validate measures across domains remains unresolved in the inspected material.",
          "page": 21,
          "quote": "While current techniques have limitations in measuring general capabilities, objective evaluation provides crucial insights complementing human assessment."
        }
      ],
      "unresolved_questions": [
        "How comprehensive and reproducible was the literature-selection process, and what criteria determined which studies entered the survey?",
        "How well does the proposed framework classify agent designs that combine or blur the module boundaries?",
        "I inspected the introduction/framework, evaluation pages, and challenges/conclusion area, not the survey's full application sections or all cited studies; do those sections reveal coverage gaps or stronger comparative analysis?"
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
        "quote_matches": false,
        "citation_verified": false,
        "matching_pages": [],
        "candidate_pages": [
          21
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
          22
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
          21
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

### Step 6: submit_review · accepted

Correct the evaluation citation using an exact, unhyphenated quote from inspected page 21 and resubmit.

[Event 30](trace.jsonl#L30)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Correct the evaluation citation using an exact, unhyphenated quote from inspected page 21 and resubmit.",
    "review": {
      "score": 0.69,
      "summary": "This survey organizes the emerging LLM-based autonomous-agent literature around construction, applications, and evaluation, and proposes a four-module framework spanning profile, memory, planning, and action. Its value is primarily structured synthesis and agenda-setting rather than new empirical validation; its broad coverage is useful, while taxonomy coverage and the surveyed literature's early-stage evaluation remain relevant constraints.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The four-part framework offers a compact organizing structure and connects modular architecture to much of the prior work.",
          "page": 2,
          "quote": "By disabling one or more modules, the majority of previous studies can be viewed as specific examples of this framework."
        },
        {
          "kind": "strength",
          "claim": "The survey treats evaluation as a distinct topic and summarizes multiple complementary approaches.",
          "page": 21,
          "quote": "objective evaluation provides crucial insights complementing human assessment."
        },
        {
          "kind": "limitation",
          "claim": "The authors explicitly characterize the field as early-stage and identify substantial unresolved problems, limiting how conclusive the survey's synthesized picture can be.",
          "page": 22,
          "quote": "this field is still at its initial stage, and many challenges exist on its development road."
        },
        {
          "kind": "uncertainty",
          "claim": "The article acknowledges that existing objective evaluation approaches do not measure general capabilities fully; how to reconcile and validate measures across domains remains unresolved in the inspected material.",
          "page": 21,
          "quote": "While current techniques have limitations in measuring general capabilities, objective evaluation provides crucial insights complementing human assessment."
        }
      ],
      "unresolved_questions": [
        "How comprehensive and reproducible was the literature-selection process, and what criteria determined which studies entered the survey?",
        "How well does the proposed framework classify agent designs that combine or blur the module boundaries?",
        "I inspected the introduction/framework, evaluation pages, and challenges/conclusion area, not the survey's full application sections or all cited studies; do those sections reveal coverage gaps or stronger comparative analysis?"
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
          21
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
          22
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
          21
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
