import bookmanagement

def main():
    cursor = bookmanagement.get_cursor()
    bookmanagement.select_category(cursor, 'romantic')




if __name__=='__main__':
    main()