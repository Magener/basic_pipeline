import asyncio
from typing import Callable

from book_batch_processor.batch_processor.ExitCatcher import ExitCatcher
from book_batch_processor.batch_processor.MessageHandling import error_handling_async_wrapper
from book_batch_processor.consts import PROCESSING_INTERVAL
from book_batch_processor.log import logger
from temporarily_shared_files.sql_alchemy.DBEndpoint import DBEndpoint


async def periodically_execute_callback(callback: Callable) -> None:
    while True:
        try:
            asyncio.create_task(callback())
            await asyncio.sleep(PROCESSING_INTERVAL)
        except BaseException as e:
            logger.error(f"An error has occurred! {e}")


async def process_book_data():
    await DBEndpoint.get_command_parser().parse_command({"name": "organize_book_data"})
    await DBEndpoint.get_command_parser().parse_command({"name": "organize_book_data"})


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    ExitCatcher.ensure_initialized()

    task = loop.create_task(error_handling_async_wrapper(periodically_execute_callback(process_book_data)))
    ExitCatcher.add_handler(task.cancel)

    try:
        loop.run_until_complete(task)
    except asyncio.CancelledError:
        pass
