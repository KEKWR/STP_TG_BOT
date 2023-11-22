import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))

FTP_HOST = str(os.getenv('FTP_HOST'))
FTP_USER = str(os.getenv('FTP_USER'))
FTP_PASSWD = str(os.getenv('FTP_PASSWD'))

DB_HOST = str(os.getenv('DB_HOST'))
DB_NAME = str(os.getenv('DB_NAME'))
DB_USER = str(os.getenv('DB_USER'))
DB_PASS = str(os.getenv('DB_PASS'))

whiteList = [
    '316157520',
    '947319785',
    '204618345',
    '533002094',
    '457256711'
]

POSTGRES_URI = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'