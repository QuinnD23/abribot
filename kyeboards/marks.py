from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

StartMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Горячие знакомства(18+)🔥"),
        ],
        [
            KeyboardButton(text="Обычные знакомства😊"),
        ],
    ],
    resize_keyboard=True
)

AdminMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Загрузить 18🔥"),
        ],
        [
            KeyboardButton(text="Загрузить😊"),
        ],
    ],
    resize_keyboard=True
)

NextMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Следующая💋"),
        ],
        [
            KeyboardButton(text="Сменить режим⬅"),
        ],
    ],
    resize_keyboard=True
)
