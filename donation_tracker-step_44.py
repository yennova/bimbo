# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: DonationTracker
def backup_data_file(data_path: str, backup_dir: str = "backups") -> str:
    """Сохраняет резервную копию файла данных с текущей датой."""
    import shutil, os, datetime
    os.makedirs(backup_dir, exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{ts}_.json")
    shutil.copy2(data_path, backup_path)
    return backup_path
