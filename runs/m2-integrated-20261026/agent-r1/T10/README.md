# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**agent · ok**

5 model calls · 4 reads · 11.56 s · $0.001975

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.76

SWE-agent makes a substantial, practically relevant contribution by treating the agent-computer interface as a design variable for repository-level software engineering. Its custom search, editing, feedback, and context-management tools are evaluated on SWE-bench and supported by interface ablations, showing notable gains over the tested shell-only and retrieval baselines. The evidence is meaningful but bounded to two leading closed models and the benchmark/setup described; the paper also reports persistent inefficient agent behavior.

- **strength**: The paper articulates a coherent ACI design methodology, emphasizing simplicity, efficient actions, informative feedback, and guardrails.
  - Page 3 · citation: exact
  - Quote: "Environment feedback should be informative."

- **strength**: The reported benchmark results show a clear improvement over the tested baselines, with interface ablations supporting the claim that design choices matter.
  - Page 6 · citation: exact
  - Quote: "w/ GPT-4 Turbo 12.47 1.59 18.00 1.67"

- **limitation**: The main reported results are restricted to two leading models; transfer of the ACI findings to other models is not established by the evaluated results described here.
  - Page 5 · citation: exact
  - Quote: "All results, ablations, and analysis are based on two leading LMs"

- **limitation**: The behavioral analysis identifies a potentially important persistence failure: agents often continue a routine without recognizing dead ends or changing approach.
  - Page 8 · citation: whitespace
  - Quote: "agents rarely deviate from this pattern but they rarely recognize dead ends or reset their problem solving approach."

Unresolved questions:

- How well do the ACI principles and performance gains transfer to other model families, open models, or substantially different software engineering tasks?
- Which individual ACI components contribute most reliably across repositories and tasks, beyond the reported Lite ablations?
- Inspection covered pages 1–9, including the main design, results, and discussion, but not pages 10–25 (including appendices); implementation details and any further caveats or analyses there remain unassessed.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — Page 3 explicitly lays out the four principles—simple actions, efficient actions, informative feedback, and guardrails—and relates them to the interface design and ablations.
- Observation 2: **supported** — Pages 5–7 report SWE-agent results against the tested baselines and Lite ablations; for example, page 6 shows 18.0% resolved versus 11.0% for the shell-only agent on SWE-bench Lite, with several ablations performing worse than the full interface.
- Observation 3: **supported** — Page 5 says the results, ablations, and analysis use two models. The paper does report results with both GPT-4 Turbo and Claude 3 Opus (pages 2 and 6), but does not establish transfer to additional model families.
- Observation 4: **supported** — Page 8 reports from manual inspection that agents rarely deviate from the repeated edit-and-test pattern and rarely recognize dead ends or reset their approach.

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: search_paper

Locate the paper’s stated scope boundaries or limitations for a balanced assessment.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "limitations",
    "reason": "Locate the paper’s stated scope boundaries or limitations for a balanced assessment."
  },
  "observation": {
    "matches": [
      {
        "page": 3,
        "snippet": "designing the ACI to achieve better performance. This means that we shape the available actions, their documentation, and the environment feedback to complement a language model’s limitations and abilities. We use two ap- proaches to enhance the ACI on a development set: We manually inspect the behaviour of the agent to identify difficulties and propose improvements, and we run a grid search over ACI configurations. This leads us to several observations on what makes for effective ACIs: 1. Actions should be simple and easy to understand. Many bash commands have documentation that incl"
      },
      {
        "page": 3,
        "snippet": "a file was removed or an edit was applied if no automatic confirmation is given. We show that LMs are substantially more effective when using interfaces built with their needs and limitations in mind. SWE-agent overcomes these challenges by introducing powerful, tailored tools to provide agents with a simplified interface to the computer; i.e. the agent-computer interface (ACI). A well-designed ACI should help the agent understand the state of the repository given the previous changes. It should also help the agent recover from mistakes, remove unnecessary context from prior observati"
      },
      {
        "page": 9,
        "snippet": "ogous to the synergy between human-computer interaction (HCI) and psychology (Carroll, 1997). Humans and LMs have different characteristics, training objectives, specialities, and limitations (Griffiths, 2020; McCoy et al., 2023), and the interface design processes can be seen as systematic behavioral experimentation that could reveal more insights into these differences, and establish a comparative understanding of human and artificial intelligence. 9"
      },
      {
        "page": 10,
        "snippet": "d Fang, Rohan Bindu, Akul Gupta, Qiusi Zhan, and Daniel Kang. Llm agents can au- tonomously hack websites, 2024. Thomas L Griffiths. Understanding human intelligence through human limitations. Trends in Cog- nitive Sciences, 24(11):873–883, 2020. Yu Gu, Yiheng Shu, Hao Yu, Xiao Liu, Yuxiao Dong, Jie Tang, Jayanth Srinivasa, Hugo Latapie, and Yu Su. Middleware for llms: Tools are instrumental for language agents in complex environments, 2024. Dan Hendrycks, Steven Basart, Saurav Kadavath, Mantas Mazeika, Akul Arora, Ethan Guo, Collin Burns, Samir Puranik, Horace He, Dawn Song, and Jaco"
      }
    ],
    "limit_reached": false
  }
}
```

</details>

### Step 2: read_pages

Inspect core ACI design and benchmark methodology/results to assess novelty and support.

[Event 10](trace.jsonl#L10)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 3,
    "end": 5,
    "reason": "Inspect core ACI design and benchmark methodology/results to assess novelty and support."
  },
  "observation": {
    "pages": [
      {
        "page": 3,
        "text": "Preprint\nIn this paper, we keep the language model fixed, and we focus on designing the ACI to achieve\nbetter performance. This means that we shape the available actions, their documentation, and the\nenvironment feedback to complement a language model’s limitations and abilities. We use two ap-\nproaches to enhance the ACI on a development set: We manually inspect the behaviour of the agent\nto identify difficulties and propose improvements, and we run a grid search over ACI configurations.\nThis leads us to several observations on what makes for effective ACIs:\n1. Actions should be simple and ea … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 4,
        "text": "Preprint\nObserv a tion (File Vie w er)\n4 0 1 :\n4 0 2 :\n4 0 3 :\n4 0 4 :\n4 0 5 :\n4 0 6 :\n4 0 7 :\n4 0 8 :\n4 0 9 :\n[ F i l e :   ( 3 0 9 3  l i n e s  t o t a l ) ]\n s o l v e r s / d i o p h a n t i n e . p y\n( 4 0 0  l i n e s  a b o v e )\n        \n( 2 6 8 4  l i n e s  b e l o w )\n     t o t a l _ d e g r e e   3 :\n        d i o p _ t y p e   \n     t o t a l _ d e g r e e   3 :\n        i f  a l l c o e f f k   1 :\n            d i o p _ t y p e   \n     d i o p _ t y p e   N o n e :\n        r e t u r n  v a r ,  c o e f f ,  d i o p _ t y p e\ne l i f = =\n=\ne l i f >\n= =\n=\ni f i s  n o t\n\" c u b i … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 5,
        "text": "Preprint\nsuccessfully and did not produce any output” is included to enhances clarity. To further improve\ncontext relevance, observations preceding the last 5 are each collapsed into a single line. By remov-\ning most of the content from prior observations, we maintain essential information about the plan\nand action history while reducing unnecessary content, which allows for more interaction cycles and\navoids showing outdated file content. More on the implementation is provided in Appendix A.\n4 E XPERIMENTAL SETUP\nDatasets. We evaluate on the SWE-bench dataset, which includes 2,294 task instan … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 3: read_pages

Review quantitative comparisons and ablation evidence, including experimental outcomes.

[Event 15](trace.jsonl#L15)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 6,
    "end": 7,
    "reason": "Review quantitative comparisons and ablation evidence, including experimental outcomes."
  },
  "observation": {
    "pages": [
      {
        "page": 6,
        "text": "Preprint\nTable 1: Main results for SWE-agent performance on the full and Lite splits of the SWE-bench\ntest set. We benchmark models in the SWE-agent, Basic CLI, and Retrieval Augmented Generation\n(RAG) settings established in SWE-bench (Jimenez et al., 2024).\nSWE-bench SWE-bench Lite\nModel % Resolved $ Avg. Cost % Resolved $ Avg. Cost\nRAG\nw/ GPT-4 Turbo 1.31 0.13 2.67 0.13\nw/ Claude 3 Opus 3.79 0.25 4.33 0.25\nShell-only agent\nw/ GPT-4 Turbo - - 11.00 1.46\nw/o Demonstration - - 7.33 0.79\nSWE-agent\nw/ GPT-4 Turbo 12.47 1.59 18.00 1.67\nw/ Claude 3 Opus 10.46 2.59 13.00 2.18\nw/ GPT-4’s performance … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 7,
        "text": "Preprint\nlarge number of search results, agents tend to look through every match exhaustively, callingnext,\nuntil each result has been inspected. This inefficient behavior can exhaust an agent’s cost budget\nor context window, leading to performance even worse than the Shell-only setting ( 15.7%↓ 2.3 for\nShell-only vs. 12.0%↓ 6.0 with Iterative search).\n T o fix the issue, w e need t o modify\nthe `Ma thema ticaP arser` class...\n \n$ sed  -i  \"/#  trig/i  \\'λ':'Symbol(\\\"λ\\\")'...\"\n I’ll use cat t o displa y `s ymp y /\nparsing/ ma thema tica.p y`...\n \n$ cat parsing/mathematica.py\nFile Cont ent (~10 … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 4: read_pages

Inspect conclusion and discussion for declared implications or scope caveats.

[Event 20](trace.jsonl#L20)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 8,
    "end": 9,
    "reason": "Inspect conclusion and discussion for declared implications or scope caveats."
  },
  "observation": {
    "pages": [
      {
        "page": 8,
        "text": "Preprint\nTable 3: The 10 most frequently\noccurring patterns in trajectories of\nresolved task instances by SWE-\nagent w/ GPT-4. We define a pat-\ntern as 3 consecutive actions.\nPattern Count\nedit (3x) 308\ncreate,edit,python 215\nedit,python,edit 196\nedit,python,rm 157\npython,rm,submit 142\npython,edit,python 125\nedit,edit,python 122\nopen,search file,goto 107\nedit,python,find file 98\nsearch file,goto,edit 82\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n25\n26\n27\n28\n29\n30\n31\n32\n33\n34\n35\n36\n37\n38\nTurn\n0\n50\n100\n150\n200\n250Frequency\nDistribution of Actions per Turn\nsearch dir\nsearch  … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 9,
        "text": "Preprint\ndemonstrated that software engineering (SE) can serve as a diverse, challenging testbed for LM\nevaluation (Zhang et al., 2023; Jimenez et al., 2024; Liu et al., 2024a). Repository-level code editing\nintroduces many reasoning challenges grounded in real SE subtasks such as spotting errant code,\nidentifying cross-file relationships, and understanding codebase-specific symbols and conventions.\nAs a field, SE has generally studied tasks in a more isolated manner; prior benchmarks tend to frame\nproblems in isolation from the rest of a codebase (Just et al., 2014; Karampatsis & Sutton, 2019 … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 5: submit_review · accepted

Evidence covers the contribution, benchmark results, interface ablations, and reported agent behavior; submit a balanced review while noting evaluation scope.

[Event 25](trace.jsonl#L25)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Evidence covers the contribution, benchmark results, interface ablations, and reported agent behavior; submit a balanced review while noting evaluation scope.",
    "review": {
      "score": 0.76,
      "summary": "SWE-agent makes a substantial, practically relevant contribution by treating the agent-computer interface as a design variable for repository-level software engineering. Its custom search, editing, feedback, and context-management tools are evaluated on SWE-bench and supported by interface ablations, showing notable gains over the tested shell-only and retrieval baselines. The evidence is meaningful but bounded to two leading closed models and the benchmark/setup described; the paper also reports persistent inefficient agent behavior.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The paper articulates a coherent ACI design methodology, emphasizing simplicity, efficient actions, informative feedback, and guardrails.",
          "page": 3,
          "quote": "Environment feedback should be informative."
        },
        {
          "kind": "strength",
          "claim": "The reported benchmark results show a clear improvement over the tested baselines, with interface ablations supporting the claim that design choices matter.",
          "page": 6,
          "quote": "w/ GPT-4 Turbo 12.47 1.59 18.00 1.67"
        },
        {
          "kind": "limitation",
          "claim": "The main reported results are restricted to two leading models; transfer of the ACI findings to other models is not established by the evaluated results described here.",
          "page": 5,
          "quote": "All results, ablations, and analysis are based on two leading LMs"
        },
        {
          "kind": "limitation",
          "claim": "The behavioral analysis identifies a potentially important persistence failure: agents often continue a routine without recognizing dead ends or changing approach.",
          "page": 8,
          "quote": "agents rarely deviate from this pattern but they rarely recognize dead ends or reset their problem solving approach."
        }
      ],
      "unresolved_questions": [
        "How well do the ACI principles and performance gains transfer to other model families, open models, or substantially different software engineering tasks?",
        "Which individual ACI components contribute most reliably across repositories and tasks, beyond the reported Lite ablations?",
        "Inspection covered pages 1–9, including the main design, results, and discussion, but not pages 10–25 (including appendices); implementation details and any further caveats or analyses there remain unassessed."
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
          5
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
          8
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
