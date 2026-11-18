# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · ok**

11 model calls · 5 reads · 34.31 s · $0.004845

11 decisions · 11 tool calls · 90286 input tokens (68548 cached) · 2953 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

The paper proposes zero-shot Plan-and-Solve prompting: ask an LLM to devise a plan and carry it out, with PS+ adding instructions about variable extraction and intermediate calculations. GPT-3 results across ten math, commonsense, and symbolic datasets generally improve over Zero-shot-CoT, and PS+ approaches few-shot CoT on arithmetic tasks. The work offers useful prompt design with broad task coverage, but evidence inspected is limited to one model family and the authors note wording sensitivity and remaining semantic errors.

- **strength**: Across arithmetic datasets the paper reports that PS+ consistently beats the zero-shot chain-of-thought baseline.
  - Page 5 · citation: whitespace
  - Quote: "PS+ prompting im- proves the accuracy over Zero-shot CoT by at least 5% for all datasets except GSM8K which sees a 2.9% improvement."

- **strength**: In the commonsense results table, PS+ outperforms Zero-shot-CoT on both listed datasets.
  - Page 6 · citation: exact
  - Quote: "Zero-shot-PS+ (ours) 71.9 65.4"

- **limitation**: The authors explicitly note that prompt wording sensitivity makes careful prompt design necessary.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3 models are sensitive to the expressions in prompts, thus we need to carefully design the prompts."

Unresolved questions:

- How robust are the gains across model families and prompt paraphrases? Main results inspected here use GPT-3 text-davinci-003.
- How stable are error-category findings across datasets and independent annotators?
- I inspected the first page, pages 5–7, and pages 9–10; other portions and appendices were not examined.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "experimental results"}` | Locate evaluation evidence and reported results for the proposed prompting method. | 1 matches on pages [5] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect quantitative results and experiment setup across evaluated reasoning tasks. | read pages [5, 6, 7] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Check whether the paper explicitly discusses limitations or scope boundaries. | 2 matches on pages [9] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 9, "end": 10}` | Read stated limitations and conclusion to accurately characterize boundaries and overall claims. | read pages [9, 10] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Evidence covers main quantitative comparisons, setup, and stated limitations; submit a balanced paper assessment while noting inspection gaps. | citation_validation_failed; #1: hyphenation_ambiguous (pages [5]); #4: hyphenation_ambiguous (pages [9]) | [event 25](trace.jsonl#L25) |
| 6 | read_pages `{"start": 6, "end": 9}` | Retrieve exact observed wording for citations flagged as ambiguous and confirm limitation language verbatim. | invalid_page_range | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Resubmit with citations corrected to exact observed phrases; evidence and inspected-page caveat remain unchanged. | citation_validation_failed; #1: hyphenation_ambiguous (pages [5]); #4: hyphenation_ambiguous (pages [9]) | [event 36](trace.jsonl#L36) |
| 8 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Submit the assessment using only exact short excerpts that appeared in the observed page text and state inspection limits. | citation_validation_failed; #1: hyphenation_ambiguous (pages [5]) | [event 42](trace.jsonl#L42) |
| 9 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Finalize review with exact, citation-validated excerpts from pages 6 and 9 and transparent inspection limitations. | citation_validation_failed; #4: hyphenation_ambiguous (pages [9]) | [event 48](trace.jsonl#L48) |
| 10 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Conclude with citation-validated excerpts copied exactly from the observed PDF text; explicitly flag inspected-page limits. | citation_validation_failed; #2: not_found; #4: hyphenation_ambiguous (pages [9]) | [event 54](trace.jsonl#L54) |
| 11 | submit_review `{"review": {"score": 0.69, "observations": 3}}` | Submit a balanced assessment using exact, directly observed excerpts from results and the stated prompt-sensitivity limitation. | review accepted | [event 60](trace.jsonl#L60) |
