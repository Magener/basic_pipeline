import asyncio
from typing import Callable

from book_batch_processor.ExitCatcher import ExitCatcher
from book_batch_processor.consts import PROCESSING_INTERVAL
from book_batch_processor.postgres.BookOperations import organize_book_data, clear_processed_books


async def periodically_execute_callback(callback: Callable) -> None:
    while True:
        await callback()
        await asyncio.sleep(PROCESSING_INTERVAL)


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
