import asyncio
import logging
from bot import bot, dp, set_commands
from hendlers import (
    start_router,
    pic_router,
    echo_router,
    opros_router,
    books_router
)


async def main():
    await set_commands()
    dp.include_router(start_router)
    dp.include_router(pic_router)
    dp.include_router(opros_router)
    dp.include_router(books_router)

    dp.include_router(echo_router)
    # запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
