from aiogram import Router, Bot, types, F
from aiogram.fsm.state import State,StatesGroup
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from utils.search_aud import updFiles,lastUpd,handing_answ
import settings
import markups

router = Router()


user_dict: dict[int, dict[str, str | int | bool]] = {}

class FSMDFillForm(StatesGroup):
    fill_prog_name = State()

menuSearch = [
    [types.KeyboardButton(text="Найти аудиторию",one_time_keyboard=True)],
    [types.KeyboardButton(text="Обновить базу")],
    [types.KeyboardButton(text="Последнее обновление")]
    ]

@router.message(F.text == 'Обновить базу')
async def upd_b(message: types.Message):
        updFiles()
        await message.answer("База обновлена!")

@router.message(F.text == 'Последнее обновление')
async def last_upd(message: types.Message):
    try:
        await message.answer('Дата последнего обновления: \n'+lastUpd())
    except:
        await message.answer("Ошибка!\nОбновите базу данных")

@router.message(F.text == 'Найти аудиторию')
async def find_aud(message: types.Message,state: FSMContext):
    await message.answer('Напишите название программы')
    await state.set_state(FSMDFillForm.fill_prog_name)

@router.message(StateFilter(FSMDFillForm.fill_prog_name))
async def find_aud_out(message: Message,state: FSMContext):
    try:
        await state.update_data(name=message.text)
        user_dict[message.from_user.id] = await state.get_data()
        await state.clear()

        if message.from_user.id in user_dict:
            await message.answer(handing_answ(user_dict[message.from_user.id]['name']))
    except:
        await message.answer("Ошибка!\nОбновите базу данных")

@router.message(F.text == 'Главное меню')
async def back_main_menu(message: types.Message):
    await message.answer(text = 'Выберите пункт',reply_markup=markups.mainMenu)