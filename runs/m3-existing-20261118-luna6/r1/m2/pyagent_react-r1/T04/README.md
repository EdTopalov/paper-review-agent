# T04: AgentBench: Evaluating LLMs as Agents

**pyagent_react · ok**

5 model calls · 3 reads · 20.35 s · $0.002347

5 decisions · 5 tool calls · 37314 input tokens (26362 cached) · 1429 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

AgentBench contributes a broad interactive benchmark spanning eight environments and evaluates 25 API and open models, with a unified toolkit intended to support further evaluation. Its breadth and reported model comparisons are useful, but several environments rely on constructed evaluation procedures and the inspected evidence leaves questions about metric reliability and generalization.

- **strength**: The benchmark brings multiple interactive task types together, including five environments the authors say were newly created for this work.
  - Page 2 · citation: whitespace
  - Quote: "AgentBench encompasses 8 distinct environments, 5 of which are created in this paper for the first time"

- **strength**: The paper reports a substantial model comparison and per-environment results, supporting its finding that performance varies considerably across the tested models.
  - Page 14 · citation: whitespace
  - Quote: "gpt-4 presents the best performance on 7 out of 8 datasets in AgentBench"

- **limitation**: Some evaluation measures depend on a model-generated host and model-assisted extraction or checking, raising a question about evaluator reliability; this is not evidence that reported scores are wrong.
  - Page 10 · citation: whitespace
  - Quote: "we limit the answer to be mostly \"Yes\", \"No\", or \"Irrelevant\", and extract the answer from gpt-3.5-turbo’s responses."

- **uncertainty**: The authors identify multi-turn consistency as a challenge, but the inspected analysis does not establish how much it explains the model performance gaps.
  - Page 15 · citation: whitespace
  - Quote: "Maintaining consistency across turns remains difficult for some models."

Unresolved questions:

- How robust are results to alternative or independent evaluators for tasks that use GPT-3.5-turbo in evaluation?
- How representative are the benchmark rankings of broader real-world agent use, beyond these eight environments and evaluated model versions?
- I inspected the abstract, pages 2–4, and pages 8–10 and 14–16; I did not inspect the appendices, all environment-specific protocols, or the full paper, so I cannot assess every task’s data construction or validation evidence.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark design and environment coverage. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 8, "end": 10}` | Inspect scoring methodology and reported evaluation evidence. | read pages [8, 9, 10] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 14, "end": 16}` | Inspect aggregate benchmark results and evaluation limitations. | read pages [14, 15, 16] | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit an evidence-based assessment using inspected benchmark design, results, and analysis pages. | citation_validation_failed; #4: hyphenation_ambiguous (pages [15]) | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Correct the citation using an exact observed sentence from page 15. | review accepted | [event 26](trace.jsonl#L26) |
