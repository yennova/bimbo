# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: DonationTracker
def import_from_text(path):
    """Импортирует записи из простого текстового формата.

    Формат каждой строки:
        сумма;донор;тип;дата
    где тип: donation (пожертвование), goal (цель).
    Возвращает список словарей и количество успешно добавленных записей.
    """
    records = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = [p.strip() for p in line.split(";")]
                if len(parts) < 4:
                    continue
                amount, donor, kind, date = parts[:4]
                try:
                    amount = float(amount)
                except ValueError:
                    continue
                if amount <= 0:
                    continue
                records.append({
                    "amount": amount,
                    "donor": donor,
                    "kind": kind,
                    "date": date,
                })
    except FileNotFoundError:
        return records, 0
    return records, len(records)
