import sqlite3

def get_status(status="default"):
    return status


def connect():
    connect = sqlite3.connect("bookstore.db")
    cursor = connect.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year INTEGER, isbn INTEGER)")
    connect.commit()
    connect.close()


def insert(title, author, year, isbn):
    connect = sqlite3.connect("bookstore.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, ?)",
                   (title, author, year, isbn))
    connect.commit()
    connect.close()


def view():
    connect = sqlite3.connect("bookstore.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    connect.close()

    print("\nBook List \n")
    for row in rows:
        print(row)

    return rows


def search(title="", author="", year="", isbn=""):
    connect = sqlite3.connect("bookstore.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",
                   (title, author, year, isbn))
    rows = cursor.fetchall()
    connect.close()

    print("\nSearch Result/s \n")
    for row in rows:
        print(row)

    return rows

def delete(id):
    connect = sqlite3.connect("bookstore.db")
    cursor = connect.cursor()
    cursor.execute("DELETE FROM books WHERE id=?",(id,))
    connect.commit()
    connect.close()
    

def update(id, title, author, year, isbn):
    connect = sqlite3.connect("bookstore.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn, id))
    connect.commit()
    connect.close()
    
    
def validate_add_entry(title, author, year, isbn):
    if title == "" or author == "" or year == "" or isbn == "":
        raise ValueError("Please provide complete details.")
    
# connect()
# #insert("The Sky", "Doe Doe", 1920, 6545644123)
# view()
# # delete(1)
# # search(author="John Doe")
# update(3, 'The Moon', 'John Doe', 2023, 315456168)
# view()

# for i in range(25):
#     insert("The Sky", "Doe Doe", 1920, 6545644123)
# view()
