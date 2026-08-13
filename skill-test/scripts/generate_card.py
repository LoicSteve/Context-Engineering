from datetime import datetime
from jinja2 import Template

TEMPLATE = """---
license: {{ license }}
---

# {{ name }}

{{ description }}

## Performance

| Metric | Value |
|--------|-------|
{% for metric, value in metrics.items() %}
| {{ metric }} | {{ "%.4f" | format(value) }} |
{% endfor %}

## Model Details
- Created: {{ created_date }}
- Framework: PyTorch

## Uses
This model is suitable for {{ use_cases }}.

## Limitations
- Trained on specific domain data
- May not generalize to other domains
"""

def create_model_card(model_name, description, metrics, license="mit", use_cases="classification"):
    """Generate a model card."""
    template = Template(TEMPLATE)
    return template.render(
        name=model_name,
        description=description,
        metrics=metrics,
        license=license,
        use_cases=use_cases,
        created_date=datetime.now().isoformat()
    )