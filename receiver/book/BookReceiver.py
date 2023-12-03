from receiver.JSONReceiver import JSONReceiver
from receiver.MessageHandlingStrategy import MessageHandlingStrategy
from receiver.MessageValidation import extract_book_data, catch_data_parsing_errors
from receiver.book.Book import commit_raw_book


class CommitRawBook(MessageHandlingStrategy):
    async def on_message(self, data: dict) -> None:
        await commit_raw_book(**catch_data_parsing_errors(data, extract_book_data))


if __name__ == "__main__":
    JSONReceiver(CommitRawBook()).start()
