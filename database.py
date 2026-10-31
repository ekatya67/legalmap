import sqlite3
import os


db_path = os.path.join(os.path.dirname(__file__), 'legalmap.db')

def connection():
    return sqlite3.connect(db_path)

def init_db():
    con = connection()
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS cases(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_number TEXT NOT NULL,
    title TEXT NOT NULL,
    date_open TEXT,
    category TEXT,
    status TEXT )''')

    con.commit()
    con.close()

def add_case(case_number, title, date_open, category, status):
    con = connection()
    cur = con.cursor()

    cur.execute('''INSERT INTO cases (case_number, title, date_open, category, status) 
    VALUES (?, ?, ?, ?, ?)''', (case_number, title, date_open, category, status))

    con.commit()
    con.close()
    print(f"Дело {case_number} добавлено.")

def cases_date(selected_date):
    con = connection()
    cur = con.cursor()

    rows = cur.execute('''SELECT * FROM cases
    WHERE date_open = ?''', (selected_date,)).fetchall()

    con.close()
    return rows

def delete_case(case_id):
    con = connection()
    cur = con.cursor()

    cur.execute('''DELETE FROM cases
    WHERE id = ?''', (case_id,))

    con.commit()
    con.close()
    print(f"Запись с ID {case_id} удалена.")