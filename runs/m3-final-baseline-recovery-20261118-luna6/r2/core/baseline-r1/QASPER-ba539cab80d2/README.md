# QASPER-ba539cab80d2

baseline · repeat 1 · ok

1 API calls · 8995 input tokens · 343 output tokens · estimated USD 0.00026172

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
    },
    {
      "document_id": "P1",
      "block_id": "b0020",
      "quote": "Thus, it is best to train a precise foreground model on an in-domain corpus and focus on frequent words, and then to resort to a general-purpose background model for rare and unobserved words."
    }
  ],
  "explanation": "The paper describes three strategies for when the foreground recognizer predicts UNK, plus the pass-through option.",
  "answer": "When the recognizer predicts UNK, pass-through returns the possibly misspelled input unchanged; neutral backoff substitutes a fixed neutral word (such as “a”); and background-model backoff sends the word to a generic recognizer trained on a larger, less-specialized corpus. The paper favors a precise in-domain foreground model for frequent words and the background model for rare or unseen words."
}
```
