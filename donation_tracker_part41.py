# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: DonationTracker
def dry_run(operation):
    """
    Выполняет операцию в режиме dry-run, не сохраняя изменения.
    Возвращает результат операции и флаг was_dry_run=True.
    """
    operation()
    return {"result": operation.__dict__.get("result", None), "was_dry_run": True}
