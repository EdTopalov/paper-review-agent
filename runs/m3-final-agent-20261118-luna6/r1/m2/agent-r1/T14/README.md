# T14: RULER: What's the Real Context Size of Your Long-Context Language Models?

**agent · ok**

5 model calls · 4 reads · 14.02 s · $0.001938

5 decisions · 5 tool calls · 28453 input tokens (16372 cached) · 559 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

RULER broadens long-context evaluation beyond single-needle retrieval with configurable synthetic tests for multi-item retrieval, variable tracking, aggregation, and QA. Its evaluation of ten models and error analyses demonstrate that strong vanilla NIAH performance does not ensure robust performance at longer contexts or on more complex tasks. The benchmark offers useful controlled diagnostics, while its synthetic emphasis and a limited model sample constrain how broadly to generalize its findings.

- **strength**: The benchmark systematically expands retrieval testing to include multiple needles and adds non-retrieval tasks.
  - Page 3 · citation: whitespace
  - Quote: "RULER comprises tasks across four categories: retrieval, multi-hop tracing, aggregation, and question answering"

- **strength**: Evaluation across models and lengths supports the central finding that claimed context length is not equivalent to effective performance.
  - Page 7 · citation: exact
  - Quote: "none of them maintains performance above the Llama2-7B baseline at their claimed length"

- **strength**: The authors diagnose concrete failure behaviors, including copying, that clarify what aggregate scores miss.
  - Page 7 · citation: whitespace
  - Quote: "Over 80% of Yi’s output in the CWE task at 128K is simply a string copied from the one-shot example"

- **limitation**: The benchmark is deliberately synthetic; its controlled configurations aid diagnosis but do not by themselves establish performance on naturally occurring long-context tasks.
  - Page 2 · citation: exact
  - Quote: "RULER consists solely of synthetic tasks"

Unresolved questions:

- How well do the synthetic task results predict performance on diverse, naturally occurring long-context workloads?
- Would broader model coverage or alternative scoring and threshold choices materially change the effective-length comparisons?
- I inspected pages 1–10, not the remaining appendix and implementation details; the benchmark’s full configuration, prompt sensitivity, and reproducibility details remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the authors’ stated scope boundaries and caveats. | 0 matches | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark design, task definitions, and evaluation setup. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Review evaluation protocol and reported quantitative evidence. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 5, "end": 7}` | Check task scope, scoring details, and comparative evaluation results. | read pages [5, 6, 7] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Evidence from benchmark design, evaluation, results, and discussion is sufficient for a qualified assessment. | review accepted | [event 25](trace.jsonl#L25) |
