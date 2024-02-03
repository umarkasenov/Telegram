import asyncio
import logging
from bot import bot, dp, set_commands, scheduler
from hendlers import (
    start_router,
    pic_router,
    echo_router,
    opros_router,
    pro_router,
    scheduler_router,
)
# from parsel import parser_router

async def main():
    await set_commands()
    dp.include_router(start_router)
    dp.include_router(pic_router)
    dp.include_router(opros_router)
    dp.include_router(pro_router)
    dp.include_router(scheduler_router)
    # dp.include_router(parser_router)

    dp.include_router(echo_router)

    scheduler.start()
    # запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
