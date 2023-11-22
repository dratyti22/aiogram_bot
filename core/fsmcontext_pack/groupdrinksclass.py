from aiogram.fsm.state import StatesGroup, State


class GroupDrinks(StatesGroup):
    choosing_drink_name = State()
    choosing_drink_size = State()
