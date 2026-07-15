# === Stage 20: Добавь восстановление записей из архива ===
# Project: DonationTracker
import json, os


def load_from_archive():
    """Восстанавливает записи из архива при старте приложения."""
    archive_path = "donation_tracker/archive.json"
    if not os.path.exists(archive_path):
        return
    try:
        with open(archive_path, encoding="utf-8") as f:
            data = json.load(f)
        for key in ["donors", "goals", "contributions"]:
            if key in data and isinstance(data[key], list):
                globals()[key] += data[key]
            elif key == "settings" and isinstance(data.get("settings"), dict):
                settings.update(data["settings"])
    except Exception:
        pass


load_from_archive()
