from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class Book:
    id: str
    book_title: str
    book_author: str
    year_of_publication: int
    publisher: str


def extract_book_data(book_data: Dict) -> Book:
    return Book(
        id=book_data["ISBN"],
        book_title=book_data["Book-Title"],
        book_author=book_data["Book-Author"],
        year_of_publication=int(book_data["Year-Of-Publication"]),
        publisher=book_data["Publisher"]
    )
