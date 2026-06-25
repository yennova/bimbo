# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: DonationTracker
def sort_donations(criteria='date', reverse=True):
    if criteria == 'date':
        return sorted(donations, key=lambda x: x['date'], reverse=reverse)
    elif criteria == 'priority':
        priority_map = {'high': 0, 'medium': 1, 'low': 2}
        return sorted(donations, key=lambda x: priority_map.get(x['priority'], 99), reverse=(not reverse))
    elif criteria == 'name':
        return sorted(donations, key=lambda x: x['donor_name'].lower(), reverse=reverse)
    else:
        raise ValueError(f"Неподдерживаемый критерий сортировки: {criteria}")
