import asyncio
from typing import Callable

from book_batch_processor.consts import PROCESSING_INTERVAL
from book_batch_processor.ExitCatcher import ExitCatcher
from book_batch_processor.log import logger
from book_batch_processor.postgres.BookOperations import clear_processed_books, organize_book_data


async def periodically_execute_callback(callback: Callable) -> None:
    while True:
        try:
            await callback()
            await asyncio.sleep(PROCESSING_INTERVAL)
        except BaseException as e:
            logger.error(f"An error has occurred! {e}")


async def process_book_data():
    await organize_book_data()
    await clear_processed_books()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    ExitCatcher.ensure_initialized()

    task = loop.create_task(periodically_execute_callback(process_book_data))
    ExitCatcher.add_handler(task.cancel)

    try:
        loop.run_until_complete(task)
    except asyncio.CancelledError:
        pass
