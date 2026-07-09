# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: DonationTracker
import calendar

def monthly_stats(donations):
    stats = {}
    for d in donations:
        if 'date' not in d or 'amount' not in d:
            continue
        month_key = f"{d['date'][5:7]}-{d['date'][8:10]}"  # MM-YYYY
        if month_key not in stats:
            stats[month_key] = {'count': 0, 'total': 0.0}
        stats[month_key]['count'] += 1
        stats[month_key]['total'] += d['amount']
    return {k: dict(v) for k, v in sorted(stats.items())}

def yearly_summary(donations):
    year_stats = {}
    for d in donations:
        if 'date' not in d or 'amount' not in d:
            continue
        y = int(d['date'][:4])
        m = int(d['date'][5:7])
        _, last_day = calendar.monthrange(y, m)
        day_in_month = int(d['date'][8:10])
        if day_in_month <= last_day:
            key = f"{y}-{m}"
            if key not in year_stats:
                year_stats[key] = {'count': 0, 'total': 0.0}
            year_stats[key]['count'] += 1
            year_stats[key]['total'] += d['amount']
    return {k: dict(v) for k, v in sorted(year_stats.items())}

def print_monthly_report(donations):
    stats = monthly_stats(donations)
    if not stats:
        print("Нет данных за месяцы.")
        return
    total_donors_count = 0
    grand_total = 0.0
    for month, info in stats.items():
        avg = info['total'] / info['count'] if info['count'] else 0
        print(f"Месяц {month}: пожертвований={info['count']}, сумма={info['total']:.2f}, среднее={avg:.2f}")

def print_yearly_report(donations):
    stats = yearly_summary(donations)
    if not stats:
        print("Нет данных за годы.")
        return
    for year, info in stats.items():
        avg = info['total'] / info['count'] if info['count'] else 0
        print(f"Год {year}: пожертвований={info['count']}, сумма={info['total']:.2f}, среднее={avg:.2f}")
