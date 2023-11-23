from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from states import DeleteCommon
from core.filters import HasLinkFilter, ViaBotFilter

router = Router()


@router.message(
    DeleteCommon.waiting_for_delete_start,
    F.text,
    ViaBotFilter(),
    HasLinkFilter()
)
async def link_deletion_handler()

