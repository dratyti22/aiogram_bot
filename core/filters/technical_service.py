from aiogram import Router, F
from aiogram.filters import MagicData, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()
router.message.filter(MagicData(F.maintenance_mode.is_(True)))
router.callback_query.filter(MagicData(F.maintenance_mode.is_(True)))


@router.message()
async def any_message(message: Message):
    await message.answer('Бот на тех обслуживание напишите позже')


@router.callback_query()
async def any_callback_query(callback_query: CallbackQuery):
    await callback_query.answer(
        text='Бот на тех обслуживание напишите позже',
        show_alert=True
    )


@router.message(CommandStart())
async def any_start(message: Message):
    builder = InlineKeyboardBuilder()
    builder.button(text='Нажми', callback_data='qazxc')
    await message.answer('Какой то текс', reply_markup=builder.as_markup())


@router.callback_query(F.data == 'qazxc')
async def callback_anything(callback: CallbackQuery):
    await callback.answer(
        text="Это какое-то обычное действие",
        show_alert=True
    )
