# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**agent · ok**

5 model calls · 4 reads · 10.71 s · $0.001680

[Structured trace](trace.jsonl). Model request inputs store only new messages; `paper_review.trace.read_events` reconstructs complete requests.

## Review · score 0.73

InterCode contributes a practical framework and benchmark formulation for interactive code generation, pairing code actions with execution feedback in containerized environments. Its Bash and SQL implementations and model evaluations demonstrate that the testbed is usable and expose meaningful benefits and failure patterns of interaction, though empirical breadth and task coverage remain limited.

- **strength**: The paper defines a modular interactive coding framework with execution-based feedback and customizable task-specific rewards, supporting extension beyond the supplied environments.
  - Page 4 · citation: whitespace
  - Quote: "InterCode exposes a reward function endpoint that has access to both the interaction history and the execution container, allowing for custom reward function definitions that can incorporate multiple signals."

- **strength**: Reported evaluations show substantial gains from iterative feedback for multiple models, especially on SQL, supporting benchmark viability and the value of interaction.
  - Page 7 · citation: exact
  - Quote: "gpt-4 19.8 7.2 4.6 3.0 9.1 87.5 76.7 66.7 52.4 73.7"

- **limitation**: The implemented benchmark has narrow language and dataset coverage, and the CTF demonstration is too small for broad evaluation.
  - Page 9 · citation: whitespace
  - Quote: "At this time, the number of InterCode based environments is limited to SQL and Bash action spaces and datasets"

- **uncertainty**: The paper says execution is sandboxed, but its own discussion warns the Bash and SQL environments lack strict action-space restrictions; safety of direct transfer is not established.
  - Page 26 · citation: exact
  - Quote: "do not explicitly impose any strict limitations on the action space."

Unresolved questions:

- How well do results generalize to additional programming languages, datasets, and independently authored tasks?
- How robust are benchmark scores to alternative reward designs, particularly where exact outputs or ordering differ despite equivalent solutions?
- What operational safeguards are needed before deploying agents trained or evaluated in these environments on real systems?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes a modular construction pipeline and a reward-function endpoint that can use interaction history and container state, enabling custom reward designs (PDF p. 4). The interface and appendix also discuss customization and extension (PDF pp. 14–15).
- Observation 2: **supported** — The reported SQL results show Try Again outperforming Single Turn for every listed model, including GPT-4 rising from 9.1% to 73.7% overall; the paper also reports gains in Bash (PDF pp. 6–7). This supports the qualified claim about interaction and benchmark viability.
- Observation 3: **supported** — The paper explicitly states that its implemented environments are limited to Bash and SQL and that the CTF dataset has only four instances, limiting broad evaluation (PDF p. 9; see also PDF p. 26).
- Observation 4: **supported** — The paper describes Docker containers as execution sandboxes, but warns that Bash and SQL impose no strict action-space limitations and that direct sim-to-real transfer may put real systems at risk (PDF pp. 3–4, 26). The claim accurately distinguishes sandboxed evaluation from unestablished deployment safety.

## Decisions

Expand a step for its arguments and observation. Long observations are previews; the structured trace retains complete text.

### Step 1: search_paper

Locate the paper's explicit scope limitations to assess benchmark coverage.

[Event 5](trace.jsonl#L5)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "query": "limitations",
    "reason": "Locate the paper's explicit scope limitations to assess benchmark coverage."
  },
  "observation": {
    "matches": [
      {
        "page": 9,
        "snippet": " and furthermore, the Bash and SQL environments, empowers task designers to construct new tasks to unlock the plethora of challenges that await in the space of interactive coding. Limitations and future directions. We point out several current limitations of InterCode. At this time, the number of InterCode based environments is limited to SQL and Bash action spaces and datasets; within the near future, we plan to expand the number of offerings to cover a wider set of programming languages and datasets that should further deliver on InterCode’s purported promises of efficient and expre"
      },
      {
        "page": 9,
        "snippet": "esigners to construct new tasks to unlock the plethora of challenges that await in the space of interactive coding. Limitations and future directions. We point out several current limitations of InterCode. At this time, the number of InterCode based environments is limited to SQL and Bash action spaces and datasets; within the near future, we plan to expand the number of offerings to cover a wider set of programming languages and datasets that should further deliver on InterCode’s purported promises of efficient and expressive task construction. Second, the CTF dataset is limited to j"
      },
      {
        "page": 13,
        "snippet": "Checklist 1. For all authors... (a) Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? [Yes] (b) Did you describe the limitations of your work? [Yes] (See §D) (c) Did you discuss any potential negative societal impacts of your work? [Yes] (See §D) (d) Have you read the ethics review guidelines and ensured that your paper conforms to them? [Yes] 2. If you ran experiments (e.g. for benchmarks)... (a) Did you include the code, data, and instructions needed to reproduce the main experi- mental results (either in the supplementa"
      },
      {
        "page": 14,
        "snippet": "urrent models’ performance on the interactive coding task. The full template for each prompting strategy is also included. Finally, we also discuss some of the impacts, risks, and limitations of our work. The webpage for InterCode is https://intercode-benchmark.github.io/. The code for InterCode is https://github.com/intercode-benchmark/intercode-benchmark; the link is also included on the InterCode webpage. A Environment Details A.1 InterCode Interface The InterCode interface inherits the OpenAI gym [ 5] environment API definition. Specifically, InterCodeEnv is written as an abstract"
      },
      {
        "page": 26,
        "snippet": "D Potential Societal Impacts & Limitations InterCode’s goal of formulating tasks to advance the development decision-making and code agents is an exciting research direction that also warrants concerns about safety and fairness. Coverage of languages. The InterCode codebase currently features two tasks with Bash and SQL programming languages as action spaces. We plan to expand the number of InterCode based tasks to cover more programming "
      },
      {
        "page": 26,
        "snippet": "nterested in InterCode as a training platform. As well as programming languages, additional ongoing work also aims to feature more datasets, task environments, and types of tasks. Limitations of the CTF task. The Capture the Flag toy dataset showcases InterCode’s serviceability for developing novel tasks with new code understanding challenges that can easily be used for training and evaluating models. With that said, this demonstration currently only has four task instances. We hope to put forth a more thorough examination of the Capture the Flag task’s challenges, provide a clearer p"
      },
      {
        "page": 26,
        "snippet": "res the safe execution of commands in a realistic simulated task environment. With this said, the Bash and SQL InterCode environments currently do not explicitly impose any strict limitations on the action space. While the execution of irreversibly detrimental commands is mitigated by Docker, a direct sim-to-real transfer of an InterCode-trained agent to a real system may put the system at risk. To combat this, theInterCodeEnv interface allows task designers to add their own execution logic that can provide guardrails on model behavior and define an allow-list of permissible commands "
      }
    ],
    "limit_reached": false
  }
}
```

</details>

### Step 2: read_pages

Inspect benchmark design and experimental results supporting the paper's claims.

[Event 10](trace.jsonl#L10)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 3,
    "end": 5,
    "reason": "Inspect benchmark design and experimental results supporting the paper's claims."
  },
  "observation": {
    "pages": [
      {
        "page": 3,
        "text": "understanding challenges across different task settings, and explore the ease with which new tasks\nand datasets can be defined using InterCode.\nTo summarize, our paper makes the following contributions:\n• We develop InterCode, a new, universal framework for interactive code generation, which\nprovides ease of use, extensibility, and safety.\n• Using InterCode, we perform a comprehensive evaluation of state-of-the-art models and\nidentify several avenues for improvements.\n• We release our framework as a new benchmark along with useful empirical tools to customize\nany new static code datasets into  … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 4,
        "text": "Action Space Environment\n Dataset\n Reward Function\nBash Ubuntu Terminal NL2Bash [29] (200) Latest Std. Output + File System ∆\nSQL MySQL Database Spider 1.0 [51] (1034) Latest Std. Output\nTable 1: Rundown of the two environments with Bash and SQL as action spaces developed using\nthe InterCode framework. The numbers in parentheses refer to the number of task instances adopted\nfrom each dataset. Each environment is defined in under 200 lines of code total. Specific discussion\nof the environment construction and reward function can be found in § A.2 and § A.3\n3 The InterCode Benchmark\n3.1 Formulat … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 5,
        "text": "We bootstrap the NL2Bash [29] dataset (which lacks specificity in queries and grounding to any\nunderlying file system, preventing it from being used directly for interactive evaluations) to create\nan interactive coding task where an agent completes an instruction viabash actions. Transferring\nNL2Bash to the interactive task setting requires simple transformations to ground instructions and\ngold code blocks in the file system. First, we consider a subset of 1000 commands with each\nhaving ≥ 4 utilities. We then filter out commands that are non-UNIX, non-Linux, or use utilities we\ncurrently do no … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 3: read_pages

Review model evaluation setup and reported benchmark outcomes.

[Event 15](trace.jsonl#L15)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 6,
    "end": 7,
    "reason": "Review model evaluation setup and reported benchmark outcomes."
  },
  "observation": {
    "pages": [
      {
        "page": 6,
        "text": "“T ry Again”\nT ermina t e when r e w ar d = 1\nor e x ceeds n turns\nUp t o n\ntimes\nQ ues tion\nWha t is the country code and firs t name...\nObserv a tion\n<std. output, reward>\nAg ent\n<action>\nInitial Msg.\nY ou ar e a SQL code g enera t or helping...\nY our task is t o int erac t with a MySQL DB...\nR eA c t\nT ermina t e when thought chain\nfinishes or e x ceeds n turns\nQ ues tion\nWha t is the country code and firs t name...\nUp t o n\ntimes\nObserv a tion\n<std. output>\nAg ent\n<thought> → <action>\nInitial Msg.\nInt erac t with a MySQL DB using SQL t o...\nUse int erlea ving Thought , A c tion, Obs...\nT e … [preview; full text in trace]",
        "truncated": false
      },
      {
        "page": 7,
        "text": "InterCode-SQL Single Turn Try Again ( n = 10)\nModel / Hardness Easy Med Hard Extra All Easy Med Hard Extra All\ntext-davinci-003 20.6 4.9 1.7 0.0 7.4 32.4 14.6 5.2 4.2 15.6\ngpt-3.5-turbo 22.6 8.3 5.7 3.6 10.5 72.5 44.3 43.7 21.1 47.3\ngpt-4 19.8 7.2 4.6 3.0 9.1 87.5 76.7 66.7 52.4 73.7\ntext-bison-001 23.8 10.9 5.7 0.6 11.5 27.0 12.3 5.7 0.6 12.9\nchat-bison-001 18.5 6.5 4.0 0.0 7.9 22.2 7.8 6.9 0.0 9.9\nVicuna-13B 8.1 1.3 0.6 0.0 2.6 18.9 3.4 1.7 0.0 6.3\nStarChat-16B 21.8 7.4 2.9 0.0 8.9 22.3 8.5 2.9 1.2 9.7\nTable 2: Success Rate for single vs. multi turn evaluation on InterCode-SQL (refer §A.3).  … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 4: read_pages

Inspect the authors' own stated limitations before judging scope and safety.

[Event 20](trace.jsonl#L20)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "start": 9,
    "end": 9,
    "reason": "Inspect the authors' own stated limitations before judging scope and safety."
  },
  "observation": {
    "pages": [
      {
        "page": 9,
        "text": "T ask\nChalleng e Descrip tion\nFlag\n: \nY ou ha v e access t o the \nfile 'unpackme.flag.p y' \ntha t contains the \nhidden flag. Find the \nflag’ s v alue.\n: picoCTF{175_chr\n157m45_85f5d0ac}\n#1 Bash Skill\nCheck ‘unpackme.flag.p y’ cont ent\nAg ent\n/bin/bash -c \"cat \nunpackme.flag.py\"\nimport base64; from crypto \ngraphy.fernet import Fernet\npayload = b'...'; key_str = \n'correctsta\npleco...’; key_base64 = \nbase64.b64encode( ...\nBash En v\n#3 Err or Corr ec tion\nKno w ho w t o r es olv e missing cryp t o lib\nAg ent\npip3 install \ncryptography\nCollecting cryptography, \nDownloading \ncryptography-40.0.2 ...  … [preview; full text in trace]",
        "truncated": false
      }
    ]
  }
}
```

</details>

### Step 5: submit_review · accepted

Evidence covers framework design, evaluation results, and explicit limitations; submit a scoped assessment.

[Event 25](trace.jsonl#L25)

<details><summary>Arguments and observation</summary>

```json
{
  "arguments": {
    "reason": "Evidence covers framework design, evaluation results, and explicit limitations; submit a scoped assessment.",
    "review": {
      "score": 0.73,
      "summary": "InterCode contributes a practical framework and benchmark formulation for interactive code generation, pairing code actions with execution feedback in containerized environments. Its Bash and SQL implementations and model evaluations demonstrate that the testbed is usable and expose meaningful benefits and failure patterns of interaction, though empirical breadth and task coverage remain limited.",
      "observations": [
        {
          "kind": "strength",
          "claim": "The paper defines a modular interactive coding framework with execution-based feedback and customizable task-specific rewards, supporting extension beyond the supplied environments.",
          "page": 4,
          "quote": "InterCode exposes a reward function endpoint that has access to both the interaction history and the execution container, allowing for custom reward function definitions that can incorporate multiple signals."
        },
        {
          "kind": "strength",
          "claim": "Reported evaluations show substantial gains from iterative feedback for multiple models, especially on SQL, supporting benchmark viability and the value of interaction.",
          "page": 7,
          "quote": "gpt-4 19.8 7.2 4.6 3.0 9.1 87.5 76.7 66.7 52.4 73.7"
        },
        {
          "kind": "limitation",
          "claim": "The implemented benchmark has narrow language and dataset coverage, and the CTF demonstration is too small for broad evaluation.",
          "page": 9,
          "quote": "At this time, the number of InterCode based environments is limited to SQL and Bash action spaces and datasets"
        },
        {
          "kind": "uncertainty",
          "claim": "The paper says execution is sandboxed, but its own discussion warns the Bash and SQL environments lack strict action-space restrictions; safety of direct transfer is not established.",
          "page": 26,
          "quote": "do not explicitly impose any strict limitations on the action space."
        }
      ],
      "unresolved_questions": [
        "How well do results generalize to additional programming languages, datasets, and independently authored tasks?",
        "How robust are benchmark scores to alternative reward designs, particularly where exact outputs or ordering differ despite equivalent solutions?",
        "What operational safeguards are needed before deploying agents trained or evaluated in these environments on real systems?"
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
          7
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
          26
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
