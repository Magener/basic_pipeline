from receiver.receiver.JSONReceiver import JSONReceiver
from receiver.receiver.MessageHandlingStrategy import MessageHandlingStrategy
from sql_alchemy.RatingModel import extract_rating_data
from receiver.rating.RatingDBInteractions import commit_review


class CommitReview(MessageHandlingStrategy):
    async def on_message(self, data: dict) -> None:
        await commit_review(extract_rating_data(data).apply_transformation())


if __name__ == "__main__":
    JSONReceiver(CommitReview()).start()
