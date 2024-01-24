from aiogram import Router, F, types
from aiogram.filters import Command
from db.data_base import get_teachers, get_course_data_by_name


books_router = Router()

@books_router.message(Command("courses"))
async def show_courses(message: types.Message):
    # keyboard
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Backend"),
                types.KeyboardButton(text="Frontend"),
            ],
            [
                types.KeyboardButton(text="Android"),
                types.KeyboardButton(text="iOS"),
            ],
            [
                types.KeyboardButton(text="Тестирование"),
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите направление:", reply_markup=kb)


@books_router.message(F.text.lower() == "преподаватели")
async def show_teachers(message: types.Message):
    teachers = get_teachers()


@books_router.message(F.text.lower() == "backend")
async def about_python(message: types.Message):
    # course = get_course_data(1)
    course = get_course_data_by_name("Бекенд")
    kb = types.ReplyKeyboardRemove()
    await message.answer(f"Название: {course[0]}\nОписание: {course[1]}\nПродолжительность: {course[2]} месяцев\nПреподаватель: {course[3]}", reply_markup=kb)