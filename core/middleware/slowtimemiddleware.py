from typing import Any, Dict, Awaitable, Callable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
import asyncio


class SlowTimeMiddleware(BaseMiddleware):
    def __init__(self, sleep_time):
        self.sleep_time = sleep_time

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        await asyncio.sleep(self.sleep_time)
        result = await handler(event, data)
        print(f"Handler was delayed by {self.sleep_time} seconds")
        return result
