# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: DonationTracker
def get_overdue_reminders():
    today = datetime.date.today()
    overdue = []
    for reminder in all_reminders:
        if reminder['target'] and reminder['date']:
            target_date = parse_date(reminder['target']['name'], reminder['target']['created_at'])
            if target_date <= today and (today - target_date).days >= 7:
                overdue.append({
                    'donor_name': reminder.get('donor', {}).get('name', ''),
                    'target_name': reminder['target']['name'] if reminder['target'] else '',
                    'target_amount': reminder['target']['amount'] if reminder['target'] and isinstance(reminder['target']['amount'], (int, float)) else 0,
                    'current_amount': sum(d.get('amount', 0) for d in reminder.get('donations', [])),
                    'days_overdue': (today - target_date).days,
                    'deadline': str(target_date),
                })
    return overdue
