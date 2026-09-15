# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: DonationTracker
def demo():
    print("=" * 50)
    print("  DonationTracker — демо сценарий")
    print("=" * 50)
    
    # 1. Создание доноров
    d1 = donor("Анна", 30)
    d2 = donor("Борис", 25)
    d3 = donor("Виктория", 35)
    print(f"Доноры: {d1.name}, {d2.name}, {d3.name}")
    
    # 2. Создание целей
    goal1 = goal("Обновить серверы", 10000)
    goal2 = goal("Покупка оборудования", 5000)
    print(f"Цели: '{goal1.name}' ({goal1.target}) и '{goal2.name}' ({goal2.target})")
    
    # 3. Регистрация пожертвований
    donations = [
        donation(d1, 500, "2024-01-15"),
        donation(d2, 300, "2024-01-16"),
        donation(d3, 700, "2024-01-17"),
        donation(d1, 400, "2024-01-18"),
    ]
    print(f"Записано пожертвований: {len(donations)}")
    
    # 4. Отчёт по донору
    print(f"\n--- Отчёт по {d1.name} ---")
    d1.show_donations_summary(donations)
    
    # 5. Отчёт по цели
    print(f"\n--- Отчёт по цели '{goal1.name}' ---")
    goal1.show_progress_summary(donations)
    
    # 6. Итоговый отчёт
    print("\n" + "=" * 50)
    print("  ИТОГО: пожертвовано $", sum(d.amount for d in donations))
    print("  Доноров: ", len(donors))
    print("  Целей: ", len(goals))
    print("=" * 50)
