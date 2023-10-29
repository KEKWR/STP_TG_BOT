from ftplib import FTP
import shutil
from  os import getenv,mkdir,listdir
from datetime import datetime

import docx

import settings

def updFiles() -> None:
    ftp = FTP(getenv('FTP_HOST'))
    ftp.login(user=getenv('FTP_USER'), passwd=getenv('FTP_PASSWD'))
    ftp.cwd('ukc/Документация/Паспорта аудиторий')

    try:
        shutil.rmtree('./pass/')
    except:
        pass

    mkdir('./pass/')
    files = ftp.nlst()
    for file in files:
        if file[0:1] != '~':
            ftp.retrbinary("RETR " + file, open(f'./pass/{file}', 'wb').write)
    
    ftp.quit()

    f =open('update.txt','w').write(str(datetime.now()))

def searchProg (nameS:str) -> list:
    files = listdir('./pass')
    res =[]
    for file in files:    
        prog =[]
        doc = docx.Document(f'./pass/{file}')
        for table in doc.tables:
            for index, row in enumerate(table.rows):
                if index == 0:
                    row_text = list(cell.text for cell in row.cells)
                    if 'Программное обеспечение' not in row_text:
                        break
                for cell in row.cells:
                    if cell.text != 'Программное обеспечение' and cell.text[-1:] != '.':
                        prog.append(cell.text)
        for name in prog:
            if nameS.lower() in name.lower():
                res.append([file[18:-5],name])
    return res

def handing_answ(nameS:str) -> str:
    output = 'Вот что удалось найти:\n' +'\n'
    answer = searchProg(nameS)
    for i in answer:
        output+= '<b>'+i[0]+'</b>' +' : '+i[1] +'\n'
    return output

def lastUpd() -> str:
    with open('update.txt','r') as f:
        return f.readline()
    

