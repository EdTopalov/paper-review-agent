# T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

**deliberative_review · ok**

8 model calls · 4 reads · 36.80 s · $0.006567

8 decisions · 5 tool calls · 40586 input tokens (1338 cached) · 3321 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.66

OSWorld contributes an interactive virtual-computer environment and a 369-task benchmark for evaluating multimodal agents on open-ended computer tasks. The inspected pages support its use of configured task states and task-specific executable checks, and provide some evidence of iterative evaluation-script review and human testing. They do not establish the full benchmark coverage or the protocol comparability behind the headline human and model success rates; this assessment is provisional because most of the paper was not inspected.

- **strength**: The paper describes concrete, task-specific execution checks, including setup and post-processing, rather than relying only on a demonstration trace.
  - Page 4 · citation: exact
  - Quote: "we design example-specific evaluation metrics including pre-setup, post-processing"

- **strength**: The authors report that evaluation examples received iterative scrutiny from different people, which is relevant validation evidence, though it does not by itself establish evaluator reliability.
  - Page 7 · citation: whitespace
  - Quote: "each example is further scrutinized and iterated upon by different individuals three times"

- **strength**: The human study used annotators with basic software skills who had not seen the samples or software before, and recorded completion time and correctness. The inspected excerpt does not specify the model evaluation protocol.
  - Page 9 · citation: whitespace
  - Quote: "annotators being computer science major college students who possess ba- sic software usage skills but have not been ex- posed to the samples or software before."

- **uncertainty**: The abstract reports a large human–model success-rate difference, but the inspected pages do not establish whether the human and agent evaluations were sufficiently comparable to interpret it as a direct capability-gap estimate.
  - Page 1 · citation: whitespace
  - Quote: "While humans can accomplish over 72.36% of the tasks, the best model achieves only 12.24% success"

Unresolved questions:

- How representative are the 369 tasks across operating systems, applications, and real-world computer use, and what evidence establishes annotation and evaluator reliability?
- What are the detailed agent and human evaluation protocols, including sample sizes, task overlap, repeatability, and treatment of partial success?
- How do the full paper’s results and analyses qualify the headline rates and reported failure modes? Pages 6–51 were not inspected in the supplied sources, so the assessment of these results and the paper’s broader limitations remains incomplete.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the benchmark construction and task/evaluation sections to verify how the 369 tasks, initial states, and execution-based success checks are defined, and whether the evidence supports claims of breadth and reproducibility.; Inspect agent and human evaluation protocols and results to assess whether the reported success rates support the central capability-gap claims and what comparisons or limitations qualify them.; Check the discussion and remaining paper pages for stated scope boundaries, failure analyses, and additional validation before characterizing gaps; currently only pag … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [1, 2, 4] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 0 matches | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [3, 4, 5] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: investigate; Issues: The page-5 citation for the second observation is incorrect: the quoted phrase appears on page 4 in E11, not page 5. Correct the page number before using that observation.; The first observation’s claim that the benchmark avoids requiring a single demonstration path is not directly supported by its cited quote, which describes task setup and evaluation scripts. Narrow the claim or cite direct evidence.; The draft appropriately flags the headline success-rate protocols as uninspected, but pages 6–51 remain unread, so its assessment of the results, limitation … | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | targeted_read | 2 matches on pages [7, 9] | [event 34](trace.jsonl#L34) · [event 39](trace.jsonl#L39) |
| 8 | revise | Draft revised; Changes: Corrected the page citation for the evaluation-design observation and narrowed its claim. Incorporated the page-7 report of iterative scrutiny and the page-9 description of the human study. The available excerpts still do not resolve whether the human and model success rates are directly comparable; no unsupported conclusion about that comparison is drawn. | [event 40](trace.jsonl#L40) · [event 43](trace.jsonl#L43) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "execution-based evaluation"}` | Locate benchmark task setup/evaluation description and supporting qualifications. | 8 matches on pages [1, 2, 4] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "human study"}` | Inspect agent/human evaluation evidence and protocol, an essential support obligation. | 0 matches | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 3, "end": 5}` | Inspect task benchmark construction and execution-based evaluation details for C1. | read pages [3, 4, 5] | [event 22](trace.jsonl#L22) |
| 7 | search_paper `{"query": "human evaluation"}` | Locate agent and human evaluation protocols, results, and qualifications for reported success rates. | 2 matches on pages [7, 9] | [event 37](trace.jsonl#L37) |
| 8 | submit_review `{"review": {"score": 0.66, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 45](trace.jsonl#L45) |
