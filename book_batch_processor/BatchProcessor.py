import asyncio

from book_batch_processor.postgres.BookOperations import read_unprocessed_books, clear_processed_books


async def main():
    result = await read_unprocessed_books()
    print(result)
    await clear_processed_books()


if __name__ == '__main__':
    asyncio.run(main())
