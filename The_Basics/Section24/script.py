import sqlite3


def create_table():
    connect = sqlite3.connect("lite.db")    # create a database connection if is not existing
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)")
    connect.commit()
    connect.close()

def insert(item, quantity, price):
    connect = sqlite3.connect("lite.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO store(item, quantity, price) VALUES(?, ?, ?)", (item, quantity, price))
    connect.commit()
    connect.close()

def view():
    connect = sqlite3.connect("lite.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM store")
    rows=cursor.fetchall()
    connect.close()
    
    for row in rows:
        print(row)
        
    return rows

view()
