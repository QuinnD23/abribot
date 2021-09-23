from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from kyeboards.inline.in_datas import check_callback

InlineForm18 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Написать❤️", url="https://bit.ly/love-girls18"),
        ],
    ],
    resize_keyboard=True
)

InlineForm = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Написать❤️", url="https://bit.ly/love-girls"),
        ],
    ],
    resize_keyboard=True
)
