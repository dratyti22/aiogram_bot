from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import ReplyKeyboardRemove, Message
from aiogram.fsm.context import FSMContext

from core.fsmcontext_pack.groupdrinksclass import GroupDrinks
from core.fsmcontext_pack.drinks_text import available_drinks_name, available_drinks_size
from core.keyboards.reply import drinks_replay

router = Router()


@router.message(Command('drinks'), StateFilter(None))
async def get_name_dariks(message: Message, state: FSMContext):
    await message.answer(
        text='выбири напиток: ',
        reply_markup=drinks_replay(available_drinks_name)
    )
    await state.set_state(GroupDrinks.choosing_drink_name)


@router.message(GroupDrinks.choosing_drink_name, F.text.in_(available_drinks_name))
async def cmd_name_drinks(message: Message, state: FSMContext):
    await state.update_data(shoused_drinks=message.text.lower())
    await message.answer(
        text='выбири размер: ',
        reply_markup=drinks_replay(available_drinks_size)
    )
    await state.set_state(GroupDrinks.choosing_drink_size)


@router.message(GroupDrinks.choosing_drink_name)
async def cmd_size_drinks(message: Message):
    await message.answer(
        text='Я не понимаю что вы написали название напитка выбирите из списка ниже: ',
        reply_markup=drinks_replay(available_drinks_size)
    )


@router.message(GroupDrinks.choosing_drink_size, F.text.in_(available_drinks_size))
async def intput_group(message: Message, state: FSMContext):
    user_drinks = await state.get_data()
    await message.answer(
        text=f'вы выбрали напиток: {message.text.lower()}, размур напитка: {user_drinks["shoused_drinks"]}\n\n'
             f'Спасибо что выбрали нас',
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()


@router.message(GroupDrinks.choosing_drink_size)
async def cmd_drinks_size(message: Message):
    await message.answer(
        text='Я не понимаю что вы написали размер напитка выбирите из списка ниже: ',
        reply_markup=drinks_replay(available_drinks_size)
    )
