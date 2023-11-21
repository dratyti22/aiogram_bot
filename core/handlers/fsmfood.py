from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import Router, types, F
from aiogram.types import ReplyKeyboardRemove

from core.handlers.ordering_food import available_food_names, available_food_sizes
from core.handlers.ordergroupclass import OrderGroup
from core.keyboards.reply import food_replay_keyboard

router = Router()


@router.message(StateFilter(None), Command('food'))
async def get_food(message: types.Message, state: FSMContext):
    await message.answer(
        text='выбири блюдо:',
        reply_markup=food_replay_keyboard(available_food_names)
    )
    await state.set_state(OrderGroup.choosing_food_name)


@router.message(
    OrderGroup.choosing_food_name,
    F.text.in_(available_food_names)
)
async def food_chosen(message: types.Message, state: FSMContext):
    await state.update_data(chosen_food=message.text.lower())
    await message.answer(
        text='Спасибо что выбрали блюдо теперь выбириту порцию:',
        reply_markup=food_replay_keyboard(available_food_sizes)
    )
    await state.set_state(OrderGroup.choosing_food_size)


@router.message(OrderGroup.choosing_food_name)
async def food_choosing_food(message: types.Message):
    await message.answer(
        text="Я не знаю такого блюда.\n\n"
             "Пожалуйста, выберите одно из названий из списка ниже:",
        reply_markup=food_replay_keyboard(available_food_names)
    )


@router.message(OrderGroup.choosing_food_size, F.text.in_(available_food_sizes))
async def food_size_choosing(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        text=f"Вы выбрали {message.text.lower()} порцию {user_data['chosen_food']}.\n"\
             f"Попробуйте теперь заказать напитки: /drinks",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()


@router.message(OrderGroup.choosing_food_size)
async def food_size_chosen_incorrectly(message: types.Message):
    await message.answer(
        text="Я не знаю такого размера порции.\n\n"
             "Пожалуйста, выберите один из вариантов из списка ниже:",
        reply_markup=food_replay_keyboard(available_food_sizes)
    )
