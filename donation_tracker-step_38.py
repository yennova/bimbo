# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: DonationTracker
def test_edge_cases():
    # Тесты ошибок и пограничных случаев
    assert DonationTracker().add_donor("  ", 0) is False
    assert DonationTracker().add_donor("", -100) is False
    assert DonationTracker().add_donor("", None) is False
    assert DonationTracker().add_donor("", "abc") is False
    assert DonationTracker().add_donor("Alice", 0) is False
    assert DonationTracker().add_donor("Alice", -1) is False

    assert DonationTracker().add_goal("  ", 0) is False
    assert DonationTracker().add_goal("", -100) is False
    assert DonationTracker().add_goal("", None) is False
    assert DonationTracker().add_goal("", "abc") is False
    assert DonationTracker().add_goal("Goal", 0) is False
    assert DonationTracker().add_goal("Goal", -1) is False

    assert DonationTracker().add_donation("A", "G", 0) is False
    assert DonationTracker().add_donation("A", "G", -1) is False
    assert DonationTracker().add_donation("A", "G", None) is False
    assert DonationTracker().add_donation("A", "G", "abc") is False

    assert DonationTracker().get_report("  ") is False
    assert DonationTracker().get_report("") is False

    dt = DonationTracker()
    dt.add_donor("A", 100)
    dt.add_goal("G", 200)
    dt.add_donation("A", "G", 50)
    assert dt.get_report("A") == "Donor: A, Goal: G, Amount: 50"
    assert dt.get_report("A") == "Donor: A, Goal: G, Amount: 50"
    assert dt.get_report("B") is False
    assert dt.get_report("G") is False

    dt2 = DonationTracker()
    dt2.add_donor("X", 100)
    dt2.add_goal("Y", 200)
    dt2.add_donation("X", "Y", 50)
    assert dt2.get_report("X") == "Donor: X, Goal: Y, Amount: 50"
    dt2.add_donation("X", "Y", 25)
    assert dt2.get_report("X") == "Donor: X, Goal: Y, Amount: 75"
