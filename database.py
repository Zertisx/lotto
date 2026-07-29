import sqlite3

conn = sqlite3.connect('lotto.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL
    )
''')
c.execute('''
    CREATE TABLE IF NOT EXISTS play (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        player_numbers TEXT,
        winning_numbers TEXT,
        prize INTEGER,
        played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
''')


conn.commit()
conn.close()
