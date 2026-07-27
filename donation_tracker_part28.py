# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: DonationTracker
def report_metrics():
    total_donations = sum(d["amount"] for d in donations)
    unique_donors = len(set(d["donor_id"] for d in donations))
    goals_met = [g["name"] for g in goals if any(
        d["amount"] >= g["target_amount"] and d["goal_id"] == g["id"] for d in donations
    )]
    print(f"📊 Метрики проекта DonationTracker:")
    print(f"   💰 Всего пожертвований: {total_donations} руб.")
    print(f"   👥 Уникальных доноров: {unique_donors}")
    if goals_met:
        print(f"   🎯 Достиженные цели ({len(goals_met)}):")
        for name in goals_met:
            print(f"      • {name}")
    else:
        print("   📈 Ни одна цель ещё не достигнута.")
