from aiogram import Bot, Dispatcher
import logging
import asyncio
from core.handlers import basic, types
from dotenv import load_dotenv
import os
from core.handlers import group_games, username
from core.filters import technical_service


async def start_bot(bot: Bot):
    await bot.send_message(1356288006, 'Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(1356288006, 'Бот остановлен')


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    # dp.include_router(technical_service.router)
    dp.include_routers(basic.router, types.router,group_games.router, username.router)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
