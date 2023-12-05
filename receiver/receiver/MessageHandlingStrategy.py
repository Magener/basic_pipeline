from abc import ABC, abstractmethod
from typing import Coroutine

from receiver.log import logger


class MessageHandlingStrategy(ABC):
    @abstractmethod
    async def on_message(self, data: dict) -> None:
        pass


async def error_handling_async_wrapper(task: Coroutine) -> None:
    try:
        await task
    except BaseException as e:
        logger.error(f"An error has occurred! {e}")
