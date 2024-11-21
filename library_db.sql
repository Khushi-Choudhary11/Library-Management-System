--Database tables setup

CREATE TABLE Authors (
    id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    country VARCHAR(100)
);


CREATE TABLE Books (
    id VARCHAR(255) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id VARCHAR(255) REFERENCES Authors (id),
    genre VARCHAR(100),
    availability BOOLEAN DEFAULT TRUE
);


CREATE TABLE Borrowers (
    id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact VARCHAR(50)
);


CREATE TABLE Borrowed_Books (
    id SERIAL PRIMARY KEY,
    book_id VARCHAR(255) REFERENCES Books (id),
    borrower_id VARCHAR(255) REFERENCES Borrowers (id),
    borrow_date DATE NOT NULL,
    return_date DATE
);



CREATE OR REPLACE FUNCTION update_book_availability()
RETURNS TRIGGER AS $$
BEGIN
    IF (TG_OP = 'INSERT') THEN
        UPDATE Books
        SET availability = FALSE
        WHERE id = NEW.book_id;

    ELSIF (TG_OP = 'UPDATE') THEN
        IF (NEW.return_date IS NOT NULL) THEN
            UPDATE Books
            SET availability = TRUE
            WHERE id = NEW.book_id;
        END IF;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER book_borrowed_or_returned
AFTER INSERT OR UPDATE ON Borrowed_Books
FOR EACH ROW
EXECUTE FUNCTION update_book_availability();

