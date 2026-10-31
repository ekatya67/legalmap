import sqlite3
import os


db_path = os.path.join(os.path.dirname(__file__), 'legalmap.db')

def connection():
    return sqlite3.connect(db_path)

def init_db():
    con = connection()
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS cases(
    id INTEGER PRIMARY KEY AUTOINCERENT,
    case_number TEXT NOT NULL,
    title TEXT NOT NULL,
    date_open TEXT,
    category TEXT,
    status TEXT )''')
    
    con.commit()
    con.close()