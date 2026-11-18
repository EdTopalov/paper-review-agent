# QASPER-ba539cab80d2

baseline · repeat 1 · ok

1 API calls · 8995 input tokens · 324 output tokens · estimated USD 0.0012863

[Full trace](trace.jsonl). This output contains no reference labels.

```json
{
  "evidence": [
    {
      "document_id": "P1",
      "block_id": "b0016",
      "quote": "Below, we explore different ways to back off when the ScRNN predicts UNK (a frequent outcome for rare and unseen words):"
    },
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
  "explanation": "The paper describes three strategies applied when the domain-specific ScRNN predicts UNK: pass through the input unchanged, substitute a neutral word, or query a more general recognizer trained on a larger corpus.",
  "answer": "When the ScRNN predicts UNK for a rare or unseen word, it can (1) pass the possibly misspelled word through unchanged, (2) replace it with a neutral word such as “a,” or (3) fall back to a generic background word recognizer trained on a larger, less-specialized corpus."
}
```
