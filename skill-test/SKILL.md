---
name: "dataset-publishing"
description: "Publish datasets to Hugging Face Hub. Use when uploading datasets, creating dataset cards, or managing dataset versions."
license: "Apache-2.0"
compatibility: "Tested with Python 3.8+ and huggingface_hub 0.16+"
metadata:
  author: "ml-team"
  version: "1.0.0"
allowed-tools: "Bash(hf:*) Python(huggingface_hub:*)"
---


Every SKILL.md starts with YAML frontmatter that describes the skill. Here’s the complete specification:

example:

---
name: "model-card-generator"
description: "Generate model cards for Hugging Face Hub. Use when documenting models, adding metadata, or creating README files."
license: "MIT"
compatibility: "Python 3.8+, requires jinja2"
metadata:
  author: "context-course"
  version: "1.0.0"
  created: "2026-04-13"
---

# Model Card Generator Skill

## Overview
This skill helps create professional model cards and README files for models published to Hugging Face Hub. Model cards document:
- Model architecture and training data
- Intended use and limitations
- Performance metrics
- Ethical considerations
- License information

## Prerequisites Checklist
- [ ] Python 3.8+ installed
- [ ] jinja2 package installed
- [ ] Model information available (name, description, metrics)

## Step-by-Step Guide

### 1. Gather Model Information
Collect the following about your model:
- Model name and description
- Training data description
- Performance metrics (accuracy, F1, BLEU, etc.)
- Intended use cases
- Limitations
- License (MIT, Apache-2.0, CC-BY-4.0, etc.)

### 2. Generate Card
```python
from generate_card import create_model_card

metrics = {
    "accuracy": 0.92,
    "f1_score": 0.89,
    "precision": 0.91
}

card = create_model_card(
    model_name="My Classifier",
    description="A transformer-based text classifier",
    metrics=metrics
)

with open("README.md", "w") as f:
    f.write(card)
```

See [the generation script](scripts/generate_card.py) for more options.

### 3. Customize
Open README.md and add:
- Detailed description
- Training procedure
- Example usage
- Citation information

## Helper Scripts
- [Model card generator](scripts/generate_card.py)
- [Validation tool](scripts/validate_card.py)

## References
- [Model Cards Paper](https://arxiv.org/abs/1810.03993)
- [HF Model Card Template](../references/hf-template)
- [Best Practices](../references/best-practices)

## Troubleshooting

### Issue: Frontmatter not rendering
**Solution**: Ensure dashes are on their own lines in the YAML section:
```yaml
---
license: mit
---
```

### Issue: Characters not displaying
**Solution**: Save file as UTF-8 encoding:
```bash
file README.md
```