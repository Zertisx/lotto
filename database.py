import sqlite3

def setup_database():
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


def find_or_create_user(username):
    conn = sqlite3.connect('lotto.db')
    c = conn.cursor()
    c.execute("SELECT id FROM users where username = ?", (username,))
    result = c.fetchone()
    if result is None:
        c.execute("INSERT INTO users(username) VALUES (?)", (username,))
        user_id = c.lastrowid
    else:
        user_id = result[0]
    conn.commit()
    conn.close()
    return user_id


if __name__ == '__main__':
    setup_database()