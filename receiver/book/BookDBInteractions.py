from receiver.log import logger
from receiver.postgresql.AsyncPostgresConnection import AsyncPostgresConnection
from sql_alchemy.UnprocessedBookModel import UnprocessedBookModel


async def commit_raw_book(book: UnprocessedBookModel):
    async with AsyncPostgresConnection.get_connection() as session:
        session.add(book)

        await session.commit()

        logger.debug(f"Regstered {book} in database.")
