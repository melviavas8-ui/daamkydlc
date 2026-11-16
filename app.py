
import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Daamky Client запущен!")

async def main():
    print("Daamky Bot started!")
    await dp.start_polling(bot)

asyncio.run(main())
