import sqlite3

DB_FILE = "clientes.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    conn.commit()
    conn.close()
