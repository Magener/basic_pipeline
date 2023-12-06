from sqlalchemy.orm import Mapped, mapped_column, relationship

from sql_alchemy.DBBase import Base
from sql_alchemy.Book import Book


class Rating(Base):
    __tablename__ = "ratings"
    rating_id: Mapped[int] = mapped_column(primary_key=True)
    reviewer_id: Mapped[int]
    score: Mapped[int]
    book_id: Mapped[int]
    book: Mapped[Book] = relationship("Book", foreign_keys=[Book.book_id], primaryjoin='Book.book_id == Rating.book_id')