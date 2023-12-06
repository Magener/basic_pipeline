from typing import Dict, List

from sqlalchemy import desc, func, select, Subquery

from insight_api.postgres.AsyncPostgresConnection import AsyncPostgresConnection
from sql_alchemy.Book import Book
from sql_alchemy.Rating import Rating


async def find_top_rated_books(minimum_ratings: int, presented_amount: int = None) -> List[Dict]:
    async with AsyncPostgresConnection.get_connection() as session:
        AVERAGE_BOOK_RATINGS = await __average_book_ratings_subquery(minimum_ratings, presented_amount)

        query = select(
            Book.book_name,
            AVERAGE_BOOK_RATINGS.c.book_id,
            AVERAGE_BOOK_RATINGS.c.average,
        ).select_from(AVERAGE_BOOK_RATINGS.join(Book, AVERAGE_BOOK_RATINGS.c.book_id == Book.book_id, isouter=True))

        result = await session.execute(query)

        # TODO: extract method?
        return [{"book_name": row[0], "book_id": row[1], "avg_score": row[2]} for row in result.fetchall()]


async def __average_book_ratings_subquery(minimum_ratings: int, presented_amount: int = None) -> Subquery:
    AVERAGE_BOOK_RATINGS = select(Rating.book_id, func.avg(Rating.score).label('average')).group_by(
        Rating.book_id).order_by(
        desc("average")).having(func.count(Rating.score) > minimum_ratings)

    if presented_amount:
        AVERAGE_BOOK_RATINGS = AVERAGE_BOOK_RATINGS.limit(presented_amount)
    AVERAGE_BOOK_RATINGS = AVERAGE_BOOK_RATINGS.alias("score")

    return AVERAGE_BOOK_RATINGS
