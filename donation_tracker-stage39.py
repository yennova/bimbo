# === Stage 39: Добавь документационную строку с описанием сценариев использования ===
# Project: DonationTracker
def _usage_scenarios(self):
        """Describe the main usage scenarios of DonationTracker."""
        scenarios = {
            "Donation Recording": "Record a donation with donor name, amount, and date. Store it in memory for later retrieval and reporting.",
            "Goal Setting": "Define a fundraising target with a name, total amount, and deadline. Track progress against the goal as donations are added.",
            "Donor Lookup": "Find all donations made by a specific donor, sorted by date, to review their contribution history.",
            "Goal Progress Check": "Calculate the percentage of a goal achieved by summing donations and comparing to the target amount.",
            "Donation Filtering": "Filter donations by date range or by donor name to create custom views of the donation history.",
            "Summary Statistics": "Compute total donations, average donation amount, and count of donors for a quick overview of fundraising activity.",
            "Goal Comparison": "Compare multiple goals by listing their names, targets, and current progress percentages side by side.",
            "Report Generation": "Generate a formatted text report that includes all goals and their progress, followed by a list of recent donations.",
        }
        return scenarios
