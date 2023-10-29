from aiogram import Router,F,types
from aiogram.types import Message

import markups

router = Router()

@router.message(F.text == 'Настройка уведомлений')
async def AlertSettings(message: types.Message):
    await message.answer(text='Какие уведомления будем получать?',reply_markup=markups.alertMenu)