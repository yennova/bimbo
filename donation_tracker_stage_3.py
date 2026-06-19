# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: DonationTracker
class DonationTracker:
    def __init__(self):
        self.donors = {}
        self.goals = {}
        self.transactions = []

    def add_donor(self, name, email=None):
        if not name or not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Имя донора должно быть непустым.")
        self.donors[name] = {"email": email}
        return True

    def add_goal(self, title, target_amount):
        if not title or not isinstance(title, str) or len(target_amount) == 0:
            raise ValueError("Заголовок цели и сумма должны быть корректными.")
        self.goals[title] = {"target": float(target_amount), "current": 0.0}
        return True

    def add_transaction(self, donor_name, goal_title, amount):
        if not all([donor_name in self.donors, goal_title in self.goals]):
            raise ValueError("Донор или цель не найдены.")
        if float(amount) <= 0:
            raise ValueError("Сумма пожертвования должна быть положительной.")
        transaction = {
            "donor": donor_name,
            "goal": goal_title,
            "amount": float(amount),
            "timestamp": __import__('datetime').datetime.now().isoformat()
        }
        self.goals[goal_title]["current"] += float(amount)
        self.transactions.append(transaction)
        return True

    def get_report(self):
        report = []
        for goal, data in self.goals.items():
            progress = (data["current"] / data["target"]) * 100 if data["target"] > 0 else 0
            report.append({
                "goal": goal,
                "raised": data["current"],
                "target": data["target"],
                "progress_percent": round(progress, 2)
            })
        return sorted(report, key=lambda x: x["progress_percent"], reverse=True)
