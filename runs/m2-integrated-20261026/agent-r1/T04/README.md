# T04: AgentBench: Evaluating LLMs as Agents

**agent · ok**

6 model calls · 5 reads · 13.73 s · $0.003413

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.69

AgentBench offers a useful, broad interactive benchmark spanning eight environments and evaluates 25 LLMs, providing a shared testbed and evidence of substantial variation in agent performance. Its breadth and release are valuable, though claims about practical capability depend on heterogeneous tasks and evaluation procedures, several of which use constructed or automated judging. This assessment inspected the introduction, portions of the task protocols, and conclusion/results snippets rather than the complete paper.

- **strength**: The benchmark contributes breadth by combining newly created and adapted settings rather than evaluating agents in only one environment.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments, 5 of which are created in this paper for the first time"

- **strength**: The reported evaluation compares a substantial set of API and open models, with GPT-4 leading across most task datasets.
  - Page 14 · citation: whitespace
  - Quote: "gpt-4 presents the best performance on 7 out of 8 datasets in AgentBench"

- **limitation**: At least one task setting simplifies its underlying game, so results in that environment do not directly establish performance in the more complex original game.
  - Page 8 · citation: exact
  - Quote: "The original design of Aquawar could be too complicated for existing LLMs."

- **uncertainty**: Lateral-puzzle results rely on an automated GPT-3.5 host and judging procedures; the inspected passages do not establish how robust these measures are to evaluator errors or prompt choices.
  - Page 9 · citation: whitespace
  - Quote: "we first design an accurate LTP host system based on gpt-3.5-turbo for automatic game playing"

Unresolved questions:

- How stable are model rankings across repeated runs, prompt variants, and updates to API models?
- How sensitive are aggregate scores to the chosen weighting across environments and task-specific metrics?
- I inspected only selected pages and search excerpts, not all environment protocols, result analyses, or appendices; further claims about reproducibility, task validity, and detailed statistical uncertainty remain unassessed.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper says AgentBench has eight environments, five newly created and three recompiled from published datasets (PDF p. 2), supporting the stated breadth through both new and adapted settings.
- Observation 2: **supported** — The paper evaluates 25 API-based and open-source models (PDF pp. 1, 3), and reports GPT-4 as best on seven of eight datasets (PDF p. 14).
- Observation 3: **supported** — The authors explicitly describe Aquawar as simplified and say they made adjustments to accommodate current LLM performance, including limiting fish types and staging game logic (PDF pp. 8–9). The observation appropriately limits what this setting establishes about the original game.
- Observation 4: **supported** — The paper describes GPT-3.5-turbo as the automatic LTP host and uses GPT-3.5-turbo-based answer extraction and checking (PDF pp. 9–10, 30–33). It also reports that automatic evaluation can be more tolerant than human evaluation for some measures and says it plans to improve the host (PDF p. 30). Thus the qualified concern about evaluator robustness and prompt choices is warranted as an open question, not a demonstrated defect.

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: search_paper

Locate the paper's stated scope and limitations to assess interpretation of the benchmark results.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "limitations",
    "reason": "Locate the paper's stated scope and limitations to assess interpretation of the benchmark results."
  },
  "observation": {
    "matches": [
      {
        "page": 2,
        "snippet": " presents a critical challenge. Historically, text-based game environments [57; 17; 30; 82] have been employed for language agent evaluation. However, they often suffer from limitations due to their closed, discrete action spaces, and their focus is primarily narrowed on models’ commonsense grounding abilities. More recently, attempts on embodied agents [ 63; 35; 2] have employed com- plicated multi-modal simulators based on games [41; 22], GUI [69; 81], and indoor scenes [68; 74]. However, these simulators, despite their complexity, do not accurately reflect the practical use-cases o"
      }
    ],
    "limit_reached": false
  }
}
```

</details>

### Step 2: read_pages

Inspect the benchmark motivation, environment design, and evaluation setup for evidence supporting its contribution.

[Event 10](trace.jsonl#L10)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 2,
    "end": 4,
    "reason": "Inspect the benchmark motivation, environment design, and evaluation setup for evidence supporting its contribution."
  },
  "observation": {
    "pages": [
      {
        "page": 2,
        "text": "Database\n(On an Ubuntu bash terminal)\nRecursively set all ﬁles in the directory to \nread-only, except those of mine.\n(Given Freebase APIs)\nWhat musical instruments do Minnesota-\nborn Nobel Prize winners play?\n(On the GUI of Aquawar)\nThis is a two-player battle game, you are a \nplayer with four pet ﬁsh cards ……\nA man walked into a restaurant, ordered a bowl \nof turtle soup, and after ﬁnishing it, he \ncommitted suicide. Why did he do that?\n(In the middle of a kitchen in a simulator)\nPlease put a pan on the dinning table.\n(On the oﬃcial website of an airline)\nBook the cheapest ﬂight from Beijing  … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 3,
        "text": "Table 1: AgentBench evaluates 25 API-based or open-sourced LLMs on LLM-as-Agent challenges.\nModel Model Size Form Version Creator\ngpt-4 [56] undisclosed api 0613\nOpenAIgpt-3.5-turbo [55] undisclosed api 0613\ntext-davinci-003 [58] undisclosed api -\ntext-davinci-002 [58] undisclosed api -\nclaude [6] undisclosed api v1.3 Anthropicclaude-instant [6] undisclosed api v1.1\ntext-bison-001 [3] undisclosed api - Google\nchatglm2 [100; 21] undisclosed api v0.2\nTsinghua & Zhipuchatglm-6b [100; 21] 6B open v1.1\ncodegeex2-6b-chat [102] 6B open -\nvicuna-13b [14] 13B open v1.1 LMSYSvicuna-7b [14] 7B open v1.1\n … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 4,
        "text": "(a) Operating System (OS)\nTask: “Find the total number of non-empty directories\ninside the ‘/etc’ directory. ”\nAction Space: Any valid bash commands\nObservation: System standard output\n(b) Database (DB)\nTask: “What was the total number of medals won by\nUnited States?”, given the table ‘Olympic Medals’\nAction space: Any valid SQL commands\nObservation: MySQL command-line interface output\n(c) Knowledge Graph (KG)\nTask: “Find tropical cyclones that are similar to Hur-\nricane Marie and affected Eastern North America. ”\nAction space: Basic KG-querying tools\nObservation: Query results\n(d) Digital Car … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 3: read_pages

Review benchmark evaluation methodology and reported model performance for supporting evidence and caveats.

[Event 15](trace.jsonl#L15)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 8,
    "end": 10,
    "reason": "Review benchmark evaluation methodology and reported model performance for supporting evidence and caveats."
  },
  "observation": {
    "pages": [
      {
        "page": 8,
        "text": "• Initialization. We prompt the LLM with the concrete task description, including the concrete\ndescription of each KG-querying tool that we provide.\n• Interaction. During this phase, the LLM is expected to invoke different tools to access the KG\nand accumulate the necessary information to respond accurately to the question. Importantly, the\nprocess is entirely autonomous, meaning the LLM determines the workflow entirely by itself.\n• Final Answer Prediction. During its interaction with the KG, the LLM may generate a list of\nvariables, each one representing a unique set of entities. If the LLM d … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 9,
        "text": "• To balance agent engagement and game complexity simultaneously, we designed two stages of\ngame logic. We remove the assertions in the first stage while keeping assertions in the second\nstage. We test all the models on both the first and second stages separately.\n• We choose two naive playing strategies (random and greedy search) as the baselines.\nEvaluation Setup. For each time of the game playing, we evaluate with the following steps:\n• Initialization. We initiated the modified game logic environment, an LLM to be tested, and the\nbaseline game agent under the Ubuntu 20.04 environment.\n• Int … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 10,
        "text": "length. In automatic evaluation, we limit the answer to be mostly \"Yes\", \"No\", or \"Irrelevant\", and\nextract the answer from gpt-3.5-turbo’s responses. LLMs are also asked to summarize their\nreasoning in automatic evaluation in order to help the termination detection to be more accurate.\n• Checking. We do the pilot study of each LLM to collect all situations in game process and design\nthe checking plan. For automatic evaluation, we set up some key words for gpt-3.5-turbo to\nanswer and remind the model to consider some flexible situation like synonyms.\nMetrics. We evaluate LLMs’ Lateral reasonin … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 4: read_pages

Inspect aggregate results and evaluation caveats to judge how strongly the paper's claims are supported.

[Event 20](trace.jsonl#L20)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 16,
    "end": 18,
    "reason": "Inspect aggregate results and evaluation caveats to judge how strongly the paper's claims are supported."
  },
  "observation": {
    "pages": [
      {
        "page": 16,
        "text": "for evaluating LLM-as-Agent with a broad coverage of practical challenges and available LLMs.\nAdditionally, it also initiates the idea of adopting agent tasks to measure LLM performance.\nEvaluating LLMs in Executive Environments.As LLMs become increasingly capable of real-world\nchallenges, there is also a trend to evaluate them in executive environments rather than static text\ndatasets, which also serves as a key feature of AgentBench. Besides text games (e.g., ALFWorld [71]),\nanother main stream of works lies in code execution. APPS [32], HumanEval [12] and MBPP [7]\npioneer the effort to eval … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 17,
        "text": "of the ACM SIGMOD International Conference on Management of Data, SIGMOD 2008,\nVancouver, BC, Canada, June 10-12, 2008, pages 1247–1250. ACM, 2008.\n[10] S. R. Bowman, G. Angeli, C. Potts, and C. D. Manning. A large annotated corpus for learning\nnatural language inference. In Proceedings of the 2015 Conference on Empirical Methods in\nNatural Language Processing. Association for Computational Linguistics, 2015.\n[11] T. B. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P. Dhariwal, A. Neelakantan,\nP. Shyam, G. Sastry, A. Askell, S. Agarwal, A. Herbert-V oss, G. Krueger, T. Henighan,\nR. Child, A … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 18,
        "text": "[24] L. Gao, A. Madaan, S. Zhou, U. Alon, P. Liu, Y . Yang, J. Callan, and G. Neubig. Pal:\nProgram-aided language models. In International Conference on Machine Learning, pages\n10764–10799. PMLR, 2023.\n[25] S. Gehrmann, T. Adewumi, K. Aggarwal, P. S. Ammanamanchi, A. Aremu, A. Bosselut, K. R.\nChandu, M.-A. Clinciu, D. Das, K. Dhole, et al. The gem benchmark: Natural language\ngeneration, its evaluation and metrics. In Proceedings of the 1st Workshop on Natural\nLanguage Generation, Evaluation, and Metrics (GEM 2021), pages 96–120. Association for\nComputational Linguistics, 2021.\n[26] X. Geng, A. … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 5: search_paper

Find the main quantitative results table and its surrounding claims for direct evidence of empirical support.

[Event 25](trace.jsonl#L25)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "GPT-4",
    "reason": "Find the main quantitative results table and its surrounding claims for direct evidence of empirical support."
  },
  "observation": {
    "matches": [
      {
        "page": 2,
        "snippet": "ial for developing effective and efficient agents to assist humans remains largely unexplored. The advent of Large Language Models (LLMs) [11; 15; 101; 66; 100; 80], such as GPT-4 [56], has brought plenty of new opportunities to this realm. Through extensive alignment training [ 75; 58; 8; 90; 65], LLMs have not only mastered traditional NLP tasks such as question answering [ 61], natural language inference [ 10], and text summarization [ 52], but also showcased an impressive ability to comprehend human intent and execute instructions. This has spurred the development of various"
      },
      {
        "page": 2,
        "snippet": "ave conducted a comprehensive evaluation of 25 different LLMs using AgentBench, including both API-based and open-source models. Our results reveal that top-tier models like GPT-4 are capable of handling a wide array of real-world tasks, indicating the potential for developing a potent, continuously learning agent. However, we also note a significant performance gap between these top-tier models and their open-source counterparts. Despite the recent success of open-source LLMs and their competitive scores on several benchmarks [], their performance on the challenging 2"
      },
      {
        "page": 3,
        "snippet": "Table 1: AgentBench evaluates 25 API-based or open-sourced LLMs on LLM-as-Agent challenges. Model Model Size Form Version Creator gpt-4 [56] undisclosed api 0613 OpenAIgpt-3.5-turbo [55] undisclosed api 0613 text-davinci-003 [58] undisclosed api - text-davinci-002 [58] undisclosed api - claude [6] undisclosed api v1.3 Anthropicclaude-instant [6] undisclosed api v1.1 text-bison-001 [3] undisclosed api - Google chatglm2 [100; 21] undisclosed api v0.2 Tsinghua & Zhipuchatglm-6b [100; 21] 6B open v1.1 codegeex2-6b-chat [102] 6B open "
      },
      {
        "page": 5,
        "snippet": "queries regarding OS could be difficult. In practice, about half of our instructions are created or collected from humans, while the other half are mostly QA problems generated by gpt-4 and strictly filtered by passing the unit tests (i.e., yield correct answers/states). For human instructions, we first gather 6000 real problems and solutions with bash or shell tag from Stack Overflow1. Then we sort them by the score (count of likes). We invite 8 annotators majored in programming to select challenging ones. For each selected problem, they create one or more task instructions and"
      },
      {
        "page": 14,
        "snippet": "Table 3: Test set (standard) results of AgentBench. A clear performance gap exists between top commercial LLMs (e.g., gpt-4) and medium-sized open-sourced competitors. “VER” stands for model version; “OA” stands for the overall AgentBench score derived from a weighted average of all environments (Cf. Section 4.1). Type Models VER OA OS DB KG DCG LTP HH WS WB API- based gpt-4 0613 4.41 36.8 33.7 52.1 50.0 17.6 78.0 58.6 22.6 claude v1.3 2.77 13.2 16.8 36.2 30.0 10.4 52.0 59.3 21.0 gpt-3.5-turbo 0613 2.55 32.6 15.0 27.2"
      },
      {
        "page": 14,
        "snippet": "ersion; “OA” stands for the overall AgentBench score derived from a weighted average of all environments (Cf. Section 4.1). Type Models VER OA OS DB KG DCG LTP HH WS WB API- based gpt-4 0613 4.41 36.8 33.7 52.1 50.0 17.6 78.0 58.6 22.6 claude v1.3 2.77 13.2 16.8 36.2 30.0 10.4 52.0 59.3 21.0 gpt-3.5-turbo 0613 2.55 32.6 15.0 27.2 30.0 14.9 14.0 67.2 15.7 text-davinci-003 - 2.10 22.9 16.3 30.8 15.0 5.2 20.0 61.4 15.5 claude-instant v1.1 1.90 14.6 8.0 29.7 35.0 6.1 26.0 44.2 0.8 text-davinci-002 - 1.46 4.9 13.7 18.9 25.0 2.3 14.0 60.1 1.1 text-bison-001 - 1.39 4.2 12.8 17.1 20.0 0"
      },
      {
        "page": 14,
        "snippet": "le 3. On this challenging benchmark, surprisingly we discover that some top LLMs have equipped strong capabilities in dealing with real-world environment interaction. For example, gpt-4 presents the best performance on 7 out of 8 datasets in AgentBench; on HH, it achieves a success rate of 78%, indicating its practical usability in this scenario. For other API-based LLMs, despite their relatively poorer performance, regardless of tasks most of them can solve at least a few percent of problems. 14"
      },
      {
        "page": 15,
        "snippet": "rced model openchat-13b-v3.2 presents a clear performance gap to gpt-3.5-turbo. This is in contrast to recent claims that some open-sourced LLMs are comparable togpt-3.5-turbo and gpt-4. 4.3 Analysis In the evaluation, we identify several specific challenges for LLMs to deal with agent-formed tasks, including action validity, long context, multi-turn consistency, and the impact of code training. Action Validity. During our evaluation, we find that the models do not follow instructions at all times. In other words, the expected outputs of the models are not always in the input sp"
      }
    ],
    "limit_reached": true
  }
}
```

</details>

### Step 6: submit_review · accepted

Evidence reviewed covers benchmark scope, selected task protocols, and reported aggregate model results; submit an independent assessment with remaining evidence gaps noted.

[Event 31](trace.jsonl#L31)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Evidence reviewed covers benchmark scope, selected task protocols, and reported aggregate model results; submit an independent assessment with remaining evidence gaps noted.",
    "review": {
      "score": 0.69,
      "summary": "AgentBench offers a useful, broad interactive benchmark spanning eight environments and evaluates 25 LLMs, providing a shared testbed and evidence of substantial variation in agent performance. Its breadth and release are valuable, though claims about practical capability depend on heterogeneous tasks and evaluation procedures, several of which use constructed or automated judging. This assessment inspected the introduction, portions of the task protocols, and conclusion/results snippets rather than the complete paper.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The benchmark contributes breadth by combining newly created and adapted settings rather than evaluating agents in only one environment.",
          "page": 2,
          "quote": "AgentBench encompasses 8 distinct environments, 5 of which are created in this paper for the first time"
        },
        {
          "kind": "strength",
          "claim": "The reported evaluation compares a substantial set of API and open models, with GPT-4 leading across most task datasets.",
          "page": 14,
          "quote": "gpt-4 presents the best performance on 7 out of 8 datasets in AgentBench"
        },
        {
          "kind": "limitation",
          "claim": "At least one task setting simplifies its underlying game, so results in that environment do not directly establish performance in the more complex original game.",
          "page": 8,
          "quote": "The original design of Aquawar could be too complicated for existing LLMs."
        },
        {
          "kind": "uncertainty",
          "claim": "Lateral-puzzle results rely on an automated GPT-3.5 host and judging procedures; the inspected passages do not establish how robust these measures are to evaluator errors or prompt choices.",
          "page": 9,
          "quote": "we first design an accurate LTP host system based on gpt-3.5-turbo for automatic game playing"
        }
      ],
      "unresolved_questions": [
        "How stable are model rankings across repeated runs, prompt variants, and updates to API models?",
        "How sensitive are aggregate scores to the chosen weighting across environments and task-specific metrics?",
        "I inspected only selected pages and search excerpts, not all environment protocols, result analyses, or appendices; further claims about reproducibility, task validity, and detailed statistical uncertainty remain unassessed."
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
          14
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
      }
    ]
  }
}
```

</details>
