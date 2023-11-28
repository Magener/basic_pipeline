from typing import Tuple


def validate_message(msg) -> None:
    if msg.error():
        raise RuntimeError(msg.error())


def extract_rating_data(rating_data) -> Tuple[int, str, int]:
    try:
        return int(rating_data["User-ID"]), rating_data["ISBN"], int(rating_data["Book-Rating"])
    except KeyError as e:
        raise TypeError(f"Required key was not supplied! {rating_data} {e}")
    except ValueError as e:
        raise ValueError(f"Value provided was not parsable! {rating_data} {e}")