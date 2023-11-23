from aiogram.fsm.state import State, StatesGroup


class SaveMode(StatesGroup):
    waiting_for_save_start = State()


class SaveText(StatesGroup):
    waiting_for_title = State()
    waiting_for_description = State()


class DeleteCommon(StatesGroup):
    waiting_for_delete_start = State()
