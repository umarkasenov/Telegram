import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging
from pprint import pprint
from random import choice
from aiogram import Router, F, types

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

# @dp.message(Command("start"))
# async def start(message: types.Message):
#     pprint(message)
#     await message.answer(f"Привет! {message.from_user.full_name}, ваш id: {message.from_user.id}")

@dp.message(Command("start"))
async def start(message: types.Message):
    # обработка команды
    # handler
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg")
            ],
            [
                types.InlineKeyboardButton(text="Наш Instagram", url="https://www.instagram.com/casen0v_1?igsh=MWN6NjRrdW1vdmtzeg%3D%3D&utm_source=qr"),
                types.InlineKeyboardButton(text="Наш Tik Tok", url="https://l.instagram.com/?u=https%3A%2F%2Fwww.tiktok.com%2F%40casen0v_1%3F_t%3D8j23qeJLt0Z%26_r%3D1&e=AT0_\n"
                                                                   "9U40u0RQ1ffo0-3m0KhiXOkYAx63VudrJqJRBOi4rh72X8T2LeQSb_0Q5qVJrh6-_1oILUU3RwpDpOfDZG1I2HAkfagrYY6PxQ"),
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about_us"),
            ],
            [
                types.InlineKeyboardButton(text="Магазин", callback_data="about_us"),
            ]
        ]
    )
    # pprint(message)
    await message.answer(f"Привет! {message.from_user.full_name}, ваш id: {message.from_user.id}", reply_markup=kb)


@dp.message(F.text.lower() == "Магазин")
async def about_python(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Курс по Python", reply_markup=kb)

@dp.callback_query(F.data == "about_us")
async def about_us(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.answer("Здесь мы хотим рассказать о нашей компании")




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
