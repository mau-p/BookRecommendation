import sqlite3


def get_cursor():
    conn = sqlite3.connect("library.db")
    return conn.cursor()

# returns Title, Author and ISBN of all books given a category
def select_category(cursor, category):
    sql = f"SELECT Title, Author FROM Book WHERE {category}=1"
    cursor.execute(sql)
    return cursor.fetchall()

# returns Title, Author of all books fitting the demographic criteria. 
def filter_demographics(cursor, age, gender, reading_level):
    sql = f"SELECT Title, Author from Book WHERE \
        Age <= {age} AND (Gender = '{gender}' OR Gender = 'A') AND ReadingLevel <= {reading_level}"
    cursor.execute(sql)
    return cursor.fetchall()
