# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: DonationTracker
def switch_profile():
    """Переключить между сохранёнными профилями (admin / viewer)."""
    from pathlib import Path
    profiles_dir = Path(__file__).parent / "profiles"
    if not profiles_dir.exists():
        profiles_dir.mkdir()
    active_file = profiles_dir / f"{active_user}.json"
    with open(active_file, "r") as f:
        profile = json.load(f)
    print(f"\n📋 Профиль: {profile['name']} ({profile['role']})")
    print("Доступные роли:")
    saved = sorted(profiles_dir.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    for i, pf in enumerate(saved):
        if pf == active_file:
            continue
        with open(pf, "r") as f2:
            d = json.load(f2)
        print(f"  [{i+1}] {d['name']} ({d['role']}) — файл: {pf.name}")
    choice = input("Выберите номер профиля (или Enter для выхода): ").strip()
    if not choice:
        return
    idx = int(choice) - 1
    if idx < len(saved):
        target = saved[idx]
        with open(target, "r") as f2:
            new_profile = json.load(f2)
        active_user = new_profile["name"]
        save_active(active_user, {**new_profile, "sessions": profile.get("sessions", [])})
        print(f"\n✅ Переключено на профиль: {active_user}")
    else:
        print("\n❌ Неверный выбор.")
