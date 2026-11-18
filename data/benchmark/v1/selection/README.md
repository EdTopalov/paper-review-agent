# Explicit-brief selection and order diagnostics

These original hypothetical candidate sets have deterministic reference choices
under an explicit selection policy. They do not encode universal scientific
quality or measured human reading-club preferences.

Six base sets each have three input orders, giving **6 development cases** and
**12 test cases**. Candidate counts are 3, 6, and 9. Development includes a unique
choice and a tie; test includes long candidate lists, a methodological-failure
discussion goal, no eligible candidate, and task/language distractors. All order
variants of a base set stay in the same split. Unique winners occur first,
centrally, and last across the three orders.

The replication brief specifies task, languages, memory, independence, and seed
reporting requirements, then preferences for the interval lower bound and lower
GPU memory. The methodological-discussion brief instead seeks a documented
best-seed-as-mean error, then prefers a larger discrepancy and lower memory.
These are explicit task contracts, not inferred human preferences. Equal
preference quantities produce acceptable ties; no eligible candidate requires
`selected_id: null`.

`inputs/` contains the brief and candidate reports. `references/` contains
candidate facts, eligible/acceptable IDs, and order/base-set identities.
`manifest.jsonl` hashes both. Give agents only public input files. Every supplied
fact is text, and references use block/document IDs rather than PDF page numbers.

Regenerate without model calls:

```shell
python scripts/prepare_controlled_benchmark.py --out runs/scratch/rebuilt-controlled
```

Report acceptable-choice accuracy (including correct abstention), eligibility
violations, tie handling, and order sensitivity per base set, alongside total
cost and latency. Orders are correlated copies of a candidate set and must not
be treated as independent preference labels. These artifacts prepare a selection
task; they do not implement rolling cross-paper agent memory or run any agent.

Original candidate reports and records are dedicated to the public domain under
[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). `source.json`
records the generator version, counts, and manifest hash.
