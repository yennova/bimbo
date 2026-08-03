# === Stage 32: Добавь журнал действий пользователя ===
# Project: DonationTracker
def log_action(action, details=None):
    """Записать действие в журнал."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"[{timestamp}] {action}"
    if details:
        entry += f" - {details}"
    print(entry)
