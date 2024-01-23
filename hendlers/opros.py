from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from aiogram import Router, types
from aiogram.fsm.context import FSMContext

opros_router = Router()


class FSM(StatesGroup):
    name = State()
    gender = State()
    age = State()
    old = State()
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
        ], resize_keyboard=True
    )
    await message.answer("opros", reply_markup=kb)
    await message.answer("Какой у вас пол?")
    await state.set_state(FSM.gender)
    await state.update_data(name=message.text)


@opros_router.message(FSM.gender)
async def fsm_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(FSM.age)
    await message.answer("Сколько вам лет?")


@opros_router.message(FSM.age)
async def process_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Возраст должен быть числом")
    elif 14 > int(message.text) > 80:
        await message.answer("Возраст должен быть от 14 до 80 лет")
    else:
        old = int(message.text)
        await state.update_data(old=old)
        await state.set_state(FSM.old)  # Замените на нужное состояние


@opros_router.message(FSM.old)
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
    await message.answer("opros", reply_markup=kb)
    await state.set_state(FSM.book)
    await state.update_data(education=message.text)


@opros_router.message(FSM.book)
async def literature(message: types.Message, state: FSMContext):
    await message.answer("ваш любимый жанр художественной литературы?")
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="romantic"),
                types.KeyboardButton(text="drama"),
                types.KeyboardButton(text="comedy")
            ]
        ], resize_keyboard=True
    )
    await message.answer("opros", reply_markup=kb)
    await state.set_state(FSM.literature)
    await state.update_data(literature=message.text)
    await state.clear()
