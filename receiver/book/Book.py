from receiver.log import logger
from receiver.postgresql.AsyncPostgresConnection import AsyncPostgresConnection


async def commit_raw_book(isbn, book_title, book_author, year_of_publication, publisher):
    connection = await AsyncPostgresConnection().get_connection()

    QUERY = "INSERT INTO hafifa.unprocessed_books" \
            "(isbn, book_title, book_author, year_of_publication, publisher)" \
            " VALUES ($1, $2, $3, $4, $5);"

    result_message = await connection.execute(QUERY, isbn, book_title, book_author, year_of_publication, publisher)

    insert_successful = result_message.startswith("INSERT")

    if insert_successful:
        logger.debug(f"Regstered {(isbn, book_title, book_author, year_of_publication, publisher)} in database.")
    else:
        raise RuntimeError(f"Insertion has failed: {result_message}")
