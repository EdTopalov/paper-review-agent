# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**agent · ok**

6 model calls · 5 reads · 13.88 s · $0.003218

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.74

AGENTLESS presents a deliberately simple repository-repair pipeline—hierarchical code localization followed by sampled patch generation, regression-test filtering, and majority voting—and shows that this design can perform competitively on SWE-bench Lite at low reported inference cost. Its useful additional contribution is a manual classification of benchmark problems and a filtered 252-problem variant, though comparative claims remain bounded by the benchmark and by reliance on reported baseline results.

- **strength**: The method is clearly specified as a practical two-stage system, and combines localization with patch selection rather than relying on autonomous tool-use planning.
  - Page 5 · citation: exact
  - Quote: "AGENTLESS solves repository-level issues using a simple step-by-step procedure."

- **strength**: On the original benchmark, the paper reports 82 resolved problems (27.33%) at $0.34 average cost; its ablations indicate gains from multi-sampling/voting and test filtering.
  - Page 8 · citation: whitespace
  - Quote: "Finally, the fullAGENTLESS performance is achieved by further applying filtering to select only the patches which can successfully pass the existing regressions tests."

- **strength**: The authors identify concrete benchmark-quality concerns and provide a filtered evaluation set; AGENTLESS resolves 71/252 (28.17%) there.
  - Page 10 · citation: exact
  - Quote: "We refer to our subset of 252 problems as SWE-bench Lite-S."

- **limitation**: Comparisons on the filtered set are not fully controlled: the authors could not rerun commercial systems on it, so their outcomes derive from excluding cases in prior reported results.
  - Page 10 · citation: whitespace
  - Quote: "as we are not able to run commercial tools ourselves on the modified problems, we simply exclude the problematic problems in the below evaluation."

Unresolved questions:

- How robust are the reported rankings and cost advantages across other repository-level benchmarks, model versions, and independently rerun baselines?
- Would the filtered Lite-S classifications and performance hold under independent annotation or a larger benchmark?
- I inspected the method, selected results and analysis pages, but not the full paper's appendices or implementation details; reproducibility and sensitivity beyond the reported setup remain uncertain.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes a two-phase localization-and-repair pipeline, with hierarchical localization and patch generation, filtering, and voting; it contrasts this with agent-based tool-use planning (PDF pp. 2–5).
- Observation 2: **supported** — The paper reports 82/300 resolved (27.33%) and $0.34 average cost (PDF pp. 6–7). Its ablation reports 70 fixes with one sample, 78 with multiple samples and majority voting, and 82 after test filtering (PDF p. 8).
- Observation 3: **supported** — The authors report a manual classification of SWE-bench Lite issues and define Lite-S as a 252-problem subset; Table 4 reports 71 resolved (28.17%) by AGENTLESS (PDF pp. 9–10).
- Observation 4: **supported** — The paper explicitly says it could not run commercial tools on the modified problems and instead excluded problematic cases from their prior results for the Lite-S evaluation (PDF p. 10).

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: search_paper

Locate the paper's evaluation setup and claims for assessing evidence.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "SWE-bench Lite-S",
    "reason": "Locate the paper's evaluation setup and claims for assessing evidence."
  },
  "observation": {
    "matches": [
      {
        "page": 3,
        "snippet": "3%) with missing critical information needed to solve the issue, and problems (4.3%) that include misleading solutions in the issue description. Recognizing these issues, we built SWE-bench Lite-S, which removes such problematic problems, and serves as a more rigor- ous benchmark to evaluate the ability to solve real-world software development problems. Overall, in an era focused on achieving top placements on leaderboards, our work highlights the overlooked potential of a simplistic, interpretable technique in autonomous software development. We hope AGENTLESS will help reset the baseline"
      },
      {
        "page": 10,
        "snippet": "ssification can provide additional insights on the type of problems that can be solved by existing and future approaches. 5.2 SWE-bench Lite- S Table 4: Performance and ranking on SWE-bench Lite-S. * indicates a tie in ranking. Tool LLM SWE-bench Lite SWE-bench Lite- S % Resolved Rank % Resolved Rank Alibaba Lingma Agent [7] GPT-4o+ Claude-3.5 99 (33.00%) 1 87 (34.52%) 1 Factory Code Droid [5] NA 94 (31.33%) 2 82 (32.54%) 2 AutoCodeRover-v2 [3] GPT-4o 92 (30.67%) 3 79 (31.35%) 3 CodeR [17] GPT-4 85 (28.33%) 4 72 (28.57%) 4 IBM Research Agent-101 [6] NA 80 (26.67%) 6 66 (26.19%) 7 OpenCSG S"
      },
      {
        "page": 10,
        "snippet": " not able to run commercial tools ourselves on the modified problems, we simply exclude the problematic problems in the below evaluation. We refer to our subset of 252 problems as SWE-bench Lite-S. Table 4 shows the results on the SWE-bench Lite- S benchmark and the corresponding ranking of each approach. We also included the results on the original 300 problems in SWE-bench Lite for comparison. While the general ranking of all approaches stay roughly the same, we do observe some small ranking changes. Compared to the original SWE-bench Lite, our filtered benchmark of SWE-bench Lite-S prov"
      },
      {
        "page": 10,
        "snippet": "on. While the general ranking of all approaches stay roughly the same, we do observe some small ranking changes. Compared to the original SWE-bench Lite, our filtered benchmark of SWE-bench Lite-S provides a more accurate reflection of the true capability of autonomous software development tools. 10"
      },
      {
        "page": 11,
        "snippet": "e keywords none (c) Location information Figure 6: Solve rate of selected approaches (orange means open-source while indigo means closed-source) on different problem categories in SWE-bench Lite-S. Red dotted line indi- cates the average solve rate on the entire SWE-bench Lite-S for each approach. Using the classification results, we further examine the types of problems that are solved by AGENTLESS and prior approaches on SWE-bench Lite-S. Figure 6 shows the solve rate of various top-performing open-source and closed-source approaches across the different categories of problems. We first "
      },
      {
        "page": 11,
        "snippet": "s (orange means open-source while indigo means closed-source) on different problem categories in SWE-bench Lite-S. Red dotted line indi- cates the average solve rate on the entire SWE-bench Lite-S for each approach. Using the classification results, we further examine the types of problems that are solved by AGENTLESS and prior approaches on SWE-bench Lite-S. Figure 6 shows the solve rate of various top-performing open-source and closed-source approaches across the different categories of problems. We first examine if having code examples to reproduce the error in the issue description can"
      },
      {
        "page": 11,
        "snippet": "e on the entire SWE-bench Lite-S for each approach. Using the classification results, we further examine the types of problems that are solved by AGENTLESS and prior approaches on SWE-bench Lite-S. Figure 6 shows the solve rate of various top-performing open-source and closed-source approaches across the different categories of problems. We first examine if having code examples to reproduce the error in the issue description can help the LLM better solve the issue in Figure 6a. Surprisingly, we found that the solve rate of all prior approaches drop when evaluated on the problems with repro"
      },
      {
        "page": 12,
        "snippet": "are also problems containing misleading patches, which can confuse the model. Recognizing these limitations, we further filter SWE-bench Lite to remove such problems and construct SWE-bench Lite-S that can serve as a more rigorous set of problems to evaluate different tools. Agent-based software development. With the emergence and popularity of agent-based frameworks [56], recently researchers and industry practitioners have begun developing agent-based approaches to solve software engineering tasks. Devin [4] (and OpenDevin [10], open-source alternative), is one of the first end-to-end LL"
      }
    ],
    "limit_reached": true
  }
}
```

</details>

### Step 2: read_pages

Inspect method details and reported experimental evidence.

[Event 10](trace.jsonl#L10)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 4,
    "end": 6,
    "reason": "Inspect method details and reported experimental evidence."
  },
  "observation": {
    "pages": [
      {
        "page": 4,
        "text": "specific lines). For the repair phase, we provide the code snippets at these edit locations\ntogether with the issue description and 5 ask the LLM to sample multiple patches to solve\nthe issue. Next, 6 we perform a simple filtering to remove any patches with syntax errors\nand regression test failures, and use majority voting to rank the remaining patches. Finally,\n7 AGENTLESS selects the top-ranked patch as the final patch for submission. We now\ndescribe the steps in each of AGENTLESS ’s two phases in more detail.\n2.1 Localization\nTo fix or implement a new feature, the first step is to obtain t … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 5,
        "text": "simple hierarchical localization process allows AGENTLESS to select a set of relevant code\nsnippets as edit locations to perform repair.\n2.2 Repair\n<<<<<<< SEARCH\nfrom flask import Flask\n=======\nimport math\nfrom flask import Flask\n>>>>>>> REPLACE\nҎҎɷ \nfrom flask import Flask\napp = Flask(ҎʢnameҎʢ)\n@app.route(\"/\")\nҎҎɷ\nҎҎɷ\n+ import math\nfrom flask import Flask\napp = Flask(ҎʢnameҎʢ)\n@app.route(\"/\")\nҎҎɷ\n<<<<<<< SEARCH\nfrom flask import Flask\nimport math\nfrom flask import Flask\n>>>>>>> REPLACE\nSearch/Replace Diff\nOriginal File\n+ import math\nGenerate \nSearch/Replace\nDiff to fix issue\nIssue:\nLambdify  … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 6,
        "text": "3 Experimental Setup\nDatasets. We evaluate AGENTLESS and baselines using the popular SWE-bench dataset\nto test the ability to solve real-world software engineering issues. Each problem in SWE-\nbench requires submitting a patch to solve the underlying issue described in the input issue\ndescription. In particular, we focus on the filtered subset SWE-bench Lite, containing 300\nproblems with tests to evaluate the functional correctness of submitted patch. Furthermore,\nwe also conduct a detailed study (Section 5.1) on the SWE-bench Lite benchmark to not\nonly demonstrate potential issues and biases  … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 3: read_pages · invalid_page_range

Inspect result comparisons, cost evidence, and benchmark filtering rationale.

[Event 15](trace.jsonl#L15)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 7,
    "end": 10,
    "reason": "Inspect result comparisons, cost evidence, and benchmark filtering rationale."
  },
  "observation": {
    "error": "invalid_page_range",
    "page_count": 17,
    "hint": "Use 1-based pages and request at most 3 pages."
  }
}
```

</details>

### Step 4: read_pages

Read results and benchmark limitations to ground the assessment.

[Event 20](trace.jsonl#L20)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 7,
    "end": 9,
    "reason": "Read results and benchmark limitations to ground the assessment."
  },
  "observation": {
    "pages": [
      {
        "page": 7,
        "text": "Table 1: Results on SWE-bench Lite. Note:\n indicates approaches that are closed-source\n(i.e., source code is not released). '-' indicates that the relevant information to compute this\nhas not been released.\nTool LLM % Resolved Avg.\n$ Cost\nAvg.\n# Tokens\n% Correct Location\nLine Function File\nAlibaba Lingma Agent [7]\n GPT-4o+\nClaude-3.5 99 (33.00%) - - 40.0% 58.7% 75.0%\nFactory Code Droid [5]\n NA 94 (31.33%) - - 36.7% 55.7% 72.7%\nAutoCodeRover-v2 [3]\n GPT-4o 92 (30.67%) - - 35.0% 52.3% 69.3%\nCodeR [17]\n GPT-4 85 (28.33%) $3.34 323,802 35.7% 52.3% 67.0%\nIBM Research Agent-101 [6]\nNA 80 (26.67%) -  … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 8,
        "text": "the solve rate. Interestingly, the highest result in terms of file-level location is OpenCSG\nStarShip at 90.0%, significantly higher than even the best-performing approaches while\nat the same time having a relatively low solve rate (23.67%). As OpenCSG StarShip is a\ncommercial product that does not provide source code or detailed trajectories, it is difficult\nto explain this huge difference between localization and repair performance. In terms of\nlocalization performance, by using our simple hierarchical approach, AGENTLESS remains\nvery competitive compared with previous agent-based approaches … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 9,
        "text": "Contains\npartial\nreproducible\nexample8.7%\nContains\nreproducible\nexample\n54.7%\nInfo in NL\n27.3%\nNot enough\ninfo\n9.3%\n(a) Description quality\nNo\nsolution\n73.7%\nMisleading4.3%\nExact\npatch\n4.3%\nSome steps\nin NL\n7.7%\nComplete steps\nin NL\n10.0% (b) Solution in description\nLine Function File Overall0\n20\n40\n60\n80\n100Percentage\n90.3%\n68.0%\n50.0% 39.3%\n3.0%\n6.7%\n13.7%\n13.7%\n6.7%\n13.7%\n15.3%\n24.7%\n11.7%\n21.0% 22.3%\nNone\nStack trace\nNatural language\nKeywords (c) Location information\nFigure 5: Categorization and corresponding breakdown of the SWE-bench Lite problems.\nproblem. Below describes each of classi … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 5: read_pages

Check filtered benchmark results and stated limitations before final scoring.

[Event 25](trace.jsonl#L25)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 10,
    "end": 12,
    "reason": "Check filtered benchmark results and stated limitations before final scoring."
  },
  "observation": {
    "pages": [
      {
        "page": 10,
        "text": "as we increase the granularity to functions and files where we found that around half of\nthe issues already provide the location of the file needed to be edited in the description. To\nrepair a bug or introduce a new feature, finding the location to make the edit is extremely\nimportant. As such, we leverage this classification and focus our later analysis on the effect\nthe provided location has on the repair performance ofAGENTLESS and baseline approaches.\nThese classification dimensions and categories raise potential issues with the SWE-bench\nLite problems such as unsolvable questions, mislead … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 11,
        "text": "AutoCodeRover\nSWE-agent-GPT4\nAider Lingma\nFactoryDroidAutoCodeRover-v2 Agentless\n0.0\n0.1\n0.2\n0.3\n0.4Solve rate\nw/o reproducible examples\nw/ reproducible examples\n(a) Description quality\nAutoCodeRover\nSWE-agent-GPT4\nAider Lingma\nFactoryDroidAutoCodeRover-v2 Agentless\n0.0\n0.1\n0.2\n0.3\n0.4\n0.5Solve rate\ncontains NL steps\nwithout steps (b) Solution in description\nAutoCodeRover\nSWE-agent-GPT4\nAider Lingma\nFactoryDroidAutoCodeRover-v2 Agentless\n0.0\n0.1\n0.2\n0.3\n0.4\n0.5Solve rate\nin NL\nin stack trace\nkeywords\nnone (c) Location information\nFigure 6: Solve rate of selected approaches (orange means open-s … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 12,
        "text": "the correctness of LLM outputs. Furthermore, other benchmarks have been proposed with\nmore robust test [37], additional programming languages [66, 16], and other programming\ndomains [26, 23, 36, 32, 62].\nMore recently, instead of evaluating on self-contained coding problems, researchers have de-\nveloped benchmarks focus on solving real-world software engineering issues by operating\non an entire coding repository [28, 63, 38]. One such popular benchmark is SWE-bench [28],\ncontaining problems where the goal is to modify the repository and resolve a real-world\nGitHub issue. The authors of SWE-ben … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 6: submit_review · accepted

Evidence covers the method, benchmark performance, ablations, and filtered-set caveats; submit an independent paper assessment.

[Event 31](trace.jsonl#L31)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Evidence covers the method, benchmark performance, ablations, and filtered-set caveats; submit an independent paper assessment.",
    "review": {
      "score": 0.74,
      "summary": "AGENTLESS presents a deliberately simple repository-repair pipeline—hierarchical code localization followed by sampled patch generation, regression-test filtering, and majority voting—and shows that this design can perform competitively on SWE-bench Lite at low reported inference cost. Its useful additional contribution is a manual classification of benchmark problems and a filtered 252-problem variant, though comparative claims remain bounded by the benchmark and by reliance on reported baseline results.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The method is clearly specified as a practical two-stage system, and combines localization with patch selection rather than relying on autonomous tool-use planning.",
          "page": 5,
          "quote": "AGENTLESS solves repository-level issues using a simple step-by-step procedure."
        },
        {
          "kind": "strength",
          "claim": "On the original benchmark, the paper reports 82 resolved problems (27.33%) at $0.34 average cost; its ablations indicate gains from multi-sampling/voting and test filtering.",
          "page": 8,
          "quote": "Finally, the fullAGENTLESS performance is achieved by further applying filtering to select only the patches which can successfully pass the existing regressions tests."
        },
        {
          "kind": "strength",
          "claim": "The authors identify concrete benchmark-quality concerns and provide a filtered evaluation set; AGENTLESS resolves 71/252 (28.17%) there.",
          "page": 10,
          "quote": "We refer to our subset of 252 problems as SWE-bench Lite-S."
        },
        {
          "kind": "limitation",
          "claim": "Comparisons on the filtered set are not fully controlled: the authors could not rerun commercial systems on it, so their outcomes derive from excluding cases in prior reported results.",
          "page": 10,
          "quote": "as we are not able to run commercial tools ourselves on the modified problems, we simply exclude the problematic problems in the below evaluation."
        }
      ],
      "unresolved_questions": [
        "How robust are the reported rankings and cost advantages across other repository-level benchmarks, model versions, and independently rerun baselines?",
        "Would the filtered Lite-S classifications and performance hold under independent annotation or a larger benchmark?",
        "I inspected the method, selected results and analysis pages, but not the full paper's appendices or implementation details; reproducibility and sensitivity beyond the reported setup remain uncertain."
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
