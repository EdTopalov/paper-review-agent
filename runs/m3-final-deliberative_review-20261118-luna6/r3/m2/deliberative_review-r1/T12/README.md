# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**deliberative_review · ok**

8 model calls · 4 reads · 34.92 s · $0.008082

8 decisions · 5 tool calls · 53412 input tokens (1243 cached) · 3122 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

InterCode formalizes interactive coding as agents issuing code actions, receiving execution feedback, and earning task rewards, and provides Bash and SQL environments built from existing datasets. Its evaluations report higher success rates with interaction than in single-turn settings across the tested models, including a large SQL gain for GPT-4. The framework and initial benchmark have clear practical value, though the evidence covers only two substantial environments and the CTF demonstration is tiny. Important gaps remain: 15 pages were uninspected, several inspected pages are partial, and the supplied excerpts do not expose all experiment details or the full limitations discussion.

- **strength**: The paper specifies a concrete interactive task formulation, including code actions and execution feedback, rather than treating coding solely as static generation.
  - Page 4 · citation: whitespace
  - Quote: "Given a coding instruction u ∈ U in natural language, an agent issues code or a specialsubmit keyword as an action at ∈ A."

- **strength**: The reported results support an advantage for multi-turn interaction on these benchmark tasks: GPT-4's SQL success rate rises substantially, and the tables report results across task difficulty and Bash file systems.
  - Page 7 · citation: exact
  - Quote: "gpt-4 19.8 7.2 4.6 3.0 9.1 87.5 76.7 66.7 52.4 73.7"

- **limitation**: The paper acknowledges limited current environment coverage and a very small CTF demonstration. These are scope boundaries for the evaluated release, not proof that the framework cannot be extended.
  - Page 26 · citation: exact
  - Quote: "With that said, this demonstration currently only has four task instances."

Unresolved questions:

- How robust are the reported interaction gains to alternative task sampling, reward definitions, and evaluation settings?
- How well do the findings transfer beyond the two implemented Bash and SQL environments, given that the CTF example contains only four instances?
- What safeguards beyond Docker isolation are required for agents that might transfer from simulated tasks to real systems?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the framework and environment sections to verify what InterCode standardizes, how execution feedback and Docker isolation work, and whether the claimed extensibility is demonstrated or mainly proposed.; Inspect benchmark construction and evaluation results for Bash and SQL: task splits, models and prompting baselines, metrics, and whether results substantiate claims about interactive coding and benchmark difficulty.; Inspect discussion and limitations for scope boundaries and caveats; since only page 1 is currently observed, check the remaining pages before judging support or a … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 7 matches on pages [9, 13, 14, 26] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [2, 3, 4] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | 8 matches on pages [1, 9, 13, 17, 19, 21] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: investigate; Issues: One observation’s page 4 quote is not verified verbatim: the citation checker marks it hyphenation-ambiguous. Replace it with a quote that matches the observed source exactly.; The empirical assessment remains materially under-supported: key results, comparison details, and benchmark construction evidence were not inspected. The draft appropriately flags this gap, but the score and claims about the paper’s evidential strength should be checked against the main evaluation pages before approval.; Target: Read the main Bash and SQL evaluation pages and determi … | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | targeted_read | read pages [5, 6, 7] | [event 34](trace.jsonl#L34) · [event 39](trace.jsonl#L39) |
| 8 | revise | Draft revised; Changes: Updated C2 based on pages 5–7: the observed tables do provide quantitative support for interaction gains on the tested tasks, so the earlier claim that main results were unavailable no longer applies. Replaced the hyphenation-ambiguous quote with an exact formulation quote. Kept the score moderate because generalization and some evaluation details remain uncertain; the observation about the small CTF set is explicitly framed as a scope limitation. | [event 40](trace.jsonl#L40) · [event 43](trace.jsonl#L43) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "Limitations"}` | Check discussion and caveats before assessing scope and evidence. | 7 matches on pages [9, 13, 14, 26] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 2, "end": 4}` | Inspect framework design and benchmark construction/results to substantiate the paper’s central claims. | read pages [2, 3, 4] | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "Results"}` | Inspect experimental results and discussion for benchmark evidence, methods, and counterevidence. | 8 matches on pages [1, 9, 13, 17, 19, 21] | [event 22](trace.jsonl#L22) |
| 7 | read_pages `{"start": 5, "end": 7}` | Inspect main Bash and SQL benchmark evaluation results and reported comparisons. | read pages [5, 6, 7] | [event 37](trace.jsonl#L37) |
| 8 | submit_review `{"review": {"score": 0.69, "observations": 3}}` | Submit after the enforced critique and source validation. | review accepted | [event 45](trace.jsonl#L45) |
