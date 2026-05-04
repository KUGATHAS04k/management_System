import sqlite3

def create_connection():
    conn = sqlite3.connect('restaurant.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cash REAL,
        card REAL,
        uber REAL,
        date TEXT,
        shift TEXT,
        staff_id TEXT
    )
    """)

    conn.commit()
    conn.close()