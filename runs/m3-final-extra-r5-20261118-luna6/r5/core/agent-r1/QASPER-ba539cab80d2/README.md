# QASPER-ba539cab80d2

agent · repeat 1 · ok

4 API calls · 14032 input tokens · 472 output tokens · estimated USD 0.00059878

[Full trace](trace.jsonl). This output contains no reference labels.

```json
{
  "evidence": [
    {
      "document_id": "P1",
      "block_id": "b0018",
      "quote": "Alternatively, noting that passing $\\colorbox {gray!20}{\\texttt {UNK}}$ -predicted words through unchanged exposes the downstream model to potentially corrupted text, we consider backing off to a neutral word like `a', which has a similar distribution across classes."
    },
    {
      "document_id": "P1",
      "block_id": "b0019",
      "quote": "We also consider falling back upon a more generic word recognition model trained upon a larger, less-specialized corpus whenever the foreground word recognition model predicts UNK."
    },
    {
      "document_id": "P1",
      "block_id": "b0020",
      "quote": "Thus, it is best to train a precise foreground model on an in-domain corpus and focus on frequent words, and then to resort to a general-purpose background model for rare and unobserved words."
    }
  ],
  "explanation": "When the specialized recognizer predicts UNK, strategies avoid passing potentially corrupted text through unchanged: substitute a neutral word such as “a,” or use a generic background recognizer trained on a larger, less-specialized corpus. The paper favors combining a precise in-domain foreground model for frequent words with a background model for rare or unseen ones.",
  "answer": "When the foreground recognizer predicts UNK, one strategy replaces the word with a neutral word such as “a” rather than passing possibly corrupted text through. Another falls back to a general-purpose background word recognizer trained on a larger, less-specialized corpus. The paper recommends using the in-domain foreground model for frequent words and the background model for rare or unseen words."
}
```
