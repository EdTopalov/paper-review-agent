# T11: Executable Code Actions Elicit Better LLM Agents

**agent · ok**

4 model calls · 3 reads · 10.28 s · $0.001932

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.74

Introduces CodeAct, using executable Python as a unified, multi-turn action format, and releases a 7k-trajectory tuning set with CodeActAgent models. Controlled comparisons across 17 LLMs and downstream evaluations provide meaningful evidence that code actions can improve complex tool use and enable useful local agents, though gains vary by model and the central benchmark is small and manually curated.

- **strength**: The multi-turn tool benchmark reports higher success and fewer turns for CodeAct in most tested models, with a notable GPT-4 result.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs), similar to the trend in §2.2."

- **strength**: The finetuned Mistral-based agent shows broad improvements in agent evaluations and several general tasks over the tested open-source baselines.
  - Page 9 · citation: whitespace
  - Quote: "CodeActAgent (both variants) perform better than all evaluated open-source LLMs on both the in-domain and out-of-domain subsets of MINT."

- **limitation**: M3ToolEval's modest, manually curated task set limits how broadly its results establish real-world generality.
  - Page 5 · citation: whitespace
  - Quote: "It contains 82 human-curated instances, spanning tasks including web browsing, finance, travel itinerary planning, science, and information processing."

- **limitation**: The authors identify hallucination and safety of executing code as practical concerns; these are not resolved by the reported evaluations.
  - Page 10 · citation: whitespace
  - Quote: "it may suffer from hallucination commonly seen in LLMs (e.g., imagine the content of a variable without actually printing it out)"

Unresolved questions:

- How robust are the benchmark gains across larger, independently constructed task sets and different tool/environment designs?
- What sandboxing and safety controls are necessary for real deployments, and how effectively do they constrain harmful or unintended code execution?
- How much of CodeActAgent’s gains comes from the action format versus differences in dataset scale, data composition, and training? I inspected pages 1–5 and 8–10, not the full appendices or all methodological details.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — Page 5 reports CodeAct as best on success rate for 12 of 17 models and on average turns for 12 of 17. It also highlights GPT-4-1106-preview’s 20.7 percentage-point success improvement and 2.1 fewer turns.
- Observation 2: **supported** — Page 9 reports both CodeActAgent variants outperforming evaluated open-source models on MINT’s in-domain and out-of-domain subsets. The table on page 8 also shows gains on several tested general tasks, with results varying by baseline and task.
- Observation 3: **supported** — Page 5 describes M3ToolEval as 82 human-curated instances across several domains. The claim that this modest curated set limits how broadly its results establish real-world generality is a reasonable, appropriately scoped inference.
- Observation 4: **supported** — Page 10 identifies hallucination as a limitation and says future work should design better safety mechanisms for code execution in a sandbox. The reported evaluations do not establish that these concerns are resolved.

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: search_paper

Locate main quantitative evaluation claims and benchmark results.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "success rate",
    "reason": "Locate main quantitative evaluation claims and benchmark results."
  },
  "observation": {
    "matches": [
      {
        "page": 1,
        "snippet": "rough multi-turn interactions. Our extensive analysis of 17 LLMs on API-Bank and a newly curated benchmark shows thatCodeAct outperforms widely used alternatives (up to 20% higher success rate). The encouraging performance of CodeAct motivates us to build an open-source LLM agent that interacts with envi- ronments by executing interpretable code and collaborates with users using natural language. To this end, we collect an instruction-tuning dataset CodeActInstruct that consists of 7k multi-turn interactions using CodeAct. We show that it can be used with existing data to improve model"
      },
      {
        "page": 2,
        "snippet": "0 10 20 30 40 50 60 70 gpt-4-1106-preview gpt-4-0613 claude-2 gpt-3.5-turbo-0613 gpt-3.5-turbo-1106 gemini-pro text-davinci-003 Llama-2-70b-chat-hf Success Rate (%) 5 6 7 8 9 10 Average Number of Interaction T urns Action Mode Code as Action JSON as Action T ext as Action Figure 1: Comparison between CodeAct and Text / JSON as action. (top) Illustrative example comparing different actions. (bottom) Quantitative results on M3ToolEval (§2.3). This work proposes CodeAct, a general-purpose framework that allows LLMs to generate executable Python code as acti"
      },
      {
        "page": 3,
        "snippet": "uire intricate coordination and composition of multiple tools. With its strengths in control and data flow, CodeAct achieves up to a 20% absolute improvement over baselines on the success rate of solving the problems while requiring up to 30% fewer actions. These performance gains widen as the capabilities of the LLMs increase (Fig. 1 bottom). The promising performance of CodeAct motivates an open-source LLM agent that can effectively act through CodeAct, and collaborate with humans through natural language. To this end, we collect an instruction-tuning dataset CodeActInstruct consisti"
      },
      {
        "page": 5,
        "snippet": "preview 76.7 82.7 73.4text-davinci-002 69.2 59.6 57.4text-davinci-003 75.4 76.9 69.7 Frequency of Best-Performing Format↑Open-source 4 0 4Closed-source 4 5 0Overall 8 5 4 Table 3: Success rates (higher the better) and average turns required per instance (lower the better) on M 3ToolEval. The best results for each model arebolded, and the second- best ones are underlined. Success Rate (%,↑) Avg. Turns (↓) Format of Action CodeActJSON Text CodeActJSON Text Open-source LLMsCodeLlama-7b-Instruct-hf4.9 2.4 2.4 9.7 9.9 9.9CodeLlama-13b-Instruct-hf4.9 4 .9 4 .9 9.8 9.8 9.7CodeLlama-34b-Instru"
      },
      {
        "page": 5,
        "snippet": "(higher the better) and average turns required per instance (lower the better) on M 3ToolEval. The best results for each model arebolded, and the second- best ones are underlined. Success Rate (%,↑) Avg. Turns (↓) Format of Action CodeActJSON Text CodeActJSON Text Open-source LLMsCodeLlama-7b-Instruct-hf4.9 2.4 2.4 9.7 9.9 9.9CodeLlama-13b-Instruct-hf4.9 4 .9 4 .9 9.8 9.8 9.7CodeLlama-34b-Instruct-hf2.4 0.0 0.0 9.9 10.0 10.0Llama-2-7b-chat-hf 0.0 1 .2 2.4 8 .9 9.5 9.6Llama-2-13b-chat-hf 0.0 0 .0 0 .0 9 .7 10.0 10.0Llama-2-70b-chat-hf11.0 3.7 3.7 9.1 9.8 9.8Mistral-7B-Instruct-v0.10.0 3"
      },
      {
        "page": 5,
        "snippet": " solution. The interaction will terminate when a maximum of 10 interaction turns are reached or a correct solution has been submitted, similar to MINT [53]. Metric. We measure the success rate by calculating the percentage of the model proposed answers that match the ground-truth solutions. We also include the avg. turns metric: the average number of turns on all evaluated instances. Quantitative Results on M3ToolEval. We include full results in Tab. 3 and a subset of results for visualization in Fig. 1. CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs), si"
      },
      {
        "page": 5,
        "snippet": "evaluated instances. Quantitative Results on M3ToolEval. We include full results in Tab. 3 and a subset of results for visualization in Fig. 1. CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs), similar to the trend in §2.2. Moreover, using CodeAct requires a lower average number of turns (12 out of 17 evaluated LLMs). For example, the best model gpt-4-1106-preview achieves a 20.7% absolute improvement compared to the next best action format (text) while requiring2.1 fewer interaction turns on average. However, there is still a significant gap in terms of a"
      },
      {
        "page": 9,
        "snippet": "aluation (i.e., MINT includes ALFWorld and MATH), hence we report separate numbers for MINT’s in- and out-of-domain performance. Unless otherwise specified, we measure MINT tasks’ success rates with interaction turn k = 5 . We also evaluate out-of-domain agent tasks using text actions from MiniWob++ (computer tasks, [21]) and ScienceWorld (text-based simulator for elementary science curriculum, [50]) to test whether CodeActAgent can generalize to different action formats. Finally, we include a suite of general LLM evaluation tasks to assess general capability: MMLU [ 17] for knowledge-"
      }
    ],
    "limit_reached": true
  }
}
```

</details>

### Step 2: read_pages

Inspect framing, benchmark setup, and results supporting the claimed action-format gains.

[Event 10](trace.jsonl#L10)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 3,
    "end": 5,
    "reason": "Inspect framing, benchmark setup, and results supporting the claimed action-format gains."
  },
  "observation": {
    "pages": [
      {
        "page": 3,
        "text": "Table 1: The benefit of CodeAct compared to using Text/JSON for LLM action.\nCodeActfor LLM action JSON or Text for LLM action\nAvailability of Data \"Large quantity of code available1for pre-training%Data curation required for particular format\nComplex Operation(e.g., looping,composition of multiple tools)\"Natively supported via control and data flow%Requires careful engineering if feasible (e.g.,define new tools to mimic if-statement)\nAvailability of Tools \"Can directly use existing software packages2 %Requires human effort to curate tools fromscratch or existing software\nAutomated Feedback \"Fe … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 4,
        "text": "A g e n t\n     A c t i o n\n     O b s e r v a t i o n\nP l a n n i n g\nC h a i n - o f - t h o u g h \nS e l f - R e fl e c t i o \nI m p r o v i n g  A c t i o n  f r o m  \nP r i o r  O b s e r v a t i o \n. . .\nI n i t i a t e  I n t e r a c t i o n\n     T h i n k\nU s e r\nC o n v e r s a t i o n\nE . g . ,  N a t u r a l  L a n g u a g e  \nI n s t r u c t i o n  o r  F e e d b a c k\nC o n v e r s a t i o n\ni n  N a t u r a l  L a n g u a g e\nS t a r t\nE n v i r o n m e n t\nS o f t w a r e  I n t e r f a c e  ( A P I )\nI n t e r f a c e  f o r  C o m p u t e r\nI n f o r m a t i o n  S e e k i n g\n … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 5,
        "text": "Table 2: Atomic API call correctness\non API-Bank [24] with different action\nformat. The best performance is bolded,\nand the second-best is underlined.\nCorrectness(%,↑)Format of Action CodeActJSON Text\nOpen-source LLMsCodeLlama-7b-Instruct-hf12.5 12.0 17.0CodeLlama-13b-Instruct-hf11.8 7.8 14.0CodeLlama-34b-Instruct-hf17.3 12.0 16 .8Llama-2-7b-chat-hf 28.8 11.3 25 .8Llama-2-13b-chat-hf 38.1 8.5 37 .3Llama-2-70b-chat-hf 35.6 14.3 37.6Mistral-7B-Instruct-v0.12.5 2.3 3.0lemur-70b-chat-v1 58.6 46.6 56 .1\nClosed-source LLMsclaude-2 76.7 59.4 73 .7claude-instant-1 75.2 64.9 73 .2gemini-pro 70.4 73.2 7 … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 3: read_pages

Review training-data and downstream agent evaluation evidence and scope.

[Event 15](trace.jsonl#L15)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 8,
    "end": 10,
    "reason": "Review training-data and downstream agent evaluation evidence and scope."
  },
  "observation": {
    "pages": [
      {
        "page": 8,
        "text": "Table 4: Statistics of our training mixture and comparison with prior work. Please refer to §3.1 and\n§3.1 for details about CodeActInstruct and general conversation data. Token statistics are computed\nusing Llama-2 tokenizer.\nData Mixture Data Type Data Name # of Data Instances # of Total Tokens Avg. Tokens Per Instance\nPrior Work - FireAct [6] 2,063 542 ,176 262 .81- AgentInstruct [65] 1,866 2 ,517,785 1349 .30\nCodeActInstruct(Ours)\nInformation Seeking HotpotQA [59] 1,664 2 ,472,227 1485 .71Software Packages (Tool) MATH (Math, [18])1,732 1 ,719,467 992 .76Software Packages (Tool) APPS (Code,  … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 9,
        "text": "3.2 CodeActAgent\nWe fine-tune Llama-2 7B [47] and Mistral 7B [ 20] on a mixture of CodeActInstruct and general\nconversations (Tab. 4) to obtain CodeActAgent.\nTraining Setup. We perform full-parameter supervised fine-tuning with a sequence length of 4,096\ntokens for Llama-2 and 16,384 for Mistral. Please refer to §D for more details.\nEvaluation Setup. We use MINT [ 53] to evaluate LLMs with CodeAct on a diverse range of\nagent tasks. CodeActAgent has some training domains overlapping with MINT’s evaluation (i.e.,\nMINT includes ALFWorld and MATH), hence we report separate numbers for MINT’s in- a … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 10,
        "text": "focusing on tool usage [40], interaction [9], and social skills [28]. CodeActInstruct aligns with the\nlatter approach and creates datasets using stronger LLMs due to limited resources for annotation.\n5 Conclusions\nThis work introduces CodeAct that employs executable Python code for the LLM agent’s action,\nwhich is advantageous over using text or JSON action, especially in complex scenarios. We collect\nCodeAct-focused multi-turn interaction trajectories CodeActInstruct for instruction tuning, and train\nCodeActAgent that is specially designed for seamless integration with Python and can execute\n … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 4: submit_review · accepted

Evidence covers core proposal, benchmark comparisons, downstream tuning evaluation, and explicit limitations; submit a balanced assessment.

[Event 20](trace.jsonl#L20)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Evidence covers core proposal, benchmark comparisons, downstream tuning evaluation, and explicit limitations; submit a balanced assessment.",
    "review": {
      "score": 0.74,
      "summary": "Introduces CodeAct, using executable Python as a unified, multi-turn action format, and releases a 7k-trajectory tuning set with CodeActAgent models. Controlled comparisons across 17 LLMs and downstream evaluations provide meaningful evidence that code actions can improve complex tool use and enable useful local agents, though gains vary by model and the central benchmark is small and manually curated.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The multi-turn tool benchmark reports higher success and fewer turns for CodeAct in most tested models, with a notable GPT-4 result.",
          "page": 5,
          "quote": "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs), similar to the trend in §2.2."
        },
        {
          "kind": "strength",
          "claim": "The finetuned Mistral-based agent shows broad improvements in agent evaluations and several general tasks over the tested open-source baselines.",
          "page": 9,
          "quote": "CodeActAgent (both variants) perform better than all evaluated open-source LLMs on both the in-domain and out-of-domain subsets of MINT."
        },
        {
          "kind": "limitation",
          "claim": "M3ToolEval's modest, manually curated task set limits how broadly its results establish real-world generality.",
          "page": 5,
          "quote": "It contains 82 human-curated instances, spanning tasks including web browsing, finance, travel itinerary planning, science, and information processing."
        },
        {
          "kind": "limitation",
          "claim": "The authors identify hallucination and safety of executing code as practical concerns; these are not resolved by the reported evaluations.",
          "page": 10,
          "quote": "it may suffer from hallucination commonly seen in LLMs (e.g., imagine the content of a variable without actually printing it out)"
        }
      ],
      "unresolved_questions": [
        "How robust are the benchmark gains across larger, independently constructed task sets and different tool/environment designs?",
        "What sandboxing and safety controls are necessary for real deployments, and how effectively do they constrain harmful or unintended code execution?",
        "How much of CodeActAgent’s gains comes from the action format versus differences in dataset scale, data composition, and training? I inspected pages 1–5 and 8–10, not the full appendices or all methodological details."
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
