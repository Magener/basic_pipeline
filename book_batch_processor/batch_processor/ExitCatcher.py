import signal
import sys
from typing import Callable


class ExitCatcher:
    __handlers = []
    __has_initialized = False

    @classmethod
    def ensure_initialized(cls):
        if not cls.__has_initialized:
            cls.__has_initialized = True

            signal.signal(signal.SIGINT, cls.__signal_handler)

    @classmethod
    def add_handler(cls, handler: Callable) -> None:
        cls.__handlers.append(handler)

    @classmethod
    def __signal_handler(cls, sig, frame):
        for handler in cls.__handlers:
            handler()
        sys.exit(0)
