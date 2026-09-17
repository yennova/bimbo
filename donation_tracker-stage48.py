# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: DonationTracker
import re

def split_large_functions(source, max_body_lines=25):
    """Split a single-file source into a list of smaller function blocks.
    Each block keeps its docstring / signature and is followed by its body
    (up to `max_body_lines` lines).  Lines that don't belong to any block
    are placed in a final 'tail' block."""

    lines = source.splitlines(keepends=True)
    blocks = []
    current = []
    current_name = None
    current_indent = 0
    tail_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped == "":
            current_indent = 0
            i += 1
            continue

        # detect a function definition
        func_match = re.match(r'^(def\s+\w+)', stripped)
        is_func_def = bool(func_match)
        if is_func_def:
            current_name = stripped
            current_indent = len(line) - len(line.lstrip())
            current.append(line)
            i += 1
            continue

        if not current_name:
            tail_lines.append(line)
            i += 1
            continue

        # compute indent of current line
        indent = len(line) - len(line.lstrip())
        if indent <= current_indent:
            # new top-level construct – close previous block
            current_indent = 0
            current_name = None
            if len(current) >= max_body_lines:
                blocks.append(current)
                current = []
            tail_lines.append(line)
            i += 1
            continue

        current.append(line)
        if len(current) >= max_body_lines:
            blocks.append(current)
            current = []
            current_name = None
            current_indent = 0
        i += 1

    if current:
        blocks.append(current)
    if tail_lines:
        blocks.append(tail_lines)

    return blocks
