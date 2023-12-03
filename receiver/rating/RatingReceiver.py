from receiver.JSONReceiver import JSONReceiver
from receiver.MessageHandlingStrategy import MessageHandlingStrategy
from receiver.MessageValidation import extract_rating_data
from receiver.postgresql.Review import commit_review


class CommitReview(MessageHandlingStrategy):
    async def on_message(self, data: dict) -> None:
        await commit_review(*extract_rating_data(data))


if __name__ == "__main__":
    JSONReceiver(CommitReview()).start()
