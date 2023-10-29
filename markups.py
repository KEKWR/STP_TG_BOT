from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

btnMain = KeyboardButton(text='Главное меню')
#--- main menu ---
btnSearshAud = KeyboardButton(text='Где установленна программа')
btnAlert = KeyboardButton(text='Настройка уведомлений')
btnHelp = KeyboardButton(text='/help')
btnSource = KeyboardButton(text='Source code')
mainMenu = ReplyKeyboardMarkup(keyboard=[[btnSearshAud],[btnAlert],[btnHelp, btnSource]],resize_keyboard=True)



#---Find programm in aud menu---
btnFind = KeyboardButton(text="Найти аудиторию")
btnUpd = KeyboardButton(text="Обновить базу")
btnLastUpd = KeyboardButton(text="Последнее обновление")
SearchMenu = ReplyKeyboardMarkup(keyboard=[[btnFind],[btnUpd, btnLastUpd],[btnMain]],resize_keyboard=True)

#---Alert settings menu--
inBtmAdm = InlineKeyboardButton(text='Административные заявки',callback_data='adm')
inBtmAlert = InlineKeyboardButton(text='Оповещения',callback_data='alert')
inBtmStud = InlineKeyboardButton(text='Учебные заявки',callback_data='stud')
alertMenu = InlineKeyboardMarkup(inline_keyboard=[[inBtmAdm],[inBtmAlert],[inBtmStud]])