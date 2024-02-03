from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler

load_dotenv()
TOKEN = getenv("TOKEN_BOT")
bot = Bot(token=TOKEN)
dp = Dispatcher()
scheduler = AsyncIOScheduler()


async def set_commands():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Старт"),
        types.BotCommand(command="pic", description="Отправить картинку"),
        types.BotCommand(command="opros", description="опрос"),
        types.BotCommand(command="shop", description="shop"),
        # types.BotCommand(command="about as",description="о нас"),
        # types.BotCommand(command="store", description="магаз")
    ])
