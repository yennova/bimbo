# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: DonationTracker
def main():
    while True:
        print("\n=== DonationTracker ===")
        print("1. Добавить донора")
        print("2. Добавить цель")
        print("3. Записать пожертвование")
        print("4. Показать отчёт по цели")
        print("5. Вывести сводную статистику")
        print("6. Сохранить и выйти")
        choice = input("Выберите действие (1-6): ").strip()

        if choice == "1":
            name = input("Имя донора: ")
            email = input("Email: ")
            donations.tracker.add_donor(name, email)
            print(f"Донор '{name}' добавлен.")
        elif choice == "2":
            goal_name = input("Название цели: ")
            target_amount = float(input("Целевая сумма: "))
            current_amount = float(input("Текущая сумма: "))
            donations.tracker.add_goal(goal_name, target_amount, current_amount)
            print(f"Цель '{goal_name}' добавлена.")
        elif choice == "3":
            donor_name = input("Имя донора: ")
            goal_name = input("Название цели: ")
            amount = float(input("Сумма пожертвования: "))
            date_str = input("Дата (YYYY-MM-DD): ") or None
            donations.tracker.record_donation(donor_name, goal_name, amount, date_str)
            print(f"Пожертвование от '{donor_name}' на цель '{goal_name}' записано.")
        elif choice == "4":
            goal_name = input("Название цели: ")
            donations.tracker.report_goal(goal_name)
        elif choice == "5":
            donations.tracker.show_summary()
        elif choice == "6":
            print("Данные сохранены. До свидания!")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
