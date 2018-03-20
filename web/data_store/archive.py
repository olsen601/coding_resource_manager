import sqlite3

global archiveDB
global cursor

def db_setup():

    global archiveDB
    global cursor

    archiveDB = sqlite3.connect('data_store/archive.db')

    cursor = archiveDB.cursor()

    cursor.execute('create table if not exists bookmarks (source text, title text, link text)')

    archiveDB.commit();

def db_add(source, title, link):

    global archiveDB
    global cursor

    try:
        cursor.execute('insert into bookmarks values (?, ?, ?)', (source, title, link))
        archiveDB.commit()
    except Exception as e:
        print('Error ', e)

def db_data():

    global archiveDB
    global cursor

    book_dict = {}
    i = 0

    try:
        bookmarks = cursor.execute('select * from bookmarks').fetchall()
        for book in bookmarks:
            book_dict.update({('index'+str(i)): {'source': book[0], 'title': book[1], 'link': book[2]}})
            i += 1

    except Exception as e:
        print('Error ', e)

    return book_dict

def db_shutdown():

    global archiveDB

    archiveDB.close()
