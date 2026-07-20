# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: DonationTracker
def print_donations_table(donations):
    if not donations:
        print("Нет пожертвований.")
        return
    headers = ["ID", "Донор", "Сумма (₽)", "Дата"]
    widths = [len(h) for h in headers]
    for d in donations:
        row = [str(d.id), d.donor, f"{d.amount} ₽", str(d.date)]
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))
    print("─" * sum(widths + [2]))
    print("  |".join(headers).center(sum(widths) + 3 * len(headers)))
    print("─" * sum(widths + [2]))
    for i, d in enumerate(donations):
        row = [str(d.id), d.donor, f"{d.amount} ₽", str(d.date)]
        print("  |".join(cell.ljust(widths[i]) for i, cell in enumerate(row)))
