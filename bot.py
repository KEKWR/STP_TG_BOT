from os import getenv
import logging
import asyncio

from aiogram import Dispatcher, Bot, types, F
from aiogram.filters import Command

import settings 
from handlers import search_handlers,alert_handlers
import markups

logging.basicConfig(level=logging.INFO)
TOKEN = str(getenv("BOT_API"))
bot = Bot(TOKEN,parse_mode='HTML')
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Это бот в помощь технической поддержке МИИГАиК", reply_markup=markups.mainMenu)

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer('')

@dp.message(F.text == 'Где установленна программа')
async def call_find_menu(message: types.Message):
    await message.answer(text = 'Выберите пункт',reply_markup=markups.SearchMenu)

dp.include_router(search_handlers.router)
dp.include_router(alert_handlers.router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())