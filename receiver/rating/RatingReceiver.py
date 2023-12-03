from receiver.JSONReceiver import JSONReceiver
from receiver.MessageHandlingStrategy import MessageHandlingStrategy
from receiver.MessageValidation import extract_rating_data, catch_data_parsing_errors
from receiver.rating.Review import commit_review


class CommitReview(MessageHandlingStrategy):
    async def on_message(self, data: dict) -> None:
        await commit_review(*catch_data_parsing_errors(data, extract_rating_data))


if __name__ == "__main__":
    JSONReceiver(CommitReview()).start()
