def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    if start + size >= len(text):
        return text[start:], len(text) - start

    end = start + size
    while end > start:
        if text[end] in '.!?':

            return text[start:end + 1], end - start + 1
        end -= 1

    return text[start:start + size], size


def prepare_text(path: str, page_size: int = 1050) -> dict[int, str]:
    book = {}

    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()

    current_position = 0
    page_number = 1

    while current_position < len(text):
        page_text, actual_size = _get_part_text(text, current_position, page_size)

        cleaned_text = page_text.lstrip()
        book[page_number] = cleaned_text

        current_position += actual_size
        page_number += 1

    return book