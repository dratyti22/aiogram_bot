from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, PhotoSize
from states import SaveMode
from storage import add_photo

router = Router()


@router.message(SaveMode.waiting_for_save_start, F.photo[-1].as_('photo'))
async def save_photo(message: Message, photo: PhotoSize, state: FSMContext):
    add_photo(message.from_user.id, photo.file_id, photo.file_unique_id)
    await message.answer("Изображение сохранено!")
    await state.clear()
