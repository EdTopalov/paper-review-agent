# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**deliberative_review · ok**

7 model calls · 3 reads · 33.74 s · $0.008080

7 decisions · 4 tool calls · 53554 input tokens (1311 cached) · 3092 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

SWE-agent argues that language-model agents perform better at repository-level software tasks when given an interface designed for agent interaction. It reports strong SWE-bench results and Lite-set ablations indicating that interface choices affect resolution rates. The contribution is substantial, but the evidence is bounded to a small set of models and Python repositories; much of the paper, including its conclusion and full limitations discussion, was not inspected.

- **strength**: The paper reports a large gain over its cited RAG result. Because that comparison is between an interactive agent and a non-interactive RAG system, it does not isolate the interface as the cause of the full benchmark gap.
  - Page 1 · citation: exact
  - Quote: "On SWE-bench, SWE-agent\nis able to solve 12.5% of issues, compared to the previous best of 3.8% achieved\nwith retrieval-augmented generation (RAG)."

- **strength**: The Lite-set ablation indicates that the linting intervention improves results in the tested setup. This component-level result does not by itself establish what explains the full-test-set advantage.
  - Page 7 · citation: exact
  - Quote: "Without Linting, 15.0% ↓ 3.0"

- **limitation**: The evaluation covers issues from 12 Python-package repositories, while the ablations are reported on the 300-instance Lite subset. Generalization beyond these settings remains an open question, not a demonstrated defect.
  - Page 5 · citation: whitespace
  - Quote: "which includes 2,294 task instances from 12 different repositories of popular Python packages"

Unresolved questions:

- Would the full-set advantage persist against a comparably interactive baseline using the same model, demonstrations, and task budget?
- How well do the ACI choices generalize to models beyond GPT-4 Turbo and Claude 3 Opus, repositories beyond the tested Python projects, and tasks outside SWE-bench?
- What limitations and future directions do the authors discuss in the uninspected conclusion and other omitted pages?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the methods and experimental-results pages for SWE-bench setup, comparison conditions, and evidence supporting the reported 12.5% versus 3.8% result.; Inspect the ACI ablations and analysis for evidence that interface design—not other system or model differences—drives performance changes, and note the scope of the tested settings.; Inspect limitations and conclusion pages for stated boundaries or unresolved questions; only page 1 is currently available, so avoid treating uninspected material as absent. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [1, 2, 3, 5] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [5, 6, 7] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [16, 17, 18] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The fourth observation’s quote is not verified as verbatim in the supplied page 18 text, so it does not meet the quotation requirement. Replace it with an exact span from an inspected source, or omit that observation.; The first observation describes the 3.8% RAG comparison but quotes only the 12.47% result. Add an exact quote supporting the baseline figure, or narrow the claim to what the current quote supports.; The second observation makes claims about several ablations but quotes only the no-linting result. Either narrow the claim to linting or use a verifie … | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Replaced the unverified page 18 quotation with an exact page 5 scope quotation. The first observation now quotes the reported RAG comparison, and the ablation observation is narrowed to the directly quoted linting result. The score is unchanged. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "SWE-bench"}` | Find the evaluation setup and results pages to inspect the primary performance evidence. | 8 matches on pages [1, 2, 3, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Inspect experimental setup, comparison conditions, and results evidence relevant to the headline and ACI comparisons. | read pages [5, 6, 7] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 16, "end": 18}` | Inspect conclusion/limitations for boundaries and unresolved issues. | read pages [16, 17, 18] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.78, "observations": 3}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
