# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: DonationTracker
import sys

ANSI_RESET = "\033[0m"
ANSI_RED = "\033[31m"
ANSI_GREEN = "\033[32m"
ANSI_YELLOW = "\033[33m"
ANSI_BLUE = "\033[34m"
ANSI_CYAN = "\033[36m"
ANSI_BOLD = "\033[1m"

def colorize(text: str, color: str = ANSI_RESET) -> str:
    """Возвращает текст с ANSI-кодом цвета, если цветовая поддержка включена."""
    if not sys.stdout.isatty():
        return text
    return f"{color}{text}{ANSI_RESET}"

def set_color_support(enable: bool = True) -> None:
    """Включает или отключает цветной вывод."""
    global _color_support
    _color_support = enable

_color_support = True

def print_donation(donor: str, amount: float, goal: str = "") -> None:
    """Печатает красивую строку о пожертвовании."""
    prefix = colorize(f"✓ {donor}", ANSI_GREEN)
    amount_str = colorize(f"{amount:.2f} ₽", ANSI_YELLOW)
    if goal:
        goal_str = colorize(f"  → {goal}", ANSI_CYAN)
    else:
        goal_str = ""
    print(f"{prefix} | {amount_str}{goal_str}")

def print_summary(total: float, goal: float) -> None:
    """Печатает сводку по прогрессу к цели."""
    pct = colorize(f"{total / goal * 100:.1f}%", ANSI_GREEN if total >= goal else ANSI_RED)
    print(f"{ANSI_BOLD}Сумма: {colorize(f'{total:.2f}', ANSI_YELLOW)} | Цель: {colorize(f'{goal:.2f}', ANSI_BLUE)} | Прогресс: {pct}{ANSI_RESET}")
