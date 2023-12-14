from temporarily_shared_files.sql_alchemy.DBEndpoint import DBEndpoint
from transformers.receiver.JSONReceiver import JSONReceiver
from transformers.receiver.MessageHandlingStrategy import MessageHandlingStrategy


def apply_transformation(rating_data: dict) -> dict:
    rating_data["Book-Rating"] = int(rating_data["Book-Rating"]) / 2
    return rating_data


class CommitReview(MessageHandlingStrategy):
    async def on_message(self, rating_data: dict) -> None:
        await DBEndpoint.get_command_parser().parse_command(
            {"name": "commit_review", "args": {"rating_data": apply_transformation(rating_data)}})


if __name__ == "__main__":
    JSONReceiver(CommitReview()).start()
