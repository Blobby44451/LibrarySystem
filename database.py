import sqlite3

DB_NAME = "library.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()
    with open("schema.sql", "r") as f:
        sql = f.read()
    cursor.executescript(sql)
    conn.commit()
    conn.close()
    print("Database initialized.")