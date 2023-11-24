from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer('Hi')


@router.message()
async def mirror_answer(msg: Message, bot: Bot):
    await bot.send_message(msg.from_user.id, msg.text)
