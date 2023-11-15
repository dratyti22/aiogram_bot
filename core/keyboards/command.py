from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import Bot, Router
from aiogram.filters import CommandStart
router = Router()


@router.message(CommandStart())
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
    ]
    await bot.set_my_commands(command, scope=BotCommandScopeDefault())
