import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="Library Management System",
    user="postgres",
    password="(same as ur pgadmin)",
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

def delete_book(book_id):
    cursor = conn.cursor()
    # Delete the book
    cursor.execute("DELETE FROM Books WHERE id = %s", (book_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return f"Book with ID {book_id} has been deleted successfully."
    
def update_book(book_id, title=None, author_id=None, genre=None, availability=None):
    cursor = conn.cursor()
    update_fields = []
    params = []
    
    if title:
        update_fields.append("title = %s")
        params.append(title)
    if author_id:
        update_fields.append("author_id = %s")
        params.append(author_id)
    if genre:
        update_fields.append("genre = %s")
        params.append(genre)
    if availability is not None:
        update_fields.append("availability = %s")
        params.append(availability)

    # Ensure there is something to update
    if not update_fields:
        return "No fields to update."

    query = f"UPDATE Books SET {', '.join(update_fields)} WHERE id = %s"
    params.append(book_id)

    cursor.execute(query, tuple(params))
    conn.commit()

    cursor.close()
    conn.close()
    return f"Book with ID {book_id} has been updated successfully."

# To Update Author
def update_author(author_id, name=None, country=None):
    cursor = conn.cursor()
    update_fields = []
    params = []
    if name:
        update_fields.append("name = %s")
        params.append(name)
    if country:
        update_fields.append("country = %s")
        params.append(country)

    if not update_fields:
        return "No fields to update."

    query = f"UPDATE Authors SET {', '.join(update_fields)} WHERE id = %s"
    params.append(author_id)
    cursor.execute(query, tuple(params))
    conn.commit()
    cursor.close()
    conn.close()
    return f"Author with ID {author_id} has been updated successfully."

#To Delete Author
def delete_author(author_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Authors WHERE id = %s", (author_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return f"Author with ID {author_id} has been deleted successfully."

#To Update Borrower
def update_borrower(borrower_id, name=None, contact=None):
    cursor = conn.cursor()
    update_fields = []
    params = []
    if name:
        update_fields.append("name = %s")
        params.append(name)
    if contact:
        update_fields.append("contact = %s")
        params.append(contact)
    if not update_fields:
        return "No fields to update."

    query = f"UPDATE Borrowers SET {', '.join(update_fields)} WHERE id = %s"
    params.append(borrower_id)

    cursor.execute(query, tuple(params))
    conn.commit()

    cursor.close()
    conn.close()
    return f"Borrower with ID {borrower_id} has been updated successfully."

# To Delete Borrower
def delete_borrower(borrower_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Borrowers WHERE id = %s", (borrower_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return f"Borrower with ID {borrower_id} has been deleted successfully."

# Close the connection
def close_connection():
    cursor.close()
    conn.close()

# Example usage
if __name__ == '__main__':
    # Example:Add a new book

    # add_author('A019','Vikram Seth','India')
    # books = get_available_books()
    # print("Available Books:", books)
    
#Example: To Update Book
#     message = update_book(
#     book_id="B011",
#     title="New Title",
#     author_id="A011",
#     genre="Science Fiction",
#     availability=True
# )
#     print(message)
    close_connection() 
