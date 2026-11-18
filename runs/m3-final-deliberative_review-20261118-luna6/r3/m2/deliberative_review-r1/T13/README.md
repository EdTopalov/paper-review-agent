# T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**deliberative_review · ok**

7 model calls · 3 reads · 31.64 s · $0.005783

7 decisions · 4 tool calls · 37061 input tokens (1507 cached) · 2667 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Self-RAG trains a language model to decide when to retrieve, assess retrieved passages and generated text with reflection tokens, and use those signals to guide decoding. The inspected pages describe the training and evaluation setup, but do not include results tables needed to verify the paper’s central performance claims. The score reflects a technically detailed proposal while preserving uncertainty about its empirical support.

- **strength**: The paper describes an integrated training and inference approach: the generator learns output and reflection tokens, while inference uses retrieval thresholds and critique-based reranking or filtering.
  - Page 6 · citation: exact
  - Quote: "the generator LM is trained with a standard LM objective"

- **strength**: The stated evaluation covers multiple task types and names task-specific evaluation measures, including a factuality metric for biographies.
  - Page 7 · citation: whitespace
  - Quote: "We use FactScore (Min et al., 2023) to evaluate biographies"

- **limitation**: Reflection supervision is partly generated with GPT-4. This creates a dependence on proprietary-model labels; the inspected pages do not quantify the effect of that dependence.
  - Page 5 · citation: whitespace
  - Quote: "We create supervised data by prompting GPT-4 to generate reflection tokens"

- **uncertainty**: The abstract claims gains over strong baselines, but the supplied pages do not include results tables or ablation analyses, so the magnitude and attribution of those gains cannot be assessed from the inspected material.
  - Page 1 · citation: whitespace
  - Quote: "significantly outperforms state-of-the-art LLMs and retrieval-augmented models"

Unresolved questions:

- How large and consistent are the reported gains across tasks, and are they statistically reliable?
- Do ablations isolate the contributions of adaptive retrieval, reflection-token training, and critique-based decoding?
- How robust are reflection judgments to errors in GPT-4 supervision or changes in retrieval corpora?
- Inspection covered pages 1–3 (partially) and 5–7; 24 pages were uninspected, including material that may qualify the claims or provide results and ablations.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the method and training sections to verify how retrieval and reflection tokens are learned, and whether the described selection procedure is supported by implementation details.; Inspect experimental tables and evaluation methods to assess whether the claimed gains across tasks, factuality, and citation accuracy are backed by appropriate comparisons and evidence.; Inspect ablations, limitations, and remaining pages for qualifications or counterevidence; only page 1 is currently available, so do not treat uninspected passages as absent. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [2, 3] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 0 matches | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [5, 6, 7] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The coverage statement says the inspection included “page 30 overall,” but the observed pages are 1–3, 5–7; page 30 is not among them. Correct this inaccurate statement. The rest of the draft appropriately qualifies that results and ablations were not inspected. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Corrected the coverage statement: page 30 was not observed. The inspected pages are 1–3 (partially) and 5–7. Kept the score unchanged because the unseen results and ablations leave empirical support uncertain. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "Training"}` | Locate method and training discussion to assess how reflection tokens and retrieval are learned. | 8 matches on pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Inspect explicit limitations and counterevidence in the supplied paper. | 0 matches | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 5, "end": 7}` | Inspect method and training procedure for evidence on token supervision and retrieval/selection. | read pages [5, 6, 7] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
