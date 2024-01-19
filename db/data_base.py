# import sqlite3
# from pathlib import Path
#
#
# def init_db():
#     global cursor, db
#     db = sqlite3.connect(
#         Path(__file__).parent.parent / 'telega.db')
#     cursor = db.cursor()
#
# def create_table():
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS courses (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             description TEXT,
#             duration INTEGER
#         )
#     """)
#     db.commit()
#
# def populate_db():
#     cursor.execute('''
#         INSERT INTO courses (name, description, duration) VALUES
#         ('Python', 'Описание пайтон', 30),
#         ('Java', 'Описание java', 30),
#         ('C++', 'Описание c++', 30)
#     ''')
#     db.commit()
#
# def add_products():
#     pass
#
# def get_products():
#     cursor = db.cursor()
#
# if __name__ == '__main__':
#     init_db()
#     create_table()
#     populate_db()
#     add_products()
#     get_products()


import sqlite3
from pathlib import Path


def init_db():
    global db, cursor
    db = sqlite3.connect(
        Path(__file__).parent.parent / "db.sqlite"
    )
    cursor = db.cursor()


def create_tables():
    cursor.execute(""" 
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
        SELECT * FROM courses 
    """)
    return cursor.fetchall()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_db()
