from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

opros_router = Router()


class FSM(StatesGroup):
    name = State()
    age = State()
    gender = State()
    hobby = State()
    education = State()
    book = State()
    literature = State()

@opros_router.message(Command("opros"))
async def fsm_start(message: types.Message, state: FSMContext):
    await state.set_state(FSM.name)
    await message.answer("Как вас зовут?")

@opros_router.message(FSM.name)
async def fsm_gender(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="мужской"),
                types.KeyboardButton(text="женский"),
            ],
            [
                types.KeyboardButton(text="чистый")
            ]
        ], resize_keyboard=True
    )
    await message.answer(reply_markup=kb)
    await message.answer("Какой у вас пол? чистый")
    await state.set_state(FSM.gender)
    await state.update_data(name=message.text)



@opros_router.message(FSM.gender)
async def fsm_age(message: types.Message, state: FSMContext):
    age = int(message.text)
    await state.update_data(age=age)
    await state.set_state(FSM.age)
    await message.answer("Сколько вам лет?")


@opros_router.message(FSM.age)
async def hobby(message: types.Message, state: FSMContext):
    await message.answer("Ваш род деятельности?")
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="учеба"),
                types.KeyboardButton(text="работа"),
                types.KeyboardButton(text="бизнес"),
                types.KeyboardButton(text="наука"),
                types.KeyboardButton(text="дом-семья"),
                types.KeyboardButton(text="другое")
            ]
        ], resize_keyboard=True
    )
    await message.answer(reply_markup=kb)
    await state.set_state(FSM.hobby)
    await state.update_data(gender=message.text)


@opros_router.message(FSM.hobby)
async def education(message: types.Message, state: FSMContext):
    await message.answer("Ваше образование")
    await state.set_state(FSM.education)
    await state.update_data(hobby=message.text)


@opros_router.message(FSM.education)
async def book(message: types.Message, state: FSMContext):
    await message.answer("как часто вы читаете художественные книг?")
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="часто"),
                types.KeyboardButton(text="редко")
            ]
        ], resize_keyboard=True
    )
    await message.answer(reply_markup=kb)
    await state.set_state(FSM.book)
    await state.update_data(education=message.text)


@opros_router.message(FSM.book)
async def literature(message: types.Message, state: FSMContext):
    await message.answer("ваш любимый жанр художественной литературы?")
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="romatic"),
                types.KeyboardButton(text="dramma"),
                types.KeyboardButton(text="comedia")
            ]
        ], resize_keyboard=True
    )
    await message.answer(reply_markup=kb)
    await state.set_state(FSM.literature)
    await state.update_data(literature=message.text)


