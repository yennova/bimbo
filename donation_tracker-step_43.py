# === Stage 43: Добавь пагинацию длинных списков ===
# Project: DonationTracker
def paginate(items, page_size=10):
    total_pages = max(1, len(items) // page_size + (1 if len(items) % page_size else 0))
    page = int(input(f"Введите номер страницы (1-{total_pages}): "))
    if page < 1 or page > total_pages:
        print("Ошибка: неверный номер страницы.")
        return
    start = (page - 1) * page_size
    end = start + page_size
    print(f"\n--- Страница {page} из {total_pages} ---")
    for i in range(start, end):
        if i < len(items):
            print(items[i])
    remaining = len(items) - end
    if remaining:
        print(f"\n... ещё {remaining} элемент(ов) на последующих страницах")
