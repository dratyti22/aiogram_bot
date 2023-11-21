from aiogram import Bot, Dispatcher
from aiogram.filters import Command
import logging
import asyncio
from core.handlers import basic, types
from dotenv import load_dotenv
import os
from core.handlers import group_games, username
from core.filters import technical_service
from core.middleware.somemiddleware import SomeMiddleware
from core.middleware.slowtimemiddleware import SlowTimeMiddleware
from core.middleware.idmiddleware import UserIntervalIDMiddleware, HappyMonthMiddleware
from core.middleware.weeks import WeekMiddleware
from core.middleware.chatactionsendlermeddleware import ChatMiddleware
from core.middleware.exemple_chat_action_middleware import ExempleChatActionMiddleware
from core.keyboards.command import get_command
from core.handlers import in_mp
from core.handlers import admin_changes_in_group
# from config_reader import config
from core.handlers import fsmfood

async def start_bot(bot: Bot):
    await get_command(bot)
    await bot.send_message(1356288006, 'Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(1356288006, 'Бот остановлен')


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    dp = Dispatcher()

    dp.message.middleware(ExempleChatActionMiddleware())
    dp.callback_query.outer_middleware(WeekMiddleware())
    dp.update.outer_middleware(UserIntervalIDMiddleware())
    dp.message.middleware(ChatMiddleware())
    dp.message.middleware(HappyMonthMiddleware())
    dp.message.middleware(SomeMiddleware())
    # dp.message.middleware(SlowTimeMiddleware(sleep_time=1))

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(basic.get_help, Command('help'), flags={'chat_action': 'typing'})#os.getenv('main_chat_id')

    dp.include_router(admin_changes_in_group.router)
    dp.include_router(in_mp.router)
    dp.include_router(technical_service.router)
    dp.include_router(basic.router)
    dp.include_router(types.router)
    dp.include_router(group_games.router)
    dp.include_router(username.router)
    dp.include_router(fsmfood.router)

    # admins = await bot.get_chat_administrators(config.main_chat_id)
    # admin_ids = {admin.user.id for admin in admins}

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot )#admins=admin_ids
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
