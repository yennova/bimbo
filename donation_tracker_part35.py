# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: DonationTracker
def get_next_action(state):
    """Рекомендует следующее действие на основе текущего состояния DonationTracker."""
    if state.get("donors", []) == [] and state.get("goals", []) == []:
        return "Создай первого донора, чтобы начать отслеживать пожертвования."
    if state.get("donors", []) == []:
        return "Добавь донора, чтобы связать его с целями и пожертвованиями."
    if state.get("goals", []) == [] and state.get("donors", []) != []:
        return "Определи цель (например, сбор на оборудование), чтобы привязать пожертвования к конкретному проекту."
    if state.get("donations", []) == [] and state.get("goals", []) != []:
        return "Добавь пожертвование от донора к существующей цели."
    if state.get("donations", []) == [] and state.get("goals", []) == [] and state.get("donors", []) != []:
        return "Создай цель, чтобы структурировать сбор средств."
    total_donated = sum(d.get("amount", 0) for d in state.get("donations", []))
    total_goal = sum(g.get("target", 0) for g in state.get("goals", []) if g.get("target", 0) > 0)
    if total_goal > 0 and total_donated > 0:
        progress = (total_donated / total_goal) * 100
        if progress < 50:
            return f"Прогресс сбора: {progress:.1f}%. Нужно ещё {(total_goal - total_donated):.0f} монет."
        elif progress < 80:
            return f"Хороший прогресс ({progress:.1f}%)! Ускорь сбор, осталось {(total_goal - total_donated):.0f} монет."
        elif progress < 100:
            return f"Почти цель! Осталось {(total_goal - total_donated):.0f} монет."
        else:
            return "🎉 Цель достигнута! Отпразднуй успех."
    if state.get("donations", []) != [] and state.get("goals", []) != []:
        return "Сгенерируй отчёт по пожертвованиям для анализа прогресса."
    return "Продолжай добавлять доноров, цели и пожертвования по мере необходимости."
