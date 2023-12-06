from __future__ import annotations

from typing import Dict

from sqlalchemy.orm import Mapped, mapped_column, relationship

from sql_alchemy.BookModel import BookModel
from sql_alchemy.DBBase import Base


class RatingModel(Base):
    __tablename__ = "ratings"
    rating_id: Mapped[int] = mapped_column(primary_key=True, server_default='DEFAULT')
    reviewer_id: Mapped[int]
    score: Mapped[int]
    book_id: Mapped[str]

    book = relationship("BookModel", foreign_keys=[BookModel.book_id], primaryjoin='BookModel.book_id == RatingModel.book_id')

    def apply_transformation(self) -> RatingModel:
        self.score /= 2
        return self


def extract_rating_data(rating_data: Dict) -> RatingModel:
    return RatingModel(
        reviewer_id=int(rating_data["User-ID"]),
        book_id=rating_data["ISBN"],
        score=int(rating_data["Book-Rating"]))
