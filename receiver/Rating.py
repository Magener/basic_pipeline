from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Rating:
    reviewer_id: int
    book_id: str
    score: int

    def apply_transformation(self) -> Rating:
        self.score /= 2
        return self
