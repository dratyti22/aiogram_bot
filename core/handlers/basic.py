from aiogram import F, Router, Bot, flags
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, Chat, CallbackQuery
from core.keyboards.reply import replay_keyboard, get_help_reply
from aiogram.enums import MessageEntityType
from core.middleware.idmiddleware import UserIntervalIDMiddleware, HappyMonthMiddleware
from core.keyboards.inline import get_inline_keyboard
from core.middleware.chatactionsendlermeddleware import ChatMiddleware

router = Router()


@router.message(Command("ban"), F.reply_to_message)
async def cmd_ban(message: Message, admins: set[int]):
    if message.from_user.id not in admins:
        await message.answer("У вас недостаточно прав для совершения этого действия")
    else:
        await message.chat.ban(
            user_id=message.reply_to_message.from_user.id
        )
        await message.answer("Нарушитель заблокирован")


async def get_help(message: Message):
    await message.answer('Тут будет помощь', reply_markup=get_help_reply())


@router.message(Command('weekdays'))
async def get_weedays(message: Message):
    await message.answer(
        text="Нажимайте эту кнопку только по будним дням!",
        reply_markup=get_inline_keyboard()
    )


@router.callback_query(F.data == 'weekdays')
async def callback_weekdays(callback_query: CallbackQuery):
    await callback_query.answer(
        text="Спасибо, что подтвердили своё присутствие!",
        show_alert=True
    )


@router.message(Command('happymonth'))
async def get_happymonth(
        message: Message,
        interval_id: int,
        is_happy_month: bool
):
    phrases = [f'Ваш ID в нашем сервисе: {interval_id}']
    if is_happy_month:
        phrases.append("Сейчас ваш счастливый месяц!")
    else:
        phrases.append("В этом месяце будьте осторожнее...")
    await message.answer('. '.join(phrases))


@router.message(Command('hello'), flags={'long_chat': 'typing'})
async def get_start(message: Message):
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


@router.message(F.forward_from_chat(F.text == 'channel').as_('channel'))
async def forwarded_from_channel(message: Message, channel: Chat):
    await message.answer(f"This channel's ID is {channel.id}")


@router.message(F.entities[:].type == MessageEntityType.EMAIL)
async def all_emails(message: Message):
    await message.answer(f'в этом сообщение есть email')
