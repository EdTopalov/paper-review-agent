# QASPER-ba539cab80d2

baseline · repeat 1 · ok

1 API calls · 8995 input tokens · 263 output tokens · estimated USD 0.00022172

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
      "quote": "Backoff to neutral word: Alternatively, noting that passing UNK-predicted words through unchanged exposes the downstream model to potentially corrupted text, we consider backing off to a neutral word like `a', which has a similar distribution across classes."
    },
    {
      "document_id": "P1",
      "block_id": "b0019",
      "quote": "Backoff to background model: We also consider falling back upon a more generic word recognition model trained upon a larger, less-specialized corpus whenever the foreground word recognition model predicts UNK."
    }
  ],
  "explanation": "The paper describes three strategies used when the foreground recognizer predicts UNK: pass through the original word, substitute a neutral word, or use a recognizer trained on a larger, more general corpus.",
  "answer": "When the foreground recognizer predicts UNK, pass-through leaves the input word unchanged; neutral backoff substitutes a fixed neutral word (such as “a”); background-model backoff sends it to a more general recognizer trained on a larger corpus."
}
```
