CREATE TABLE hafifa.unprocessed_books (
    isbn VARCHAR(20) PRIMARY KEY,
    book_title VARCHAR(255),
    book_author VARCHAR(255),
    year_of_publication INTEGER,
    publisher VARCHAR(255)
);

CREATE TABLE hafifa.book (
    book_id SERIAL PRIMARY KEY,
    book_name VARCHAR(255)
);