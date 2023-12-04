from insight_api.postgres.AsyncPostgresConnection import AsyncPostgresConnection
from receiver.Rating import Rating
from receiver.log import logger


async def commit_review(rating: Rating) -> None:
    connection = await AsyncPostgresConnection().get_connection()
    QUERY = "INSERT INTO hafifa.ratings(reviewer_id, book_id, score) VALUES ($1, $2, $3);"

    result_message = await connection.execute(QUERY, rating.reviewer_id, rating.book_id, rating.score)

    insert_successful = result_message.startswith("INSERT")

    if insert_successful:
        logger.info(f"Regstered {rating} in database.")
    else:
        raise RuntimeError(f"Insertion has failed: {result_message}")
