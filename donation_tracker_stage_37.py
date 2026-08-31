# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: DonationTracker
import unittest

class TestDonationTracker(unittest.TestCase):
    def test_add_donor(self):
        dt = DonationTracker()
        dt.add_donor("Иван", 1000)
        dt.add_donor("Мария", 2000)
        self.assertEqual(len(dt.donors), 2)
        self.assertEqual(dt.donors[0], ("Иван", 1000))
        self.assertEqual(dt.donors[1], ("Мария", 2000))

    def test_add_goal(self):
        dt = DonationTracker()
        dt.add_goal("Помощь больным", 50000)
        dt.add_goal("Образование", 30000)
        self.assertEqual(len(dt.goals), 2)
        self.assertEqual(dt.goals[0], ("Помощь больным", 50000))
        self.assertEqual(dt.goals[1], ("Образование", 30000))

    def test_add_donation(self):
        dt = DonationTracker()
        dt.add_donor("Иван", 1000)
        dt.add_goal("Помощь больным", 50000)
        dt.add_donation("2024-01-15", "Иван", "Помощь больным", 500)
        self.assertEqual(dt.donations[0], ("2024-01-15", "Иван", "Помощь больным", 500))

    def test_get_report(self):
        dt = DonationTracker()
        dt.add_donor("Иван", 1000)
        dt.add_goal("Помощь больным", 50000)
        dt.add_donation("2024-01-15", "Иван", "Помощь больным", 500)
        dt.add_donation("2024-02-20", "Иван", "Помощь больным", 300)
        dt.add_donation("2024-03-10", "Мария", "Помощь больным", 1000)
        report = dt.get_report("Помощь больным", "2024-01-01", "2024-12-31")
        self.assertEqual(report[0], "Помощь больным")
        self.assertEqual(report[1], 3)
        self.assertEqual(report[2], 1800)
        self.assertEqual(report[3], 50000)

if __name__ == "__main__":
    unittest.main()
