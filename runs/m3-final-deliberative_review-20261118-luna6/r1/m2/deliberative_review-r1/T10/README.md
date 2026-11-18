# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**deliberative_review · ok**

8 model calls · 4 reads · 36.36 s · $0.008141

8 decisions · 5 tool calls · 52028 input tokens (0 cached) · 3301 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

SWE-agent introduces an agent-computer interface designed around language-model behavior and evaluates it on repository-level software issues. Its full-test-set results and Lite-set ablations offer useful evidence for the system and for interface design, while the evidence remains bounded by the tested models and benchmark.

- **strength**: The paper specifies concrete interface mechanisms, including file viewing, integrated editing, and lint feedback, making the proposed ACI design inspectable.
  - Page 4 · citation: whitespace
  - Quote: "Invalid edits are discarded and the model is asked to try editing the file again."

- **strength**: The evaluation reports a full-test-set result and describes its models, baselines, and pass-tests metric, giving the headline result a clear evaluation context.
  - Page 5 · citation: exact
  - Quote: "solving 12.47% (286/2,294) of the full SWE-bench test set"

- **strength**: Lite-set ablations report differences across interface configurations, including a 7.7-point drop for the shell-only editor comparison. This supports the interface claim on the 300-instance Lite split, not necessarily across other tasks or models.
  - Page 6 · citation: exact
  - Quote: "Shell-only 10.3 ↓ 7.7"

- **limitation**: The authors state that results and analyses use two leading models, limiting how broadly the findings establish ACI effectiveness. The inspected discussion page emphasizes future study but gives no further specific limitation; most of the PDF was not inspected.
  - Page 5 · citation: exact
  - Quote: "All results, ablations, and analysis are based on two leading LMs"

Unresolved questions:

- How do the ACI effects vary across a wider range of models, repository types, and software-engineering task distributions?
- How much do interface effects vary across individual tasks beyond the aggregate Lite-set ablations?
- What qualifications or limitations, if any, appear in the 15 PDF pages not inspected?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the paper’s methods and evaluation pages to verify how SWE-agent and its ACI are implemented, and whether the reported 12.5% SWE-bench result is supported by a clear setup, baselines, and evaluation evidence.; Check the ACI ablations or comparisons for evidence that interface design drives the claimed performance gains, and note any qualifications or scope limits stated elsewhere in the paper.; Inspect enough of the remaining pages to identify limitations and unresolved questions; only page 1 is currently available, so observations and quotations must be grounded in additional  … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 2 matches on pages [1, 2] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 4 matches on pages [3, 9, 10] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [4, 5, 6] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: investigate; Issues: The fourth observation’s quote is not verified as verbatim by the citation check, so that observation does not currently meet the quote requirement. Its claim also combines model scope, repository scope, and development-set design, while the quote addresses only model scope.; The draft acknowledges that 17 pages were not inspected, but the limitations and unresolved-questions obligation calls for further source inspection. The score and summary are otherwise reasonably qualified by the inspected evidence.; Target: Read the paper’s discussion and limitations … | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | targeted_read | read pages [7, 8, 9] | [event 34](trace.jsonl#L34) · [event 39](trace.jsonl#L39) |
| 8 | revise | Draft revised; Changes: Replaced the unverified fourth-observation quotation with an exact quote from page 5 and narrowed its claim to the two-model scope. Inspected the available discussion page (page 9); it does not supply additional specific limitations, so uncertainty about the uninspected pages is retained. The available evidence does not warrant a score change. | [event 40](trace.jsonl#L40) · [event 43](trace.jsonl#L43) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "12.5%"}` | Locate evaluation results and supporting setup for the headline SWE-bench performance. | 2 matches on pages [1, 2] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Locate the paper’s discussion of scope and limitations, then inspect method/evaluation evidence for the main claims. | 4 matches on pages [3, 9, 10] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 4, "end": 6}` | Inspect implementation and evaluation/ablation details supporting SWE-agent performance claims. | read pages [4, 5, 6] | [event 22](trace.jsonl#L22) |
| 7 | read_pages `{"start": 7, "end": 9}` | Inspect discussion/conclusion pages for explicit limitations and scope boundaries. | read pages [7, 8, 9] | [event 37](trace.jsonl#L37) |
| 8 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 45](trace.jsonl#L45) |
