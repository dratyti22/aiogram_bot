from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, KICKED, LEFT, MEMBER, RESTRICTED, \
    ADMINISTRATOR, CREATOR, IS_MEMBER, IS_NOT_MEMBER, JOIN_TRANSITION
from aiogram import Router
router = Router()

@router.my_chat_member(ChatMemberUpdatedFilter(
    member_status_changed=(
        KICKED | LEFT | -RESTRICTED
    )>>(
        +RESTRICTED |MEMBER | ADMINISTRATOR | CREATOR
    )
))


@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=(
            IS_NOT_MEMBER >> IS_MEMBER
        )
    )
)


@router.my_chat_member(
    ChatMemberUpdatedFilter(
        chat_member_status = JOIN_TRANSITION
    )
)
async def aaaa():
    pass

