from sqlalchemy import delete, select
from sqlalchemy.dialects.postgresql import insert

from book_batch_processor.log import logger
from book_batch_processor.postgres.AsyncPostgresConnection import AsyncPostgresConnection
from sql_alchemy.BookModel import BookModel
from sql_alchemy.UnprocessedBookModel import UnprocessedBookModel


async def organize_book_data():
    async with AsyncPostgresConnection.get_connection() as session:
        UNPROCESSED_BOOK_SELECTION = select(
            UnprocessedBookModel.isbn.label('book_id'),
            UnprocessedBookModel.book_title.label('book_name'))

        QUERY = insert(BookModel).from_select(
            ['book_id', 'book_name'],
            UNPROCESSED_BOOK_SELECTION
        ).on_conflict_do_nothing()

        await session.execute(QUERY)

        await session.commit()

        logger.info(f"Processed books successfully.")


async def clear_processed_books():
    async with AsyncPostgresConnection.get_connection() as session:
        QUERY = delete(UnprocessedBookModel)

        await session.execute(QUERY)

        await session.commit()

        logger.info(f"Cleared processed books successfully.")
