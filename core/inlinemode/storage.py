from typing import Optional
from aiogram import html

data = dict()


def add_link(
        telegram_id: int,
        link: str,
        title: str,
        description: Optional[str]
):
    data.setdefault(telegram_id, dict())
    data[telegram_id].setdefailt('links', dict())
    data[telegram_id]['links'][link] = {
        'title': title,
        'description': description
    }


def add_photo(
        telegram_id: int,
        photo_file_id: str,
        photo_unique_id: str
):
    data.setdefault(telegram_id, dict())
    data[telegram_id].setdefault("images", [])
    if photo_file_id not in data[telegram_id]["images"]:
        data[telegram_id]["images"].append(photo_file_id, photo_unique_id)


def get_link_by_id(telegram_id: int) -> dict:
    if telegram_id in data and 'links' in data[telegram_id]:
        return data[telegram_id]['links']
    return dict()


def get_images_by_id(telegram_id: int) -> list[str]:
    if telegram_id in data and 'images' in data[telegram_id]:
        return [item[0] for item in data[telegram_id]['images']]
    return []


def deleted_link(telegram_id: int, link: str):
    if telegram_id in data:
        if 'links' in data[telegram_id]:
            if link in data[telegram_id]['links']:
                del data[telegram_id]['links'][link]


def deleted_photo(telegram_id: int, photo_file_unique_id: str):
    if telegram_id in data and 'images' in data[telegram_id]:
        for index, (_, unique_id) in enumerate(data[telegram_id]['imeges']):
            if unique_id == photo_file_unique_id:
                data[telegram_id]['images'].pop(index)


def get_message_text(
        link: str,
        title: str,
        description: Optional[str]
) -> str:
    text_parts = [f'{html.bold(html.quote(title))}']
    if description:
        text_parts.append(html.quote(description))
    text_parts.append("")
    text_parts.append(link)
    return "\n".join(text_parts)
