# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: DonationTracker
import json, sys

def load_initial_data(json_string):
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        donors = data.get('donors', [])
        goals = data.get('goals', [])
        donations = data.get('donations', [])
        
        for d in donors:
            if 'id' not in d or 'name' not in d:
                raise ValueError("Некорректный донор")
            
        for g in goals:
            if 'id' not in g or 'title' not in g:
                raise ValueError("Некорректная цель")
                
        for don in donations:
            if 'donor_id' not in don or 'goal_id' not in don:
                raise ValueError("Некорректное пожертвование")

        return {
            'donors': donors,
            'goals': goals,
            'donations': donations
        }
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}", file=sys.stderr)
        sys.exit(1)
