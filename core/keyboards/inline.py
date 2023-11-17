from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Я на работе!', callback_data='weekdays')
    return keyboard.as_markup()
