# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**deliberative_review · ok**

9 model calls · 4 reads · 45.73 s · $0.010925

9 decisions · 6 tool calls · 71423 input tokens (1311 cached) · 4321 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

SWE-agent’s central contribution is a purpose-built agent-computer interface for repository-level software engineering, evaluated through benchmark results and interface ablations. The reported results support a meaningful benefit in the tested setting, particularly against a same-model shell-only baseline on SWE-bench Lite. However, the headline comparison to prior RAG results is not established as like-for-like, and the available pages do not allow a full assessment of the paper’s later discussion or limitations.

- **strength**: The paper explicitly presents interface design—not changing model weights—as a contribution, and describes tools for searching, navigating, editing, and receiving feedback on code.
  - Page 1 · citation: whitespace
  - Quote: "we introduce SWE-agent, an autonomous system that uses a language model to interact with a computer to solve software engineering tasks."

- **strength**: The results include a same-model comparison on the 300-instance Lite split: GPT-4 Turbo resolves 18.00% with SWE-agent and 11.00% with the shell-only agent. This supports an interface benefit in that setting, though not across all settings.
  - Page 6 · citation: exact
  - Quote: "w/ GPT-4 Turbo 1.31 0.13 2.67 0.13"

- **limitation**: The authors say final ACI design drew on qualitative analysis of hand-picked, easier development examples. This is a stated design procedure and a reason to be cautious about generalizing the gains, not evidence that the test results are invalid.
  - Page 5 · citation: whitespace
  - Quote: "qualitative analysis of system behavior on small set of hand-picked easier examples from the development split of SWE-bench."

- **uncertainty**: The inspected material covers pages 1–7 and partial excerpts from pages 9–10; pages 8 and 11–25 are uninspected. The full discussion and limitations therefore remain unassessed.
  - Page 7 · citation: whitespace
  - Quote: "In this section, we discuss several model behaviors and problem solving patterns"

Unresolved questions:

- How do the uninspected discussion and later pages qualify the findings, limitations, and failure modes?
- How robust are the Lite-set ablation results to issue-subset variation, and do interface gains hold beyond the tested models and benchmark?
- How comparable are the prior RAG results and SWE-agent’s headline full-test result in model and evaluation protocol?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the methods and evaluation pages for the SWE-bench setup, baselines, model/tool settings, and evidence supporting the headline 12.5% versus 3.8% claim.; Inspect ACI comparisons and ablations elsewhere in the paper to determine whether the claimed interface benefit is isolated from other factors and supported across relevant tasks or settings.; Inspect discussion and limitations, then select 2–4 specific observations with exact page-numbered quotes; explicitly note that only page 1 is currently available and avoid treating uninspected content as absent. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | read pages [2, 3, 4] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 4 matches on pages [2, 3, 6] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | 4 matches on pages [3, 9, 10] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: investigate; Issues: The draft is appropriately cautious about the incomplete evidence, but the required evaluation and limitations inspection remains unfinished: 18 pages are uninspected, and the available ablation-page excerpt is partial. A targeted read is needed before settling the score and scope assessment.; The first observation's quote is not verified by the citation check. Replace it with a short verbatim passage that matches the observed page text exactly. The other two quotes are verified.; Target: On the evaluation pages, what are the SWE-bench setup and baseline/mo … | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | targeted_read | read pages [5, 6, 7] | [event 34](trace.jsonl#L34) · [event 39](trace.jsonl#L39) |
| 8 | revise | Draft revised; Changes: Updated the evaluation assessment using the supplied pages 5–7: distinguished the cross-model RAG headline comparison from the same-model Lite shell-only comparison, and incorporated the reported ablation results and configuration-selection procedure. Replaced the first observation’s quote with an exact observed passage. The remaining discussion and limitations are still uninspected, so uncertainty is retained rather than treating that gap as a demonstrated defect. | [event 40](trace.jsonl#L40) · [event 43](trace.jsonl#L43) |
| 9 | revise | Draft revised; Changes: Replaced the unverified page-2 quotation with a verbatim quotation from page 1. Retained the caution about incomplete coverage and the qualified assessment of the benchmark comparisons; the supplied material does not include additional pages to resolve the critic’s request for a fuller inspection. | [event 48](trace.jsonl#L48) · [event 51](trace.jsonl#L51) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect method/evaluation setup and supporting evidence beyond the abstract. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "Table 2"}` | Locate ACI ablations and evaluation evidence beyond the supplied opening pages. | 4 matches on pages [2, 3, 6] | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "limitations"}` | Inspect discussion/limitations and obtain evidence beyond the currently inspected introduction pages. | 4 matches on pages [3, 9, 10] | [event 22](trace.jsonl#L22) |
| 7 | read_pages `{"start": 5, "end": 7}` | Inspect evaluation setup, baseline comparisons, and ACI ablation results. | read pages [5, 6, 7] | [event 37](trace.jsonl#L37) |
| 8 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Submit after the enforced critique and source validation. | citation_validation_failed; #1: hyphenation_ambiguous (pages [2]) | [event 45](trace.jsonl#L45) |
| 9 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 53](trace.jsonl#L53) |
