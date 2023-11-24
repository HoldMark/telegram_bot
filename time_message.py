from aiogram import Bot
from get_msg import get_msg
from config import TG_USER_ID


async def auto_send_msg(bot: Bot):

    """
        Указываем id чата/пользователя и отправляем текст по указанному времени
    """

    for i in get_msg():
        await bot.send_message(TG_USER_ID, text=i)
