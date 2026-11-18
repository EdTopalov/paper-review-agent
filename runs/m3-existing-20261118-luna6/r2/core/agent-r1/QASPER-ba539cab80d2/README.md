# QASPER-ba539cab80d2

agent · repeat 1 · ok

3 API calls · 10016 input tokens · 387 output tokens · estimated USD 0.00048661000000000006

[Full trace](trace.jsonl). This output contains no reference labels.

```json
{
  "evidence": [
    {
      "document_id": "P1",
      "block_id": "b0017",
      "quote": "Pass-through: word-recognizer passes on the (possibly misspelled) word as is."
    },
    {
      "document_id": "P1",
      "block_id": "b0018",
      "quote": "Backoff to neutral word: Alternatively, noting that passing $\\colorbox {gray!20}{\\texttt {UNK}}$ -predicted words through unchanged exposes the downstream model to potentially corrupted text, we consider backing off to a neutral word like `a', which has a similar distribution across classes."
    },
    {
      "document_id": "P1",
      "block_id": "b0019",
      "quote": "Backoff to background model: We also consider falling back upon a more generic word recognition model trained upon a larger, less-specialized corpus whenever the foreground word recognition model predicts UNK."
    }
  ],
  "explanation": "The paper describes three fallback behaviors: pass a recognized word through unchanged; substitute a neutral word when the recognizer predicts UNK; or invoke a more generic background recognizer on UNK predictions.",
  "answer": "The strategies are: (1) pass the possibly misspelled input through unchanged; (2) replace a word predicted as UNK with a neutral word such as “a”; or (3) when the foreground recognizer predicts UNK, use a more generic recognizer trained on a larger, less-specialized corpus."
}
```
