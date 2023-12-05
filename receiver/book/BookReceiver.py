from receiver.book.Book import extract_book_data
from receiver.book.BookDBInteractions import commit_raw_book
from receiver.receiver.JSONReceiver import JSONReceiver
from receiver.receiver.MessageHandlingStrategy import MessageHandlingStrategy


class CommitRawBook(MessageHandlingStrategy):
    async def on_message(self, data: dict) -> None:
        await commit_raw_book(extract_book_data(data))


if __name__ == "__main__":
    JSONReceiver(CommitRawBook()).start()
