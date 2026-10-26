# T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**agent · ok**

6 model calls · 5 reads · 16.24 s · $0.002759

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.72

AutoGen presents a flexible infrastructure for building LLM applications as conversations among customizable agents that can combine models, tools, and human participation. Its contribution is a practical, general-purpose framework demonstrated across diverse workflows; evidence is promising but largely illustrative and task-specific rather than a broad validation of general performance.

- **strength**: The framework’s central value is composable, varied agent interaction, with concrete application examples spanning multiple task families.
  - Page 9 · citation: exact
  - Quote: "We present six examples of diverse applications built using AutoGen."

- **strength**: Some empirical support goes beyond demonstrations: the MiniWob++ comparison reports performance across twelve task types and ten instances per task.
  - Page 16 · citation: exact
  - Quote: "For each clicking task, we reported the success rate for ten different instances."

- **limitation**: The math comparison is very small and qualitative, so its results provide only weak grounds for broad claims of competitiveness.
  - Page 10 · citation: whitespace
  - Quote: "We use two level-5 problems from the MATH dataset for the qualitative evaluation and test on each problem for 3 times."

- **uncertainty**: The report itself identifies optimal workflow design as unresolved, including when multi-agent workflows help and how to choose cost-effective configurations.
  - Page 23 · citation: exact
  - Quote: "For a given task, what is the optimal (e.g., cost-effective) multi-agent workflow?"

Unresolved questions:

- How reliably do the framework’s benefits generalize across tasks, model backends, and larger independent evaluations?
- What workflow choices provide consistent gains relative to simpler pipelines, and at what cost?
- I inspected framework descriptions, selected math and MiniWob++ evidence, and future-work discussion; I did not inspect the full report or all application evaluations, so evidence beyond these passages may affect the assessment.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper presents six diverse application examples and describes varied agent roles and conversation patterns (PDF pp. 2, 8–9).
- Observation 2: **supported** — The MiniWob++ comparison covers twelve clicking tasks, and reports success rates over ten instances for each task (PDF pp. 15–16).
- Observation 3: **overstated** — The initial comparison is indeed qualitative and limited to two MATH problems tested three times each (PDF pp. 10–11). But the paper also reports a follow-up quantitative evaluation on 12 level-5 problems, with one trial per problem, so describing the math comparison overall as very small and qualitative omits relevant evidence (PDF p. 11).
- Observation 4: **supported** — The paper explicitly lists unresolved questions about which tasks benefit from multi-agent workflows and what workflow is optimal and cost-effective (PDF p. 23).

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: search_paper

Locate the paper’s evidence and evaluation discussion to assess support for its claimed framework benefits.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "evaluation",
    "reason": "Locate the paper’s evidence and evaluation discussion to assess support for its claimed framework benefits."
  },
  "observation": {
    "matches": [
      {
        "page": 9,
        "snippet": "ing (scenario 2). We further demonstrate a novel scenario where multiple human users can participate in the conversations3 during the problem solving process (scenario 3). For the evaluation, we test on randomly selected level-5 problems from the MATH dataset [19]. We compare AutoGen with the following LLM-based agent systems. For all evaluations, we use GPT-4 as the base model, and pre-install the “sympy” package in the execution environment. 3https://github.com/microsoft/FLAML/blob/main/notebook/autogen_agentchat_two_users.ipynb 9"
      },
      {
        "page": 9,
        "snippet": " (scenario 3). For the evaluation, we test on randomly selected level-5 problems from the MATH dataset [19]. We compare AutoGen with the following LLM-based agent systems. For all evaluations, we use GPT-4 as the base model, and pre-install the “sympy” package in the execution environment. 3https://github.com/microsoft/FLAML/blob/main/notebook/autogen_agentchat_two_users.ipynb 9"
      },
      {
        "page": 10,
        "snippet": "added a LangChain code executor, “PythonREPL” to the agent as a tool. Scenario 1: Autonomous Problem Solving. We use two level-5 problems from the MATH dataset for the qualitative evaluation and test on each problem for 3 times. The first problem asks to simplify a square root fraction and the second problem asks to solve a number theory problem. Using this setup, we analyzed the correctness of results, user experience regarding the verbosity of response and whether the LLM-based system can run without unexpected behaviors. Table 2 details correctness counts and failure reasons. • Co"
      },
      {
        "page": 11,
        "snippet": "Table 2: Qualitative evaluation on two math problems from the MATH dataset under the autonomous problem solving setting. Each LLM-based system is tested three times on each of the problems. We report the problem solving correctness and summarize the failure reasons in this table. Correctness Failure Reason AutoGen 3/3 N/A. Auto-GPT 0/3 The LLM gives code without the print function so the result is not printed. ChatGPT+Plugin 0/"
      },
      {
        "page": 11,
        "snippet": " answer, but GPT-4 always chooses the wrong answer. ChatGPT+Code Interpreter 2/3 Returns a wrong decimal result. LangChain ReAct 0/3 LangChain gives 3 different wrong answers. (a) Evaluation on the first problem that asks to simplify a square root fraction. Correctness Failure Reason AutoGen 2/3 The final answer from code execution is wrong. Auto-GPT 0/3 The LLM gives code without the print function so the result is not printed. ChatGPT+Plugin 1/3 For one trial, GPT-4 got stuck because it keeps giving wrong queries and has to be stopped. Another trial simply gives a wrong answer. Cha"
      },
      {
        "page": 11,
        "snippet": "ped. Another trial simply gives a wrong answer. ChatGPT+Code Interpreter 0/3 It gives 3 different wrong answers. LangChain ReAct 0/3 LangChain gives 3 different wrong answers. (b) Evaluation on the second number theory problem. without execptions. We note the occurrences of undesired behaviors from other LLM-based systems that could affect user experience: Auto-GPT keeps giving code without the ‘print’ statement and cannot correct it, so the user needs to run them manually; ChatGPT with Wolfram Alpha plugin has the potential to stuck in a loop that needs to be manually stopped; and L"
      },
      {
        "page": 12,
        "snippet": "on’t continue to the next step, we give the last hint: Use point (-5,-1,-5) to determine which is correct and give the final answer. 5. Final answer is 11x+6y+5z+86=0 . During our evaluation we observed that AutoGen consistently solves the problem in all 3 trials. Both ChatGPT+Code Interpreter and ChatGPT+Plugin managed to solve the problem in 2 out of 3 tri- als and AutoGPT fails to solve it all 3 times. In its unsuccessful attempt, ChatGPT+Code In- terpreter failed to follow our instructions to walk through the step of removing the absolute sign. ChatGPT+Plugin, in its failed trial"
      },
      {
        "page": 12,
        "snippet": " two trials, it formulated the distance equation and followed provided hints, but the final answer was wrong from code execution. Auto-GPT is still the most verbose system in this evaluation. The ChatGPT+Plugin and Chat- GPT+Code Interpreter are more verbose than AutoGen. Their request to external tools is automatic, so they would keep sending queries and try to revise them as long as there are errors. Since this prob- lem is hard and very likely to result in wrong queries, we have to wait for a long time for the system to finish trying all the queries. However, with human input enab"
      }
    ],
    "limit_reached": true
  }
}
```

</details>

### Step 2: read_pages

Inspect framework design and the math evaluation setup and reported results.

[Event 10](trace.jsonl#L10)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 8,
    "end": 10,
    "reason": "Inspect framework design and the math evaluation setup and reported results."
  },
  "observation": {
    "pages": [
      {
        "page": 8,
        "text": "Table 1: Summary of differences between AutoGen and other related multi-agent systems. In this\ntable, the “infrastructure” aspect evaluates whether the system is designed as a generic infrastructure\nfor building new LLM applications; the “conversation pattern” aspect assesses the types of patterns\nsupported by the implemented systems; the “execution-capable” aspect determines whether the system\ncan execute LLM-generated code; the “human involvement” aspect evaluates whether (and how) the\nsystem allows human participation during the execution process of the system.\nAspect AutoGen Multi-agent\nDe … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 9,
        "text": "A1. Math Problem Solving\nA3. Online Decision Making\nAssistantExecutor\nA2. Multi-agent Coding\nCommander\nSafeguard\nWriter\nA4. Retrieval-augmented Chat\nA6. Conversational Chess\nRetrieval-augmentedAssistantRetrieval-augmentedUser Proxy\nChess Board\nHuman/AI Chess Player A\nHuman/AI Chess Player B\nStudent\nAssistant\nAssistant\nExpert\nAsk  expert\nBroadcast\nManager\nSpeak\nA5. Dynamic Group Chat\nFigure 5: We present six examples of diverse applications built using AutoGen. Their conversation\npatterns show AutoGen’s flexibility and power.\n• A4: Retrieval-augmented chat uses retrieval augmented agents to sol … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 10,
        "text": "Enable Multi-User Problem Solving ViaStudent        and Expert \nStudent Proxy\nStudentAssistant\nExpertAssistant\nExpert Proxy\nAsk for expert\nEnable Autonomous and Human-in-the-loop Problem Solving\nFigure 6: Examples of three settings we used to solve math problems using AutoGen. (Gray) Enables\nimplementing a workflow where a single “student” works with a student assistant to solve problems in\neither autonomous mode or human-in-the-loop mode. (Gray + Orange) Enables a more sophisticated\nworkflow where the student assistant can on the fly ask another user called “expert”, who is in the\nloop with i … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 3: read_pages

Check whether later sections report broader quantitative evidence or explicit limitations for the showcased applications.

[Event 15](trace.jsonl#L15)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 15,
    "end": 17,
    "reason": "Check whether later sections report broader quantitative evidence or explicit limitations for the showcased applications."
  },
  "observation": {
    "pages": [
      {
        "page": 15,
        "text": "Executor\nReward & State\nAction DecisionAssistant\nEnvironment State: HTML code for current web pagesReward: Success/Fail/Ongoing\nAction decision: Next action to perform on a web pageAction decision=“Click the button with xpath’//button[id = ‘subbtn’]’“Environment State = “<div id=\"wrap\" data-wob_ref=\"2\" data-wob_eps=\"e0\"><div id=\"query\">Click button ONE, then click button TWO.</div><div id=\"area\" data-wob_ref=\"3\" data-wob_eps=\"e0\"><button id=\"subbtn\" style=\"position:absolute; left:50px; top:74px\" data-wob_ref=\"4\" data-wob_eps=\"e0\">ONE</button><button id=\"subbtn2\" style=\"position:absolute; left: … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 16,
        "text": "click-button\nclick-button-sequence\nclick-checkboxes-transfer\nclick-dialogclick-dialog-2\nclick-menu\nclick-scroll-list\nclick-tabclick-test\nclick-widget\nclick-collapsible\nclick-option\n0.0\n0.5\n1.0success rate\nRCI MiniWobChat\nFigure 9: Comparisons between RCI (state-of-the-art prior work) and MiniWobChat on the Mini-\nWob++ benchmark. We selected a set of clicking tasks in MiniWob++ with varying degrees of\ndifficulty. For each clicking task, we reported the success rate for ten different instances. The results\nshow that MiniWobChat achieves comparable performance with RCI.\nRetrieval-augmentedAssista … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 17,
        "text": "them into chunks of a specific size, computes embeddings, and store them in a vector database. Then\nonce a chat is initiated, they work together for code generation and question answering automatically\nfollowing the procedures below:\n1. The Retrieval-augmented User Proxy retrieves document chunks based on the embedding similarity.\nIt sends them along with the question to the Retrieval-augmented Assistant.\n2. The Retrieval-augmented Assistant uses LLM to generate code or text as answers based on the\nquestion and context. The LLM is instructed to reply “Update Context” to the Retrieval-augmented … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 4: search_paper

Check for explicit scope boundaries or limitations before finalizing the review.

[Event 20](trace.jsonl#L20)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "limitations",
    "reason": "Check for explicit scope boundaries or limitations before finalizing the review."
  },
  "observation": {
    "matches": [
      {
        "page": 3,
        "snippet": "ghly capable LLM has the abilities of language understanding, generation, and some reasoning. Besides LLM, agents in AutoGen can also be powered by tools or humans to overcome LLM limitations and harness human intelligence. 1. LLMs. The main goal of Autogen is to enable next-gen LLM applications through multi-agent conversations, making LLM a critical component as the back-end of agents in Autogen. Different agents can be backed by various LLM configurations. For instance, some may use LLMs or config- urations tuned on private data [47, 37]. Additionally, LLMs can be set up to play di"
      },
      {
        "page": 4,
        "snippet": "the human starts talking to the AssistantAgent after an initial plot is created through several rounds of automated chat. 3. Tools. Using tools is an effective way to overcome LLM limitations. AutoGen natively supports a generic form of tool usage through code generation and execution. Specifically, when using a default assistant agent from AutoGen, the system message prompts the LLM to suggest Python code or shell scripts to solve problems in several cases. These cases cover common scenarios where tools are needed, such as situations requiring information collection. The system messa"
      },
      {
        "page": 7,
        "snippet": "53]. All agents provided in LangChain Agents follow a single-agent paradigm and are not inherently designed for communicative and collaborative modes. A significant summary of its limitations can be found in [51]. Due to these limitations, even the multi-agent systems in LangChain (e.g., reimplementation of CAMEL 2) are not based on LangChain Agents but are implemented from 2https://python.langchain.com/docs/use_cases/agent_simulations/camel_role_playing 7"
      },
      {
        "page": 7,
        "snippet": "llow a single-agent paradigm and are not inherently designed for communicative and collaborative modes. A significant summary of its limitations can be found in [51]. Due to these limitations, even the multi-agent systems in LangChain (e.g., reimplementation of CAMEL 2) are not based on LangChain Agents but are implemented from 2https://python.langchain.com/docs/use_cases/agent_simulations/camel_role_playing 7"
      },
      {
        "page": 15,
        "snippet": "ghtforward. A4: Retrieval Augmented Code Generation and Question Answering Retrieval augmentation has emerged as a practical and effective approach for mitigating many intrin- sic limitations of LLM in many applications by incorporating external documents. In this section, we employ AutoGen to build a Retrieval Augmented Generation (RAG) system for code generation and question-answering [26, 39]. Retrieval Augmented Generation (RAG) combines the advantages of retrieval-based and generation-based models in natural language processing, and has practical ap- plications in chatbots, quest"
      },
      {
        "page": 20,
        "snippet": "m programmatically sending requests to Google Scholar. Even being an unofficial API, it doesn't make using scholarly legal as per the use policy. It's important you consider these limitations when handling this tool and any consequences that may arise on its usage. …. Alice Bob … // revise based on Bob’s comment … // reviewing the updated code from Alice Bob That's correct. Make sure to install the 'feedparser' module using the provided command, and then you should be able to execute the updated arxiv_search.pyscript successfully. User Proxy exitcode: 0 (execution succeeded)Code outpu"
      },
      {
        "page": 24,
        "snippet": "It is important to consider the impact of this interaction on user experience, trust, and reliance on AI systems. Clear communication and user education about the capabilities and limitations of the system will be essential [9]. • Unintended Consequences: As discussed before, the use of multi-agent conversations and au- tomation in complex tasks may have unintended consequences. Especially, allowing LLM agents to make changes in external environments through code execution or function calls, such as in- stall packages, could be risky. Developers should carefully consider the potential"
      }
    ],
    "limit_reached": false
  }
}
```

</details>

### Step 5: read_pages

Read the paper’s discussion of risks and scope to cite a relevant caveat accurately.

[Event 25](trace.jsonl#L25)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 23,
    "end": 24,
    "reason": "Read the paper’s discussion of risks and scope to cite a relevant caveat accurately."
  },
  "observation": {
    "pages": [
      {
        "page": 23,
        "text": "triggers an entire series of chat, one can define behaviors more easily than defining each single\nmessage passing event.\n4. When developing a new application with UserProxyAgent, start with humans always in the\nloop, i.e., human input mode=‘ALWAYS’, even if the target operation mode is more autonomous.\nThis could help understand the effectiveness of AssistantAgent, tuning the prompt, discovering\ncorner cases, and debugging. When confident with small-scale success, consider generating diverse\ntest cases by setting human input mode=‘NEVER’, enable LLM as a backend, and either use LLM\nor manually … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 24,
        "text": "mode AutoGen supports could be desirable in many scenarios, a high level of autonomy can also pose\npotential risks, especially in high-risk/stakes applications [4, 50]. As a result, building fail-safes against\ncascading failures and exploitation, mitigating reward hacking, out of control and undesired behaviors,\nmaintaining effective human oversight of applications built with AutoGen agents will become impor-\ntant. While AutoGen provides convenient and seamless involvement of humans through a user proxy\nagent, developers and stakeholders still need to understand and determine the appropriate l … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 6: submit_review · accepted

Evidence inspected supports a framework contribution but only narrow selected evaluations; submit an absolute assessment with that limitation stated.

[Event 31](trace.jsonl#L31)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Evidence inspected supports a framework contribution but only narrow selected evaluations; submit an absolute assessment with that limitation stated.",
    "review": {
      "score": 0.72,
      "summary": "AutoGen presents a flexible infrastructure for building LLM applications as conversations among customizable agents that can combine models, tools, and human participation. Its contribution is a practical, general-purpose framework demonstrated across diverse workflows; evidence is promising but largely illustrative and task-specific rather than a broad validation of general performance.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The framework’s central value is composable, varied agent interaction, with concrete application examples spanning multiple task families.",
          "page": 9,
          "quote": "We present six examples of diverse applications built using AutoGen."
        },
        {
          "kind": "strength",
          "claim": "Some empirical support goes beyond demonstrations: the MiniWob++ comparison reports performance across twelve task types and ten instances per task.",
          "page": 16,
          "quote": "For each clicking task, we reported the success rate for ten different instances."
        },
        {
          "kind": "limitation",
          "claim": "The math comparison is very small and qualitative, so its results provide only weak grounds for broad claims of competitiveness.",
          "page": 10,
          "quote": "We use two level-5 problems from the MATH dataset for the qualitative evaluation and test on each problem for 3 times."
        },
        {
          "kind": "uncertainty",
          "claim": "The report itself identifies optimal workflow design as unresolved, including when multi-agent workflows help and how to choose cost-effective configurations.",
          "page": 23,
          "quote": "For a given task, what is the optimal (e.g., cost-effective) multi-agent workflow?"
        }
      ],
      "unresolved_questions": [
        "How reliably do the framework’s benefits generalize across tasks, model backends, and larger independent evaluations?",
        "What workflow choices provide consistent gains relative to simpler pipelines, and at what cost?",
        "I inspected framework descriptions, selected math and MiniWob++ evidence, and future-work discussion; I did not inspect the full report or all application evaluations, so evidence beyond these passages may affect the assessment."
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
          16
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
      },
      {
        "checker_version": "m2-citations-v2",
        "page_valid": true,
        "quote_nonempty": true,
        "quote_matches": true,
        "citation_verified": true,
        "matching_pages": [
          23
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
