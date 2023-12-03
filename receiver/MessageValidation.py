from typing import Tuple


def validate_message(msg) -> None:
    if msg.error():
        raise RuntimeError(msg.error())


def extract_book_data(data) -> dict:
    return {
        "isbn": data["ISBN"],
        "book_title": data["Book-Title"],
        "book_author": data["Book-Author"],
        "year_of_publication": int(data["Year-Of-Publication"]),
        "publisher": data["Publisher"]
    }


def extract_rating_data(rating_data) -> Tuple[int, str, int]:
    return int(rating_data["User-ID"]), rating_data["ISBN"], int(rating_data["Book-Rating"])


def catch_data_parsing_errors(data, extraction_method) -> dict:
    try:
        return extraction_method(data)
    except KeyError as e:
        raise TypeError(f"Required key was not supplied! {data} {e}")
    except ValueError as e:
        raise ValueError(f"Value provided was not parsable! {data} {e}")
