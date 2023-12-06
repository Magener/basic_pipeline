from receiver.log import logger
from receiver.postgresql.AsyncPostgresConnection import AsyncPostgresConnection
from sql_alchemy.RatingModel import RatingModel


async def commit_review(rating: RatingModel) -> None:
    async with AsyncPostgresConnection.get_connection() as session:
        session.add(rating)

        await session.commit()

        logger.info(f"Regstered {rating} in database.")
