# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**deliberative_review · ok**

8 model calls · 4 reads · 32.73 s · $0.006655

8 decisions · 5 tool calls · 43000 input tokens (0 cached) · 2585 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.6

Self-RAG trains a language model to decide when retrieval is useful and to generate reflection tokens assessing passage relevance, answer support, and usefulness. It combines offline critic-generated annotations with retrieval-aware, critique-guided decoding. The method is described in detail, and the inspected results page reports gains over several baselines; however, the results table and later discussion are only partially observed, limiting assessment of the strength and qualifications of the empirical case.

- **strength**: The inference procedure uses a retrieval decision and critique signals to evaluate and rank candidate outputs, making the proposed control mechanism concrete.
  - Page 4 · citation: whitespace
  - Quote: "Finally, a new critique token evaluates the overall utility of the response."

- **limitation**: Critic supervision depends partly on proprietary GPT-4 predictions; the paper notes possible cost and reproducibility consequences. This is a stated dependency, not evidence that the method fails.
  - Page 5 · citation: whitespace
  - Quote: "depending on such proprietary LMs can raise API costs and diminish reproducibility"

- **strength**: The results-page prose reports gains over supervised fine-tuned models across the evaluated tasks, while also claiming advantages over ChatGPT on some tasks. The observed table is incomplete, so the magnitude and comparability of these gains cannot be checked here.
  - Page 8 · citation: whitespace
  - Quote: "Our SELF -RAG (bottom two rows) demonstrates a substantial performance advantage over supervised fine-tuned LLMs in all tasks"

- **uncertainty**: The available results page is partial and does not expose enough table headings or evaluation detail to independently assess metric-by-metric performance or the robustness of the claims; later discussion and limitations were not inspected.
  - Page 8 · citation: exact
  - Quote: "Table 2: Overall experiment results on six tasks."

Unresolved questions:

- How large and consistent are the reported gains across tasks, baselines, and metrics, and how are factuality and citation accuracy evaluated?
- How sensitive are retrieval and critique behavior to critic annotations, retrieval choices, and inference-time weights?
- What further experimental qualifications or limitations appear in the uninspected pages?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the method and training sections to verify how retrieval/critique tokens are learned and used, and whether the described inference procedure supports the central adaptive-retrieval and self-reflection claims.; Inspect the main results and evaluation details, including baselines, tasks, metrics, and tables, to assess whether the claimed gains are supported and how broad the evidence is.; Inspect discussion, limitations, and later experimental details for scope boundaries or qualifications; only page 1 is currently observed, so note gaps explicitly if the remaining pages cannot b … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [2, 3] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 0 matches | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [4, 5, 6] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: investigate; Issues: The score of 0.56 is presented despite the central empirical evidence and later qualifications remaining uninspected. The draft appropriately flags this uncertainty, but the score should be revisited after targeted inspection of results and discussion.; Target: On the uninspected results pages, what do the main tables show about Self-RAG versus the stated baselines across tasks and metrics, and what evaluation qualifications accompany those results? | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | targeted_read | 2 matches on pages [8] | [event 34](trace.jsonl#L34) · [event 39](trace.jsonl#L39) |
| 8 | revise | Draft revised; Changes: Updated C2 to reflect the newly observed page-8 results prose and partial Table 2, and revised the score modestly to account for this limited empirical evidence. The table fragment does not permit a fuller quantitative assessment, so uncertainty remains. The quotation diagnostics are addressed with short verbatim spans from observed pages; no unsupported criticism or additional defect is inferred. | [event 40](trace.jsonl#L40) · [event 43](trace.jsonl#L43) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "Training"}` | Locate method/training evidence for how reflection tokens are learned and used. | 8 matches on pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "Experimental Results"}` | Locate main results/evaluation evidence and page locations. | 0 matches | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 4, "end": 6}` | Inspect method and training details for reflection-token construction and adaptive inference. | read pages [4, 5, 6] | [event 22](trace.jsonl#L22) |
| 7 | search_paper `{"query": "Table 2"}` | Locate main results tables and associated evaluation qualifications. | 2 matches on pages [8] | [event 37](trace.jsonl#L37) |
| 8 | submit_review `{"review": {"score": 0.6, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 45](trace.jsonl#L45) |
