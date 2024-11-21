import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="Library Management System",
    user="postgres",
    password="k123456789ch",
    host="127.0.0.1",
    port="5433"
)
cursor = conn.cursor()

# Add a new book
def add_book(id, title, author_id, genre, availability):
    cursor.execute("INSERT INTO books (id, title, author_id, genre, availability) VALUES (%s, %s, %s, %s, %s)",
                   (id, title, author_id, genre, availability))
    conn.commit()

# Add a new author
def add_author(id, name, country):
    cursor.execute("INSERT INTO authors (id, name, country) VALUES (%s, %s, %s)", (id, name, country))
    conn.commit()

# Add a new borrower
def add_borrower(id, name, contact):
    cursor.execute("INSERT INTO borrowers (id, name, contact) VALUES (%s, %s, %s)", (id, name, contact))
    conn.commit()

# Borrow a book
def borrow_book(book_id, borrower_id, borrow_date, return_date):
    cursor.execute("INSERT INTO borrowed_books (book_id, borrower_id, borrow_date, return_date) VALUES (%s, %s, %s, %s)",
                   (book_id, borrower_id, borrow_date, return_date))
    cursor.execute("UPDATE books SET availability = %s WHERE id = %s", ('f', book_id)) 
    conn.commit()

# Return a book
def return_book(book_id, borrower_id):
    cursor.execute("DELETE FROM borrowed_books WHERE book_id = %s AND borrower_id = %s", (book_id, borrower_id))
    cursor.execute("UPDATE books SET availability = %s WHERE id = %s", ('t', book_id)) 
    conn.commit()

# Get available books
def get_available_books():
    cursor.execute("SELECT * FROM books WHERE availability = 't'")
    return cursor.fetchall()

# Close the connection
def close_connection():
    cursor.close()
    conn.close()

# Example usage
if __name__ == '__main__':
    # Example: Add a new book
    # add_author('A019','Vikram Seth','India')
    # books = get_available_books()
    # print("Available Books:", books)
    close_connection()
