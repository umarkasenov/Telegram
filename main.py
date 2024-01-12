import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging
from pprint import pprint
from random import choice

load_dotenv()
TOKEN = getenv("TOKEN_BOT")
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("pic"))
async def send_pic(message: types.Message):
    photo = [
        "media/1.jpg",
        "media/2.jpg",
        "media/3.jpeg",
        "media/4.jpeg",
        "media/5.jpeg",
        "media/6.jpeg"
    ]
    photo = types.FSInputFile(choice(photo))
    await bot.send_photo(message.from_user.id, photo=photo, caption="фото")

# обработка команды
# handler

@dp.message(Command("start"))
async def start(message: types.Message):
    pprint(message)
    await message.answer(f"Привет! {message.from_user.full_name}, ваш id: {message.from_user.id}")

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Старт"),
        types.BotCommand(command="pic", description="Отправить картинку"),
    ])

    # запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
