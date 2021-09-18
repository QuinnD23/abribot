from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Command

# config
from data.config import admin_id

# date
import datetime

# db_commands
from handlers.db_commands import insert_db, update_db, select_db, delete_db

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import StartMenu, NextMenu, AdminMenu
from kyeboards.inline.in_buttons import InlineForm18, InlineForm


@dp.message_handler(Command("start"))
async def mess(message: Message):
    user_id = str(message.from_user.id)
    user_name = str(message.from_user.username)
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))).strftime("%d-%m-%Y")

    if user_id == admin_id:
        try:
            await insert_db("admin", "user_id", user_id)
        except:
            pass
        await update_db("admin", "user_id", "user_name", user_id, user_name)

        await message.answer("Привет, хозяин😎", reply_markup=AdminMenu)
        await StateMachine.Admin.set()
    else:
        try:
            await insert_db("users", "user_id", user_id)
        except:
            pass
        await update_db("users", "user_id", "user_name", user_id, user_name)
        await update_db("users", "user_id", "reg_date", user_id, now)

        await message.answer("Привет, хочешь найти девушку?😻\n"
                             "Выбери режим:", reply_markup=StartMenu)
        await StateMachine.Start.set()


@dp.message_handler()
async def mess(message: Message):
    user_id = str(message.from_user.id)
    user_name = str(message.from_user.username)

    if user_id == admin_id:
        check = True

        try:
            await select_db("admin", "user_id", "count", user_id)
        except:
            check = False

        if check:
            await message.answer("Привет, хозяин😎", reply_markup=AdminMenu)
            await StateMachine.Admin.set()
    else:
        check = True

        try:
            await select_db("users", "user_id", "user_name", user_id)
        except:
            check = False

        if check:
            await message.answer("Привет, хочешь найти девушку?😻\n"
                                 "Выбери режим:", reply_markup=StartMenu)
            await StateMachine.Start.set()


@dp.message_handler(state=StateMachine.Start)
async def mess(message: Message):
    user_id = str(message.from_user.id)
    user_name = str(message.from_user.username)
    mx = int(await select_db("admin", "user_id", "count", admin_id))

    # ----- start
    if message.text == "/start":
        await message.answer("Привет, хочешь найти девушку?😻\n"
                             "Выбери режим:", reply_markup=StartMenu)
        await StateMachine.Start.set()
    # -----

    if message.text == "Горячие знакомства(18+)🔥":
        status = int(await select_db("users", "user_id", "status", user_id))
        await update_db("users", "user_id", "help", user_id, "forms18")
        if status < mx:
            photo_id = str(await select_db("forms18", "index", "photo_id", status))
            text = str(await select_db("forms18", "index", "message", status))
            nick = str(await select_db("forms18", "index", "nick", status))

            await dp.bot.send_photo(user_id, photo_id, caption=text, reply_markup=InlineForm18)
            await message.answer(f"Имя на сайте: {nick}", reply_markup=NextMenu)

            status += 1
            await update_db("users", "user_id", "status", user_id, status)

            await StateMachine.Next.set()
        else:
            await message.answer("Доступные анкеты закончились")

    if message.text == "Обычные знакомства😊":
        status = int(await select_db("users", "user_id", "status", user_id))
        await update_db("users", "user_id", "help", user_id, "forms")
        if status < mx:
            photo_id = str(await select_db("forms", "index", "photo_id", status))
            text = str(await select_db("forms", "index", "message", status))
            nick = str(await select_db("forms", "index", "nick", status))

            await dp.bot.send_photo(user_id, photo_id, caption=text, reply_markup=InlineForm)
            await message.answer(f"Имя на сайте: {nick}", reply_markup=NextMenu)

            status += 1
            await update_db("users", "user_id", "status", user_id, status)

            await StateMachine.Next.set()
        else:
            await message.answer("Доступные анкеты закончились")


@dp.message_handler(state=StateMachine.Next)
async def mess(message: Message):
    user_id = str(message.from_user.id)
    user_name = str(message.from_user.username)
    mx = int(await select_db("admin", "user_id", "count", admin_id))

    # ----- start
    if message.text == "/start":
        await message.answer("Привет, хочешь найти девушку?😻\n"
                             "Выбери режим:", reply_markup=StartMenu)
        await StateMachine.Start.set()
    # -----

    if message.text == "Следующая💋":
        table = str(await select_db("users", "user_id", "help", user_id))
        status = int(await select_db("users", "user_id", "status", user_id))
        if status < mx:
            photo_id = str(await select_db(table, "index", "photo_id", status))
            text = str(await select_db(table, "index", "message", status))
            nick = str(await select_db(table, "index", "nick", status))

            if table == "forms":
                await dp.bot.send_photo(user_id, photo_id, caption=text, reply_markup=InlineForm)
            else:
                await dp.bot.send_photo(user_id, photo_id, caption=text, reply_markup=InlineForm18)
            await message.answer(f"Имя на сайте: {nick}", reply_markup=NextMenu)

            status += 1
            await update_db("users", "user_id", "status", user_id, status)
        else:
            await message.answer("Доступные анкеты закончились")

    if message.text == "Сменить режим⬅":
        await message.answer("Выбери режим:", reply_markup=StartMenu)
        await StateMachine.Start.set()