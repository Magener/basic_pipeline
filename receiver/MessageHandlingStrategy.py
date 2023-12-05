from abc import ABC, abstractmethod


class MessageHandlingStrategy(ABC):
    @abstractmethod
    async def on_message(self, data: dict) -> None:
        pass
