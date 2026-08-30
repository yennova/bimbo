# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: DonationTracker
def verify_and_repair_data():
    """
    Проверяет целостность данных и пытается исправить простые проблемы.
    Возвращает словарь с результатами проверки и восстановления.
    """
    report = {"integrity": True, "issues": [], "fixed": 0, "total_donations": 0}
    
    for donation in donations:
        issues = []
        
        # Проверка обязательных полей
        if not donation.get("donor_id"):
            issues.append("donor_id is missing")
        if not donation.get("goal_id"):
            issues.append("goal_id is missing")
        if not donation.get("amount"):
            issues.append("amount is missing")
        if not donation.get("date"):
            issues.append("date is missing")
        
        # Проверка корректности данных
        if "amount" in donation and donation["amount"] <= 0:
            issues.append("amount must be positive")
        
        # Попытка исправить проблемы
        if issues:
            donation["integrity_issues"] = issues
            if "donor_id" in donation and not donation["donor_id"]:
                donation["donor_id"] = "unknown"
            if "goal_id" in donation and not donation["goal_id"]:
                donation["goal_id"] = "unknown"
            if "amount" in donation and donation["amount"] <= 0:
                donation["amount"] = 0.0
            if "date" in donation and not donation["date"]:
                donation["date"] = "unknown"
            report["fixed"] += 1
            report["issues"].append(donation)
        else:
            report["total_donations"] += 1
    
    report["integrity"] = report["fixed"] == 0
    return report

# Пример использования
if __name__ == "__main__":
    # Добавим проблемные данные для тестирования
    donations.append({
        "donor_id": "",
        "goal_id": "",
        "amount": -100,
        "date": ""
    })
    donations.append({
        "donor_id": "donor_1",
        "goal_id": "goal_1",
        "amount": 50.0,
        "date": "2023-01-15"
    })
    
    result = verify_and_repair_data()
    print("Integrity check result:", result)
