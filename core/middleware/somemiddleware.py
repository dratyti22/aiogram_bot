from typing import Any, Dict, Awaitable, Callable
from aiogram import BaseMiddleware, Router
from aiogram.types import TelegramObject


class SomeMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str,Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        print("Before handler")
        result = await handler(event, data)
        print("After handler")
        return result


