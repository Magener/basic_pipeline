#TODO: should I move it to batch book processing?
    # contained within BookDBInteractions as well
from typing import Dict

from sqlalchemy.orm import Mapped, mapped_column

from sql_alchemy.DBBase import Base


class UnprocessedBookModel(Base):
    __tablename__ = "unprocessed_books"
    isbn: Mapped[str] = mapped_column(primary_key=True)
    book_title: Mapped[str]
    book_author: Mapped[str]
    year_of_publication: Mapped[int]
    publisher: Mapped[str]


def extract_book_data(book_data: Dict) -> UnprocessedBookModel:
    return UnprocessedBookModel(
        isbn=book_data["ISBN"],
        book_title=book_data["Book-Title"],
        book_author=book_data["Book-Author"],
        year_of_publication=int(book_data["Year-Of-Publication"]),
        publisher=book_data["Publisher"]
    )