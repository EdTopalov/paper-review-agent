# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**agent · ok**

4 model calls · 2 reads · 15.50 s · $0.001555

4 decisions · 4 tool calls · 13999 input tokens (6054 cached) · 1027 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

SWE-agent presents a thoughtfully designed agent-computer interface for repository-level software engineering and reports a sizable improvement on SWE-bench over the cited prior RAG result. It combines concrete interface design choices with benchmark evaluation and ablations, making it a substantial empirical and systems contribution. Evidence is bounded by a small set of strong models; detailed ablation and failure-analysis pages were not inspected.

- **strength**: The paper's central contribution is an LM-oriented interface integrating repository search, bounded file viewing, editing feedback, and context management, rather than relying on a generic shell alone.
  - Page 4 · citation: whitespace
  - Quote: "The SWE-agent system uses informative prompts, error messages, and history processors to keep agent context concise and informative."

- **strength**: The reported full benchmark result is meaningful evidence on a large software issue set, though it does not establish generalization beyond the benchmark.
  - Page 5 · citation: exact
  - Quote: "solving 12.47% (286/2,294) of the full SWE-bench test set and 18.00% (54/300) of the Lite split."

- **limitation**: The evaluation focuses on two leading hosted models, limiting how broadly the demonstrated benefit can be generalized across model capabilities.
  - Page 5 · citation: exact
  - Quote: "All results, ablations, and analysis are based on two leading LMs, GPT-"

- **uncertainty**: The inspected pages establish the headline result and evaluation design, but do not expose detailed ablation outcomes or broader failure analysis; their strength and robustness remain unassessed here.
  - Page 5 · citation: whitespace
  - Quote: "We present several empirical ablations that quantify Agent-Computer Interface design’s effect on task performance."

Unresolved questions:

- How large and consistent are the individual ACI component effects across the reported ablations?
- How sensitive are results to model choice, prompt/configuration choices, and the per-instance cost cap?
- What are the detailed failure modes and uncertainty in the benchmark's resolved-task estimates?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Check the paper's explicit scope and limitations for a balanced assessment. | 4 matches on pages [3, 9, 10] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 5}` | Inspect benchmark setup and quantitative results to assess evidence and scope. | read pages [4, 5] | [event 10](trace.jsonl#L10) |
| 3 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | The inspected abstract, interface design, and experimental setup/results support a provisional balanced review; remaining evidence gaps are stated explicitly. | citation_validation_failed; #3: not_found | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Correct the non-verbatim model-scope citation using the exact wording visible on page 5 and submit the assessment. | review accepted | [event 22](trace.jsonl#L22) |
