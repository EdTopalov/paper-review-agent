# Evidence-assessment benchmark experiment

Model: `gpt-6-luna`. Split: `test`. 64 tasks per variant and 1 repetitions.

[Frozen plan](plan.json) · [Evaluated source](source.zip) · [Per-track quality scores](scores.json) · [Attempt records](records.jsonl)

Completion is a returned prediction, not a correctness score. Quality is reported separately for each track; evidence matching does not establish that the explanation is sound. Costs include failed attempts and retries.

| Variant | Completed / attempts | Calls / attempt | Input/output tokens / attempt | USD / attempt | Seconds / attempt |
|---|---:|---:|---:|---:|---:|
| baseline | 64/64 | 1.00 | 6720.7/197.3 | 0.000183 | 3.57 |

## Content by track

Repeat values show run variation before pooling. Failures remain in every denominator. The JSON report includes evidence F1, category slices, group intervals, and per-attempt costs.

| Track | Variant | Primary measure | Each repeat | Pooled |
|---|---|---|---|---:|
| controlled | baseline | Verdict accuracy | r1: 1.000 | 1.000 |
| qasper | baseline | Answer F1 | r1: 0.447 | 0.447 |
| reviewcritique | baseline | Binary macro-F1 | r1: 0.627 | 0.627 |

## Attempts

- [baseline-r1/CB-12d6c0559e77](baseline-r1/CB-12d6c0559e77/README.md): ok
- [baseline-r1/CB-20fe26ed8a63](baseline-r1/CB-20fe26ed8a63/README.md): ok
- [baseline-r1/CB-25cf58af89f2](baseline-r1/CB-25cf58af89f2/README.md): ok
- [baseline-r1/CB-40388578e13d](baseline-r1/CB-40388578e13d/README.md): ok
- [baseline-r1/CB-449d322624b5](baseline-r1/CB-449d322624b5/README.md): ok
- [baseline-r1/CB-527f16549e56](baseline-r1/CB-527f16549e56/README.md): ok
- [baseline-r1/CB-54f05a314634](baseline-r1/CB-54f05a314634/README.md): ok
- [baseline-r1/CB-5501cd8dd300](baseline-r1/CB-5501cd8dd300/README.md): ok
- [baseline-r1/CB-6d1256f826e3](baseline-r1/CB-6d1256f826e3/README.md): ok
- [baseline-r1/CB-72101445106e](baseline-r1/CB-72101445106e/README.md): ok
- [baseline-r1/CB-74e44d72cfb9](baseline-r1/CB-74e44d72cfb9/README.md): ok
- [baseline-r1/CB-7ad89dbcdedc](baseline-r1/CB-7ad89dbcdedc/README.md): ok
- [baseline-r1/CB-80bd654cbc97](baseline-r1/CB-80bd654cbc97/README.md): ok
- [baseline-r1/CB-8fe165c89164](baseline-r1/CB-8fe165c89164/README.md): ok
- [baseline-r1/CB-9445ca674aeb](baseline-r1/CB-9445ca674aeb/README.md): ok
- [baseline-r1/CB-b36c4ba21009](baseline-r1/CB-b36c4ba21009/README.md): ok
- [baseline-r1/CB-bc5465d35ac1](baseline-r1/CB-bc5465d35ac1/README.md): ok
- [baseline-r1/CB-bd50b5c34b5a](baseline-r1/CB-bd50b5c34b5a/README.md): ok
- [baseline-r1/CB-c1f1e166dec3](baseline-r1/CB-c1f1e166dec3/README.md): ok
- [baseline-r1/CB-cedf9028d20e](baseline-r1/CB-cedf9028d20e/README.md): ok
- [baseline-r1/CB-d08f00314b8d](baseline-r1/CB-d08f00314b8d/README.md): ok
- [baseline-r1/CB-d2c80b428f6e](baseline-r1/CB-d2c80b428f6e/README.md): ok
- [baseline-r1/CB-e758c8885528](baseline-r1/CB-e758c8885528/README.md): ok
- [baseline-r1/CB-fba8e76583d6](baseline-r1/CB-fba8e76583d6/README.md): ok
- [baseline-r1/QASPER-01209a3bead7](baseline-r1/QASPER-01209a3bead7/README.md): ok
- [baseline-r1/QASPER-0c234db3b380](baseline-r1/QASPER-0c234db3b380/README.md): ok
- [baseline-r1/QASPER-220d11a03897](baseline-r1/QASPER-220d11a03897/README.md): ok
- [baseline-r1/QASPER-25c1c4a91f5d](baseline-r1/QASPER-25c1c4a91f5d/README.md): ok
- [baseline-r1/QASPER-2e37e681942e](baseline-r1/QASPER-2e37e681942e/README.md): ok
- [baseline-r1/QASPER-4e748cb2b5e7](baseline-r1/QASPER-4e748cb2b5e7/README.md): ok
- [baseline-r1/QASPER-6c96e910bd98](baseline-r1/QASPER-6c96e910bd98/README.md): ok
- [baseline-r1/QASPER-7bd6a6ec230e](baseline-r1/QASPER-7bd6a6ec230e/README.md): ok
- [baseline-r1/QASPER-893ec40b678a](baseline-r1/QASPER-893ec40b678a/README.md): ok
- [baseline-r1/QASPER-8db6f8714bda](baseline-r1/QASPER-8db6f8714bda/README.md): ok
- [baseline-r1/QASPER-8dc707a0daf7](baseline-r1/QASPER-8dc707a0daf7/README.md): ok
- [baseline-r1/QASPER-8eefa116e3c3](baseline-r1/QASPER-8eefa116e3c3/README.md): ok
- [baseline-r1/QASPER-ababb79dd3c3](baseline-r1/QASPER-ababb79dd3c3/README.md): ok
- [baseline-r1/QASPER-b21bc0919369](baseline-r1/QASPER-b21bc0919369/README.md): ok
- [baseline-r1/QASPER-b591853e9389](baseline-r1/QASPER-b591853e9389/README.md): ok
- [baseline-r1/QASPER-b970f48d3077](baseline-r1/QASPER-b970f48d3077/README.md): ok
- [baseline-r1/QASPER-b9ea841b817b](baseline-r1/QASPER-b9ea841b817b/README.md): ok
- [baseline-r1/QASPER-ba539cab80d2](baseline-r1/QASPER-ba539cab80d2/README.md): ok
- [baseline-r1/QASPER-c59802881506](baseline-r1/QASPER-c59802881506/README.md): ok
- [baseline-r1/QASPER-dfca00be3284](baseline-r1/QASPER-dfca00be3284/README.md): ok
- [baseline-r1/RC-16a23f11844e](baseline-r1/RC-16a23f11844e/README.md): ok
- [baseline-r1/RC-17ae89b7e529](baseline-r1/RC-17ae89b7e529/README.md): ok
- [baseline-r1/RC-196c24d86b88](baseline-r1/RC-196c24d86b88/README.md): ok
- [baseline-r1/RC-19e4af168032](baseline-r1/RC-19e4af168032/README.md): ok
- [baseline-r1/RC-1d03f02eb4d7](baseline-r1/RC-1d03f02eb4d7/README.md): ok
- [baseline-r1/RC-2518e6de7eb6](baseline-r1/RC-2518e6de7eb6/README.md): ok
- [baseline-r1/RC-357185295521](baseline-r1/RC-357185295521/README.md): ok
- [baseline-r1/RC-39282147886f](baseline-r1/RC-39282147886f/README.md): ok
- [baseline-r1/RC-59408ce4ca25](baseline-r1/RC-59408ce4ca25/README.md): ok
- [baseline-r1/RC-599e8dc3a69c](baseline-r1/RC-599e8dc3a69c/README.md): ok
- [baseline-r1/RC-81274ac167fc](baseline-r1/RC-81274ac167fc/README.md): ok
- [baseline-r1/RC-88f98dcc0dee](baseline-r1/RC-88f98dcc0dee/README.md): ok
- [baseline-r1/RC-97b4064e1659](baseline-r1/RC-97b4064e1659/README.md): ok
- [baseline-r1/RC-9813f9c2cf5d](baseline-r1/RC-9813f9c2cf5d/README.md): ok
- [baseline-r1/RC-ae631d292d42](baseline-r1/RC-ae631d292d42/README.md): ok
- [baseline-r1/RC-cc398745c3c8](baseline-r1/RC-cc398745c3c8/README.md): ok
- [baseline-r1/RC-d574e4d2099d](baseline-r1/RC-d574e4d2099d/README.md): ok
- [baseline-r1/RC-f0e2b1a1f91a](baseline-r1/RC-f0e2b1a1f91a/README.md): ok
- [baseline-r1/RC-f5097b168055](baseline-r1/RC-f5097b168055/README.md): ok
- [baseline-r1/RC-f94db276afa4](baseline-r1/RC-f94db276afa4/README.md): ok
