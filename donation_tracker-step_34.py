# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: DonationTracker
TEMPLATE_REGISTRY = {}

def register_template(name, field_values):
    TEMPLATE_REGISTRY[name] = field_values

def get_template(name):
    return TEMPLATE_REGISTRY.get(name)

def apply_template(template_name, record_class, record_id, **kwargs):
    template = get_template(template_name)
    if template is None:
        raise ValueError(f"Template '{template_name}' not found")
    base = template.copy()
    base["id"] = record_id
    base.update(kwargs)
    return base
