# This file contains all the functions used to link the administrative interface and the database 'Bookstore'

# Connection to the database

from myconnection import get_connection

connection = get_connection()
print("Connection successful!")


#### Summary view of book list
def book_summary():
    cursor = connection.cursor()
    sql = "select B_ID, B_TITLE, A_FNAME, A_LNAME, B_PUBLISHER, B_PUB_DATE, " \
          "B_SUBJECT, B_UNIT_PRIZE, B_STOCK from Books, Authors where B_A_ID = A_ID"

    cursor.execute(sql)
    books = cursor.fetchall()

    cursor.close()

    return books

    # for book in books: print(book[0])


#### Display book details of the book with ID 'id'
def book_details(b_id):
    cursor = connection.cursor()
    sql = "select B_TITLE, A_FNAME, A_LNAME, B_PUBLISHER, B_PUB_DATE, " \
          "B_SUBJECT, B_UNIT_PRIZE, B_STOCK  from Books, Authors where B_ID = %s"

    cursor.execute(sql, (b_id))
    books = cursor.fetchone()

    cursor.close()

    return books

#### Get the list of authors from the Bookstore
def authors_list():
    cursor = connection.cursor()
    sql = "select * from Authors"

    cursor.execute(sql)
    authors = cursor.fetchall()

    cursor.close()

    return authors

##### Add author in database
def add_author(author_fn, author_ln):
    cursor = connection.cursor()
    sql_insert_author = "insert into Authors (A_FNAME, A_LNAME) values (%s,%s)"

    cursor.execute(sql_insert_author, (author_fn, author_ln))

    cursor.close()

##### Add book in database
def add_book(title, author_id, publisher, pub_date, subject, unit_prize, qt_stock):
    cursor = connection.cursor()

    sql_insert_book = "insert into Books (B_TITLE, B_A_ID, B_PUBLISHER, B_PUB_DATE, " \
                      "B_SUBJECT, B_UNIT_PRIZE, B_STOCK) values (%s,%s,%s,%s,%s,%s,%s)"

    arguments = (title, author_id, publisher, pub_date, subject, unit_prize, qt_stock)
    cursor.execute(sql_insert_book, arguments)

    cursor.close()


##### Edit book details
def edit_book(b_id, title, author_id, publisher, pub_date, subject, unit_prize, qt_stock):
    cursor = connection.cursor()

    sql_update = "update Books set B_TITLE=%s, B_A_ID=%s, B_PUBLISHER=%s, " \
                 "B_PUB_DATE=%s, B_SUBJECT=%s, B_UNIT_PRIZE=%s, B_STOCK=%s " \
                 "where B_ID = %s"
    arguments = (title, author_id, publisher, pub_date, subject, unit_prize, qt_stock, b_id)
    cursor.execute(sql_update, arguments)

    cursor.close()


#### Delete book from database
def delete_book(b_id):
    cursor = connection.cursor()

    sql = "delete from Books where B_ID = %s"
    cursor.execute(sql, (str(b_id)))

    cursor.close()


#### Display summary of bookstore

# Total number of books 
def books_number():
    cursor = connection.cursor()

    sql_books_number = "select * from Books"
    cursor.execute(sql_books_number)

    # books = cursor.fetchall()
    books_count = cursor.rowcount
    print("There are ", books_count, " books in the bookstore")

    cursor.close()

    return books_count


# Number of books per subject
def books_per_area():
    cursor = connection.cursor()
    sql_books_per_area = "select B_SUBJECT as subject, COUNT(*) as number from Books group by B_SUBJECT"
    cursor.execute(sql_books_per_area)

    area = cursor.fetchall()

    cursor.close()

    return area


# Latest and earliest books' publication dates
def books_range_pub_date():
    cursor = connection.cursor()
    sql_range_pub_date = "select min(B_PUB_DATE) as min, max(B_PUB_DATE) as max from Books"
    cursor.execute(sql_range_pub_date)

    book = cursor.fetchone()
    print("Books were published from %s to %s" % (book[0], book[1]))

    cursor.close()

    return book


# Greatest and lowest books' unit prices
def books_range_prices():
    cursor = connection.cursor()
    sql_range_prices = "select min(B_UNIT_PRIZE) as min, max(B_UNIT_PRIZE) as max from Books"
    cursor.execute(sql_range_prices)

    book = cursor.fetchone()
    print("Books cost from %s to %s" % (book[0], book[1]))

    cursor.close()

    return book


# Average books' unit price
def books_average_price():
    cursor = connection.cursor()
    sql_average_price = "select AVG(B_UNIT_PRIZE) as average from Books"
    cursor.execute(sql_average_price)

    book = cursor.fetchone()
    print("The average unit price of a book is ", book[0])

    cursor.close()

    return book[0]


# Commit INSERT, DELETE, UPDATE statements
def validate():
    connection.commit()


# Rollback INSERT, DELETE, UPDATE statements
def cancel():
    connection.rollback()
