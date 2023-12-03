from insight_api.postgres.AsyncPostgresConnection import AsyncPostgresConnection
from receiver.consts import RATING_TABLE_NAME
from receiver.log import logger


async def commit_review(reviewer_id, book_id, score):
    connection = await AsyncPostgresConnection().get_connection()
    QUERY = f"""INSERT INTO {RATING_TABLE_NAME}(reviewer_id, book_id, score) VALUES ($1, $2, $3);"""

    result_message = await connection.execute(QUERY, reviewer_id, book_id, score)

    insert_successful = result_message.startswith("INSERT")

    if insert_successful:
        logger.debug(f"Regstered {(reviewer_id, book_id, score)} in database.")
    else:
        raise RuntimeError(f"Insertion has failed: {result_message}")
