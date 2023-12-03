from typing import Protocol


class MessageHandlingStrategy(Protocol):
    async def on_message(self, data: dict) -> None:
        pass
