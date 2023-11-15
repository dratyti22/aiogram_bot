from aiogram import F, Router
from aiogram.types import Message


router = Router()


@router.message(F.text)
async def get_text(message: Message):
    await message.answer('Это текст')


@router.message(F.sticker)
async def get_sticker(message: Message):
    await message.answer('Это стикер')


@router.message(F.animation)
async def get_animation(message: Message):
    await message.answer('Это GIF')

