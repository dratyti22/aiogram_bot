from random import randint
from typing import Any, Callable, Dict, Awaitable
from datetime import datetime
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


class UserIntervalIDMiddleware(BaseMiddleware):

    def get_interval_id(self, user_id: int) -> int:
        return randint(100_000_000, 999_999_999) + user_id

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        user = data['event_from_user']
        data['interval_id'] = self.get_interval_id(user.id)
        return await handler(event, data)


class HappyMonthMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        interval_id: int = data['interval_id']
        current_month: int = datetime.now().month
        is_happy_month: bool = (interval_id % 12) == current_month
        data['is_happy_month'] = is_happy_month
        return await handler(event, data)
