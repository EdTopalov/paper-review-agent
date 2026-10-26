# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**agent · ok**

6 model calls · 4 reads · 16.55 s · $0.001905

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.63

CAMEL introduces a role-playing and inception-prompt framework for two LLM agents to collaborate with limited human guidance, alongside scalable conversation-generation pipelines and datasets for AI-society and coding scenarios. Its main contribution is a concrete research scaffold and prompt-design analysis, not evidence of robust real-world task completion.

- **strength**: The approach produces sizeable generated conversation datasets in the stated scenarios.
  - Page 9 · citation: whitespace
  - Quote: "yielding a total of 25,000 conversations."

- **strength**: Prompt modifications shift termination behavior, though the paper also reports increased flake messages.
  - Page 12 · citation: normalized
  - Quote: "both modifications considerably increases the number of conversations that terminate with end of task token, and reduce the number of messages with assistant instruction."

- **limitation**: The authors explicitly identify expert evaluation of task completion as a challenge, limiting claims about demonstrated task success.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

Unresolved questions:

- How often do generated conversations yield correct, independently verified task outcomes across domains?
- How well do findings generalize across models and settings with more than two agents?
- What is the quality of the generated conversations under independent human assessment?
- This assessment inspected experimental setup, dataset analysis, and conclusion/limitations, not the full paper or supplementary materials; additional evidence may change the assessment.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — Page 9 reports 25,000 AI Society conversations and 50,000 Code conversations, supporting the claim that the framework generated sizeable datasets in both stated scenarios.
- Observation 2: **supported** — Page 12 reports that both prompt modifications increased end-of-task termination and reduced assistant-instruction terminations, and also reports a significant increase in flake messages. The claim accurately captures these effects.
- Observation 3: **supported** — Page 13 explicitly says that evaluating task-completion capabilities is challenging and requires numerous domain experts. This appropriately qualifies what the paper demonstrates about task success.

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: search_paper

Locate evaluation evidence and reported experimental results.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "experiments",
    "reason": "Locate evaluation evidence and reported experimental results."
  },
  "observation": {
    "matches": [
      {
        "page": 4,
        "snippet": " harms [34, 64, 27, 23]. Achieving a high level of alignment requires researchers to grapple with complex ethical, philosophical, and technical issues. We conduct large-scale experiments to study different role-playing situations, which probe the alignment of LLMs. 3 Methodology In this paper, we focus on studying communicative agents under AI-AI cooperative scenarios where they share pure common interests. In particular, we are studying the assistant-user scenario, where a preliminary idea is given at the start. Agents will conceptualize the idea into a speciﬁc task and complete it a"
      },
      {
        "page": 5,
        "snippet": "on and import of essential Python libraries for sentiment analysis and stock trading by instructing the AI assistant through conversations. This example is drawn from our experiments, and the entire conversation is available in the supplementary section. 5"
      },
      {
        "page": 7,
        "snippet": "ario follow a similar sprint as the AI society scenario, but with some additional engineering related to programming languages. For more information, please refer to Figure 3. 4 Experiments In this section, we will discuss the various experiments that we conducted to arrive at our ﬁnal design choices. Speciﬁcally, we will examine the interesting observations, challenging issues, and several examples we have encountered while enabling agents to communicate with each other under different prompt design choices to achieve autonomous cooperation. In our experiments, we employed twogpt- 3."
      },
      {
        "page": 7,
        "snippet": "but with some additional engineering related to programming languages. For more information, please refer to Figure 3. 4 Experiments In this section, we will discuss the various experiments that we conducted to arrive at our ﬁnal design choices. Speciﬁcally, we will examine the interesting observations, challenging issues, and several examples we have encountered while enabling agents to communicate with each other under different prompt design choices to achieve autonomous cooperation. In our experiments, we employed twogpt- 3.5-turbo agents, referred to for simplicity as LLM agents,"
      },
      {
        "page": 7,
        "snippet": ", and several examples we have encountered while enabling agents to communicate with each other under different prompt design choices to achieve autonomous cooperation. In our experiments, we employed twogpt- 3.5-turbo agents, referred to for simplicity as LLM agents, with Inception Prompts, as described in Section 3.2, to simulate assistant-user cooperation. We examined the AI Society and Code scenarios in particular. We also gathered conversational data, named CAMEL AI Society and CAMEL Code 7"
      },
      {
        "page": 13,
        "snippet": ", we also note that due to the complexity of society and the cost of using OpenAI API, this work only touches the tip of the iceberg of the AI society. For future work, in our experiments, we considered the setting where two conversational agents communicate with each other to solve a problem. This setting can be easily 13"
      },
      {
        "page": 19,
        "snippet": "Chandrasekaran, Ronen Eldan, Johannes Gehrke, Eric Horvitz, Ece Kamar, Peter Lee, Yin Tat Lee, Yuanzhi Li, Scott Lundberg, et al. Sparks of artiﬁcial general intelligence: Early experiments with gpt-4. arXiv preprint arXiv:2303.12712, 2023. [11] N Carlini, F Tramer, E Wallace, M Jagielski, A Herbert-V oss, K Lee, A Roberts, T Brown, D Song, Ú Erlingsson, et al. Extracting training data from large language models. arxiv. Preprint posted online December, 14, 2020. [12] Nicholas Carlini, Jamie Hayes, Milad Nasr, Matthew Jagielski, Vikash Sehwag, Florian Tramèr, Borja Balle, Daphne Ippoli"
      }
    ],
    "limit_reached": false
  }
}
```

</details>

### Step 2: read_pages

Inspect experiment setup, findings, and evidence for the paper's claims.

[Event 10](trace.jsonl#L10)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 7,
    "end": 9,
    "reason": "Inspect experiment setup, findings, and evidence for the paper's claims."
  },
  "observation": {
    "pages": [
      {
        "page": 7,
        "text": "AI Society Inception Prompt\nTask Speciﬁer Prompt:\nHere is a task that <ASSISTANT_ROLE> will help <USER_ROLE> to complete: <TASK>.\nPlease make it more specific. Be creative and imaginative.\nPlease reply with the specified task in <WORD_LIMIT> words or less. Do not add anything else.\nAssistant System Prompt:\nNever forget you are a <ASSISTANT_ROLE> and I am\na <USER_ROLE>. Never flip roles! Never instruct\nme!\nWe share a common interest in collaborating to\nsuccessfully complete a task.\nYou must help me to complete the task.\nHere is the task: <TASK>. Never forget our task!\nI must instruct you based  … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 8,
        "text": "Code Inception Prompt\nTask Speciﬁer Prompt:\nHere is a task that a programmer will help a person working in <DOMAIN> to complete using\n<LANGUAGE>: <TASK>.\nPlease make it more specific. Be creative and imaginative.\nPlease reply with the specified task in <WORD_LIMIT> words or less. Do not add anything else.\nAssistant System Prompt\nNever forget you are a Computer Programmer and\nI am a person working in <DOMAIN>. Never flip\nroles! Never instruct me!\nWe share a common interest in collaborating to\nsuccessfully complete a task.\nYou must help me to complete the task using\n<LANGUAGE> programming langua … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 9,
        "text": "Data Generation Prompts of AI Society & Code\nAI Society\nAssistant Role Generation Prompt:\nYou are a helpful assistant that can play many\ndifferent roles. Now please list <NUM_ROLES>\ndifferent roles that you can play with your\nexpertise in diverse fields. Sort them by\nalphabetical order. No explanation required.\nUser Role Generation Prompt:\nPlease list <NUM_ROLES> most common and diverse\ngroups of internet users or occupations.\nUse singular form. No explanation.\nSort them by alphabetical order. No explanation\nrequired.\nTask Generation Prompt:\nList <NUM_TASKS> diverse tasks that <ASSISTANT_ROLE> … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 3: search_paper

Find the authors' stated scope boundaries and discussion of limitations.

[Event 15](trace.jsonl#L15)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "limitations",
    "reason": "Find the authors' stated scope boundaries and discussion of limitations."
  },
  "observation": {
    "matches": [
      {
        "page": 1,
        "snippet": "ng the conversation toward task completion without any human supervision? To tackle this issue, it is crucial to conduct more research exploring the potential, capabilities, and limitations of communicative agents that operate entirely on their own to complete tasks. It is important to consider how multiple agents interact with each other, as this understanding is crucial ∗Equal contribution Pre-print. Work in Progress. arXiv:2303.17760v1 [cs.AI] 31 Mar 2023"
      },
      {
        "page": 13,
        "snippet": " insights into the future of large language artiﬁcial intelligence models and cooperative AI systems. Risk, Limitation and Future Work. We are aware of the potential risks and limitations of this work. For the risks, since existing LLMs are not fully tuned to be harmless, they can be easily exploited by malicious users for harmful purposes. We provide an example of the “evil mind” that LLM agents could possess in the supplemental materials by asking a hacker to help an AGI agent to “ take control of the world”. For the limitations, due to the large scale and diversity of tasks generat"
      },
      {
        "page": 13,
        "snippet": "vide an example of the “evil mind” that LLM agents could possess in the supplemental materials by asking a hacker to help an AGI agent to “ take control of the world”. For the limitations, due to the large scale and diversity of tasks generated by our role-playing framework, evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts. However, we also note that due to the complexity of society and the cost of using OpenAI API, this work only touches the tip of the iceberg of the AI society. For future work, in our experime"
      },
      {
        "page": 21,
        "snippet": "ity well-being. International Journal of Community Well-Being, 3:443 – 463, 2020. [64] Alex Tamkin, Miles Brundage, Jack Clark, and Deep Ganguli. Understanding the capabilities, limitations, and societal impact of large language models. arXiv preprint arXiv:2102.02503, 2021. [65] Ming Tan. Multi-agent reinforcement learning: Independent versus cooperative agents. In International Conference on Machine Learning, 1997. [66] Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos Guestrin, Percy Liang, and Tatsunori B. Hashimoto. Stanford alpaca: An instruction-follo"
      }
    ],
    "limit_reached": false
  }
}
```

</details>

### Step 4: read_pages

Read conclusions and limitations to calibrate the assessment and cite scope.

[Event 20](trace.jsonl#L20)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 12,
    "end": 13,
    "reason": "Read conclusions and limitations to calibrate the assessment and cite scope."
  },
  "observation": {
    "pages": [
      {
        "page": 12,
        "text": "• User No Instruct: If the user does not instruct the assistant for 3 rounds, the conversa-\ntion is terminated.\n• Assistant Instruct: If the assistant provides an instruction to the user, it indicates a\nrole reversal, and the conversation is terminated.\n• End of Task Token : If the user believes that the task has been solved, they are expected\nto say <CAMEL_TASK_DONE> to signify the completion of the task. Once this message is\nreceived, the conversation is terminated to ensure that the data generated accurately reﬂects\nthe completion of the task.\n• Assistant & User Token Limit: Given that gpt- … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 13,
        "text": "Figure 7: Distribution of Conversation Termination Reasons. In our AI society dataset, most\nmethods are terminated due to Assistant Instruct ﬂag, whereas in the code dataset the main\ntermination reason is Token Limit . The latter is due big chunks of code in the assistant responses.\nFigure 8: Ablation Distribution of Conversation Termination Reasons (AI Society) Due to\nPrompt Modiﬁcation. We run two ablations: (1) Prompt V2 which refers to modifying the original\nAI society prompt by removing the assistant output format, i.e. starting with “Output:” and ending\nwith “Next Request” and (2) Adding … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 5: submit_review · citation_validation_failed

Evidence covers framework, generated datasets, prompt ablations, and explicit evaluation limitations; submit independent assessment.

[Event 25](trace.jsonl#L25)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Evidence covers framework, generated datasets, prompt ablations, and explicit evaluation limitations; submit independent assessment.",
    "review": {
      "score": 0.63,
      "summary": "CAMEL introduces a role-playing/inception-prompt framework for two LLM agents to collaborate with limited human guidance, and supplies scalable conversation-generation pipelines and datasets for AI-society and coding scenarios. Its main value is a concrete research and data-generation scaffold, with prompt-design analyses and candid discussion of evaluation limits; it does not establish robust real-world task completion.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The work operationalizes the framework through role-specific inception prompts and generated conversational datasets at substantial scale.",
          "page": 9,
          "quote": "yielding a total of 25,000 conversations."
        },
        {
          "kind": "strength",
          "claim": "The paper reports prompt ablations with trade-offs in task-ending behavior and undesirable replies, rather than presenting prompt changes as unambiguously successful.",
          "page": 12,
          "quote": "both modifications considerably increases the number of conversations that terminate with end of task token, and reduce the number of messages with assistant instruction."
        },
        {
          "kind": "limitation",
          "claim": "The authors say task-completion evaluation is difficult at the breadth claimed, so the paper's evidence is stronger for dataset generation and observed interaction patterns than validated task success.",
          "page": 13,
          "quote": "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."
        },
        {
          "kind": "uncertainty",
          "claim": "The reported experiments use two GPT-3.5-turbo agents in assistant-user cooperation; generalization to other models and broader multi-agent settings is not established in the inspected passages.",
          "page": 7,
          "quote": "we employed twogpt-3.5-turbo agents, referred to for simplicity as LLM agents"
        }
      ],
      "unresolved_questions": [
        "How often do generated conversations produce correct, independently verified task outcomes across domains?",
        "How robust are the findings across different base models, and across settings with more than two agents?",
        "What are the quality and diversity of the released conversations under independent human assessment?",
        "This assessment inspected the experimental setup, dataset analysis, and conclusion/limitations, not the full paper or supplementary materials; detailed robustness and data-quality evidence may lie outside the inspected passages."
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
        "citation_verified": true,
        "matching_pages": [
          12
        ],
        "candidate_pages": [],
        "status": "normalized",
        "observed": true
      },
      {
        "checker_version": "m2-citations-v2",
        "page_valid": true,
        "quote_nonempty": true,
        "quote_matches": true,
        "citation_verified": true,
        "matching_pages": [
          13
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

### Step 6: submit_review · accepted

Resubmit with exact observed quotations and remove unsupported citation; evaluation evidence remains partial.

[Event 30](trace.jsonl#L30)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Resubmit with exact observed quotations and remove unsupported citation; evaluation evidence remains partial.",
    "review": {
      "score": 0.63,
      "summary": "CAMEL introduces a role-playing and inception-prompt framework for two LLM agents to collaborate with limited human guidance, alongside scalable conversation-generation pipelines and datasets for AI-society and coding scenarios. Its main contribution is a concrete research scaffold and prompt-design analysis, not evidence of robust real-world task completion.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The approach produces sizeable generated conversation datasets in the stated scenarios.",
          "page": 9,
          "quote": "yielding a total of 25,000 conversations."
        },
        {
          "kind": "strength",
          "claim": "Prompt modifications shift termination behavior, though the paper also reports increased flake messages.",
          "page": 12,
          "quote": "both modifications considerably increases the number of conversations that terminate with end of task token, and reduce the number of messages with assistant instruction."
        },
        {
          "kind": "limitation",
          "claim": "The authors explicitly identify expert evaluation of task completion as a challenge, limiting claims about demonstrated task success.",
          "page": 13,
          "quote": "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."
        }
      ],
      "unresolved_questions": [
        "How often do generated conversations yield correct, independently verified task outcomes across domains?",
        "How well do findings generalize across models and settings with more than two agents?",
        "What is the quality of the generated conversations under independent human assessment?",
        "This assessment inspected experimental setup, dataset analysis, and conclusion/limitations, not the full paper or supplementary materials; additional evidence may change the assessment."
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
        "citation_verified": true,
        "matching_pages": [
          12
        ],
        "candidate_pages": [],
        "status": "normalized",
        "observed": true
      },
      {
        "checker_version": "m2-citations-v2",
        "page_valid": true,
        "quote_nonempty": true,
        "quote_matches": true,
        "citation_verified": true,
        "matching_pages": [
          13
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
