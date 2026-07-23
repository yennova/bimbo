# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: DonationTracker
def validate_date(date_str):
    """Проверяет дату в формате YYYY-MM-DD и возвращает True/False."""
    try:
        parts = date_str.split('-')
        if len(parts) != 3 or not all(parts[i].isdigit() for i in range(3)):
            return False
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        if month < 1 or month > 12:
            return False
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[1] = 29
        return 1 <= day <= days_in_month[month - 1]
    except Exception:
        return False

def format_error(message):
    """Формирует понятное сообщение об ошибке."""
    return f"Ошибка: {message}"

print(validate_date("2024-02-30"), validate_date("2024-13-01"), validate_date("2024-06-15"))
