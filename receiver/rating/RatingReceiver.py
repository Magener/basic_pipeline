from receiver.receiver.JSONReceiver import JSONReceiver
from receiver.receiver.MessageHandlingStrategy import MessageHandlingStrategy
from temporarily_shared_files.sql_alchemy.models.RatingModel import extract_rating_data
from temporarily_shared_files.sql_alchemy.repositories.RatingRepository import commit_review


def apply_transformation(rating_data: dict) -> dict:
    rating_data["Book-Rating"] = int(rating_data["Book-Rating"]) / 2
    return rating_data


class CommitReview(MessageHandlingStrategy):
    async def on_message(self, rating_data: dict) -> None:
        await commit_review(extract_rating_data(apply_transformation(rating_data)))


if __name__ == "__main__":
    JSONReceiver(CommitReview()).start()
