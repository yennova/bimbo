# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: DonationTracker
def search_donations(query: str) -> list[dict]:
    if not query.strip():
        return []
    q = query.lower()
    results = []
    for d in donations:
        fields = [d.get(k, '') for k in ('donor_name', 'goal_name', 'amount_str', 'date')]
        combined = ' '.join(fields)
        if q in combined:
            results.append(d.copy())
    return results
