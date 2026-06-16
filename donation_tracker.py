# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: DonationTracker
import json, datetime, uuid
from dataclasses import asdict, field
from typing import List, Optional, Dict, Any

class Donation:
    def __init__(self, donor_name: str, goal_name: str, amount: float, date: datetime.date):
        self.id = str(uuid.uuid4())[:8]
        self.donor_name = donor_name
        self.goal_name = goal_name
        self.amount = round(amount, 2)
        self.date = date

class Goal:
    def __init__(self, name: str, target_amount: float):
        self.id = str(uuid.uuid4())[:8]
        self.name = name
        self.target_amount = target_amount
        self.current_amount = 0.0

def load_demo_data() -> Dict[str, Any]:
    goals = [Goal("Обучение", 1000), Goal("Помощь детям", 500)]
    donations = []
    today = datetime.date.today()
    for i in range(3):
        d = Donation("Иванов И.И.", "Обучение", round(200 + i * 10, 2), today - datetime.timedelta(days=i))
        donations.append(d)
    return {"goals": goals, "donations": donations}

def save_to_file(data: Dict[str, Any], filename: str = "data.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump({k: [asdict(v) for v in items] if isinstance(items, list) else items for k, items in data.items()}, f, ensure_ascii=False, indent=2)

def main():
    demo = load_demo_data()
    save_to_file(demo)
    print(f"Демо-данные сохранены в {len(demo['goals'])} целях и {len(demo['donations'])} пожертвованиях.")
