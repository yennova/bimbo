# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: DonationTracker
SELECTED = set()

def toggle_selected(index, records):
    if index in SELECTED:
        SELECTED.discard(index)
    else:
        SELECTED.add(index)

def mark_all_selected(records):
    if SELECTED:
        SELECTED.clear()
    SELECTED.update(range(len(records)))

def clear_selected():
    SELECTED.clear()

def is_selected(index):
    return index in SELECTED

def get_selected_records(records):
    return [records[i] for i in SELECTED if i < len(records)]

def show_selected_summary(records):
    selected = get_selected_records(records)
    if not selected:
        print("Нет избранных записей")
        return
    total = sum(r["amount"] for r in selected)
    print(f"Выбрано: {len(selected)} записей")
    for r in selected:
        print(f"  {r['donor']} — {r['amount']} ₽ ({r['date']})")
    print(f"Итого: {total} ₽")
    print("1) Удалить избранные  2) Снять выделение")
    choice = input("Выбор: ").strip()
    if choice == "1":
        for i in list(SELECTED):
            records.pop(i)
        SELECTED.clear()
        print("Избранные удалены")
    elif choice == "2":
        SELECTED.clear()
        print("Выделение снято")
    else:
        print("Отмена")
