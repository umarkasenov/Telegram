from aiogram import Router
from aiogram.filters import Command
from random import choice
from aiogram import Bot, types

pic_router = Router()

@pic_router.message(Command("pic"))
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
    await Bot.send_photo(message.from_user.id, photo=photo, caption="фото")
