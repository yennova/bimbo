# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: DonationTracker
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "donors": list(donors.values()),
        "goals": list(goals.values()),
        "transactions": transactions,
        "exported_at": datetime.utcnow().isoformat() + "Z"
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
