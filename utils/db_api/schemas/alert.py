from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

class AlertModel(Base):
    __tablename__ = 'alertModel'

    user_id: Mapped[int] = mapped_column(primary_key=True,nullable=False,unique=True)
    admin_alert: Mapped[bool] = mapped_column(nullable=False)
    alert_alert: Mapped[bool] = mapped_column(nullable=False)
    stud_alert:  Mapped[bool] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"User(user_id={self.user_id!r}, admin_alert={self.admin_alert!r}, alert_alert={self.alert_alert!r}), stud_alert={self.stud_alert!r})"