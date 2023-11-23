from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.filters.state import StateFilter

from core.keyboards.inline import cmd_deleted_keyboard
from states import DeleteCommon
router = Router()


@router.message(Command('delete'), StateFilter(None))
async def cmd_deleted(message: types.Message, state: FSMContext):
    await state.set_state(DeleteCommon.waiting_for_delete_start)
    await message.answer(
        text='Выберите, что хотите удалить:',
        reply_markup=cmd_deleted_keyboard()
    )
