from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Я на работе!', callback_data='weekdays')
    return keyboard.as_markup()


def cmd_deleted_keyboard():
    kb = [
        [
            InlineKeyboardButton(
                text="Выбрать ссылку",
                switch_inline_query_current_chat="links"
            )
        ],
        [
            InlineKeyboardButton(
                text="Выбрать изображение",
                switch_inline_query_current_chat="images"
            )
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb, resize_keyboard=True)
