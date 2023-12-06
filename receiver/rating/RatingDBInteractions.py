from sqlalchemy import insert

from receiver.log import logger
from receiver.postgresql.AsyncPostgresConnection import AsyncPostgresConnection
from receiver.rating.Rating import Rating
from sql_alchemy.RatingModel import RatingModel


async def commit_review(rating: Rating) -> None:
    async with AsyncPostgresConnection.get_connection() as session:
        QUERY = insert(RatingModel).values(reviewer_id=rating.reviewer_id, book_id=rating.book_id, score=rating.score)

        await session.execute(QUERY)

        await session.commit()

        logger.info(f"Regstered {rating} in database.")
