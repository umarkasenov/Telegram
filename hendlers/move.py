from aiogram import types, Router, F
from db.data_base import get_genre, get_movies

pro_router = Router()

@pro_router.callback_query(F.data == 'shop')
async def products(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='drama', callback_data="drama"),
             types.InlineKeyboardButton(text='comedy', callback_data="comedy"),
             types.InlineKeyboardButton(text='romantic', callback_data="romantic"),
             types.InlineKeyboardButton(text="all", callback_data="all")]
        ]
    )
    await call.message.answer('что вы хотите посмотреть', reply_markup=kb)


@pro_router.callback_query(F.data == 'drama')
async def book(call: types.CallbackQuery):
    pro = get_genre(1)
    for movies in pro:
        await call.message.answer(f'название {movies[1]}\n'
                                  f'рейтинг {movies[2]}')

@pro_router.callback_query(F.data == 'comedy')
async def comics(call: types.CallbackQuery):
    pro = get_genre(2)
    for movies in pro:
        await call.message.answer(f'название {movies[1]}\n'
                                  f'рейтинг {movies[2]}')

@pro_router.callback_query(F.data == 'romantic')
async def manga(call: types.CallbackQuery):
    pro = get_genre(3)
    for movies in pro:
        await call.message.answer(f'название {movies[1]}\n'
                                  f'рейтинг {movies[2]}')

@pro_router.callback_query(F.data == 'all')
async def product(call: types.CallbackQuery):
    pro = get_movies()
    for movies in pro:
        await call.message.answer(f'название {movies[1]}\n'
                                  f'рейтинг {movies[2]}')