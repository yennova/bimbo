# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: DonationTracker
import json, os

DATA_FILE = "donations.json"

def save_data(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"[Error] Не удалось сохранить данные в {DATA_FILE}: {e}")

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"donors": [], "goals": [], "transactions": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"[Warning] Ошибка чтения файла {DATA_FILE}: {e}. Загружено пустое состояние.")
        return {"donors": [], "goals": [], "transactions": []}

def get_data():
    data = load_data()
    # Синхронизация структуры данных при загрузке (защита от старых версий)
    if not all(k in data for k in ["donors", "goals", "transactions"]):
        missing_keys = [k for k in ["donors", "goals", "transactions"] if k not in data]
        print(f"[Warning] Отсутствуют ключи: {missing_keys}. Инициализация пустых списков.")
        for key in missing_keys:
            data[key] = []
    return data

def update_data(data):
    save_data(data)
