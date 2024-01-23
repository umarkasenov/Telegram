import sqlite3
from pathlib import Path
from pprint import pprint


def init_db():
    global db, cursor
    db = sqlite3.connect(
        Path(__file__).parent.parent / "db.sqlite"
    )
    cursor = db.cursor()

def create_tables():
    cursor.execute("""
        --sql
        DROP TABLE IF EXISTS courses;
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
    db.commit()

def populate_db():
    cursor.execute("""
        --sql
        INSERT INTO courses (name, description, duration) VALUES
            ("Бекенд", "Описание бекенда", 5),
            ("Фронтенд", "Описание фронтенда", 5),
            ("iOS", "Описание iOS", 6),
            ("Android", "Описание Android", 6),
            ("Тестирование", "Описание тестирования", 4)
        """
    )
    db.commit()


def get_courses():
    cursor.execute("""
        --sql
        SELECT name FROM courses
    """)
    # return cursor.fetchone()
    return cursor.fetchall()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_db()
    pprint(get_courses())

# SQL - Structured Query Language Структурированный язык запросов
# СУБД - Система управления базами данных
# Реляцтонные базы данных Ralational databases
# Relation - связь, отношение
# Primary key - первичный ключ

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