---
license: mit
task_categories:
  - text-classification
language:
  - en
size_categories:
  - n<1K
---

# Sample Sentiment Dataset

## Dataset Description

A minimal text-classification example dataset with binary sentiment labels, used to test the `hf-dataset-validation` skill.

## Dataset Structure

| Column  | Type   | Description                                  |
|---------|--------|-----------------------------------------------|
| `text`  | string | Input text sample                             |
| `label` | int    | Sentiment label: `0` = negative, `1` = positive |
| `split` | string | Data split: `train` or `test`                 |

## Size

3 rows total (2 train, 1 test).

**This is a placeholder/test fixture, not a production-ready dataset.** It exists to exercise the validation tooling and is far too small for actual model training. Before using it for real training or publishing it as a dataset in its own right, expand it to a representative size and re-run validation.

## License

MIT — see `LICENSE`.
