from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart, Command


from get_msg import get_msg


router = Router()


@router.message(Command('get_all'))
async def get_all(msg: Message, bot: Bot):
    for i in get_msg(get_all=True):
        await bot.send_message(msg.from_user.id, i)


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer('Hi')


# mirror_answer have to be the last, because it's other catching all messages

@router.message()
async def mirror_answer(msg: Message, bot: Bot):
    await bot.send_message(msg.from_user.id, msg.text)
