# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: DonationTracker
import time
from datetime import datetime, timezone

class ChangeLog:
    def __init__(self):
        self.entries = []

    def log(self, action, entity, details):
        entry = {
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'action': action,
            'entity': entity,
            'details': details
        }
        self.entries.append(entry)
        print(f"[{entry['timestamp']}] {action} {entity}: {details}")

    def get_changes(self, since=None):
        if since:
            return [e for e in self.entries if e['timestamp'] >= since]
        return list(self.entries)
