# Experiment results

Open a task to read its review, decisions, tool outcomes, and optional evidence audit. [Settings](experiment.json) · [Evaluated source](source.zip)

Completion means the workflow returned an accepted review. The agent also blocks invalid citations; the one-call baseline does not. Verified citations match source text, not necessarily the meaning of a claim. Summary rates include failed attempts.

An evidence audit is a separate model judgment of claim support; supported counts are provisional verdicts. A first submission is the review proposed before citation repair.

| Method | Completed | All citations verified | Steps/task | Tools/task | Reads/task | Calls/task | Input tokens/task | Output tokens/task | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| baseline | 20/20 | 8/20 | 1.00 | 0.00 | 0.00 | 1.00 | 24778.5 | 597.6 | $0.000547 | 7.27 |

## Repetition variation

Verified success requires both a completed review and all quotations verified. It measures citation compliance, not assessment quality. Every planned attempt, including a failed attempt, stays in the denominator. Model IDs are not pooled.

| Method | Repeat | Completed | Verified success | Calls/task | Tokens/task (in/out) | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---|---:|---:|
| baseline | 1 | 20/20 | 8/20 | 1.00 | 24778.5/597.6 | $0.000547 | 7.27 |

### Reliability across repetitions

pass^k estimates success on every one of k independent attempts: mean over papers of C(s,k)/C(n,k), where s is the number of verified successes and n the number of attempts for that paper. It is not success at least once. Independence is an assumption; few repetitions give limited precision.

| Method | Always / sometimes / never verified (papers) | pass^k | Mean absolute score difference within a paper | Score pairs |
|---|---|---|---:|---:|
| baseline | 8 / 0 / 12 | k=1: 0.400 | unavailable | 0 |

### Paired differences between methods

Each paper contributes its mean over observed repetitions. Differences are left minus right. The 95% percentile bootstrap intervals resample papers 2,000 times, keeping each paper's repetitions together (seed 20261118). These exploratory intervals describe this convenience sample conditional on the observed repetitions; they do not capture future API model drift. A single paper has no interval. Scores use only completed reviews from papers completed by both methods and are not validated quality labels.

| Pair | Verified success difference (95% interval) | Score difference (95% interval) | Mean absolute task score difference | USD/task difference | Seconds/task difference |
|---|---|---|---:|---:|---:|

### Per-paper consistency

Score spread excludes failed attempts; completion counts retain them. Compare within-paper score variation above with between-method differences before interpreting small gaps.

| Method | Task | Completed / attempts | Verified / attempts | Mean score | Score sample SD | Score range |
|---|---|---:|---:|---:|---:|---|
| baseline | T01 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| baseline | T02 | 1/1 | 0/1 | 0.6500 | unavailable | [0.65, 0.65] |
| baseline | T03 | 1/1 | 1/1 | 0.6200 | unavailable | [0.62, 0.62] |
| baseline | T04 | 1/1 | 0/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T05 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| baseline | T06 | 1/1 | 0/1 | 0.7400 | unavailable | [0.74, 0.74] |
| baseline | T07 | 1/1 | 0/1 | 0.7800 | unavailable | [0.78, 0.78] |
| baseline | T08 | 1/1 | 0/1 | 0.7400 | unavailable | [0.74, 0.74] |
| baseline | T09 | 1/1 | 0/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T10 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| baseline | T11 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T12 | 1/1 | 0/1 | 0.7200 | unavailable | [0.72, 0.72] |
| baseline | T13 | 1/1 | 0/1 | 0.7500 | unavailable | [0.75, 0.75] |
| baseline | T14 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| baseline | T15 | 1/1 | 0/1 | 0.6400 | unavailable | [0.64, 0.64] |
| baseline | T16 | 1/1 | 0/1 | 0.5800 | unavailable | [0.58, 0.58] |
| baseline | T17 | 1/1 | 0/1 | 0.6900 | unavailable | [0.69, 0.69] |
| baseline | T18 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| baseline | T19 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| baseline | T20 | 1/1 | 0/1 | 0.6500 | unavailable | [0.65, 0.65] |

## baseline

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [baseline-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](baseline-r1/T01/README.md) | ok | 0.78 | 0 | yes | not audited | 1 | 30789/513 | $0.000565 | 6.91 |
| [baseline-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](baseline-r1/T05/README.md) | ok | 0.78 | 0 | yes | not audited | 1 | 16657/536 | $0.000435 | 6.69 |
| [baseline-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](baseline-r1/T07/README.md) | ok | 0.78 | 0 | no | not audited | 1 | 38684/616 | $0.000695 | 6.74 |
| [baseline-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](baseline-r1/T14/README.md) | ok | 0.76 | 0 | yes | not audited | 1 | 24226/575 | $0.000530 | 6.09 |
| [baseline-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](baseline-r1/T13/README.md) | ok | 0.75 | 0 | no | not audited | 1 | 27075/481 | $0.000512 | 5.72 |
| [baseline-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](baseline-r1/T06/README.md) | ok | 0.74 | 0 | no | not audited | 1 | 35056/552 | $0.000627 | 7.64 |
| [baseline-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](baseline-r1/T08/README.md) | ok | 0.74 | 0 | no | not audited | 1 | 36934/612 | $0.000676 | 7.59 |
| [baseline-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](baseline-r1/T10/README.md) | ok | 0.74 | 0 | yes | not audited | 1 | 23863/546 | $0.000512 | 6.04 |
| [baseline-r1/T04: AgentBench: Evaluating LLMs as Agents](baseline-r1/T04/README.md) | ok | 0.72 | 0 | no | not audited | 1 | 36072/576 | $0.000649 | 7.24 |
| [baseline-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](baseline-r1/T09/README.md) | ok | 0.72 | 0 | no | not audited | 1 | 16572/657 | $0.000494 | 7.97 |
| [baseline-r1/T11: Executable Code Actions Elicit Better LLM Agents](baseline-r1/T11/README.md) | ok | 0.72 | 0 | yes | not audited | 1 | 30099/663 | $0.000633 | 7.67 |
| [baseline-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](baseline-r1/T12/README.md) | ok | 0.72 | 0 | no | not audited | 1 | 26994/510 | $0.000525 | 5.65 |
| [baseline-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](baseline-r1/T17/README.md) | ok | 0.69 | 0 | no | not audited | 1 | 18064/734 | $0.000548 | 9.69 |
| [baseline-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](baseline-r1/T18/README.md) | ok | 0.68 | 0 | yes | not audited | 1 | 17424/606 | $0.000478 | 7.04 |
| [baseline-r1/T19: A Survey on Large Language Model based Autonomous Agents](baseline-r1/T19/README.md) | ok | 0.68 | 0 | yes | not audited | 1 | 33041/699 | $0.000680 | 9.40 |
| [baseline-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](baseline-r1/T02/README.md) | ok | 0.65 | 0 | no | not audited | 1 | 14416/710 | $0.000499 | 9.99 |
| [baseline-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](baseline-r1/T20/README.md) | ok | 0.65 | 0 | no | not audited | 1 | 13497/674 | $0.000472 | 7.30 |
| [baseline-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](baseline-r1/T15/README.md) | ok | 0.64 | 0 | no | not audited | 1 | 8838/633 | $0.000405 | 7.07 |
| [baseline-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](baseline-r1/T03/README.md) | ok | 0.62 | 0 | yes | not audited | 1 | 23878/552 | $0.000515 | 6.92 |
| [baseline-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](baseline-r1/T16/README.md) | ok | 0.58 | 0 | no | not audited | 1 | 23392/508 | $0.000488 | 5.99 |

Per-task cost/time includes unsuccessful attempts; audit cost is separate.
