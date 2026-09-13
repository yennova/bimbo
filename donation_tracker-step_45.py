# === Stage 45: Добавь восстановление из резервной копии ===
# Project: DonationTracker
def load_from_backup():
    """Восстанавливает данные из JSON-резервной копии."""
    import json
    backup_file = "donation_backup.json"
    try:
        with open(backup_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        donors = data.get('donors', [])
        goals = data.get('goals', [])
        donations = data.get('donations', [])
        reports = data.get('reports', [])
        print("Резервная копия успешно загружена.")
        return True
    except FileNotFoundError:
        print("Резервная копия не найдена.")
        return False
    except json.JSONDecodeError:
        print("Ошибка: некорректный формат резервной копии.")
        return False
