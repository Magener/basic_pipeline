from receiver.JSONReceiver import JSONReceiver
from receiver.MessageHandlingStrategy import MessageHandlingStrategy
from receiver.Rating import extract_rating_data
from receiver.rating.Review import commit_review


class CommitReview(MessageHandlingStrategy):
    async def on_message(self, data: dict) -> None:
        await commit_review(extract_rating_data(data).apply_transformation())


if __name__ == "__main__":
    JSONReceiver(CommitReview()).start()
