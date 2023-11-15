from aiogram import Router, F
from typing import List
from aiogram.types import Message
from core.filters.find_user_name import FindUserNameFilter

router = Router()


@router.message(
    F.text,
    FindUserNameFilter()
)
async def message_text_username(message: Message, usernames: List[str]):
    await message.reply(
        f'Спасибо! Обязательно подпишусь на '
        f'{", ".join(usernames)}'
    )
