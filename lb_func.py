import sqlite3

conn = sqlite3.connect('lb_data.db', check_same_thread=False)
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS books(book_name TEXT,author TEXT,available TEXT)')


def add_data(book, author, available):
    c.execute('INSERT INTO books(book_name,author,available) VALUES (?,?,?)',
              (book, author, available))
    conn.commit()


def view_all_data():
    c.execute('SELECT * FROM books')
    data = c.fetchall()
    return data