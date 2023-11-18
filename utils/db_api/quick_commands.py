
from sqlalchemy.orm import Session
from sqlalchemy import select,update

from utils.db_api.schemas.alert import AlertModel


def get_data(engine,user_id) -> list:
    with Session(engine) as session:
        ada = session.execute(select(AlertModel.admin_alert).where(AlertModel.user_id == user_id)).first()._tuple()[0]
        ala = session.execute(select(AlertModel.alert_alert).where(AlertModel.user_id == user_id)).first()._tuple()[0]
        sua = session.execute(select(AlertModel.stud_alert).where(AlertModel.user_id == user_id)).first()._tuple()[0]

    data = [ada,ala,sua]
    return data

async def add_user(engine,user_id):
    with Session(engine) as session:
        user =AlertModel(user_id=user_id,admin_alert=False,alert_alert=False,stud_alert=False)
        session.add(user)
        session.commit()

async def upd_admin_alert(engine,user_id,new_status):
    data = get_data(engine,user_id)

    with Session(engine) as session:
        session.execute(
            update(AlertModel),[
                {'user_id':user_id,
                'admin_alert': new_status,
                'alert_alert':data[1],
                'stud_alert':data[2]}
            ],
        )
        session.commit()

async def upd_alert_alert(engine,user_id,new_status):
    data = get_data(engine,user_id)

    with Session(engine) as session:
        session.execute(
            update(AlertModel),[
                {'user_id':user_id,
                'admin_alert': data[0],
                'alert_alert':new_status,
                'stud_alert':data[2]}
            ],
        )
        session.commit()

async def upd_stud_alert(engine,user_id,new_status):
    data = get_data(engine,user_id)

    with Session(engine) as session:
        session.execute(
            update(AlertModel),[
                {'user_id':user_id,
                'admin_alert': data[0],
                'alert_alert':data[1],
                'stud_alert':new_status}
            ],
        )
        session.commit()
