# QASPER-ba539cab80d2

agent · repeat 1 · ok

3 API calls · 10202 input tokens · 474 output tokens · estimated USD 0.0005397900000000001

[Full trace](trace.jsonl). This output contains no reference labels.

```json
{
  "evidence": [
    {
      "document_id": "P1",
      "block_id": "b0018",
      "quote": "Backoff to neutral word: Alternatively, noting that passing $\\colorbox {gray!20}{\\texttt {UNK}}$ -predicted words through unchanged exposes the downstream model to potentially corrupted text, we consider backing off to a neutral word like `a', which has a similar distribution across classes."
    },
    {
      "document_id": "P1",
      "block_id": "b0019",
      "quote": "Backoff to background model: We also consider falling back upon a more generic word recognition model trained upon a larger, less-specialized corpus whenever the foreground word recognition model predicts UNK. Figure 1 depicts this scenario pictorially."
    },
    {
      "document_id": "P1",
      "block_id": "b0020",
      "quote": "Empirically, we find that the background model (by itself) is less accurate, because of the large number of words it is trained to predict. Thus, it is best to train a precise foreground model on an in-domain corpus and focus on frequent words, and then to resort to a general-purpose background model for rare and unobserved words."
    }
  ],
  "explanation": "The paper distinguishes two strategies for words the foreground recognizer predicts as UNK: substitute a neutral word instead of passing the possibly corrupted input through, or use a broader background recognizer. It recommends the latter as a fallback after an accurate in-domain foreground model.",
  "answer": "For an input predicted as UNK, one strategy replaces it with a neutral word such as “a” rather than passing potentially corrupted text downstream. Another backs off to a general-purpose word recognizer trained on a larger, less-specialized corpus. The paper suggests using an accurate in-domain foreground model for frequent words and the background model for rare or unseen words."
}
```
