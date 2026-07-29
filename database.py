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

def save_play(username, player_numbers, winning_numbers, prize):
    user_id = find_or_create_user(username)
    conn = sqlite3.connect('lotto.db')
    c = conn.cursor()
    player_str = ",".join(str(n) for n in player_numbers)
    winning_str = ",".join(str(n) for n in winning_numbers)
    c.execute("INSERT INTO play (user_id, player_numbers, winning_numbers, prize) VALUES (?, ?, ?, ?)", (user_id, player_str, winning_str, prize))
    conn.commit()
    conn.close()

def get_history(username):
    user_id = find_or_create_user(username)
    conn = sqlite3.connect('lotto.db')
    c = conn.cursor()
    c.execute("SELECT player_numbers, winning_numbers, prize, played_at FROM play WHERE user_id = ? ORDER BY played_at DESC", (user_id,))
    rows = c.fetchall()
    history = []
    for row in rows:
        player_list = [int(n) for n in row[0].split(",")]
        winning_list = [int(n) for n in row[1].split(",")]
        history.append((player_list, winning_list, row[2], row[3]))
    conn.close()
    return history

def get_stats(username):
    user_id = find_or_create_user(username)
    conn = sqlite3.connect('lotto.db')
    c = conn.cursor()   
    c.execute("SELECT COUNT(*), SUM(prize) FROM play WHERE user_id = ?", (user_id,))
    stats = c.fetchone()
    count, total = stats
    if total is None:
        total = 0
    conn.close()
    return (count, total)

if __name__ == '__main__':
    setup_database()