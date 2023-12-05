from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class Rating:
    reviewer_id: int
    book_id: str
    score: int

    def apply_transformation(self) -> Rating:
        self.score /= 2
        return self


def extract_rating_data(rating_data: Dict) -> Rating:
    return Rating(
        reviewer_id=int(rating_data["User-ID"]),
        book_id=rating_data["ISBN"],
        score=int(rating_data["Book-Rating"])

    )
