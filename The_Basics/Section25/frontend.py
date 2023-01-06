from tkinter import *
import backend


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():

    list1.delete(0, END)
    try:
        temp_book_list = backend.view()
        if len(temp_book_list) == 0:
            list1.insert(END, "No books found! Please add books.")

        else:
            for book in temp_book_list:
                # list1.insert(
                #     END, f"{book[0]}: '{book[1]}' by {book[2]} ({book[3]}) - ISBN: {book[4]}")
                list1.insert(
                    END, (book[0], book[1], book[2], book[3], book[4]))
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
                END, (book[0], book[1], book[2], book[3], book[4]))


def add_entry_command():
    list1.delete(0, END)

    title_txt = title_text.get().strip()
    author_txt = author_text.get().strip()
    year_txt = year_text.get().strip()
    isbn_txt = isbn_text.get().strip()

    try:
        backend.validate_add_entry(title_txt, author_txt, year_txt, isbn_txt)

        backend.insert(title_txt, author_txt, year_txt, isbn_txt)
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        list1.insert(END, "Entry successfully addded.")
    except ValueError as e:
        list1.insert(END, e)


def delete_command():
    backend.delete(selected_tuple[0])
    list1.delete(0, END)
    list1.insert(END, "Selected book deleted.")


def update_command():
    backend.update(selected_tuple[0], title_text.get(
    ), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, "Entry updated.")


def entry_converter(id, title, author, year, isbn):
    def to_string():
        return f"{id}: '{title}' by {author} ({year}) - ISBN: {isbn}"


window = Tk()
backend.connect()

window.wm_title("Bookstore")
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

sb2 = Scrollbar(window, orient='horizontal')
sb2.grid(row=7, column=0, columnspan=2)

list1 = Listbox(window, height=6, width=35,
                xscrollcommand=sb2.set, yscrollcommand=sb1.set)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1.configure(command=list1.yview)
sb2.configure(command=list1.xview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12, command=add_entry_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
