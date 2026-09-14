# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: DonationTracker
class VersionMigration:
    """Миграция структуры данных при изменении версий проекта."""
    VERSION = 1

    @staticmethod
    def migrate_old_data(old_records):
        if old_records is None:
            return []
        return old_records

    @staticmethod
    def export_for_migration(data):
        return data
