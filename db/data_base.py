import sqlite3
from pathlib import Path
from pprint import pprint

db = sqlite3.connect('server.db')
sql = db.cursor()

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
    sql.execute("""CREATE TABLE IF NOT EXISTS genre (
        id INTEGER PRIMARY KEY,
        genre TEXT
    )""")

    sql.execute("""CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        name TEXT,
        rating INTEGER,
        year INTEGER,
        genre_id INTEGER,
        FOREIGN KEY (genre_id) REFERENCES genre (id)
    )""")

    db.commit()


def fill_tables():
    # Проверяем, существует ли уже хотя бы одна запись в таблице movies
    sql.execute("SELECT COUNT(*) FROM movies")
    result = sql.fetchone()[0]

    # Если нет записей, то заполняем таблицы данными
    if result == 0:
        # Заполняем таблицу genre
        sql.executemany("""INSERT INTO genre (genre) VALUES (?)""", [
            ("drama",),
            ("comedy",)
        ])

        # Заполняем таблицу movies
        sql.executemany("""INSERT INTO movies (name, rating, year, genre_id) VALUES (?, ?, ?, ?)""", [
            ("The Shawshank Redemption", 95, 2020, 1),  # 1 corresponds to "romantic" in the genre table
            ("The Godfather", 96, 2010, 2),  # 2 corresponds to "drama" in the genre table
            ("The Dark Knight", 87, 2029, 3)  # 3 corresponds to "comedy" in the genre table
        ])

        db.commit()


def add_more_movies():
    # Заполняем таблицу movies дополнительными данными
    sql.executemany("""INSERT INTO movies (name, rating, year, genre_id) VALUES (?, ?, ?, ?)""", [
        # ("Inception", 90, 2010, 1),
        # ("Pulp Fiction", 94, 1994, 2),
        # ("The Grand Budapest Hotel", 87, 2014, 3),
        # ("The Matrix", 88, 1999, 1),
        # ("Forrest Gump", 92, 1994, 2)
    ])

    db.commit()


def get_movies():

    sql.execute("""
        SELECT * FROM movies
    """)
    return sql.fetchall()

def get_move(id):
    sql.execute("""
        SELECT * FROM movies WHERE id = :cid
    """, {"cid": id})
    return sql.fetchone()

def get_genre(id):
    sql.execute("""
        SELECT * FROM movies WHERE genre_id = :cid
    """, {"cid": id})
    return sql.fetchall()

if __name__ == '__main__':
    init_db()
    # populate_db()
    create_tables()
    print(get_genre(3))
#
# # Создаем таблицы, если они не существуют
# create_tables()
#
# # Заполняем таблицы данными, если это еще не было сделано
# fill_tables()
#
# # Добавляем еще несколько фильмов
# add_more_movies()
#
# # Закрываем соединение с базой данных
# db.close()
