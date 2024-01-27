from aiogram import types, Router, F
from db.data_base import get_genre, get_movies

pro_router = Router()

@pro_router.callback_query(F.data == 'shop')
async def products(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='book', callback_data="book"),
             types.InlineKeyboardButton(text='comics', callback_data="comics"),
             types.InlineKeyboardButton(text='manga', callback_data="manga")]
        ]
    )
    await call.message.answer('что вы хотите посмотреть', reply_markup=kb)


@pro_router.callback_query(F.data == 'book')
async def book(call: types.CallbackQuery):
    pro = get_genre(1)
    for movies in pro:
        await call.message.answer(f'название {movies[1]}\n'
                                  f'цена {movies[2]}')

@pro_router.callback_query(F.data == 'comics')
async def comics(call: types.CallbackQuery):
    pro = get_genre(2)
    for movies in pro:
        await call.message.answer(f'название {movies[1]}\n'
                                  f'цена {movies[2]}')

@pro_router.callback_query(F.data == 'manga')
async def manga(call: types.CallbackQuery):
    pro = get_genre(3)
    for movies in pro:
        await call.message.answer(f'название {movies[1]}\n'
                                  f'цена {movies[2]}')

@pro_router.callback_query(F.data == 'all')
async def product(call: types.CallbackQuery):
    pro = get_movies()
    for movies in pro:
        await call.message.answer(f'название {movies[1]}\n'
                                  f'цена {movies[2]}')