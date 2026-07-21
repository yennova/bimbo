# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: DonationTracker
def show_donation(d):
    print(f"ID: {d.id} | Донор: {d.donor_name}")
    print(f"Сумма: {d.amount:.2f} | Цель: {d.goal_name}")
    print(f"Дата: {d.date.strftime('%Y-%m-%d') if d.date else 'Не указана'}")
    return d

def show_goal(g):
    print(f"ID: {g.id} | Наименование: {g.name}")
    print(f"Цель: {g.description}")
    print(f"Сумма: {g.target_amount:.2f} | Собрано: {g.collected_sum:.2f}")
    return g

def show_report(r):
    print(f"ID: {r.id} | Название: {r.title}")
    print(f"Период: {r.start_date.strftime('%Y-%m-%d') if r.start_date else 'Н/Д'} — {r.end_date.strftime('%Y-%m-%d') if r.end_date else 'Н/Д'}")
    print(f"Статус: {r.status}")
    return r
