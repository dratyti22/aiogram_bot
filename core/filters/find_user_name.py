from typing import Union, Dict, Any

from aiogram.filters import BaseFilter
from aiogram.types import Message


class FindUserNameFilter(BaseFilter):
    async def __call__(self, message: Message) -> Union[bool, Dict[str, Any]]:
        entities = message.entities or []

        found_username = [
            item.extract_from(message.text) for item in entities
            if item.type == 'mention'
        ]

        if len(found_username) > 0:
            return {'username': found_username}
        return False

