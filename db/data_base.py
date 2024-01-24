import sqlite3
from pathlib import Path
from pprint import pprint


def init_db():
    """
    Создается соединение с БД и курсор
    """
    global db, cursor
    db = sqlite3.connect(
        Path(__file__).parent.parent / "db.sqlite"
    )
    cursor = db.cursor()

def create_tables():
    """
    Создание таблиц
    """
    cursor.execute("""
        --sql
        DROP TABLE IF EXISTS courses;
    """)
    cursor.execute("""
        --sql
        DROP TABLE IF EXISTS teachers;
    """)
    cursor.execute("""
        --sql
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            duration INTEGER
        );
    """)
    cursor.execute("""
        --sql
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            course_id INTEGER,
            FOREIGN KEY (course_id) REFERENCES courses(id)
        )
    """)
    db.commit()

def populate_db():
    """
    Заполнение таблиц
    """
    cursor.execute("""
        --sql
        INSERT INTO courses (name, description, duration) VALUES
            ("naruto", "Описание", 5),
            ("blich", "Описание", 5),
            ("one piece", "Описание", 6),
            ("baron", "Описание", 6),
            ("gun", "Описание", 4)
        """
    )
    cursor.execute("""
        INSERT INTO teachers (name, course_id) VALUES
        ("umar", 1),
        ("Igor", 2),
        ("nurbol", 5)
    """)
    db.commit()


def get_courses():
    """
    Получение данных о всех курсах
    """
    cursor.execute("""
        --sql
        SELECT * FROM courses
    """)
    # return cursor.fetchone()
    return cursor.fetchall()


def get_courses_with_teachers():
    """
    Получение данных о курсах и их преподавателях
    """
    cursor.execute("""
        --sql
        SELECT c.name, t.name FROM courses AS c
        JOIN teachers AS t ON c.id = t.course_id
    """)
    return cursor.fetchall()


def get_teachers():
    cursor.execute("""
        --sql
        SELECT c.name, t.name FROM teachers AS t
        JOIN courses AS c ON c.id = t.course_id
    """)
    return cursor.fetchall()


def get_course_data(id: int):
    """
    Получение данных о курсе и его преподавателе по id курса
    """
    # cursor.execute("""
    #     --sql
    #     SELECT name, description, duration FROM courses
    #     WHERE id = :cid
    # """, {"cid": id})
    cursor.execute("""
        --sql
        SELECT c.name, c.description, c.duration, t.name FROM courses AS c
        JOIN teachers AS t ON c.id = t.course_id
        WHERE c.id = :cid
    """, {"cid": id})
    return cursor.fetchone()


def get_course_data_by_name(name: str):
    """
    Получение данных о курсе и его преподавателе по названию курса
    """
    cursor.execute("""
        --sql
        SELECT c.name, c.description, c.duration, t.name FROM courses AS c
        JOIN teachers AS t ON c.id = t.course_id
        WHERE c.name = :cname
    """, {"cname": name})
    return cursor.fetchone()


def get_teachers_by_course_name(name: str):
    """
    Получение имен проподвателей по названию курса
    """
    cursor.execute("""
        --sql
        SELECT teachers.name FROM teachers 
        WHERE teachers.course_id = (
            SELECT id FROM courses WHERE name = :cname
        )
    """, {"cname": name})
    return cursor.fetchall()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_db()
    # pprint(get_courses())
    # pprint(get_courses_with_teachers())
    # pprint(get_teachers())
    # pprint(get_course_data(1))
    pprint(get_teachers_by_course_name("Бекенд"))

# SQL - Structured Query Language Структурированный язык запросов
# СУБД - Система управления базами данных
# Реляцтонные базы данных Ralational databases
# Relation - связь, отношение
# Primary key - первичный ключ
# Foreign key - внешний ключ

# Courses:
# 1, "Бекенд", "Описание бекенда", 5,     1
# 2, "Фронтенд", "Описание фронтенда", 5, 1
# 3, "iOS", "Описание iOS", 6,            2
# 4, "Android", "Описание Android", 6,    4
# 5, "Тестирование", "Описание тестирования", 4, 3

# Teachers:
# 1, "Игорь",
# 2, "Алексей"
# 3, "Нурдин"
# 4, "Бекболот"