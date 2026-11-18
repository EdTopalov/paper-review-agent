# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**deliberative_review · ok**

7 model calls · 3 reads · 33.28 s · $0.005891

7 decisions · 4 tool calls · 35670 input tokens (1238 cached) · 3169 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Reflexion adds a reflection-and-memory loop to a ReAct agent: heuristics trigger reflection, the agent stores it, and it retries with that memory. In the reported AlfWorld and HotPotQA evaluations, it improves over retry-only baselines. These are promising demonstrations, but the evidence is bounded to small evaluations and does not isolate the effects of reflection from memory or other prompt choices.

- **strength**: The method describes heuristic-triggered reflection and stored memory to address repeated actions and inefficient planning.
  - Page 3 · citation: normalized
  - Quote: "The reflection loop aims to help the agent correct common cases of hallucination and inefficiency through trial and error."

- **strength**: On 134 AlfWorld environments, the authors report success on 97% within 12 trials, comparing against a retry-only ReAct setup. This supports improvement in this evaluation, not general superiority.
  - Page 5 · citation: exact
  - Quote: "the agent used ReAct to solve 97% of the given environments in 12 trials"

- **limitation**: The HotPotQA evaluation uses 100 questions. Its results section reports 54% success, while the abstract reports 51%; this discrepancy is unresolved in the observed material.
  - Page 6 · citation: normalized
  - Quote: "Reflexion enabled the agent to successfully answer 54% of the questions from the dataset"

- **uncertainty**: The observed passages do not establish how much gain is due specifically to reflection versus added memory or prompt differences. This is an evidentiary gap, not a demonstrated defect; substantial portions of the paper were not inspected.
  - Page 7 · citation: whitespace
  - Quote: "the growing, dynamic working memory promoted learning through trial"

Unresolved questions:

- Why does the abstract report 51% HotPotQA success while the results section reports 54%?
- How much of the gains comes from reflection itself versus memory, additional trials, or prompt configuration?
- How robust are results across models, random seeds, larger test sets, and other tasks?
- What do the uninspected pages and appendix report about implementation details, ablations, and limitations? Coverage is partial: pages 1, 3–7, and partial page 10 were observed; ten pages were uninspected.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the methods and experiment pages to verify how dynamic memory and self-reflection are implemented, what baselines and evaluation protocols support the reported 97% AlfWorld and 51% HotPotQA success rates, and whether results are reported across enough trials to support the claims.; Check later pages for ablations, error analysis, and stated limitations that clarify whether gains are attributable to reflection or memory and how broadly the findings apply; do not treat material as absent based only on the inspected first page.; Gather 2–4 short verbatim quotations with PDF page n … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 2 matches on pages [10] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [3, 4, 5] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [6, 7] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The page 3 quotation is not verbatim as supplied: the source has “If the heuristich suggests reﬂection at t,” rather than the draft’s “If the heuristic h suggests reflection at t,”. Replace it with an exact source span; the other three quotations are verified.; The draft’s unresolved questions ask about results in uninspected material, which is appropriately framed as unknown, but keep the existing explicit coverage caveat when revising.; Target: Replace the page 3 quotation with a verbatim span from E4 and retain its PDF page number. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Replaced the non-verbatim page 3 quotation with an exact span from E4. Retained the coverage caveat and uncertainty about uninspected material; no unsupported criticism required a score change. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "limitations"}` | Inspect later-paper evidence about scope and caveats before evaluating. | 2 matches on pages [10] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 3, "end": 5}` | Inspect methods and evaluation design, including memory/reflection and baseline setup. | read pages [3, 4, 5] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 6, "end": 7}` | Inspect HotPotQA setup/results and comparative evidence supporting the reported performance. | read pages [6, 7] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
