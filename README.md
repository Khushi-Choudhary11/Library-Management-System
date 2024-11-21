# Library Management System(LMS)

## Project Description
The Library Management System is a Python- and PostgreSQL-based application designed to manage library resources efficiently. It provides features for managing books, authors, and borrowers, along with functionalities to handle book borrowing and returning processes. The system also includes reporting features such as generating weekly borrow statistics.

## Features
- Add, update, and delete books, authors, and borrowers.
- Borrow and return books, with automatic availability updates.
- View all available books and borrowed books.
- Generate a weekly report of borrowed books with borrower details.

## Setup and Run Instructions

### Prerequisites
1. Install **Python 3.7+** on your system.
2. Install **PostgreSQL** (I have used PgAdmin 4 and PostgreSQL 14) database and ensure it is running.
3. Install **Git** to clone the repository.

## You are provided with 2 .py files 
- lib.py : This basically contains all the necesssary functions that can be directly used to CRUD tables and related data.
- library.py : In this file, I have used Flask frame work to create LMS web app.


## Dependencies
The project dependencies are listed in the `requirements.txt` file. (Note: requirements.txt not only contains requirements for this project but also some others too so You can skip those). Install them using:
```bash
pip install -r requirements.txt
```

### Key Dependencies
- `Flask`: For building the web application.
- `psycopg2`: For connecting to the PostgreSQL database.

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
- **GitHub**: [Khushi-Choudhary11](https://github.com/your-username)
