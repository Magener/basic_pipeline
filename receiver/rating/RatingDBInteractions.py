from sqlalchemy import insert
from sqlalchemy.orm import Mapped, mapped_column

from receiver.log import logger
from receiver.postgresql.AsyncPostgresConnection import AsyncPostgresConnection
from receiver.rating.Rating import Rating
from sql_alchemy.DBBase import Base


class RatingModel(Base):
    __tablename__ = "ratings"

    rating_id: Mapped[int] = mapped_column(primary_key=True, server_default='DEFAULT')
    reviewer_id: Mapped[int]
    book_id: Mapped[str]  # TODO: add relationship as necessary.
    score: Mapped[int]


async def commit_review(rating: Rating) -> None:
    async with AsyncPostgresConnection.get_connection() as session:
        QUERY = insert(RatingModel).values(reviewer_id=rating.reviewer_id, book_id=rating.book_id, score=rating.score)

        await session.execute(QUERY)

        await session.commit()

        logger.info(f"Regstered {rating} in database.")
