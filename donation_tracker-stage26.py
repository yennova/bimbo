# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: DonationTracker
def demo_quick_test():
    """Быстрый набор демо-команд для ручного тестирования DonationTracker."""
    import datetime

    print("=" * 60)
    print("DEMO: Быстрое ручное тестирование DonationTracker")
    print("=" * 60)

    # --- Демо доноры ---
    donors = [
        {"id": "D1", "name": "Алексей Иванов", "email": "alex@example.com"},
        {"id": "D2", "name": "Мария Петрова", "email": "maria@example.com"},
        {"id": "D3", "name": "ООО 'Радость'", "email": "info@radost.ru"},
    ]
    print(f"\n[1] Демо-доноры ({len(donors)}):")
    for d in donors:
        print(f"  • {d['id']}: {d['name']} <{d['email']}>")

    # --- Демо цели ---
    goals = [
        {"id": "G1", "title": "Помощь детям сиротам", "target_amount": 50000, "currency": "RUB"},
        {"id": "G2", "title": "Кормить бездомных",   "target_amount": 10000, "currency": "RUB"},
        {"id": "G3", "title": "Медицина для всех",    "target_amount": 200000, "currency": "RUB"},
    ]
    print(f"\n[2] Демо-цели ({len(goals)}):")
    for g in goals:
        print(f"  • {g['id']}: '{g['title']}' — цель {g['target_amount']} {g['currency']}")

    # --- Демо пожертвования ---
    donations = [
        {"id": "DON1", "goal_id": "G1", "donor_id": "D1", "amount": 5000,   "date": datetime.date(2024, 3, 1),     "status": "done"},
        {"id": "DON2", "goal_id": "G1", "donor_id": "D2", "amount": 7500,   "date": datetime.date(2024, 3, 10),    "status": "done"},
        {"id": "DON3", "goal_id": "G1", "donor_id": "D3", "amount": 10000,  "date": datetime.date(2024, 4, 5),     "status": "pending"},
        {"id": "DON4", "goal_id": "G2", "donor_id": "D1", "amount": 3000,   "date": datetime.date(2024, 4, 15),    "status": "done"},
        {"id": "DON5", "goal_id": "G3", "donor_id": "D2", "amount": 15000,  "date": datetime.date(2024, 5, 1),     "status": "pending"},
    ]
    print(f"\n[3] Демо-пожертвования ({len(donations)}):")
    for d in donations:
        print(f"  • {d['id']}: {d['amount']} RUB → цель {d['goal_id']}, от донора {d['donor_id']}, статус={d['status']}")

    # --- Демо отчёт по цели ---
    def report_for_goal(g_id):
        goal = next(g for g in goals if g["id"] == g_id)
        goal_donations = [x for x in donations if x["goal_id"] == g_id]
        total = sum(x["amount"] for x in goal_donations)
        pct = (total / goal["target_amount"]) * 100
        print(f"\n[4] Отчёт по цели '{goal['title']}':")
        print(f"    Сумма собранных: {total} RUB из {goal['target_amount']} RUB ({pct:.1f}%)")
        return total, goal["target_amount"]

    report_for_goal("G1")
    report_for_goal("G2")
    report_for_goal("G3")

    # --- Демо сводка по донору ---
    def donor_summary(d_id):
        d = next(x for x in donors if x["id"] == d_id)
        d_donations = [x for x in donations if x["donor_id"] == d_id]
        total = sum(x["amount"] for x in d_donations)
        print(f"\n[5] Сводка донора '{d['name']}':")
        print(f"    Всего пожертвований: {len(d_donations)}, сумма: {total} RUB")

    donor_summary("D1")
    donor_summary("D2")

    # --- Демо экспорт JSON ---
    import json
    export_data = {"donors": donors, "goals": goals, "donations": donations}
    print(f"\n[6] Экспорт демо-данных (JSON):")
    print(json.dumps(export_data, ensure_ascii=False, indent=2)[:300])

    print("\n✓ Демо-тест завершен. Проверьте корректность работы модуля.")
