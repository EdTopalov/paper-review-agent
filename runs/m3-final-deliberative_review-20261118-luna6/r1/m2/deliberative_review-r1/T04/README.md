# T04: AgentBench: Evaluating LLMs as Agents

**deliberative_review · ok**

8 model calls · 4 reads · 37.44 s · $0.005831

8 decisions · 5 tool calls · 35691 input tokens (0 cached) · 2765 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.71

AgentBench combines eight interactive environments, an evaluation toolkit, and reported evaluations of 25 LLMs. Its varied tasks and per-environment results make it a useful empirical benchmark, while its modest test-set sizes, weighted aggregate, and still-evolving scope leave questions about the stability and interpretation of comparisons.

- **strength**: The benchmark spans diverse interactive settings, with distinct action spaces and feedback, rather than relying on one task format.
  - Page 4 · citation: exact
  - Quote: "Figure 3: Examples of all environments in AgentBench."

- **strength**: The results table reports scores for 25 models across eight environments, and shows GPT-4 leading in most of them; this supports a performance gap in these reported comparisons.
  - Page 14 · citation: whitespace
  - Quote: "gpt-4 presents the best performance on 7 out of 8 datasets in AgentBench"

- **limitation**: The authors acknowledge that the benchmark's scenario coverage is not exhaustive and describe it as evolving.
  - Page 3 · citation: exact
  - Quote: "there are definitely more scenarios and tasks to cover in LLM-as-agent evaluation."

- **uncertainty**: The aggregate uses task weights derived from average scores across the evaluated models, while the standard test sets vary in size; how sensitive comparisons are to this weighting and sampling is not established in the inspected excerpts.
  - Page 14 · citation: whitespace
  - Quote: "we utilize the reciprocal of the average score of all the tested LLMs in each task as a weight."

Unresolved questions:

- How sensitive are model rankings and the API-versus-open-source comparison to the aggregate weighting and the relatively small standard test sets?
- What validation or robustness analyses are reported elsewhere, including repeated-run or prompt-sensitivity checks?
- I inspected pages 1–5 and 12–14 (page 2 partial); pages 6–11 and 15–38 remain uninspected, so I cannot assess all environment construction details or the paper's full validation and caveats.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the benchmark’s eight environments, task construction, scoring procedures, and stated scope to determine what capabilities the evaluation actually measures.; Check the evidence for the central performance claims: model coverage, experimental protocol, results across environments, and whether conclusions are supported beyond aggregate comparisons.; Inspect limitations and validation details elsewhere in the paper, including robustness, reproducibility, and any caveats; only the abstract and first page are currently available. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 1 matches on pages [2] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 0 matches | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [3, 4, 5] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: investigate; Issues: The score of 0.67 is difficult to substantiate from pages 1–5 alone: the contribution is described, but evidence about the benchmark’s scoring and empirical results remains largely uninspected.; The second observation’s quote, “Each evaluation sample in OS dataset encompasses following contents:”, does not itself support the observation’s claims about executable tasks, task types, or task sourcing. Use a quote that directly supports the stated details, or narrow the claim.; Target: On pages 6–38, what experimental protocol, scoring and aggregation procedure … | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | targeted_read | read pages [12, 13, 14] | [event 34](trace.jsonl#L34) · [event 39](trace.jsonl#L39) |
| 8 | revise | Draft revised; Changes: Updated C2 using the newly observed protocol, test-size, weighting, and results pages. Replaced the OS quotation that did not directly support its claim. The critic's concern about limited initial-page evidence was consequential; the new excerpts substantiate the reported comparisons, but do not resolve their sensitivity or the uninspected validation details. | [event 40](trace.jsonl#L40) · [event 43](trace.jsonl#L43) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "limitations"}` | Inspect stated caveats and evidence for unresolved benchmark scope and validation. | 1 matches on pages [2] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "eight environments"}` | Inspect benchmark composition and task scope. | 0 matches | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 3, "end": 5}` | Inspect benchmark environments and experimental setup/results, addressing evidence obligations C1-C2. | read pages [3, 4, 5] | [event 22](trace.jsonl#L22) |
| 7 | read_pages `{"start": 12, "end": 14}` | Inspect experimental protocol, scoring and cross-environment model results. | read pages [12, 13, 14] | [event 37](trace.jsonl#L37) |
| 8 | submit_review `{"review": {"score": 0.71, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 45](trace.jsonl#L45) |
