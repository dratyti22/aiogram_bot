from aiogram.dispatcher.flags import get_flag
from aiogram.utils.chat_action import ChatActionSender
from typing import Callable, Awaitable, Any, Dict
from aiogram import BaseMiddleware, Bot
from aiogram.types import Message


class ExempleChatActionMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        chat_action = get_flag(data, "chat_action")
        if not chat_action:
            return await handler(event, data)
        async with ChatActionSender(
                action=chat_action,
                chat_id=event.chat.id,
                bot=event.bot):
            return await handler(event, data)
