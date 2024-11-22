# Library Management System(LMS)

## Project Description
The Library Management System is a Python- and PostgreSQL-based application designed to manage library resources efficiently. It provides features for managing books, authors, and borrowers, along with functionalities to handle book borrowing and returning processes. The system also includes reporting features such as generating weekly borrow statistics.

## Features
- Add, update, and delete books, authors, and borrowers.
- Borrow and return books, with automatic availability updates.
- View all available books and borrowed books.
- Generate a weekly report of borrowed books with borrower details.


### Prerequisites
1. Install **Python 3.7+** on your system.
2. Install **PostgreSQL** (I have used PgAdmin 4 and PostgreSQL 14) database and ensure it is running.
3. Install **Git** to clone the repository.

### You are provided with 2 .py files :

## lib.py
This file serves as the core backend for your LMS. It contains all the necessary functions required to perform CRUD operations on the PostgreSQL database. These functions can be directly called to manipulate or query the database, ensuring modularity and reusability.

### Key Features:
CRUD Functions for Each Table:

Functions to add, update, delete, and fetch records from the tables:
- Books: Functions to manage books (e.g., add_book, update_book, delete_book, get_books).
- Authors: Functions to manage authors (e.g., add_author, get_authors).
- Borrowers: Functions to manage borrower information.
- Borrowed_Books: Functions to handle borrowing and returning operations.
EXAMPLE:
```
from lib import add_book, get_available_books

# Adding a new book
add_book("B011", "1984", "A003", "Dystopian Fiction")

# Fetching all available books
books = get_available_books()
print(books)
```


## library_mgmt.py 
This file uses Flask to build a web application interface for the LMS. It provides a user-friendly way to interact with the backend functions.Each route in Flask corresponds to a specific action (e.g., adding books, viewing authors).Web Interface:

### Web Interface:

- Templates: HTML templates in the /templates folder are rendered for each page.
- Routes:
  - Home Page (/): A welcome page with navigation options.
  - Add/View Books, Authors, Borrowers: Forms and tables for managing data.
  - Borrow/Return Books: Interfaces for borrowing and returning books.
  - Weekly Report: Displays the borrowing statistics.




## Dependencies
The project dependencies are listed in the `requirements.txt` file. (Note: requirements.txt not only contains requirements for this project but also some others too so You can skip those). 

### Key Dependencies
- `Flask`: For building the web application.
- `psycopg2`: For connecting to the PostgreSQL database.
- `jinja2`: For template rendering.

### USAGE:
- Run the web app using:
```bash
python library_mgmt.py
```
- Access the app in a browser at http://127.0.0.1:5000/.

## HOW TO USE PROJECT:
- Set up the database using the provided SQL scripts.Ensure PostgreSQL is running.
(NOTE: inside function get_db_connection() remember to use your own **dbname** and **password**   and the rest 3 are same for all users. Also, insert the test_data values into respective table using test_data.csv in PostgreSQL or web app.)
- Install basic needed dependencies .
- Run library_mgmt.py to launch the web app.
- Use the web interface for all operations: Add, View, Borrow, and Return books.
- Manage authors and borrowers.
- Generate weekly reports.


## Database Schema
The database consists of the following tables:

### Authors
| Column   | Type         | Description                   |
|----------|--------------|-------------------------------|
| id       | VARCHAR(255) | Unique author ID (Primary Key)|
| name     | VARCHAR(255) | Author's name                |
| country  | VARCHAR(100) | Author's country             |

### Books
| Column       | Type         | Description                          |
|--------------|--------------|--------------------------------------|
| id           | VARCHAR(255) | Unique book ID (Primary Key)        |
| title        | VARCHAR(255) | Book title                          |
| author_id    | VARCHAR(255) | Foreign Key linking to `Authors`    |
| genre        | VARCHAR(100) | Book genre                          |
| availability | CHAR(1)      | Availability ('t' = true, 'f' = false)|

### Borrowers
| Column   | Type         | Description                   |
|----------|--------------|-------------------------------|
| id       | VARCHAR(255) | Unique borrower ID (Primary Key)|
| name     | VARCHAR(255) | Borrower's name              |
| contact  | VARCHAR(100) | Borrower's contact details   |

### Borrowed_Books
| Column       | Type         | Description                          |
|--------------|--------------|--------------------------------------|
| id           | SERIAL       | Unique ID for the borrowed record   |
| book_id      | VARCHAR(255) | Foreign Key linking to `Books`      |
| borrower_id  | VARCHAR(255) | Foreign Key linking to `Borrowers`  |
| borrow_date  | DATE         | Date when the book was borrowed     |
| return_date  | DATE         | Due/returned date                   |

## Contact
For questions or feedback, feel free to reach out to:
- **Your Name**: khushich9085@gmail.com
- **GitHub**: (https://github.com/Khushi-Choudhary11)
