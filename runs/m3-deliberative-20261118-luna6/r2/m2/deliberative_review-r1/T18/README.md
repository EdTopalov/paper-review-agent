# T18: Gorilla: Large Language Model Connected with Massive APIs

**deliberative_review · ok**

7 model calls · 3 reads · 32.04 s · $0.006580

7 decisions · 4 tool calls · 42068 input tokens (1302 cached) · 2961 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.66

Gorilla fine-tunes a LLaMA-7B model to generate API calls and explores retrieval-aware training, introducing an API benchmark across HuggingFace, Torch Hub, and TensorFlow Hub. On the reported holdout tasks it often exceeds GPT-4’s accuracy, and the paper reports reduced hallucinations under its AST-based definition. The work offers a systematic evaluation pipeline, but the measured task and correctness criterion are narrow, and the inspected evidence does not establish the breadth or robustness of its documentation-change results.

- **strength**: The paper reports strong API-call accuracy for Gorilla on its benchmark, including results above GPT-4 in the zero-shot table. The comparison needs qualification: for HuggingFace, the paper uses different scoring for Gorilla and other models.
  - Page 7 · citation: normalized
  - Quote: "lightly fine-tuned Gorilla gets the state-of-the-art performance zero-shot over all the models"

- **limitation**: The evaluation’s correctness and hallucination measures are tied to matching a call against the collected API database; this offers a concrete metric but does not by itself establish semantic correctness or cover multi-call tasks. The authors explicitly limit this paper to one API call.
  - Page 5 · citation: exact
  - Quote: "Since we only consider one API call in this paper"

- **uncertainty**: The paper describes retrieval-aware training as supporting adaptation to changed documentation and reduced hallucination, and reports low hallucination rates for Gorilla in the inspected results. The detailed test-time change conditions and supporting results were not available in the inspected pages, so the strength and generality of that claim remain unresolved.
  - Page 5 · citation: whitespace
  - Quote: "We demonstrate that this a) makes the LLM adapt to test-time changes in API documentation, and b) improves performance from in-context learning, and finally c) show that it reduces hallucination error."

Unresolved questions:

- How large and diverse are the test-time documentation or version changes, and what are the detailed results against non-retrieval and alternative-retrieval baselines?
- How robust are the reported advantages beyond the self-instruct holdout and the three ML model hubs, especially on semantic correctness, executable calls, and multi-step API use?
- What further limitations, analyses, and results appear in the 11 pages not inspected?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the methods, APIBench construction, and evaluation setup to determine whether the claimed API-call accuracy advantage over GPT-4 is supported by comparable, clearly defined tests.; Check results and analyses for evidence that retrieval handles documentation or version changes and reduces hallucinated API usage; look for relevant baselines, metrics, and test-time change conditions beyond the abstract.; Inspect remaining pages for limitations, scope boundaries, and other evidence needed to ground page-quoted observations and unresolved questions; only page 1 is currently availabl … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [1, 2, 3, 4] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 8 matches on pages [3, 6, 7] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [5, 6, 7] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The first observation’s page 6 quote fails the supplied citation check, so it does not currently meet the requirement for a verified verbatim quotation. Replace it with a quote confirmed against the page text; the comparison caveat itself is supported by E19. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Replaced the unverified page 6 quotation with an observed page 7 quotation supporting the reported accuracy claim. Retained the score and the caveats: the HuggingFace scoring difference, limited one-call evaluation, and uninspected documentation-change evidence remain important qualifications. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "GPT-4"}` | Inspect the paper's directly relevant comparison results and evaluation evidence for the claimed API-call accuracy advantage. | 8 matches on pages [1, 2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "Evaluation"}` | Inspect evaluation methodology and results supporting claimed API accuracy and retrieval benefits. | 8 matches on pages [3, 6, 7] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 5, "end": 7}` | Inspect benchmark setup and reported results, including counterevidence and evaluation limitations. | read pages [5, 6, 7] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.66, "observations": 3}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
