from sqlalchemy.orm import Mapped, mapped_column, relationship

from sql_alchemy.DBBase import Base
from sql_alchemy.BookModel import BookModel


class RatingModel(Base):
    __tablename__ = "ratings"
    rating_id: Mapped[int] = mapped_column(primary_key=True, server_default='DEFAULT')
    reviewer_id: Mapped[int]
    score: Mapped[int]
    book_id: Mapped[str]
    book: Mapped[BookModel] = relationship("Book", foreign_keys=[BookModel.book_id], primaryjoin='Book.book_id == Rating.book_id')