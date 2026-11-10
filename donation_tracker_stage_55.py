# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: DonationTracker
def find_duplicates(records, key_fields):
    """Находит дубликаты по списку ключевых полей и возвращает их индексы."""
    seen = {}
    duplicates = []
    for i, rec in enumerate(records):
        key = tuple(rec.get(f) for f in key_fields)
        if key in seen:
            duplicates.append((seen[key], i))
        else:
            seen[key] = i
    return duplicates


def add_duplicate_check(records, key_fields):
    """Добавляет мягкую проверку дубликатов: предупреждает перед созданием записи."""
    if not key_fields:
        key_fields = ["donor", "amount", "date"]
    duplicates = find_duplicates(records, key_fields)
    if duplicates:
        print("Обнаружены возможные дубликаты:")
        for i, j in duplicates:
            print(f"  Запись {i} и {j} могут совпадать по полям: {', '.join(key_fields)}")
        return False
    return True
