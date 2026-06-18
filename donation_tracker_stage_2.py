# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: DonationTracker
class DonationModel:
    def __init__(self, donor_name: str, goal_name: str, amount: float, date_str: str):
        self.donor_name = self._validate_donor(donor_name)
        self.goal_name = self._validate_goal(goal_name)
        self.amount = self._validate_amount(amount)
        self.date = self._parse_date(date_str)

    def _validate_donor(self, name: str) -> str:
        if not name or len(name.strip()) < 2:
            raise ValueError("Имя донора должно быть не пустым и содержать минимум 2 символа.")
        return name.strip().title()

    def _validate_goal(self, name: str) -> str:
        if not name or len(name.strip()) < 3:
            raise ValueError("Название цели должно быть не пустым и содержать минимум 3 символа.")
        return name.strip().capitalize()

    def _validate_amount(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Сумма пожертвования должна быть положительным числом.")
        return round(amount, 2)

    def _parse_date(self, date_str: str):
        from datetime import datetime
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Дата должна быть в формате YYYY-MM-DD.")
