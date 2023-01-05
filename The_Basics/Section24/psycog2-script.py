import psycopg2


def create_table():
    # create a database connection if is not existing
    connect = psycopg2.connect(
        "dbname='database1' user='postgres' password='superuser' host='localhost' port='5432'")
    cursor = connect.cursor()
    cursor.execute(
        "CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)")
    connect.commit()
    connect.close()


def insert(item, quantity, price):
    # create a database connection if is not existing
    connect = psycopg2.connect(
        "dbname='database1' user='postgres' password='superuser' host='localhost' port='5432'")
    cursor = connect.cursor()
    # cursor.execute("INSERT INTO store(item, quantity, price) VALUES(?, ?, ?)", (item, quantity, price))   #using sqlite3
    # cursor.execute(
    #     "INSERT INTO store(item, quantity, price) VALUES('%s', '%s', '%s')" % (item, quantity, price))  # vulnerable to SQL injection postgres
    cursor.execute(
        "INSERT INTO store(item, quantity, price) VALUES(%s, %s, %s)", (item, quantity, price))  # vulnerable to SQL injection postgres
    connect.commit()
    connect.close()


def view():
    # create a database connection if is not existing
    connect = psycopg2.connect(
        "dbname='database1' user='postgres' password='superuser' host='localhost' port='5432'")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    connect.close()

    for row in rows:
        print(row)

    return rows


def remove(item):
    # create a database connection if is not existing
    connect = psycopg2.connect(
        "dbname='database1' user='postgres' password='superuser' host='localhost' port='5432'")
    cursor = connect.cursor()
    cursor.execute(
        "DELETE FROM store WHERE item=%s", (item,))
    connect.commit()
    connect.close()


def update(item, quantity, price):
    # create a database connection if is not existing
    connect = psycopg2.connect(
        "dbname='database1' user='postgres' password='superuser' host='localhost' port='5432'")
    cursor = connect.cursor()
    cursor.execute(
        "UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    connect.commit()
    connect.close()


remove('Apple')
