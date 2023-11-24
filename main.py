import asyncio
import logging

from datetime import datetime
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import BOT_TOKEN
from handlers import router
from time_message import auto_send_msg


logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Start bot')

    bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(auto_send_msg, trigger='cron', hour=21, minute=45, start_date=datetime.now(), kwargs={'bot': bot})
    scheduler.add_job(auto_send_msg, trigger='cron', hour=1, minute=55, start_date=datetime.now(), kwargs={'bot': bot})
    scheduler.start()

    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
