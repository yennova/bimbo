# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: DonationTracker
def filter_records(status=None, category=None, tags=None):
    filtered = []
    for record in records:
        if status is not None and record['status'] != status:
            continue
        if category is not None and record.get('category') != category:
            continue
        if tags is not None and set(record.get('tags', [])).isdisjoint(tags):
            continue
        filtered.append(record)
    return filtered
