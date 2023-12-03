from typing import Dict


def validate_message(msg) -> None:
    if msg.error():
        raise RuntimeError(msg.error())


def extract_rating_data(rating_data) -> Dict:
    try:
        result = {
            "reviewer_id": int(rating_data["User-ID"]),
            "book_id": rating_data["ISBN"],
            "score": int(rating_data["Book-Rating"])

        }

        return result
    except KeyError as e:
        raise TypeError(f"Required key was not supplied! {rating_data} {e}")
    except ValueError as e:
        raise ValueError(f"Value provided was not parsable! {rating_data} {e}")
