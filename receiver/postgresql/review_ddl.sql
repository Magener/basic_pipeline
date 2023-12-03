CREATE SCHEMA IF NOT EXISTS hafifa;

CREATE TABLE IF NOT EXISTS hafifa.ratings (
    rating_id SERIAL PRIMARY KEY,
    reviewer_id INT,
    book_id VARCHAR(20),
    score INT
);