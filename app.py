
import asyncio
import os
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL")
WELCOME_TEXT = os.getenv(
    "WELCOME_TEXT",
    "Добро пожаловать в Daamky Client!"
)
WELCOME_IMAGE_URL = os.getenv("WELCOME_IMAGE_URL")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не задан!")

if not WEBAPP_URL:
    raise RuntimeError("WEBAPP_URL не задан!")


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def get_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Открыть Daamky",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ]
        ]
    )


@dp.message(CommandStart())
async def start_handler(message: Message):
    keyboard = get_keyboard()

    if WELCOME_IMAGE_URL:
        await message.answer_photo(
            photo=WELCOME_IMAGE_URL,
            caption=WELCOME_TEXT,
            reply_markup=keyboard
        )
    else:
        await message.answer(
            WELCOME_TEXT,
            reply_markup=keyboard
        )


@dp.message(Command("app"))
async def app_handler(message: Message):
    await message.answer(
        "Открывай Daamky:",
        reply_markup=get_keyboard()
    )


async def main():
    logging.info("Daamky Bot started!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    