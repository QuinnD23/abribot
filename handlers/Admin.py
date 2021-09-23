from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Command

# config
from data.config import admin_id

# db_commands
from handlers.db_commands import insert_db, update_db, select_db, delete_db

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import AdminMenu


@dp.message_handler(content_types=["photo"], state=StateMachine.EnterPhoto)
async def send_photo(message: Message):
    table = str(await select_db("admin", "user_id", "table_name", admin_id))

    photo_id = str(message.photo[-1].file_id)
    await insert_db(table, "photo_id", photo_id)
    await update_db("admin", "user_id", "help", admin_id, photo_id)

    await message.answer("Отправьте Ник:")

    await StateMachine.EnterNick.set()


@dp.message_handler(state=StateMachine.Admin)
async def mess(message: Message):

    # ----- start
    if message.text == "/start":
        await message.answer("Привет, хозяин😎", reply_markup=AdminMenu)
        await StateMachine.Admin.set()
    # -----

    if message.text == "Загрузить 18🔥":
        await message.answer("Отправьте фотографию:", reply_markup=ReplyKeyboardRemove())
        await update_db("admin", "user_id", "table_name", admin_id, "forms18")
        await StateMachine.EnterPhoto.set()

    if message.text == "Загрузить😊":
        await message.answer("Отправьте фотографию:", reply_markup=ReplyKeyboardRemove())
        await update_db("admin", "user_id", "table_name", admin_id, "forms")
        await StateMachine.EnterPhoto.set()


@dp.message_handler(state=StateMachine.EnterNick)
async def mess(message: Message):

    # ----- start
    if message.text == "/start":
        await message.answer("Привет, хозяин😎", reply_markup=AdminMenu)
        await StateMachine.Admin.set()
    # -----

    else:
        table = str(await select_db("admin", "user_id", "table_name", admin_id))

        nick = message.text
        photo_id = str(await select_db("admin", "user_id", "help", admin_id))
        await update_db(table, "photo_id", "nick", photo_id, nick)

        await message.answer("Отправьте текст:", reply_markup=AdminMenu)

        await StateMachine.EnterText.set()


@dp.message_handler(state=StateMachine.EnterText)
async def mess(message: Message):

    # ----- start
    if message.text == "/start":
        await message.answer("Привет, хозяин😎", reply_markup=AdminMenu)
        await StateMachine.Admin.set()
    # -----

    else:
        table = str(await select_db("admin", "user_id", "table_name", admin_id))

        mess = message.text
        photo_id = str(await select_db("admin", "user_id", "help", admin_id))
        await update_db(table, "photo_id", "message", photo_id, mess)

        await message.answer("Форма сохранена⚡", reply_markup=AdminMenu)
        if table == "forms":
            count = int(await select_db("admin", "user_id", "count", admin_id))
            count += 1
            await update_db("admin", "user_id", "count", admin_id, count)
        else:
            count = int(await select_db("admin", "user_id", "count18", admin_id))
            count += 1
            await update_db("admin", "user_id", "count18", admin_id, count)

        await StateMachine.Admin.set()
