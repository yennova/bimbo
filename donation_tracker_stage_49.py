# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: DonationTracker
def self_check():
    """Финальная самопроверка DonationTracker."""
    from collections import defaultdict
    donations = load_donations()
    donors = load_donors()
    goals = load_goals()
    if not donations:
        print("⚠ Нет данных — запустите ввод (etap_48_input).")
        return
    donor_sums = defaultdict(float)
    for d in donations:
        donor_sums[d.donor] += d.amount
    for donor, total in donor_sums.items():
        if donor in donors:
            print(f"✅ Донор {donor}: {total:.2f}")
        else:
            print(f"❌ Неизвестный донор: {donor}")
    for goal in goals:
        progress = sum(d.amount for d in donations if d.goal == goal.id)
        print(f"🎯 Цель {goal.id}: {progress:.2f} / {goal.target:.2f} ({progress/goal.target*100:.1f}%)")
