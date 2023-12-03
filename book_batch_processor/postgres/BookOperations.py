from book_batch_processor.postgres.AsyncPostgresConnection import AsyncPostgresConnection
from book_batch_processor.log import logger


async def read_unprocessed_books():
    connection = await AsyncPostgresConnection().get_connection()

    QUERY = "SELECT * FROM hafifa.unprocessed_books;"

    logger.debug("Queried unprocessed books")

    rows = await connection.fetch(QUERY)
    return [dict(row) for row in rows]


async def clear_processed_books():
    connection = await AsyncPostgresConnection().get_connection()

    QUERY = "DELETE FROM hafifa.unprocessed_books;"

    results = await connection.execute(QUERY)

    deleted_successfully = results.startswith("DELETE")

    if deleted_successfully:
        logger.debug(f"Cleared processed books successfully.")
    else:
        raise RuntimeError(f"An error has occurred {results}")