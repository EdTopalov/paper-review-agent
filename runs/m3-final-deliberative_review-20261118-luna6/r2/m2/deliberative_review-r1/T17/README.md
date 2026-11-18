# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**deliberative_review · ok**

8 model calls · 3 reads · 37.25 s · $0.004561

8 decisions · 5 tool calls · 23566 input tokens (1565 cached) · 3610 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

The paper proposes zero-shot Plan-and-Solve prompting, which asks an LLM to make a plan and then carry it out, and PS+ with more detailed instructions. The authors report gains over Zero-shot-CoT across ten datasets and performance comparable to 8-shot CoT on math reasoning. This is a practical prompting contribution, but the supplied excerpts do not allow a thorough assessment of the experimental comparisons or the proposed mechanism.

- **strength**: The paper motivates its approach with an error analysis of incorrect Zero-shot-CoT answers. The excerpt does not provide enough detail to assess the reliability of the error categorization.
  - Page 1 · citation: whitespace
  - Quote: "we assign “Calculation Error” (7%), “Step Missing Error” (12%), or “Semantic misunder-\nstanding Error” (27%) to each incorrect answer."

- **strength**: The authors describe a broad evaluation, and the partial results excerpt reports PS+ gains on arithmetic datasets. Full tables and protocol details were not supplied, so the magnitude and robustness of the gains cannot be assessed here.
  - Page 1 · citation: whitespace
  - Quote: "We evaluate our proposed prompting strategy on ten datasets across three reasoning problems."

- **limitation**: The authors acknowledge prompt-design effort and sensitivity. This is a stated scope limitation, not evidence of failure on a particular tested case.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3 models are sensitive to the expressions in prompts, thus we need to carefully design the prompts."

Unresolved questions:

- How are prompts, model/API settings, sampling parameters, and evaluation conditions matched across the proposed method and baselines?
- What do the complete results and error analyses show about the size and consistency of gains, and do they establish that planning itself addresses missing-step errors?
- How well does the approach transfer beyond the evaluated GPT-3 models and datasets?
- Most of the paper was not inspected: only excerpts from pages 1, 4, 5, and 9 were supplied, and pages 4, 5, and 9 are partial.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the prompt formulations, model/API settings, datasets, and evaluation protocol to determine whether the comparison with Zero-shot-CoT and other baselines is controlled and sufficiently specified.; Review results and any error analyses across the paper to verify the claimed gains across datasets and assess the support for the proposed plan-and-solve mechanisms; check whether apparent gaps in the abstract are addressed elsewhere.; Inspect discussion, limitations, and conclusion for scope boundaries and unresolved issues, and collect short verbatim quotations with PDF page numbers … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 1 matches on pages [4] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 2 matches on pages [9] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | 1 matches on pages [5] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: Two quotes are flagged as not verified or hyphenation-ambiguous. Replace them with short spans that match the supplied source text unambiguously, while retaining the required page citations.; Target: Revise the page 1 and page 5 observation quotes to use unambiguous verbatim spans from E1 and E5. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Replaced the page 1 and page 5 quotations flagged as ambiguous with short, unambiguous quotations verified against the supplied source text. The limited excerpts still do not support stronger conclusions about the full protocol, results, or mechanism. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |
| 8 | revise | Draft revised; Changes: Replaced the page 1 error-analysis quotation with the exact observed wording, preserving its line-break hyphenation. The page 1 evaluation quotation and page 9 limitation quotation are also verified against the supplied excerpts. The page 5 results excerpt remains reflected in the summary and ledger; no page 5 quotation is needed. The supplied excerpts are insufficient to resolve the critic's broader questions about controlled comparisons or complete results. | [event 42](trace.jsonl#L42) · [event 45](trace.jsonl#L45) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "Experimental Setup"}` | Inspect model settings, datasets, and evaluation protocol to assess experimental comparability. | 1 matches on pages [4] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Locate discussion of scope and limitations to support an evidence-based assessment. | 2 matches on pages [9] | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "Experimental Results"}` | Inspect results and comparison evidence supporting the paper’s claims. | 1 matches on pages [5] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.62, "observations": 3}}` | Submit after the enforced critique and source validation. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1]) | [event 39](trace.jsonl#L39) |
| 8 | submit_review `{"review": {"score": 0.62, "observations": 3}}` | Submit after the enforced critique and source validation. | review accepted | [event 47](trace.jsonl#L47) |
