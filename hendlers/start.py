from aiogram import Router, F, types
from aiogram.filters import Command
from pprint import pprint

start_router = Router()

@start_router.message(Command("start"))
async def start(message: types.Message):
    # обработка команды
    # handler
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg")
            ],
            [
                types.InlineKeyboardButton(text="Наш Instagram", url="https://www.instagram.com/casen0v_1?igsh=MWN6NjRrdW1vdmtzeg%3D%3D&utm_source=qr"),
                types.InlineKeyboardButton(text="Наш Tik Tok", url="https://l.instagram.com/?u=https%3A%2F%2Fwww.tiktok.com%2F%40casen0v_1%3F_t%3D8j23qeJLt0Z%26_r%3D1&e=AT0_\n"
                                                                   "9U40u0RQ1ffo0-3m0KhiXOkYAx63VudrJqJRBOi4rh72X8T2LeQSb_0Q5qVJrh6-_1oILUU3RwpDpOfDZG1I2HAkfagrYY6PxQ"),
            ],
            [
                types.InlineKeyboardButton(text="about us", callback_data="about_us"),
            ],
            [
                types.InlineKeyboardButton(text="sotre", callback_data="store"),
                types.InlineKeyboardButton(text="movie", callback_data="movie"),
            ]
        ]
    )
    pprint(message)
    await message.answer(f"Hello! {message.from_user.full_name}, your id: {message.from_user.id}", reply_markup=kb)

# @start_router.callback_query(F.data == "store")
# async def store(callback: types.CallbackQuery):
#     await callback.answer()
#     kb = types.ReplyKeyboardMarkup(
#         keyboard=[
#             [
#                 types.KeyboardButton(text="manga"),
#                 types.KeyboardButton(text="anime")
#             ]
#         ], resize_keyboard=True
#     )
#     await callback.message.answer("choos",  reply_markup=kb)
#
#
#
# @start_router.message(F.text == "manga")
# async def store1(message: types.Message):
#     kb = types.ReplyKeyboardMarkup(
#         keyboard=[
#             [
#                 types.KeyboardButton(text="Milli-seconds"),
#                 types.KeyboardButton(text="Lord"),
#                 types.KeyboardButton(text="Dark")
#             ]
#         ], resize_keyboard=True
#     )
#
#     await message.answer("choose manga", reply_markup=kb)
#
#
# @start_router.message(F.text == "anime")
# async def store2(message: types.Message):
#     kb = types.ReplyKeyboardMarkup(
#         keyboard=[
#             [
#                 types.KeyboardButton(text="Class superiority"),
#                 types.KeyboardButton(text="Patriotism Mariarti"),
#                 types.KeyboardButton(text="One Piece")
#             ]
#         ], resize_keyboard=True
#     )
#
#     await message.answer("choose anime", reply_markup=kb)
#
#
# @start_router.message(F.text == "Class superiority")
# async def store3(message: types.Message):
#     kb = types.ReplyKeyboardMarkup(
#         keyboard=[
#             [
#                 types.KeyboardButton(text="https://jut.su/shugi-no-kyoushitsu/season-3/")
#             ]
#         ], resize_keyboard=True
#     )
#     await message.answer(".", reply_markup=kb)

@start_router.callback_query(F.data == "about_us")
async def about_us(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Here you can find films to suit your taste\n"
                                  "For any questions you can write to WhatsApp 0706101906")
