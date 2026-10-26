# Frozen M2 evaluation sample

One task is one independent paper review against the common `m2-v1` rubric. The
20 versioned papers were selected before model evaluation. `data/selection.json` fixes the paper
identifiers. `tasks.jsonl` binds each task to the SHA-256 of its exact input.

The environment is the committed JSON text snapshot in `papers/`, with the PDF
page boundaries preserved. Both the agent's tools and the one-shot baseline use
this identical text. No live websites or downloads are used during evaluation.
The original PDF bytes can be downloaded using `scripts/freeze_sample.py` and
checked against the recorded `pdf_sha256`, but are not needed to run the agent.
Extraction is frozen; changing parser versions does not change existing inputs.

This is a convenience sample of public ML papers about agents, tools, coding,
retrieval, reasoning, and context evaluation, including one survey. It favors
well-known 2022–2024 papers with CC BY 4.0 licenses and extractable PDFs. It does
not represent all scientific fields, all paper types, or contemporary unpublished
submissions. The model may already know these papers. Results establish behavior
on these inputs, not performance on unseen research. The five pilot papers are
not counted as evaluation tasks or used as approved gold labels.

Each snapshot includes source/version, title, author attribution, license URL,
PDF hash, extraction software, modification notice, and page text. The source
papers retain their authors' CC BY 4.0 license. The snapshots omit page images,
figures, and original layout: this is an explicitly text-only M2 environment.
Broken table extraction is a known limitation, not repaired using model output.

Reference scores remain null. Do not derive numerical gold scores from review
tone, paper popularity, or task identifiers. Quality evaluation uses separately
reported mechanical checks and an evidence audit, not score MAE. Model-produced
audits are provisional judgments and must be identified as such.

Run `paper-review verify --sample data/eval/tasks.jsonl` before evaluation. Keep
this exact manifest and snapshots for M3. Prompt development uses separate input
papers; any tuning after seeing this sample's outcomes must be disclosed.
