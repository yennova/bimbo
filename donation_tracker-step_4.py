# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: DonationTracker
def edit_record(record_id, updates):
    if record_id not in donations:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
        return False
    
    for key, value in updates.items():
        if key in ['id', 'created_at']:
            continue
        donations[record_id][key] = value
    
    print(f"Запись #{record_id} успешно обновлена.")
    return True

def delete_record(record_id):
    if record_id not in donations:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
        return False
    del donations[record_id]
    print(f"Запись #{record_id} удалена.")
    return True
