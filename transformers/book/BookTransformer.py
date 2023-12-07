from temporarily_shared_files.sql_alchemy.DBEndpoint import DBEndpoint
from transformers.receiver.JSONReceiver import JSONReceiver
from transformers.receiver.MessageHandlingStrategy import MessageHandlingStrategy


class CommitRawBook(MessageHandlingStrategy):
    async def on_message(self, data: dict) -> None:
        await DBEndpoint.get_command_parser().parse_command(
            {"name": "commit_raw_book", "args": {"book_data": data}})


if __name__ == "__main__":
    JSONReceiver(CommitRawBook()).start()
