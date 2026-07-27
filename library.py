import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    country TEXT
)
""")

cursor.executemany("""
INSERT INTO authors (name, country) VALUES (?, ?)
""", [
    ('Jonas Jonaitis', 'Lithuania'),
    ('Emily', 'USA'),
    ('Haruki', 'Japan')
])

cursor.execute("""
SELECT * FROM authors
""")

cursor.execute("""DROP TABLE IF EXISTS authors""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    year INTEGER,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id)
)
""")

cursor.executemany("""
INSERT INTO books (title, year, author_id) VALUES (?, ?, ?)
""", [
    ('Sun', 2012, 1),
    ('Wind', 2009, 1),
    ('Super code', 2015, 2),
    ('Forest', 2007, 2),
    ('Naruto', 1997, 3),
    ('Sakura', 1998, 3),
    ('Sakura', 1998, 99)
])

cursor.execute("""
SELECT * FROM books
""")

cursor.execute("""DROP TABLE IF EXISTS books""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

cursor.execute("""
INSERT INTO genres (name) VALUES ('Science Fiction'), ('Fantasy'), ('Mystery'), ('Manga')
""")

cursor.execute("""
SELECT * FROM genres
""")

cursor.execute("""DROP TABLE IF EXISTS genres""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS readers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS favorites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    reader_id INTEGER,
    book_id INTEGER,
    genre_id INTEGER,
    FOREIGN KEY(reader_id) REFERENCES readers(id),
    FOREIGN KEY(book_id) REFERENCES books(id),
    FOREIGN KEY(genre_id) REFERENCES genres(id)
)
""")

cursor.execute("""
INSERT INTO favorites (reader_id, book_id, genre_id) VALUES (?, ?, ?)
""", [(1, 1, 1)])

cursor.execute("""
SELECT favorites.id, readers.name, readers.surname, books.title, genres.name
FROM favorites
JOIN readers ON favorites.reader_id = readers.id
JOIN books ON favorites.book_id = books.id
JOIN genres ON favorites.genre_id = genres.id
""")

cursor.execute("""DROP TABLE IF EXISTS favorites""")


for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()
