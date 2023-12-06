from sqlalchemy import insert

from receiver.book.Book import Book
from receiver.log import logger
from receiver.postgresql.AsyncPostgresConnection import AsyncPostgresConnection
from sql_alchemy.UnprocessedBook import UnprocessedBook


async def commit_raw_book(book: Book):
    async with AsyncPostgresConnection.get_connection() as session:
        QUERY = insert(UnprocessedBook).values((book.id, book.book_title, book.book_author,
                                                book.year_of_publication, book.publisher))

        await session.execute(QUERY)
        await session.commit()

        logger.debug(f"Regstered {book} in database.")
