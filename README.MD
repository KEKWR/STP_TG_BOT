Бот для оповещений и поиска аудиторий по названию программы
-----------------------------------
Короче тут все просто 

Для начала в корневой папке создаем файл .env

В него пишем:

    BOT_TOKEN= #токен бота, логично

    FTP_HOST= #адрес ftp 
    FTP_USER= #имя пользователя
    FTP_PASSWD= #пароль

    DB_HOST=localhost #можно и так оставить если они в одним контейнере, если нет то меняем 
    DB_NAME=stp_miigaik #перед этим нужно создать такую 
    DB_USER=postgres #это оба по умолчанию, тут уж по вашему выбору, но лучше поменять
    DB_PASS=postgres

-----------------------------------
дальше скачиваем все пакеты для питона 
```shall
python3 -m pip install -r requirements.txt
```
-----------------------------------
 и запускаем 
 ```shall
python3 bot.py
 ```