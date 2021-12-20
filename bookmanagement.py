import sqlite3

def get_cursor():
    conn = sqlite3.connect("library.db")
    return conn.cursor()

def select_category(cursor):
    sql = 'SELECT Title, Author, ISBN FROM Book WHERE Romantic=1'
    cursor.execute(sql)
    print("\nHere is a listing of the rows in the table\n")
    for row in cursor.execute("SELECT rowid, Title, Author, ISBN FROM Book"):
        print(row)
