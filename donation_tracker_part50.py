# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: DonationTracker
def print_report():
    """Выводит краткий отчёт по пожертвованиям."""
    if not donations:
        print("Пока нет записей о пожертвованиях.")
        return
    total = sum(d['amount'] for d in donations)
    print(f"Всего пожертваний: {len(donations)}")
    print(f"Общая сумма: {total:.2f}")
    print(f"Среднее: {total / len(donations):.2f}")
