# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: DonationTracker
def archive_records(cutoff_date=None, status="completed"):
    """Archive completed or old donation records."""
    if cutoff_date is None:
        from datetime import date
        cutoff_date = date.today() - timedelta(days=365)  # default: 1 year ago
    
    archived = []
    for record in donations:
        rec_date = parse_date(record.get("date", ""))
        if (record.get("status") == status or 
            (cutoff_date and rec_date <= cutoff_date)):
            archive_records.archive_records[record["id"]] = record.copy()
            donations.remove(record)
            archived.append(record)
    
    return archived
