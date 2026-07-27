import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

readers = [
    ('John', 'Doe', 'john.doe@example.com'),
    ('Jane', 'Smith', 'jane.smith@example.com'),
    ('Alice', 'Johnson', 'alice.johnson@example.com'),
    ('Bob', 'Brown', 'bob.brown@example.com'),
    ('Charlie', 'Davis', 'charlie.davis@example.com'),
    ('David', 'Wilson', 'david.wilson@example.com')
]

cursor.execute("""
CREATE TABLE IF NOT EXISTS readers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    email TEXT
)
""")

cursor.executemany("""
INSERT INTO readers (name, surname, email) VALUES (?, ?, ?)
""", readers)

cursor.execute("""
UPDATE readers
SET email = REPLACE(email, '@example.com', '@newdomain.com')
WHERE email LIKE '%@example.com'
""")

cursor.execute("""
SELECT * FROM readers
WHERE email LIKE '%@example.com'
""")

cursor.execute("""DROP TABLE IF EXISTS readers""")


for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()
