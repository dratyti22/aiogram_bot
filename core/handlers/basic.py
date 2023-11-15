from aiogram import F, Router, Bot
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, Chat
from core.keyboards.reply import replay_keyboard
from core.keyboards.command import get_command
from aiogram.enums import MessageEntityType

router = Router()


@router.message(Command('start'))
async def get_start(message: Message, bot: Bot):
    await get_command(bot)
    await message.answer('Привет!', reply_markup=replay_keyboard())


@router.message(F.text == 'Да')
async def get_yes(message: Message):
    await message.answer('Хорошо', reply_markup=ReplyKeyboardRemove())


@router.message(F.text == 'нет')
async def get_no(message: Message):
    await message.answer('Ну нет', reply_markup=ReplyKeyboardRemove())


@router.message(F.photo)
async def text_photo(message: Message):
    await message.answer('Это фото')


@router.message(F.forward_from_chat(F.text=='channel').as_('channel'))
async def forwarded_from_channel(message: Message, channel: Chat):
    await message.answer(f"This channel's ID is {channel.id}")


@router.message(F.entities[:].type == MessageEntityType.EMAIL)
async def all_emails(message: Message, mesemail: MessageEntityType):
    await message.answer(f'в этом сообщение есть email: {mesemail.EMAIL}')
