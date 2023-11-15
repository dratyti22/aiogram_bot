from aiogram import Router
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import Message
from aiogram.filters import Command

from core.filters.chat_type import ChatTypeFIlter

router = Router()
router.message.filter(
    ChatTypeFIlter(
        chat_type=["group", "supergroup", 'private'],
    )
)


@router.message(Command("dice"))
async def cmd_dice_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)


@router.message(Command("basketball"))
async def cmd_basketball_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.BASKETBALL)
