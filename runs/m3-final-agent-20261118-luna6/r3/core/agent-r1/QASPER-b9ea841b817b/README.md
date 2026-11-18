# QASPER-b9ea841b817b

agent · repeat 1 · ok

6 API calls · 19230 input tokens · 396 output tokens · estimated USD 0.001139715

[Full trace](trace.jsonl). This output contains no reference labels.

```json
{
  "evidence": [
    {
      "document_id": "P1",
      "block_id": "b0034",
      "quote": "For Back Translation, we use Vietnamese monolingual data from VNESEcorpus of DongDu which includes 349578 sentences."
    },
    {
      "document_id": "P1",
      "block_id": "b0034",
      "quote": "For Mix-Source, instead of using a subsampled monolingual corpus, we use the Vietnamese part of the Japanese-Vietnamese parallel corpus"
    }
  ],
  "explanation": "The methods describe reusing an existing Vietnamese corpus and the Vietnamese portion of a parallel corpus, plus synthetic data augmentation. They do not state that the authors collected their own data.",
  "answer": "No. They used existing corpora and generated synthetic training data; the paper does not report collecting their own data."
}
```
