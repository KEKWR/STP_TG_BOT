from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

btnMain = KeyboardButton(text='Главное меню')
#--- main menu ---
btnSearshAud = KeyboardButton(text='Где установленна программа')
btnAlert = KeyboardButton(text='Настройка уведомлений')
btnHelp = KeyboardButton(text='/help')
btnSource = KeyboardButton(text='Source code',callback_data='huy')
mainMenu = ReplyKeyboardMarkup(keyboard=[[btnSearshAud],[btnAlert],[btnHelp, btnSource]],resize_keyboard=True)



#---Find programm in aud menu---
btnFind = KeyboardButton(text="Найти аудиторию")
btnUpd = KeyboardButton(text="Обновить базу")
btnLastUpd = KeyboardButton(text="Последнее обновление")
SearchMenu = ReplyKeyboardMarkup(keyboard=[[btnFind],[btnUpd, btnLastUpd],[btnMain]],resize_keyboard=True)

#---Alert add settings menu--
inBtnaAdm = InlineKeyboardButton(text='Административные заявки',callback_data='add_adm')
inBtnaAlert = InlineKeyboardButton(text='Оповещения',callback_data='add_alert')
inBtnaStud = InlineKeyboardButton(text='Учебные заявки',callback_data='add_stud')
inalertaMenu = InlineKeyboardMarkup(inline_keyboard=[[inBtnaAdm],[inBtnaAlert],[inBtnaStud]])

#---Alert del settings menu--
inBtndAdm = InlineKeyboardButton(text='Административные заявки',callback_data='del_adm')
inBtnadAlert = InlineKeyboardButton(text='Оповещения',callback_data='del_alert')
inBtndStud = InlineKeyboardButton(text='Учебные заявки',callback_data='del_stud')
inalertdMenu = InlineKeyboardMarkup(inline_keyboard=[[inBtndAdm],[inBtnadAlert],[inBtndStud]])

#--Non menu button --
inBtnSource = InlineKeyboardButton(text='Клик',url='https://www.google.com/')
linkSource = InlineKeyboardMarkup(inline_keyboard=[[inBtnSource]])

#---Alert menu---
btnAddAlert = KeyboardButton(text='Включить уведомления')
btnDeleteAlert = KeyboardButton(text='Выключить уведомления')
btnProfile = KeyboardButton(text='Профиль')
alertMenu = ReplyKeyboardMarkup(keyboard=[[btnAddAlert],[btnDeleteAlert],[btnProfile,btnMain]],resize_keyboard=True)
