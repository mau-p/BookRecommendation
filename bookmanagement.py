import sqlite3


def get_cursor():
    conn = sqlite3.connect("library.db")
    return conn.cursor()

# Returns all properties of a book given an ID
def get_properties(cursor, ID):
    sql = f"SELECT Gender, Age, ReadingLevel, Entertaining, Suspense, Romantic, \
        Historic, FeelGood, Funny, Gripping, Sad, Social from BOOK Where ID = {ID}"
    cursor.execute(sql)
    return list(cursor.fetchone())

# Returns Title, Author, ISBN and Summary of book given an ID
def get_book(cursor, ID):
    sql = f"SELECT Title, Author, ISBN, Summary from BOOK Where ID = {ID}"
    cursor.execute(sql)
    return list(cursor.fetchone())

def count_books(cursor):
    sql = f"SELECT COUNT(*) FROM Book"
    cursor.execute(sql)
    return int(cursor.fetchone()[0])
