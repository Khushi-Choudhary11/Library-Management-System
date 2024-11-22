from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = "lib123"


# Database connection helper
def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="Library Management System",
            user="postgres",
            password="k123456789ch",
            host="127.0.0.1",
            port="5433"
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"Database connection error: {e}")
        return None


# Route: Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Route: Add new Author
@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        author_id = request.form.get('id')
        name = request.form.get('name')
        country = request.form.get('country')

        try:
            # Connect to the database
            conn = get_db_connection()
            cursor = conn.cursor()

            # Insert into Authors table
            cursor.execute(
                """
                INSERT INTO Authors (id, name, country)
                VALUES (%s, %s, %s)
                """,
                (author_id, name, country)
            )

            # Commit the transaction
            conn.commit()
            cursor.close()
            conn.close()

            return redirect(url_for('view_authors'))  # Redirect to authors list page

        except Exception as e:
            return f"Error: {str(e)}"

    return render_template('add_author.html')

# Route: View authors
@app.route('/view_author')
def view_authors():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query to fetch all authors
        cursor.execute("SELECT * FROM Authors")
        authors = cursor.fetchall()

        cursor.close()
        conn.close()

        return render_template('view_authors.html', authors=authors)
    except Exception as e:
        return f"Error: {str(e)}"

# Route: View Available Books
@app.route('/view_books')
def view_books():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Books WHERE availability = TRUE")
        books = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('view_books.html', books=books)
    except Exception as e:
        return f"Error: {str(e)}"

# Route: Borrow Book
@app.route('/borrow', methods=['GET', 'POST'])
def borrow_book():
    if request.method == 'POST':
        book_id = request.form.get('book_id')
        borrower_id = request.form.get('borrower_id')
        borrow_date = request.form.get('borrow_date')
        return_date = request.form.get('return_date') or None  # Default to None if not specified

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Insert into Borrowed_Books table
            cursor.execute(
                """
                INSERT INTO Borrowed_Books (book_id, borrower_id, borrow_date, return_date)
                VALUES (%s, %s, %s, %s)
                """,
                (book_id, borrower_id, borrow_date, return_date)
            )

            # Update availability in Books table
            cursor.execute("UPDATE Books SET availability = FALSE WHERE id = %s", (book_id,))
            conn.commit()

            cursor.close()
            conn.close()

            return redirect(url_for('view_books'))
        except Exception as e:
            return f"Error: {str(e)}"

    # Fetch list of available books and borrowers for dropdowns
    books = get_books()
    borrowers = get_borrowers()
    current_date = datetime.now().date()

    return render_template('borrow.html', books=books, borrowers=borrowers, current_date=current_date, timedelta=timedelta)

# Route: Return Book
@app.route('/return', methods=['GET', 'POST'])
def return_book():
    if request.method == 'POST':
        book_id = request.form.get('book_id')
        return_date = request.form.get('return_date')

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Update the Borrowed_Books table with the return date
            cursor.execute(
                """
                UPDATE Borrowed_Books
                SET return_date = %s
                WHERE book_id = %s AND return_date IS NULL
                """,
                (return_date, book_id)
            )

            # Set the book's availability to TRUE
            cursor.execute(
                "UPDATE Books SET availability = TRUE WHERE id = %s",
                (book_id,)
            )

            conn.commit()
            cursor.close()
            conn.close()

            return redirect(url_for('view_books'))
        except Exception as e:
            return f"Error: {str(e)}"

    # Fetch list of borrowed books (that haven't been returned yet)
    books = get_borrowed_books()
    current_date = datetime.now().date()

    return render_template('return.html', books=books, current_date=current_date)


# Route: Add Book (for demonstration purposes)
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        book_id=request.form.get('id')
        title = request.form.get('title')
        author_id = request.form.get('author_id')
        genre = request.form.get('genre')
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Books (id, title, author_id, genre, availability) VALUES (%s,%s, %s, %s, TRUE)",
                (book_id, title, author_id, genre)
            )
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('view_books'))
        except Exception as e:
            return f"Error: {str(e)}"
    return render_template('add_book.html')

# Add Borrower Route
@app.route('/add_borrower', methods=['GET', 'POST'])
def add_borrower():
    if request.method == 'POST':
        borrower_id = request.form['id']
        name = request.form['name']
        contact = request.form['contact']
        
        try:
            # Database connection
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Insert query
            cursor.execute(
                """
                INSERT INTO Borrowers (id, name, contact)
                VALUES (%s, %s, %s)
                """,
                (borrower_id, name, contact)
            )
            
            # Commit changes and close connection
            conn.commit()
            cursor.close()
            conn.close()
            
            flash("Borrower added successfully!", "success")
            return redirect(url_for('add_borrower'))
        except psycopg2.Error as e:
            flash(f"An error occurred: {e.pgerror}", "danger")
            return redirect(url_for('add_borrower'))
    
    return render_template('add_borrower.html')

# Route : Weekly Borrow Report
# Route: Weekly Borrow Report
@app.route('/report/weekly')
def weekly_borrow_report():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = """
            SELECT b.title AS book_title, 
                   bo.name AS borrower_name, 
                   bb.borrow_date, 
                   COUNT(bb.book_id) AS borrow_count
            FROM Borrowed_Books bb
            JOIN Books b ON bb.book_id = b.id
            JOIN Borrowers bo ON bb.borrower_id = bo.id
            WHERE bb.borrow_date >= (CURRENT_DATE - INTERVAL '7 days')
            GROUP BY b.id, bo.name, bb.borrow_date
            ORDER BY borrow_count DESC, bb.borrow_date ASC
        """
        cursor.execute(query)
        report_data = cursor.fetchall()

        cursor.close()
        conn.close()

        return render_template('weekly_report.html', report_data=report_data)
    except Exception as e:
        return f"Error: {str(e)}"
    
# Route: help page
@app.route('/help')
def help():
    return render_template('help.html')


# Helper Functions
def get_books():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query to fetch books
        query = "SELECT id, title FROM Books WHERE availability = TRUE"
        cursor.execute(query)
        books = cursor.fetchall()

        cursor.close()
        conn.close()

        return books

    except Exception as e:
        print(f"Error fetching books: {e}")
        return []

def get_borrowers():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query to fetch borrowers
        query = "SELECT id, name FROM Borrowers"
        cursor.execute(query)
        borrowers = cursor.fetchall()

        cursor.close()
        conn.close()

        return borrowers

    except Exception as e:
        print(f"Error fetching borrowers: {e}")
        return []

def get_borrowed_books():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Fetch only borrowed books (not yet returned)
        query = """
        SELECT b.id, b.title
        FROM Books b
        JOIN Borrowed_Books bb ON b.id = bb.book_id
        WHERE bb.return_date IS NULL
        """
        cursor.execute(query)
        books = cursor.fetchall()

        cursor.close()
        conn.close()

        return books
    except Exception as e:
        print(f"Error fetching borrowed books: {e}")
        return []

# Run the application
if __name__ == "__main__":
    app.run(debug=True)

  

  
