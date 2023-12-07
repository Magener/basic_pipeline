from typing import Coroutine

from book_batch_processor.log import logger


async def error_handling_async_wrapper(task: Coroutine) -> None:
    try:
        await task
    except BaseException as e:
        logger.error(f"An error has occurred! {e}")