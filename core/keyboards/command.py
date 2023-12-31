from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import Bot


async def get_command(bot: Bot):
    command = [
        BotCommand(
            command='start',
            description='запустить бота'
        ),
        BotCommand(
            command='food',
            description='выбирите еду'
        ),
        BotCommand(
            command='drinks',
            description='выбоать напитки'
        ),
        BotCommand(
            command='cancel',
            description='отмена'
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
            command='users',
            description='пользователи бота'
        ),
        BotCommand(
            command='hi',
            description='поприветствовать будет добавен в список'
        ),
        BotCommand(
            command='hello',
            description='поприветствовать'
        ),
        BotCommand(
            command='ban',
            description='заблокировать'
        ),
        BotCommand(
            command='starting',
            description='что заказать?'
        ),
    ]
    await bot.set_my_commands(command, scope=BotCommandScopeDefault())
