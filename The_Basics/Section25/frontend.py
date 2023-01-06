from tkinter import *
import backend


def view_command():

    list1.delete(0, END)
    try:
        for book in backend.view():
            list1.insert(
                END, f"{book[0]}: '{book[1]}' by {book[2]} - ISBN: {book[3]}")
    except:
        list1.insert(END, "No books found! Please add books.")


def search_command():
    list1.delete(0, END)
    temp_book_list = backend.search(
        title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    if len(temp_book_list) == 0:
        list1.insert(END, "Book not found!")

    else:
        for book in temp_book_list:
            list1.insert(
                END, f"{book[0]}: '{book[1]}' by {book[2]} - ISBN: {book[3]}")


def add_entry_command():
    list1.delete(0, END)

    title_txt = title_text.get().strip()
    author_txt = author_text.get().strip()
    year_txt = year_text.get().strip()
    isbn_txt = isbn_text.get().strip()

    try:
        backend.validate_add_entry(title_text, author_txt, year_txt, isbn_txt)

        backend.insert(title_text, author_txt, year_txt, isbn_txt)
        list1.insert(END, "Entry successfully addded.")
    except ValueError as e:
        list1.insert(END, e)


window = Tk()
backend.connect()

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l1 = Label(window, text="Author")
l1.grid(row=0, column=2)

l1 = Label(window, text="Year")
l1.grid(row=1, column=0)

l1 = Label(window, text="ISBN")
l1.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)


sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1 = Listbox(window, height=6, width=35, yscrollcommand=sb1.set)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1.configure(command=list1.yview)

b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12, command=add_entry_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
