from temporarily_shared_files.sql_alchemy.repositories.BookRepository import commit_raw_book
from transformers.receiver.JSONReceiver import JSONReceiver
from transformers.receiver.MessageHandlingStrategy import MessageHandlingStrategy
from temporarily_shared_files.sql_alchemy.models.UnprocessedBookModel import extract_book_data


class CommitRawBook(MessageHandlingStrategy):
    async def on_message(self, data: dict) -> None:
        await commit_raw_book(extract_book_data(data))


if __name__ == "__main__":
    JSONReceiver(CommitRawBook()).start()
