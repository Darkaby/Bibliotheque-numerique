from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mybookstore

####### Get author list
def fill_author_ComboBox():
    author_list = []
    author_tuple = mybookstore.authors_list()
    if len(author_tuple) > 0:
     for row in author_tuple:
        author = "{} {} {}".format(row[0], row[1], row[2])
        author_list.append(author)
    return author_list


###################    Open window to add author    ######################
def open_add_author_window():

    # Adding confirmation
    # You have to close all windows, then run the program again to see the changes
    def add_author():
        mybookstore.add_author(author_fn.get(), author_ln.get())

        ans = messagebox.askokcancel('Add book', 'Do you want to add this author?')
        if ans:
            mybookstore.validate()
        else:
            mybookstore.cancel()

    # New window
    add_window = Toplevel()
    add_window.title("Add an auhtor")
    add_window.geometry("300x150")

    # Form
    author_fn_label = Label(add_window, text="Author's first name").grid(row=0, column=0)
    author_fn = Entry(add_window)
    author_fn.grid(row=0, column=1)
    author_ln_label = Label(add_window, text="Author's last name").grid(row=1, column=0)
    author_ln = Entry(add_window)
    author_ln.grid(row=1, column=1)

    # Add book button
    add_button = Button(add_window, text="Confirm", command=add_author).grid(row=2, column=1, columnspan=2)


###################    Open window to add book    ######################
def open_add_book_window():

    # Adding confirmation
    # You have to close all windows, then run the program again to see the changes
    def add_book():
        author_text = author.get()
        a_id, fname, lname = author_text.split()

        mybookstore.add_book(title.get(), a_id,
                 publisher.get(), pub_date.get(), subject.get(),
                 unit_prize.get(), qt_stock.get())

        ans = messagebox.askokcancel('Add book', 'Do you want to add this book?')
        if ans:
            mybookstore.validate()
        else:
            mybookstore.cancel()

    # New window
    add_window = Toplevel()
    add_window.title("Add a book")
    add_window.geometry("300x300")

    author_list = fill_author_ComboBox()

    # Form
    title_label = Label(add_window, text="Title").grid(row=0, column=0)
    title = Entry(add_window)
    title.grid(row=0, column=1)
    author_label = Label(add_window, text="Author").grid(row=1, column=0)
    author = ttk.Combobox(add_window, state='readonly', values=author_list)
    author.grid(row=1, column=1)
    author.current(0)
    publisher_label = Label(add_window, text="Publisher").grid(row=2, column=0)
    publisher = Entry(add_window)
    publisher.grid(row=2, column=1)
    pub_date_label = Label(add_window, text="Publication date").grid(row=3, column=0)
    pub_date = Entry(add_window)
    pub_date.grid(row=3, column=1)
    subject_label = Label(add_window, text="Subject").grid(row=4, column=0)
    subject = Entry(add_window)
    subject.grid(row=4, column=1)
    unit_prize_label = Label(add_window, text="Unit prize").grid(row=5, column=0)
    unit_prize = Entry(add_window)
    unit_prize.grid(row=5, column=1)
    qt_stock_label = Label(add_window, text="Quantity in stock").grid(row=6, column=0)
    qt_stock = Entry(add_window)
    qt_stock.grid(row=6, column=1)

    # Add book button
    add_button = Button(add_window, text="Confirm", command=add_book).grid(row=7, column=0, columnspan=2)


################# Open window to edit book details #####################
def open_edit_window(b_id):

    # New window
    edit_window = Toplevel()
    edit_window.title("Edit book details")
    edit_window.geometry("300x300")

    # Adding confirmation
    # You have to close all windows, then run the program again to see the changes
    def edit_book():

        author = author_entry.get()
        a_id, fname, lname = author.split()

        mybookstore.edit_book(book[0], title_entry.get(), a_id,
                  publisher_entry.get(), pub_date_entry.get(),
                  subject_entry.get(), unit_prize_entry.get(),
                  qt_stock_entry.get())

        ans = messagebox.askokcancel('Edit book', 'Do you want to edit this book?')
        if ans:
            mybookstore.validate()
        else:
            mybookstore.cancel()


    # Variables
    title = StringVar()
    author = StringVar()
    publisher = StringVar()
    pub_date = StringVar()
    subject = StringVar()
    unit_prize = StringVar()
    qt_stock = StringVar()

    # Set variables
    book = book_summary_list.get(b_id)
    title.set(book[1])
    publisher.set(book[4])
    pub_date.set(book[5])
    subject.set(book[6])
    unit_prize.set(book[7])
    qt_stock.set(book[8])

    author_list = fill_author_ComboBox()

    # Form
    title_label = Label(edit_window, text="Title").grid(row=0, column=0)
    title_entry = Entry(edit_window, textvariable=title)
    title_entry.grid(row=0, column=1)
    author_label = Label(edit_window, text="Author").grid(row=1, column=0)
    author_entry = ttk.Combobox(edit_window, state='readonly', values=author_list)
    author_entry.grid(row=1, column=1)
    author_entry.current(0)
    publisher_label = Label(edit_window, text="Publisher").grid(row=2, column=0)
    publisher_entry = Entry(edit_window, textvariable=publisher)
    publisher_entry.grid(row=2, column=1)
    pub_date_label = Label(edit_window, text="Publication date").grid(row=3, column=0)
    pub_date_entry = Entry(edit_window, textvariable=pub_date)
    pub_date_entry.grid(row=3, column=1)
    subject_label = Label(edit_window, text="Subject").grid(row=4, column=0)
    subject_entry = Entry(edit_window, textvariable=subject)
    subject_entry.grid(row=4, column=1)
    unit_prize_label = Label(edit_window, text="Unit prize").grid(row=5, column=0)
    unit_prize_entry = Entry(edit_window, textvariable=unit_prize)
    unit_prize_entry.grid(row=5, column=1)
    qt_stock_label = Label(edit_window, text="Quantity in stock").grid(row=6, column=0)
    qt_stock_entry = Entry(edit_window, textvariable=qt_stock)
    qt_stock_entry.grid(row=6, column=1)

    # Add book button
    add_button = Button(edit_window, text="Confirm", command=edit_book).grid(row=7, column=0, columnspan=2)


################  Open window to show book details  ####################
def open_details_window(b_id):
    # New window
    details_window = Toplevel()
    details_window.title("Book details")
    details_window.geometry("300x300")

    # Variables
    title = StringVar()
    author_text = StringVar()
    publisher = StringVar()
    pub_date = StringVar()
    subject = StringVar()
    unit_prize = StringVar()
    qt_stock = StringVar()


    # Form
    title_label = Label(details_window, text="Title").grid(row=0, column=0)
    title_entry = Label(details_window, textvariable=title).grid(row=0, column=1)
    author_text_label = Label(details_window, text="Author").grid(row=1, column=0)
    author_text_entry = Label(details_window, textvariable=author_text).grid(row=1, column=1)
    publisher_label = Label(details_window, text="Publisher").grid(row=2, column=0)
    publisher_entry = Label(details_window, textvariable=publisher).grid(row=2, column=1)
    pub_date_label = Label(details_window, text="Publication date").grid(row=3, column=0)
    pub_date_entry = Label(details_window, textvariable=pub_date).grid(row=3, column=1)
    subject_label = Label(details_window, text="Subject").grid(row=4, column=0)
    subject_entry = Label(details_window, textvariable=subject).grid(row=4, column=1)
    unit_prize_label = Label(details_window, text="Unit prize").grid(row=5, column=0)
    unit_prize_entry = Label(details_window, textvariable=unit_prize).grid(row=5, column=1)
    qt_stock_label = Label(details_window, text="Quantity in stock").grid(row=6, column=0)
    qt_stock_entry = Label(details_window, textvariable=qt_stock).grid(row=6, column=1)

    # Set labels
    global book
    book = book_summary_list.get(b_id)
    author = "%s %s " % (book[2], book[3])

    title.set(book[1])
    author_text.set(author)
    publisher.set(book[4])
    pub_date.set(book[5])
    subject.set(book[6])
    unit_prize.set(book[7])
    qt_stock.set(book[8])


############## Define what happens when a book is selected #############

#### Select a book in the listbox
def get_book_selected(event):

    # Delete confirmation
    def delete_book(b_id):
        book = book_summary_list.get(b_id)
        mybookstore.delete_book(book[0])

        ans = messagebox.askokcancel('Delete book', 'Are you sure you want to delete this book?')
        if ans:
            mybookstore.validate()
        else:
            mybookstore.cancel()

    # Get book ID selected
    index = book_summary_list.curselection()
    #open_details_window(index)

    # Open a new window
    what_to_do_window = Toplevel()
    what_to_do_window.title("What to do?")
    what_to_do_window.geometry("250x50")

    # To show book details
    show_button = Button(what_to_do_window, text="Show details", command=lambda :open_details_window(index))
    show_button.pack(side=LEFT)

    # To edit book details
    edit_button = Button(what_to_do_window, text="Edit", command=lambda :open_edit_window(index))
    edit_button.pack(side=LEFT)

    # To delete a book
    delete_button = Button(what_to_do_window, text="Delete", command=lambda :delete_book(index))
    delete_button.pack(side=LEFT)


#####################        Main window         #######################

home = Tk()
home.title("Bookstore")
home.geometry("800x500")

title = Label(home, text="Home", font=14).grid(row=0, column=0, columnspan=5)

#### Summary of books: Listbox
#book_summary = Label(home, text="Books", font=(4)).grid(row=1, column=0)

book_summary_frame = LabelFrame(home, text="Book summary", font=(4), width=400, height=400).grid(row=1, column=0, columnspan=2, rowspan=7)

book_summary_list = Listbox(book_summary_frame, height=10, width=50)
book_summary_list.grid(row=2, column=0, rowspan=6, columnspan=2)

for book in mybookstore.book_summary(): # Fill with list of books from database
    book_summary_list.insert(END, book)

scrollbar = Scrollbar(book_summary_frame)
scrollbar.configure(command=book_summary_list.yview)

# Bind 'get_book_selected' function event to the listbox
book_summary_list.bind('<<ListboxSelect>>', get_book_selected)

#### Summary of bookstore
bookstore_summary_frame = LabelFrame(home, text="Bookstore summary", font=(4), width=400, height=400).grid(row=1, column=2, columnspan=3, rowspan=7)

# Variables
books_number = StringVar()
books_per_area = StringVar()
books_range_pub_date_min = StringVar()
books_range_pub_date_max = StringVar()
books_range_prices_min = StringVar()
books_range_prices_max = StringVar()
books_average_price = StringVar()

# Form
books_number_label = Label(bookstore_summary_frame, text="Total number of books: ").grid(row=2, column=2)
books_number_entry = Label(bookstore_summary_frame, textvariable=books_number).grid(row=2, column=3, columnspan=2)

books_range_pub_date_label = Label(bookstore_summary_frame, text="Range of publication dates: ").grid(row=3, column=2)
books_range_pub_date_min_entry = Label(bookstore_summary_frame, textvariable=books_range_pub_date_min).grid(row=3,
                                                                                                            column=3)
books_range_pub_date_max_entry = Label(bookstore_summary_frame, textvariable=books_range_pub_date_max).grid(row=3,
                                                                                                            column=4)

books_range_prices_label = Label(bookstore_summary_frame, text="Range of unit prices: ").grid(row=4, column=2)
books_range_prices_min_entry = Label(bookstore_summary_frame, textvariable=books_range_prices_min).grid(row=4, column=3)
books_range_prices_max_entry = Label(bookstore_summary_frame, textvariable=books_range_prices_max).grid(row=4, column=4)

books_average_price_label = Label(bookstore_summary_frame, text="Average unit price: ").grid(row=5, column=2)
books_average_price_entry = Label(bookstore_summary_frame, textvariable=books_average_price).grid(row=5, column=3, columnspan=2)

books_per_area_label = Label(bookstore_summary_frame, text="Number of books per subject").grid(row=6, column=2)
books_per_area_entry = Listbox(bookstore_summary_frame, width=30)
books_per_area_entry.grid(row=6, column=3, columnspan=2)

# Set labels
books_number.set(mybookstore.books_number())

book_pub_date = mybookstore.books_range_pub_date()
books_range_pub_date_min.set(book_pub_date[0])
books_range_pub_date_max.set(book_pub_date[1])

book_prices = mybookstore.books_range_prices()
books_range_prices_min.set(book_prices[0])
books_range_prices_max.set(book_prices[1])

books_average_price.set(mybookstore.books_average_price())

subjects = mybookstore.books_per_area()  # Fill with list of books per area from database
for subject in subjects:
    subject_statistic = "{} : {} books".format(subject[0], subject[1])
    books_per_area_entry.insert(END, subject_statistic)

#### Buttons to add a new book and a new author
add_button = Button(home, text="Add author", command=open_add_author_window, ).grid(row=9, column=0, columnspan=2)
add_button = Button(home, text="Add book", command=open_add_book_window, ).grid(row=9, column=2, columnspan=3)

home.mainloop()
