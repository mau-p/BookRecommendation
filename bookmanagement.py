import sqlite3

def get_cursor():
    conn = sqlite3.connect("library.db")
    return conn.cursor()

# returns title, auther and ISBN of all books given a category
def select_category(cursor, category):
    sql = f'SELECT Title, Author, ISBN FROM Book WHERE {category}=1;'
    cursor.execute(sql)
    return cursor.fetchall()