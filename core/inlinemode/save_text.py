from typing import Optional
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandObject

from core.filters import HasLinkFilter
from core.inlinemode.states import SaveMode, SaveText
from core.inlinemode.storage import add_link, data

router = Router()


@router.message(SaveMode.waiting_for_save_start, F.text, HasLinkFilter())
async def save_text_has_link(message: Message, link: str, state: FSMContext):
    await state.update_data(link=link)
    await state.set_state(SaveText.waiting_for_title)
    await message.answer(
        text=f"Окей, я нашёл в сообщении ссылку {link}. "
             f"Теперь отправь мне заголовок (не больше 30 символов)"
    )


@router.message(SaveText.waiting_for_title, F.text.func(len) <= 30)
async def save_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text, description=None)
    await state.set_state(SaveText.waiting_for_description)
    await message.answer(
        text="Так, заголовок вижу. Теперь введи описание "
             "(тоже не больше 30 символов) "
             "или нажми /skip, чтобы пропустить этот шаг"

    )


@router.message(SaveText.waiting_for_description, F.text.len() <= 30)
@router.message(SaveText.waiting_for_description, Command('skip'))
async def last_skip(
        message: Message,
        state: FSMContext,
        command: Optional[CommandObject] = None
):
    if not Command:
        await state.update_data(description=message.text)
    data = await state.get_data()
    add_link(message.from_user.id, data['link'], data['title'], data['description'])
    await message.answer("Ссылка сохранена!")
    await state.clear()


@router.message(SaveText.waiting_for_title, F.text)
@router.message(SaveText.waiting_for_description, F.text)
async def text_too_long(message: Message):
    await message.answer("Слишком длинный заголовок. Попробуй ещё раз")
    return
