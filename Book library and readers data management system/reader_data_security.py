import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()

# Create the user table
c.execute('''CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)''')

# Insert sample data
sample_users = [
    ('john_doe', 'password123'),
    ('jane_smith', 'password456'),
    ('alice_johnson', 'password789'),
    ('bob_brown', 'password101'),
    ('charlie_davis', 'password202'),
    ('david_wilson', 'password303')
    
]

c.executemany("INSERT INTO user (username, password) VALUES (?, ?)", sample_users)
conn.commit()

# Get user input
inp_username = input("Enter username: ")
inp_password = input("Enter password: ")

# Query with parameterized statement (safe from SQL injection)
with conn:
    c.execute("SELECT * FROM user WHERE username = ? AND password = ?", (inp_username, inp_password))
    res = c.fetchall()
    if res:
        print("Reader profile data is:")
        print(res)
    else:
        print(f"Reader {inp_username} does not exist or incorrect password")

conn.close()