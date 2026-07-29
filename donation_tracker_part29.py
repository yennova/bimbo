# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: DonationTracker
def load_config():
    defaults = {
        "app_name": "DonationTracker",
        "max_donors": 20,
        "default_currency": "RUB",
        "date_format": "%Y-%m-%d",
        "log_file": "donations.log",
        "backup_dir": "backups",
        "notification_email": None,
    }
    config_path = os.path.join(os.getcwd(), "config.txt")
    if not os.path.exists(config_path):
        with open(config_path, "w") as f:
            for k, v in defaults.items():
                f.write(f"{k}={v}\n")
        return defaults.copy()

    config = {}
    with open(config_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, value = line.split("=", 1)
            config[key.strip()] = value.strip().strip('"')

    result = defaults.copy()
    for key, val in config.items():
        try:
            result[key] = int(val) if "." not in val else float(val)
        except ValueError:
            result[key] = val
    return result

config = load_config()
