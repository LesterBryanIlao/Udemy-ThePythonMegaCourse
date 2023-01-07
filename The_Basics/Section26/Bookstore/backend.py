import sqlite3

class Database:

    def __init__(self, db):
        self.connect = sqlite3.connect(db)
        self.cursor = self.connect.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year INTEGER, isbn INTEGER)")
        self.connect.commit()


    def insert(self, title, author, year, isbn):
        self.cursor.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, ?)",
                    (title, author, year, isbn))
        self.connect.commit()

    def view(self):
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()

        print("\nBook List \n")
        for row in rows:
            print(row)

        return rows

    def search(self, title="", author="", year="", isbn=""):
        self.cursor.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",
                    (title, author, year, isbn))
        rows = self.cursor.fetchall()

        print("\nSearch Result/s \n")
        for row in rows:
            print(row)

        return rows

    def search_by_id(self, id):
        self.cursor.execute("SELECT * FROM books WHERE id=?",
                    (id,))
        rows = self.cursor.fetchall()

        print("\nSearch Result/s \n")
        for row in rows:
            print(row)

        return rows

    def delete(self, id):
        self.cursor.execute("DELETE FROM books WHERE id=?", (id,))
        self.connect.commit()

        
    def update(self, id, title, author, year, isbn):
        self.cursor.execute(
            "UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.connect.commit()

        
    def validate_add_entry(self, title, author, year, isbn):
        if title == "" or author == "" or year == "" or isbn == "":
            raise ValueError("Please provide complete details.")
    
    def __del__(self):
        print("Database connection closed.")
        self.connect.close()

