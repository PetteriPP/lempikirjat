PAGE_SIZE = 20


def get_page(value, item_count):
    page_count = max(1, (item_count + PAGE_SIZE - 1) // PAGE_SIZE)
    try:
        page = int(value)
    except (TypeError, ValueError):
        page = 1
    page = max(1, min(page, page_count))
    return page, page_count
