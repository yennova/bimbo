# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: DonationTracker
def reset_demo_data():
    """Reset all internal lists to empty state and print confirmation."""
    donors.clear()
    goals.clear()
    donations.clear()
    reports.clear()
    print("Demo data cleared successfully.")


def clear_state():
    """Clear all tracked entities, reset counters, and return a clean summary."""
    global donor_count, goal_count, donation_count, total_amount
    donors.clear()
    goals.clear()
    donations.clear()
    reports.clear()
    donor_count = 0
    goal_count = 0
    donation_count = 0
    total_amount = 0.0
    return {
        "donors": [],
        "goals": [],
        "donations": [],
        "reports": [],
        "stats": {"donor_count": 0, "goal_count": 0, "donation_count": 0, "total_amount": 0.0}
    }


if __name__ == "__main__":
    reset_demo_data()
