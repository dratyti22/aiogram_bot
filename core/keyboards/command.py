from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import Bot


async def get_command(bot: Bot):
    command = [
        BotCommand(
            command='start',
            description='запустить бота'
        ),
        BotCommand(
            command='dice',
            description='это кубик'
        ),
        BotCommand(
            command='basketball',
            description='это баскетболл'
        ),
        BotCommand(
            command='happymonth',
            description='предсказать твою судьбу'
        ),
        BotCommand(
            command='weekdays',
            description='дни нидели'
        ),
        BotCommand(
            command='help',
            description='🚑 помощь'
        ),
        BotCommand(
            command='user',
            description='пользователи бота'
        ),
        BotCommand(
            command='hi',
            description='поприветствовать'
        ),
    ]
    await bot.set_my_commands(command, scope=BotCommandScopeDefault())
