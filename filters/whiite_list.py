from aiogram.filters import BaseFilter
from aiogram.types import Message

from data.config import whiteList

class InWhiteList(BaseFilter):
    async def __call__(self,message: Message) -> bool:
        return str(message.from_user.id) in whiteList