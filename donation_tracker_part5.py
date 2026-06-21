# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: DonationTracker
def delete_donation(donation_id):
    donations = get_all_donations()
    if not donations:
        print("Ошибка: список пожертвований пуст.")
        return False
    for i, d in enumerate(donations):
        if d['id'] == donation_id:
            del donations[i]
            save_donations_to_file(donations)
            print(f"Пожертвание #{donation_id} успешно удалено.")
            return True
    print("Ошибка: пожертвование с указанным ID не найдено.")
    return False

def delete_goal(goal_id):
    goals = get_all_goals()
    if not goals:
        print("Ошибка: список целей пуст.")
        return False
    for i, g in enumerate(goals):
        if g['id'] == goal_id:
            del goals[i]
            save_goals_to_file(goals)
            print(f"Цель #{goal_id} успешно удалена.")
            return True
    print("Ошибка: цель с указанным ID не найдена.")
    return False

def delete_donor(donor_id):
    donors = get_all_donors()
    if not donors:
        print("Ошибка: список доноров пуст.")
        return False
    for i, d in enumerate(donors):
        if d['id'] == donor_id:
            del donors[i]
            save_donors_to_file(donors)
            # Удаляем связанные пожертвования и цели (опционально или с предупреждением)
            donations = get_all_donations()
            filtered_dons = [d for d in donations if str(d['donor_id']) != donor_id]
            save_donations_to_file(filtered_dons)
            goals = get_all_goals()
            filtered_goals = [g for g in goals if str(g['donor_id']) != donor_id]
            save_goals_to_file(filtered_goals)
            print(f"Донор #{donor_id} успешно удален, связанные записи очищены.")
            return True
    print("Ошибка: донор с указанным ID не найден.")
    return False
