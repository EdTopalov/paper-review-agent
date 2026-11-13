# Experiment results

Open a task to read its review, decisions, tool outcomes, and optional evidence audit. [Settings](experiment.json) · [Evaluated source](source.zip)

Completion means the workflow returned an accepted review. The agent also blocks invalid citations; the one-call baseline does not. Verified citations match source text, not necessarily the meaning of a claim. Summary rates include failed attempts.

An evidence audit is a separate model judgment of claim support; supported counts are provisional verdicts. A first submission is the review proposed before citation repair.

| Method | Completed | All citations verified | Steps/task | Tools/task | Reads/task | Calls/task | Input tokens/task | Output tokens/task | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agent | 16/20 | 16/20 | 3.80 | 3.80 | 2.00 | 3.80 | 14222.4 | 845.6 | $0.001532 | 11.57 |
| baseline | 20/20 | 7/20 | 1.00 | 0.00 | 0.00 | 1.00 | 24778.5 | 581.8 | $0.003388 | 5.50 |
| pyagent_react | 17/20 | 17/20 | 4.25 | 3.85 | 1.85 | 4.25 | 19912.7 | 1226.6 | $0.002029 | 16.81 |

## agent

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [agent-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](agent-r1/T07/README.md) | ok | 0.78 | 0 | yes | not audited | 3 | 14251/500 | $0.001845 | 7.32 |
| [agent-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](agent-r1/T01/README.md) | ok | 0.76 | 1 | no | not audited | 4 | 12104/956 | $0.001366 | 15.06 |
| [agent-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](agent-r1/T05/README.md) | ok | 0.74 | 1 | no | not audited | 4 | 13439/896 | $0.001430 | 13.63 |
| [agent-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](agent-r1/T08/README.md) | ok | 0.74 | 0 | yes | not audited | 3 | 9175/483 | $0.001206 | 7.44 |
| [agent-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](agent-r1/T10/README.md) | ok | 0.74 | 1 | no | not audited | 4 | 13999/1027 | $0.001555 | 15.50 |
| [agent-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](agent-r1/T14/README.md) | ok | 0.74 | 0 | yes | not audited | 3 | 8404/556 | $0.001140 | 7.18 |
| [agent-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](agent-r1/T06/README.md) | ok | 0.72 | 1 | no | not audited | 4 | 12465/916 | $0.001377 | 13.98 |
| [agent-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](agent-r1/T09/README.md) | ok | 0.72 | 1 | no | not audited | 4 | 14715/1089 | $0.001667 | 12.69 |
| [agent-r1/T11: Executable Code Actions Elicit Better LLM Agents](agent-r1/T11/README.md) | ok | 0.72 | 1 | no | not audited | 4 | 20533/1011 | $0.001964 | 12.44 |
| [agent-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](agent-r1/T12/README.md) | ok | 0.72 | 0 | yes | not audited | 3 | 9507/525 | $0.001275 | 6.79 |
| [agent-r1/T19: A Survey on Large Language Model based Autonomous Agents](agent-r1/T19/README.md) | ok | 0.72 | 0 | yes | not audited | 3 | 10715/529 | $0.001435 | 9.89 |
| [agent-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](agent-r1/T03/README.md) | ok | 0.67 | 0 | yes | not audited | 3 | 7829/420 | $0.001035 | 8.73 |
| [agent-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](agent-r1/T20/README.md) | ok | 0.66 | 0 | yes | not audited | 3 | 9550/500 | $0.001229 | 6.47 |
| [agent-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](agent-r1/T02/README.md) | ok | 0.64 | 2 | no | not audited | 5 | 15218/1361 | $0.001617 | 18.24 |
| [agent-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](agent-r1/T18/README.md) | ok | 0.63 | 0 | yes | not audited | 3 | 7584/502 | $0.001017 | 7.30 |
| [agent-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](agent-r1/T16/README.md) | ok | 0.62 | 0 | yes | not audited | 3 | 8446/456 | $0.001116 | 7.26 |
| [agent-r1/T04: AgentBench: Evaluating LLMs as Agents](agent-r1/T04/README.md) | error | — | 3 | no | not audited | 5 | 17666/1170 | $0.001616 | 16.40 |
| [agent-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](agent-r1/T13/README.md) | error | — | 3 | no | not audited | 5 | 26686/1515 | $0.002403 | 16.37 |
| [agent-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](agent-r1/T15/README.md) | error | — | 3 | no | not audited | 5 | 20321/1193 | $0.001763 | 13.52 |
| [agent-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](agent-r1/T17/README.md) | error | — | 3 | no | not audited | 5 | 31841/1307 | $0.002585 | 15.21 |

## baseline

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [baseline-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](baseline-r1/T01/README.md) | ok | 0.79 | 0 | no | not audited | 1 | 30789/569 | $0.004133 | 7.09 |
| [baseline-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](baseline-r1/T07/README.md) | ok | 0.78 | 0 | yes | not audited | 1 | 38684/643 | $0.005157 | 6.34 |
| [baseline-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](baseline-r1/T13/README.md) | ok | 0.78 | 0 | no | not audited | 1 | 27075/459 | $0.003614 | 4.88 |
| [baseline-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](baseline-r1/T05/README.md) | ok | 0.74 | 0 | no | not audited | 1 | 16657/585 | $0.002375 | 6.04 |
| [baseline-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](baseline-r1/T06/README.md) | ok | 0.74 | 0 | no | not audited | 1 | 35056/551 | $0.004657 | 4.97 |
| [baseline-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](baseline-r1/T10/README.md) | ok | 0.73 | 0 | no | not audited | 1 | 23863/755 | $0.003360 | 7.07 |
| [baseline-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](baseline-r1/T14/README.md) | ok | 0.73 | 0 | yes | not audited | 1 | 24226/560 | $0.003308 | 5.33 |
| [baseline-r1/T04: AgentBench: Evaluating LLMs as Agents](baseline-r1/T04/README.md) | ok | 0.72 | 0 | yes | not audited | 1 | 36072/640 | $0.004829 | 6.00 |
| [baseline-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](baseline-r1/T08/README.md) | ok | 0.72 | 0 | no | not audited | 1 | 36934/619 | $0.004926 | 5.61 |
| [baseline-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](baseline-r1/T09/README.md) | ok | 0.72 | 0 | no | not audited | 1 | 16572/624 | $0.002383 | 5.86 |
| [baseline-r1/T11: Executable Code Actions Elicit Better LLM Agents](baseline-r1/T11/README.md) | ok | 0.72 | 0 | no | not audited | 1 | 30099/557 | $0.004041 | 4.67 |
| [baseline-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](baseline-r1/T12/README.md) | ok | 0.72 | 0 | no | not audited | 1 | 26994/503 | $0.003626 | 4.59 |
| [baseline-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](baseline-r1/T17/README.md) | ok | 0.69 | 0 | no | not audited | 1 | 18064/631 | $0.002573 | 5.52 |
| [baseline-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](baseline-r1/T20/README.md) | ok | 0.68 | 0 | no | not audited | 1 | 13497/665 | $0.002020 | 6.53 |
| [baseline-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](baseline-r1/T18/README.md) | ok | 0.67 | 0 | yes | not audited | 1 | 17424/535 | $0.002445 | 4.50 |
| [baseline-r1/T19: A Survey on Large Language Model based Autonomous Agents](baseline-r1/T19/README.md) | ok | 0.67 | 0 | yes | not audited | 1 | 33041/487 | $0.004374 | 4.53 |
| [baseline-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](baseline-r1/T03/README.md) | ok | 0.63 | 0 | no | not audited | 1 | 23878/592 | $0.003281 | 5.23 |
| [baseline-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](baseline-r1/T02/README.md) | ok | 0.62 | 0 | yes | not audited | 1 | 14416/669 | $0.002136 | 5.86 |
| [baseline-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](baseline-r1/T15/README.md) | ok | 0.59 | 0 | yes | not audited | 1 | 8838/441 | $0.001325 | 4.40 |
| [baseline-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](baseline-r1/T16/README.md) | ok | 0.57 | 0 | no | not audited | 1 | 23392/551 | $0.003199 | 5.05 |

## pyagent_react

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [pyagent_react-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](pyagent_react-r1/T13/README.md) | ok | 0.76 | 0 | yes | not audited | 4 | 17080/1166 | $0.002053 | 14.33 |
| [pyagent_react-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](pyagent_react-r1/T05/README.md) | ok | 0.75 | 1 | no | not audited | 4 | 16323/1688 | $0.002008 | 22.59 |
| [pyagent_react-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](pyagent_react-r1/T08/README.md) | ok | 0.72 | 0 | yes | not audited | 5 | 18270/1854 | $0.002385 | 25.50 |
| [pyagent_react-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](pyagent_react-r1/T09/README.md) | ok | 0.72 | 0 | yes | not audited | 4 | 17625/975 | $0.002092 | 12.55 |
| [pyagent_react-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](pyagent_react-r1/T10/README.md) | ok | 0.72 | 1 | no | not audited | 4 | 25619/1345 | $0.002572 | 16.01 |
| [pyagent_react-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](pyagent_react-r1/T12/README.md) | ok | 0.72 | 1 | no | not audited | 4 | 23119/1153 | $0.002256 | 16.19 |
| [pyagent_react-r1/T04: AgentBench: Evaluating LLMs as Agents](pyagent_react-r1/T04/README.md) | ok | 0.7 | 2 | no | not audited | 5 | 31940/1854 | $0.002683 | 23.72 |
| [pyagent_react-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](pyagent_react-r1/T07/README.md) | ok | 0.69 | 1 | no | not audited | 4 | 21638/1767 | $0.002437 | 21.90 |
| [pyagent_react-r1/T11: Executable Code Actions Elicit Better LLM Agents](pyagent_react-r1/T11/README.md) | ok | 0.68 | 0 | yes | not audited | 5 | 24435/884 | $0.002655 | 15.05 |
| [pyagent_react-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](pyagent_react-r1/T14/README.md) | ok | 0.68 | 0 | yes | not audited | 5 | 19913/1004 | $0.002137 | 14.90 |
| [pyagent_react-r1/T19: A Survey on Large Language Model based Autonomous Agents](pyagent_react-r1/T19/README.md) | ok | 0.68 | 0 | yes | not audited | 4 | 11426/662 | $0.001199 | 10.81 |
| [pyagent_react-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](pyagent_react-r1/T20/README.md) | ok | 0.68 | 1 | no | not audited | 4 | 25807/1233 | $0.002452 | 14.56 |
| [pyagent_react-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](pyagent_react-r1/T02/README.md) | ok | 0.67 | 0 | yes | not audited | 4 | 14194/754 | $0.001576 | 13.05 |
| [pyagent_react-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](pyagent_react-r1/T18/README.md) | ok | 0.65 | 0 | yes | not audited | 3 | 14887/700 | $0.001853 | 13.11 |
| [pyagent_react-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](pyagent_react-r1/T03/README.md) | ok | 0.63 | 0 | yes | not audited | 4 | 17136/751 | $0.001696 | 12.50 |
| [pyagent_react-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](pyagent_react-r1/T16/README.md) | ok | 0.55 | 0 | yes | not audited | 5 | 28199/1529 | $0.002484 | 22.23 |
| [pyagent_react-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](pyagent_react-r1/T01/README.md) | ok | 0.54 | 0 | yes | not audited | 2 | 4735/1539 | $0.001128 | 17.19 |
| [pyagent_react-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](pyagent_react-r1/T06/README.md) | error | — | 3 | no | not audited | 5 | 32350/2023 | $0.002834 | 25.39 |
| [pyagent_react-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](pyagent_react-r1/T15/README.md) | error | — | 1 | no | not audited | 5 | 14937/729 | $0.000891 | 10.42 |
| [pyagent_react-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](pyagent_react-r1/T17/README.md) | error | — | 1 | no | not audited | 5 | 18621/922 | $0.001195 | 14.30 |

Per-task cost/time includes unsuccessful attempts; audit cost is separate.
