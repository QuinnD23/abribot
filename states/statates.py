from aiogram.dispatcher.filters.state import StatesGroup, State


class StateMachine(StatesGroup):
    Start = State()

    Admin = State()
    EnterPhoto = State()
    EnterNick = State()
    EnterText = State()

    Next = State()
