from receiver.log import logger
from receiver.postgresql.AsyncPostgresConnection import AsyncPostgresConnection
from receiver.rating.Rating import Rating


async def commit_review(rating: Rating) -> None:
    async with await AsyncPostgresConnection.get_connection() as connection:
        QUERY = "INSERT INTO hafifa.ratings(reviewer_id, book_id, score) VALUES ($1, $2, $3);"

        result_message = await connection.execute(QUERY, rating.reviewer_id, rating.book_id, rating.score)

        insert_successful = result_message.startswith("INSERT")

        if insert_successful:
            logger.info(f"Regstered {rating} in database.")
        else:
            raise RuntimeError(f"Insertion has failed: {result_message}")
