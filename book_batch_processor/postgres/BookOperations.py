from book_batch_processor.log import logger
from book_batch_processor.postgres.AsyncPostgresConnection import AsyncPostgresConnection


async def organize_book_data():
    connection = await AsyncPostgresConnection().get_connection()

    QUERY = """INSERT INTO hafifa.book (book_id, book_name) SELECT isbn as book_id, book_title as book_name FROM hafifa.unprocessed_books ON CONFLICT DO NOTHING;"""

    logger.debug("Queried unprocessed books")

    results = await connection.execute(QUERY)
    inserted_successfully = results.startswith("INSERT")

    if inserted_successfully:
        logger.info(f"Processed books successfully. {results}")
    else:
        raise RuntimeError(f"An error has occurred {results}")


async def clear_processed_books():
    connection = await AsyncPostgresConnection().get_connection()

    QUERY = "DELETE FROM hafifa.unprocessed_books;"

    results = await connection.execute(QUERY)

    deleted_successfully = results.startswith("DELETE")

    if deleted_successfully:
        logger.info(f"Cleared processed books successfully. {results}")
    else:
        raise RuntimeError(f"An error has occurred {results}")
