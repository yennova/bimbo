# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: DonationTracker
class Reminder:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date

    def is_overdue(self):
        return datetime.now().date() > self.due_date.date()


def print_reminders(reminders):
    overdue = [r for r in reminders if r.is_overdue()]
    not_overdue = [r for r in reminders if not r.is_overdue()]
    if overdue:
        print("⚠️  Просроченные напоминания:")
        for r in overdue:
            print(f"   - {r.title} (срок: {r.due_date})")
        print()
    if not_overdue:
        today = datetime.now().date()
        upcoming = [r for r in not_overdue if abs((r.due_date - today).days) <= 7]
        other = [r for r in not_overdue if (r.due_date - today).days > 7]
        if upcoming:
            print("📅 В ближайшие 7 дней:")
            for r in upcoming:
                days_left = (r.due_date - today).days
                print(f"   - {r.title} ({days_left} дн.)")
            print()
        if other:
            print("✅ Другие напоминания:")
            for r in other:
                days_left = (r.due_date - today).days
                print(f"   - {r.title} ({days_left} дн.)")

# Пример использования в конце файла:
# reminders = [Reminder("Сдать отчёт", datetime(2024, 12, 31)), Reminder("Помыть машину", datetime(2025, 6, 1))]
# print_reminders(reminders)
