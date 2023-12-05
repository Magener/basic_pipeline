from receiver.Book import extract_book_data
from receiver.book.Book import commit_raw_book
from receiver.JSONReceiver import JSONReceiver
from receiver.MessageHandlingStrategy import MessageHandlingStrategy


class CommitRawBook(MessageHandlingStrategy):
    async def on_message(self, data: dict) -> None:
        await commit_raw_book(extract_book_data(data))


if __name__ == "__main__":
    JSONReceiver(CommitRawBook()).start()
