# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: DonationTracker
def summary_report():
    donors = get_donors()
    goals = get_goals()
    donations = get_donations()
    
    total_raised = sum(d['amount'] for d in donations)
    avg_amount = total_raised / len(donations) if donations else 0
    
    active_goal_count = sum(1 for g in goals if g.get('active', True))
    goal_total_target = sum(g['target'] for g in goals)
    
    top_donor_name = donors[0]['name'] if donors else 'Нет доноров'
    top_donation_amount = donations[0]['amount'] if donations else 0
    
    print(f"=== Сводка по пожертвованиям ===")
    print(f"Всего доноров: {len(donors)}")
    print(f"Активных целей: {active_goal_count}")
    print(f"Сумма собрано: {total_raised:.2f}")
    print(f"Средняя сумма пожертвования: {avg_amount:.2f}")
    print(f"Лучший донор: {top_donor_name} ({donations[0]['amount'] if donations else 0:.2f})")
