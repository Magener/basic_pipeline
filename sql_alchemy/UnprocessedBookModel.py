#TODO: should I move it to batch book processing?
    # contained within BookDBInteractions as well
from sqlalchemy.orm import Mapped, mapped_column

from sql_alchemy.DBBase import Base


class UnprocessedBookModel(Base):
    __tablename__ = "unprocessed_books"
    isbn: Mapped[str] = mapped_column(primary_key=True)
    book_title: Mapped[str]
    book_author: Mapped[str]
    year_of_publication: Mapped[int]
    publisher: Mapped[str]
