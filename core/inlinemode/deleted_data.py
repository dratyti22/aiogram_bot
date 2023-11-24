from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from states import DeleteCommon
from core.filters import HasLinkFilter, ViaBotFilter
from aiogram.types import Message
from storage import *

router = Router()


@router.message(
    DeleteCommon.waiting_for_delete_start,
    F.text,
    ViaBotFilter(),
    HasLinkFilter()
)
async def link_deletion_handler(message: Message, link: str, state: FSMContext):
    deleted_link(message.from_user.id, link)
    await message.answer(
        text="Ссылка удалена! "
             "Выдача инлайн-режима обновится в течение нескольких минут.")


@router.message(
    DeleteCommon.waiting_for_delete_start,
    F.photo[-1].file_unique_id.as_("file_unique_id"),
    ViaBotFilter(),
)
async def image_deletion_handler(message: Message, state: FSMContext, file_unique_id: str):
    deleted_link(message.from_user.id, file_unique_id)
    await message.answer(
        text="Изображение удалено! "
             "Выдача инлайн-режима обновится в течение нескольких минут.")

