from sqlalchemy import delete, select
from sqlalchemy.dialects.postgresql import insert

from book_batch_processor.log import logger
from book_batch_processor.postgres.AsyncPostgresConnection import AsyncPostgresConnection
from sql_alchemy.Book import Book
from sql_alchemy.UnprocessedBook import UnprocessedBook


async def organize_book_data():
    async with AsyncPostgresConnection.get_connection() as session:
        UNPROCESSED_BOOK_SELECTION = select(
            UnprocessedBook.isbn.label('book_id'),
            UnprocessedBook.book_title.label('book_name'))

        QUERY = insert(Book).from_select(
            ['book_id', 'book_name'],
            UNPROCESSED_BOOK_SELECTION
        ).on_conflict_do_nothing()

        await session.execute(QUERY)

        logger.info(f"Processed books successfully.")

        await session.commit()


async def clear_processed_books():
    async with AsyncPostgresConnection.get_connection() as session:
        QUERY = delete(UnprocessedBook)
        await session.execute(QUERY)

        logger.info(f"Cleared processed books successfully.")
        await session.commit()
