# === Stage 17: Добавь группировку записей по категориям ===
# Project: DonationTracker
def categorize_donations(records):
    cats = {}
    for r in records:
        name = r.get("category", "Uncategorized")
        if name not in cats:
            cats[name] = []
        cats[name].append(r)
    return dict(sorted(cats.items(), key=lambda x: sum(x[1]["amount"] for x in x[1]), reverse=True))
