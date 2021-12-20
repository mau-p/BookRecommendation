import bookmanagement

def main():
    cursor = bookmanagement.get_cursor()
    bookmanagement.select_category(cursor)




if __name__=='__main__':
    main()