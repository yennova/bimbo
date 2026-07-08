# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: DonationTracker
def weekly_stats(records):
    """Returns a dict: {week_start_date_str: {'donations': int, 'unique_donors': set}}."""
    from collections import defaultdict
    stats = defaultdict(lambda: {'donations': 0, 'donors': set()})
    for r in records:
        if not isinstance(r, dict) or 'date' not in r:
            continue
        d = r['date']
        if isinstance(d, str):
            year, month, day = int(d[:4]), int(d[5:7]), int(d[8:10])
        elif isinstance(d, tuple):
            year, month, day = d
        else:
            continue
        week_start = (year, month - 1 + day // 7, day % 7)
        stats[week_start]['donations'] += r.get('amount', 0)
        if 'donor' in r:
            stats[week_start]['donors'].add(r['donor'])
    return dict(stats)
