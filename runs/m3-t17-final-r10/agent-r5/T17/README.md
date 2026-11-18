# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · ok**

15 model calls · 5 reads · 49.86 s · $0.007091

15 decisions · 15 tool calls · 159504 input tokens (130809 cached) · 4486 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.71

The paper proposes zero-shot Plan-and-Solve prompting: explicitly ask a model to devise and execute a plan, with PS+ adding guidance for variables and intermediate calculations. GPT-3 experiments across ten datasets report gains over Zero-shot-CoT and math performance close to manual few-shot CoT. It is a useful, practical prompting contribution, though the evidence is limited to the tested model and setup.

- **strength**: The method explicitly asks the model to form a plan before solving.
  - Page 2 · citation: normalized
  - Quote: "we propose Plan-and-Solve (PS) Prompting."

- **strength**: PS+ improves the reported average arithmetic accuracy compared with Zero-shot-CoT.
  - Page 6 · citation: exact
  - Quote: "PS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7"

- **limitation**: The main results use one specific GPT-3 engine; transfer beyond it is not demonstrated in the inspected experiments.
  - Page 5 · citation: whitespace
  - Quote: "text-davinci-003 engine for GPT-3 in the main paper."

- **uncertainty**: The authors state that their evaluation spans multiple datasets, but the inspected excerpts do not establish generalization beyond those benchmarks.
  - Page 2 · citation: exact
  - Quote: "two commonsense reasoning datasets"

Unresolved questions:

- Do the reported gains transfer to other model families, model sizes, and later LLMs?
- How sensitive are results to prompt wording and answer extraction?
- I inspected the introduction, implementation/results excerpts, and a few appendix examples, not the full paper; additional qualifications may be present.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "experimental results"}` | Locate the paper’s results section to inspect empirical support for its prompting claims. | 1 matches on pages [5] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 5, "end": 7}` | Read reported benchmark results and evaluation details to gauge evidence and comparative performance. | read pages [5, 6, 7] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 1, "end": 2}` | Inspect the stated motivation and proposed prompt structure to assess the contribution and its intended scope. | read pages [1, 2] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 17, "end": 18}` | Inspect authors’ stated limitations and conclusion for scope boundaries and acknowledged gaps. | read pages [17, 18] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.71, "observations": 4}}` | Evidence covers the proposed prompting method, benchmark results, and evaluation scope; submit an evidence-bounded reading-club assessment. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1, 2]); #2: hyphenation_ambiguous (pages [5]); #3: not_found; #4: not_found | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.71, "observations": 4}}` | Correct quotations using verbatim excerpts and provide a concise assessment grounded in inspected pages. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1, 2]); #2: hyphenation_ambiguous (pages [5]); #3: hyphenation_ambiguous (pages [5]); #4: not_found | [event 30](trace.jsonl#L30) |
| 7 | read_pages `{"start": 2, "end": 2}` | Retrieve exact, citeable wording for the proposed method to correct citation validation. | read pages [2] | [event 35](trace.jsonl#L35) |
| 8 | submit_review `{"review": {"score": 0.71, "observations": 4}}` | Submit the final evidence-bounded review with exact wording from inspected pages and disclose what was not inspected. | citation_validation_failed; #1: not_found; #2: hyphenation_ambiguous (pages [5]); #3: not_found; #4: wrong_page (pages [6]) | [event 41](trace.jsonl#L41) |
| 9 | submit_review `{"review": {"score": 0.71, "observations": 4}}` | Submit concise assessment using short unambiguous verbatim excerpts from observed pages; note inspection limits. | citation_validation_failed; #2: not_found; #4: wrong_page (pages [6]) | [event 47](trace.jsonl#L47) |
| 10 | submit_review `{"review": {"score": 0.71, "observations": 4}}` | Correct remaining citation mismatches with short exact excerpts already observed, and submit the evidence-bounded review. | citation_validation_failed; #2: not_found; #4: wrong_page (pages [6]) | [event 53](trace.jsonl#L53) |
| 11 | submit_review `{"review": {"score": 0.71, "observations": 4}}` | Finalize the review with verified verbatim quotes on correctly cited pages and acknowledge inspected-scope gaps. | citation_validation_failed; #4: not_found | [event 59](trace.jsonl#L59) |
| 12 | submit_review `{"review": {"score": 0.71, "observations": 4}}` | Submit final review with exact observed page quotations, preserving the page numbers and acknowledging portions not inspected. | citation_validation_failed; #2: not_found; #4: wrong_page (pages [6]) | [event 65](trace.jsonl#L65) |
| 13 | submit_review `{"review": {"score": 0.71, "observations": 4}}` | Submit evidence-bounded review with only exact quotations confirmed in the inspected excerpts; disclose scope gaps. | citation_validation_failed; #2: not_found | [event 71](trace.jsonl#L71) |
| 14 | submit_review `{"review": {"score": 0.71, "observations": 4}}` | Submit final assessment with verbatim quotations from inspected pages and clearly state the limits of the inspected material. | citation_validation_failed; #1: not_found; #2: not_found | [event 77](trace.jsonl#L77) |
| 15 | submit_review `{"review": {"score": 0.71, "observations": 4}}` | Finalize assessment using short exact quotes directly copied from the observed results table and method text, with inspection limits disclosed. | review accepted | [event 83](trace.jsonl#L83) |
