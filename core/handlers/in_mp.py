from aiogram import F, Router
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, MEMBER, KICKED
from aiogram.filters.command import Command
from aiogram.types import Message, ChatMemberUpdated

router = Router()
router.my_chat_member.filter(F.chat.type == 'private')
router.message.filter(F.chat.type == 'private')

users = {111, 222}


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def user_blocked_bot(event: ChatMemberUpdated):
    users.discard(event.from_user.id)


@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=MEMBER
    )
)
async def user_unblocked_bot(event: ChatMemberUpdated):
    users.add(event.from_user.id)


@router.message(Command('hi'))
async def cmd_start(message: Message):
    await message.answer('Hello')
    users.add(message.from_user.id)


@router.message(Command('user'))
async def get_user(message: Message):
    await message.answer("\n".join(f" • {user_id}" for user_id in users))
