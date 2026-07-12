# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: DonationTracker
import re, json, os

TAG_RE = re.compile(r'^[a-zA-Z0-9_ -]+$')

def add_tag(item_id, tag):
    if not TAG_RE.match(tag):
        raise ValueError("Недопустимое имя тега")
    item = load_item(item_id)
    tags = item.get('tags', [])
    if tag in tags:
        return False
    tags.append(tag)
    item['tags'] = tags
    save_item(item_id, item)
    return True

def remove_tag(item_id, tag):
    item = load_item(item_id)
    tags = item.get('tags', [])
    if tag not in tags:
        raise ValueError("Тег не найден")
    tags.remove(tag)
    item['tags'] = tags
    save_item(item_id, item)
    return True
