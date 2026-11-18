# T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering

**deliberative_review · ok**

9 model calls · 3 reads · 50.30 s · $0.011999

9 decisions · 6 tool calls · 77633 input tokens (1550 cached) · 4966 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

AlphaCodium proposes a multi-stage, test-driven inference flow for code generation: it prepares problem reflections and tests, generates candidate solutions, then iteratively runs and fixes code. On CodeContests, the paper reports higher pass@5 than direct prompting for three models on both validation and test sets. The evidence is promising but scoped to this benchmark. Page 10 was not inspected, so the complete discussion of limitations and evaluation cannot be assessed.

- **strength**: The flow iteratively runs candidate code against public tests and attempts fixes when a test fails.
  - Page 4 · citation: whitespace
  - Quote: "If the code fails on a specific test, try to fix it, given the error message."

- **strength**: Table 1 reports higher AlphaCodium pass@5 scores than direct prompting for all three models on both validation and test sets.
  - Page 7 · citation: exact
  - Quote: "AlphaCodium 44%"

- **limitation**: The reported evaluation uses CodeContests validation and test sets; the observed results do not establish gains in other code-generation settings.
  - Page 3 · citation: whitespace
  - Quote: "which contain 107 and 165 problems, respectively."

- **uncertainty**: The inspected results report aggregate scores without repeated-run or uncertainty evidence. Page 10 was not inspected, so this does not characterize any further evidence or limitations discussed there.
  - Page 7 · citation: exact
  - Quote: "pass@5 score improves from 19% to 44%"

Unresolved questions:

- How sensitive are the reported gains to model versions, prompting and sampling settings, and the exact evaluation procedure?
- How much does each flow component contribute, and how often do AI-generated tests contain incorrect expected outputs?
- Do the gains generalize beyond CodeContests to other code-generation tasks and settings?
- What, if anything, does uninspected page 10 add about limitations or evaluation?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the flow and experimental setup to verify what stages, model settings, sampling budgets, and comparison baselines underlie the reported pass@5 increase.; Check the results pages for validation/test-set distinctions, per-model and per-baseline outcomes, uncertainty or repeated-run evidence, and whether the central performance claims are supported across problems.; Inspect later discussion and limitations for scope boundaries and unresolved concerns; only page 1 is currently available, so do not treat uninspected material as absent. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | read pages [2, 3, 4] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [5, 6, 7] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [7, 8, 9] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The first observation’s quote is not verified against the supplied page text. Replace it with a short verbatim span that matches the source exactly.; Explicitly acknowledge that page 10 was not inspected. This matters when characterizing what the paper does or does not establish, including component-level evidence and limitations.; Target: Revise the first observation’s quotation and add an explicit note that page 10 was uninspected; qualify any claims about evidence not present in the inspected pages. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Replaced the first observation’s unverified quotation with an exact span from page 4. Explicitly noted that page 10 was not inspected and qualified claims about component-level evidence and the paper’s complete limitations. The supplied evidence supports retaining the score. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |
| 8 | revise | Draft revised; Changes: Replaced the first observation’s unverified quotation with an exact observed quote. Explicitly noted that page 10 was not inspected and qualified claims about evidence and limitations accordingly. | [event 42](trace.jsonl#L42) · [event 45](trace.jsonl#L45) |
| 9 | revise | Draft revised; Changes: Replaced the first observation’s quote with an exact span from page 4 and used an exact Table 1 entry for the reported score. Explicitly noted that page 10 was uninspected and qualified conclusions about evidence not present in the supplied passages. | [event 50](trace.jsonl#L50) · [event 53](trace.jsonl#L53) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect flow details and experimental setup for AlphaCodium evidence. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Inspect methods/settings and central results to assess evidence behind the performance claim. | read pages [5, 6, 7] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 7, "end": 9}` | Inspect remaining results, implementation/setup, and discussion/limitations for evidence and counterevidence. | read pages [7, 8, 9] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit after the enforced critique and source validation. | citation_validation_failed; #1: not_found | [event 39](trace.jsonl#L39) |
| 8 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit after the enforced critique and source validation. | citation_validation_failed; #1: hyphenation_ambiguous (pages [4]); #2: not_found | [event 47](trace.jsonl#L47) |
| 9 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 55](trace.jsonl#L55) |
