# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: DonationTracker
def load_from_json(filepath):
    try:
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            for item in data:
                add_donation(item.get('donor_name'), item.get('goal_name'), item.get('amount'), item.get('date'))
        elif isinstance(data, dict):
            for key, value in data.items():
                if callable(value) and hasattr(value, '__call__'):
                    continue
                try:
                    add_donation(key, str(value).split(':')[0], float(str(value).split(':')[1].replace(',', '.')) if ':' in str(value) else 0.0, '')
                except (ValueError, TypeError):
                    pass
        print(f"Загружено данных из {filepath}")
    except FileNotFoundError:
        print(f"Файл не найден: {filepath}")
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке: {type(e).__name__}: {e}")
