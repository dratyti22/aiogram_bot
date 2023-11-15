from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def replay_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='Да')
    kb.button(text='нет')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True)
