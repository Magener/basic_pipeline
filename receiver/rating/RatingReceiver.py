from receiver.receiver.JSONReceiver import JSONReceiver
from receiver.receiver.MessageHandlingStrategy import MessageHandlingStrategy
from temporarily_shared_files.sql_alchemy.models.RatingModel import extract_rating_data
from temporarily_shared_files.sql_alchemy.repositories.RatingRepository import commit_review


class CommitReview(MessageHandlingStrategy):
    async def on_message(self, data: dict) -> None:
        await commit_review(extract_rating_data(data).apply_transformation())


if __name__ == "__main__":
    JSONReceiver(CommitReview()).start()
