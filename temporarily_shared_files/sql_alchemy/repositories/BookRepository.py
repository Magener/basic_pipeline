from sqlalchemy import delete, select
from sqlalchemy.dialects.postgresql import insert

from temporarily_shared_files.sql_alchemy.AsyncPostgresConnection import AsyncPostgresConnection
from temporarily_shared_files.sql_alchemy.log import logger
from temporarily_shared_files.sql_alchemy.models.BookModel import BookModel
from temporarily_shared_files.sql_alchemy.models.UnprocessedBookModel import extract_book_data, UnprocessedBookModel


async def commit_raw_book(book_data: dict):
    book = extract_book_data(book_data)
    async with AsyncPostgresConnection.get_connection() as session:
        session.add(book)

        await session.commit()

        logger.debug(f"Regstered {book} in database.")


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
