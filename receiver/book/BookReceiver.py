import asyncio

from receiver.book.Book import Book, extract_book_data
from receiver.book.BookDBInteractions import commit_raw_book
from receiver.rating.Rating import Rating
from receiver.rating.RatingDBInteractions import commit_review
from receiver.receiver.MessageHandlingStrategy import MessageHandlingStrategy


class CommitRawBook(MessageHandlingStrategy):
    async def on_message(self, data: dict) -> None:
        await commit_raw_book(extract_book_data(data))


if __name__ == "__main__":
    # JSONReceiver(CommitRawBook()).start()
    # TODO; replace with JSON Receiver.
    # TODO: test rating receiver here as well.
    example_review = Rating(
        reviewer_id=5,
        book_id="abc",
        score=4

    )

    asyncio.run(commit_review(example_review))
