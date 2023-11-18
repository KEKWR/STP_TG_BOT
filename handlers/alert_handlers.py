from aiogram import Router,F,types
from aiogram.types import Message
from sqlalchemy import create_engine

import markups
from data import config
from utils.db_api.quick_commands import add_user, upd_admin_alert, upd_alert_alert, upd_stud_alert,get_data

router = Router()
engine = create_engine(config.POSTGRES_URI,echo=True)

@router.message(F.text == 'Настройка уведомлений')
async def AlertSettings(message: Message):
    try:
        await add_user(engine, message.from_user.id)
    except:
        print('чел уже в базе')
    await message.answer(text='Выберите пункт',reply_markup=markups.alertMenu)

@router.message(F.text == 'Включить уведомления')
async def addAlertMenu(message: Message):
    await message.answer(text='Какие уведобления включить',reply_markup=markups.inalertaMenu)

@router.message(F.text == 'Выключить уведомления')
async def delAlertMenu(message: Message):
    await message.answer(text='Какие уведобления выключить',reply_markup=markups.inalertdMenu)

@router.callback_query(F.data.startswith("add_"))
async def addAlert(callback: types.CallbackQuery):
    action = callback.data.split("_")[1]
    match action:
        case 'adm':
            await upd_admin_alert(engine,callback.from_user.id,True)
        case 'alert':
            await upd_alert_alert(engine,callback.from_user.id,True)
        case 'stud':
            await upd_stud_alert(engine,callback.from_user.id,True)

@router.callback_query(F.data.startswith("del_"))
async def addAlert(callback: types.CallbackQuery):
    action = callback.data.split("_")[1]
    match action:
        case 'adm':
            await upd_admin_alert(engine,callback.from_user.id,False)
        case 'alert':
            await upd_alert_alert(engine,callback.from_user.id,False)
        case 'stud':
            await upd_stud_alert(engine,callback.from_user.id,False)

def gvno_code(i,id):
    d = get_data(engine,id)
    if d[i]: 
        return '✅\n' 
    else: 
        return '❌\n'


@router.message(F.text == 'Профиль')
async def delAlertMenu(message: Message):
    id = message.from_user.id
    out= '<b>Ваш id</b>: ' + str(id) +'\n'+'<b>Административные заявки</b>  ' + gvno_code(0,id) + '<b>Серверные заявки</b>  ' + gvno_code(1,id) + '<b>Учеьные заявки</b>  ' + gvno_code(2,id)
    await message.answer(text=out)
    