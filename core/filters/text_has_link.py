from typing import Dict, Any, Union

from aiogram.filters import BaseFilter
from aiogram.types import Message


class HasLinkFilter(BaseFilter):
    async def __call__(self, message: Message)-> Union[bool, Dict[str,Any]]:

        entities = message.entities or []

        for entity in entities:
            if entity.type == 'url':
                return {'link': entity.extract_from(message.text)}
        return False


class ViaBotFilter(BaseFilter):
    async def __call__(self, message: Message, bot: Bot) -> Union[bool, Dict[str, Any]]:
        return message.via_bot and message.via_bot.id == bot.id
