
import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message):
    await message.answer("Daamky Client запущен!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
