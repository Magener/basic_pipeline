from typing import Callable, Coroutine

from temporarily_shared_files.sql_alchemy.log import logger


class CommandParser:
    def __init__(self):
        self.__available_commands = {}

    def parse_command(self, command: dict) -> Coroutine:
        command_name, kwargs = command["name"], command.get("args", {})

        try:
            return self.__available_commands[command_name](**kwargs)
        except BaseException as e:
            logger.error(e)
            raise BaseException("Command failed. (Check out command name or args)")

    def add_command(self, command_name: str, command_callback: Callable) -> None:
        self.__available_commands[command_name] = command_callback