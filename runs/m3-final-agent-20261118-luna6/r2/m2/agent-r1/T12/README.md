# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**agent · ok**

7 model calls · 5 reads · 16.93 s · $0.003519

7 decisions · 7 tool calls · 52415 input tokens (31081 cached) · 1127 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

InterCode contributes a flexible, execution-feedback benchmark framework and Bash/SQL environments for evaluating interactive code generation. Its experiments show that feedback and structured prompting can substantially improve task success, while also exposing persistent reasoning difficulties. The work is valuable as benchmark infrastructure, though its empirical coverage is limited to two principal environments and the CTF demonstration is explicitly small.

- **strength**: The paper specifies an interactive coding benchmark in standard decision-process terms, with execution as feedback.
  - Page 4 · citation: whitespace
  - Quote: "Given a coding instruction u ∈ U in natural language, an agent issues code or a specialsubmit keyword as an action at ∈ A."

- **strength**: Across tested models, iterative feedback is associated with large gains, particularly for GPT-4 on SQL; the result supports benchmark utility, though does not by itself establish broad generality.
  - Page 6 · citation: whitespace
  - Quote: "with a notable multi-fold increase for GPT-4 (9.1% → 73.7%) on the InterCode-SQL task."

- **limitation**: The paper identifies a concrete scope boundary: the available environments cover only Bash and SQL, so claims of generality rely partly on extensibility rather than demonstrated breadth.
  - Page 9 · citation: whitespace
  - Quote: "At this time, the number of InterCode based environments is limited to SQL and Bash action spaces and datasets;"

- **limitation**: The CTF example is a useful extensibility demonstration but is not a substantial evaluation set, as the authors acknowledge.
  - Page 9 · citation: whitespace
  - Quote: "Second, the CTF dataset is limited to just four task instances due to our manual curation procedure."

Unresolved questions:

- How robust are the reported improvements across additional programming languages, environment designs, and independently constructed tasks?
- How sensitive are conclusions to the custom Bash lexical-similarity reward and SQL output-order scoring choices?
- I inspected the framework description, main experiments, and stated limitations, but not the full appendices, prompting templates, or robustness analyses; those details could refine judgments about reproducibility and evaluation sensitivity.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "results"}` | Locate reported benchmark findings and evidence for the paper's evaluation. | 8 matches on pages [1, 9, 13, 17, 19, 21] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect framework design and environment/task definitions supporting the claimed contribution. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Inspect experimental results and evaluation design to judge empirical support and scope. | read pages [5, 6, 7] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "limitations"}` | Check the authors' stated scope boundaries and limitations before final assessment. | 7 matches on pages [9, 13, 14, 26] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 9, "end": 9}` | Inspect conclusion and explicit limitations for balanced scope and uncertainty. | read pages [9] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Evidence inspected covers framework formulation, benchmark design, main success-rate results, and stated scope limitations; submit an independent assessment. | citation_validation_failed; #1: not_found | [event 31](trace.jsonl#L31) |
| 7 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Correct the unmatched framework citation by quoting the exact formulation observed on page 4; other evidence remains verified. | review accepted | [event 37](trace.jsonl#L37) |
