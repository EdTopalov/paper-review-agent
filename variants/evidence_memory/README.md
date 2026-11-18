# Evidence memory

Variant flag: `evidence_memory`. This version changes the context supplied to
the native ReAct loop. The model, rubric, tool schemas, citation acceptance,
reading and decision budgets, retries, and output limit are shared with `agent`.

## Mechanism and hypothesis

The M2 T17 run grows from 4,348 to 46,764 serialized input characters over eight
decisions. Its final four decisions submit reviews; rejected drafts and their
feedback remain in every later request. See the [failure trace](../../runs/m2-integrated-20261026/agent-r1/T17/README.md#decisions),
decisions at events 25, 30, 35, and 40. Repeating previous drafts may increase cost
and encourage further revisions of an already incorrect quotation. The trace
establishes repetition, but does not establish that repetition causes the failure.

**Prediction, registered before evaluation:** replacing the complete conversation
with an exact evidence packet and compact action ledger will reduce mean input
tokens per attempted review without reducing verified-review completion by more
than five percentage points on the frozen 20-paper sample. Cost is a secondary
outcome because losing cached conversation prefixes may offset token savings.
Repair-heavy cases, including T17, should show the largest reduction in context
growth. A quality improvement is not assumed; independent assessment labels are
needed to test whether discarding drafts loses useful conclusions.

Every model request starts afresh with:

- The paper metadata and every distinct excerpt already observed, grouped by its
  original page number. Identical text on the same page is stored once.
- A ledger of actions, queries or requested ranges, and concise outcomes.
- The latest tool feedback, remaining reading budget, and the most recent rejected
  quotations with their page numbers and validation diagnostics.

Earlier model outputs, scores, summaries, claims, and full draft reviews are
omitted. Rejected quotations are explicitly marked as feedback and never added to
observed evidence. No model generates summaries, and no extra API calls are made.
This memory lasts for one paper; it is not shared between papers or runs.

The evidence packet has no additional truncation or arbitrary token cap. Its size
is constrained by the existing reading budget and tool limits: at most three
8,000-character page excerpts per page-read action or eight snippets per search,
plus the complete initial page. Search snippets also contain the query match,
whose length is not assigned a separate fixed limit. Deduplication reduces exact
repeats; distinct overlapping excerpts remain intact. This is context curation,
not a promise of a fixed maximum prompt size.

**Expected trace evidence:** `context_memory` precedes each decision and records
the policy, evidence page/fragment counts, evidence characters, action count, and
serialized input characters. Full requests remain reconstructible from the trace.
A rejected draft's summary should disappear from the next request while its
observed source text and failed-quotation feedback remain. A reread of the same
page should not add another identical fragment. Success and cost comparisons must
include failed attempts and repeated runs of every variant and the baseline.

## Execution

After the [shared installation](../../README.md#installation):

```shell
paper-review review data/eval/papers/T17.json --task-id T17 --variant evidence_memory --out runs/scratch/memory-T17
paper-review eval --variants agent pyagent_react evidence_memory baseline --repeats 5 --workers 3 --out runs/memory-comparison
python -m pytest -q tests/test_context_memory.py
```

The first two commands use the configured API and incur costs. Use the same
explicit model and limits for every method in each comparison. The common output
layout, metrics, and offline checks are described in the [root guide](../../README.md).

The implementation is in [context_memory.py](../../src/paper_review/context_memory.py)
and the shared native loop in [runner.py](../../src/paper_review/runner.py).
The policy is inspired by structured note-taking and context curation in
[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
All code is original; no source code is copied from that article.
