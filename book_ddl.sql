CREATE TABLE IF NOT EXISTS hafifa.unprocessed_books (
    isbn VARCHAR(20) PRIMARY KEY,
    book_title VARCHAR(255),
    book_author VARCHAR(255),
    year_of_publication INTEGER,
    publisher VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS hafifa.book (
    book_id VARCHAR(20) PRIMARY KEY,
    book_name VARCHAR(255)
);