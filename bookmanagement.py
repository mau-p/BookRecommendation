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
def filter_demographics(cursor, age, gender):
    sql = f"SELECT ID from Book WHERE \
        Age <= {age} AND (Gender = '{gender}' OR Gender = 'A')"
    cursor.execute(sql)
    return cursor.fetchall()

def get_properties(cursor, ID):
    sql = f"SELECT Gender, Age, ReadingLevel, Entertaining, Romantic, Historic, FeelGood, Funny, Gripping, Sad, Social \
        from BOOK Where ID = {ID}"
    cursor.execute(sql)
    return list(cursor.fetchone())

def get_book(cursor, ID):
    sql = f"SELECT Title, Author, Summary from BOOK Where ID = {ID}"
    cursor.execute(sql)
    return list(cursor.fetchone())
