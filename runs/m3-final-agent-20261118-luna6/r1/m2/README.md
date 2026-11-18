# Experiment results

Open a task to read its review, decisions, tool outcomes, and optional evidence audit. [Settings](experiment.json) · [Evaluated source](source.zip)

Completion means the workflow returned an accepted review. The agent also blocks invalid citations; the one-call baseline does not. Verified citations match source text, not necessarily the meaning of a claim. Summary rates include failed attempts.

An evidence audit is a separate model judgment of claim support; supported counts are provisional verdicts. A first submission is the review proposed before citation repair.

| Method | Completed | All citations verified | Steps/task | Tools/task | Reads/task | Calls/task | Input tokens/task | Output tokens/task | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agent | 18/20 | 18/20 | 5.80 | 5.70 | 4.25 | 5.80 | 31103.8 | 819.8 | $0.002174 | 14.33 |

## Repetition variation

Verified success requires both a completed review and all quotations verified. It measures citation compliance, not assessment quality. Every planned attempt, including a failed attempt, stays in the denominator. Model IDs are not pooled.

| Method | Repeat | Completed | Verified success | Calls/task | Tokens/task (in/out) | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---|---:|---:|
| agent | 1 | 18/20 | 18/20 | 5.80 | 31103.8/819.8 | $0.002174 | 14.33 |

### Reliability across repetitions

pass^k estimates success on every one of k independent attempts: mean over papers of C(s,k)/C(n,k), where s is the number of verified successes and n the number of attempts for that paper. It is not success at least once. Independence is an assumption; few repetitions give limited precision.

| Method | Always / sometimes / never verified (papers) | pass^k | Mean absolute score difference within a paper | Score pairs |
|---|---|---|---:|---:|
| agent | 18 / 0 / 2 | k=1: 0.900 | unavailable | 0 |

### Paired differences between methods

Each paper contributes its mean over observed repetitions. Differences are left minus right. The 95% percentile bootstrap intervals resample papers 2,000 times, keeping each paper's repetitions together (seed 20261118). These exploratory intervals describe this convenience sample conditional on the observed repetitions; they do not capture future API model drift. A single paper has no interval. Scores use only completed reviews from papers completed by both methods and are not validated quality labels.

| Pair | Verified success difference (95% interval) | Score difference (95% interval) | Mean absolute task score difference | USD/task difference | Seconds/task difference |
|---|---|---|---:|---:|---:|

### Per-paper consistency

Score spread excludes failed attempts; completion counts retain them. Compare within-paper score variation above with between-method differences before interpreting small gaps.

| Method | Task | Completed / attempts | Verified / attempts | Mean score | Score sample SD | Score range |
|---|---|---:|---:|---:|---:|---|
| agent | T01 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| agent | T02 | 0/1 | 0/1 | unavailable | unavailable | unavailable |
| agent | T03 | 1/1 | 1/1 | 0.6900 | unavailable | [0.69, 0.69] |
| agent | T04 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T05 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| agent | T06 | 1/1 | 1/1 | 0.7900 | unavailable | [0.79, 0.79] |
| agent | T07 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| agent | T08 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| agent | T09 | 1/1 | 1/1 | 0.7300 | unavailable | [0.73, 0.73] |
| agent | T10 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| agent | T11 | 1/1 | 1/1 | 0.7500 | unavailable | [0.75, 0.75] |
| agent | T12 | 1/1 | 1/1 | 0.7400 | unavailable | [0.74, 0.74] |
| agent | T13 | 1/1 | 1/1 | 0.7700 | unavailable | [0.77, 0.77] |
| agent | T14 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| agent | T15 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| agent | T16 | 1/1 | 1/1 | 0.6400 | unavailable | [0.64, 0.64] |
| agent | T17 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| agent | T18 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| agent | T19 | 0/1 | 0/1 | unavailable | unavailable | unavailable |
| agent | T20 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |

## agent

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [agent-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](agent-r1/T06/README.md) | ok | 0.79 | 0 | yes | not audited | 5 | 23612/650 | $0.001478 | 10.23 |
| [agent-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](agent-r1/T01/README.md) | ok | 0.78 | 0 | yes | not audited | 4 | 23000/594 | $0.001914 | 10.82 |
| [agent-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](agent-r1/T05/README.md) | ok | 0.78 | 0 | yes | not audited | 6 | 20333/531 | $0.001745 | 10.86 |
| [agent-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](agent-r1/T07/README.md) | ok | 0.78 | 0 | yes | not audited | 6 | 30121/653 | $0.002609 | 13.36 |
| [agent-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](agent-r1/T08/README.md) | ok | 0.78 | 2 | no | not audited | 8 | 58666/1511 | $0.003958 | 18.79 |
| [agent-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](agent-r1/T13/README.md) | ok | 0.77 | 0 | yes | not audited | 6 | 30443/712 | $0.002624 | 15.29 |
| [agent-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](agent-r1/T14/README.md) | ok | 0.76 | 0 | yes | not audited | 5 | 28453/559 | $0.001938 | 14.02 |
| [agent-r1/T11: Executable Code Actions Elicit Better LLM Agents](agent-r1/T11/README.md) | ok | 0.75 | 0 | yes | not audited | 6 | 22938/636 | $0.001866 | 11.93 |
| [agent-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](agent-r1/T10/README.md) | ok | 0.74 | 1 | no | not audited | 6 | 28925/1238 | $0.001944 | 16.29 |
| [agent-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](agent-r1/T12/README.md) | ok | 0.74 | 0 | yes | not audited | 6 | 34860/596 | $0.002906 | 11.68 |
| [agent-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](agent-r1/T09/README.md) | ok | 0.73 | 0 | yes | not audited | 5 | 23096/616 | $0.001579 | 11.77 |
| [agent-r1/T04: AgentBench: Evaluating LLMs as Agents](agent-r1/T04/README.md) | ok | 0.72 | 1 | no | not audited | 7 | 48086/1059 | $0.003512 | 20.78 |
| [agent-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](agent-r1/T15/README.md) | ok | 0.72 | 3 | no | not audited | 7 | 46123/1840 | $0.002567 | 22.63 |
| [agent-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](agent-r1/T20/README.md) | ok | 0.72 | 3 | no | not audited | 9 | 68529/2034 | $0.004086 | 30.68 |
| [agent-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](agent-r1/T03/README.md) | ok | 0.69 | 0 | yes | not audited | 5 | 23393/632 | $0.001595 | 13.59 |
| [agent-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r1/T17/README.md) | ok | 0.68 | 1 | no | not audited | 5 | 25829/1022 | $0.001622 | 14.59 |
| [agent-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](agent-r1/T18/README.md) | ok | 0.68 | 0 | yes | not audited | 5 | 23478/599 | $0.001440 | 14.14 |
| [agent-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](agent-r1/T16/README.md) | ok | 0.64 | 0 | yes | not audited | 5 | 26262/557 | $0.001724 | 10.00 |
| [agent-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](agent-r1/T02/README.md) | error | — | 0 | unavailable | not audited | 5 | 13209/147 | $0.000864 | 9.15 |
| [agent-r1/T19: A Survey on Large Language Model based Autonomous Agents](agent-r1/T19/README.md) | error | — | 0 | unavailable | not audited | 5 | 22721/210 | $0.001515 | 5.95 |

Per-task cost/time includes unsuccessful attempts; audit cost is separate.
