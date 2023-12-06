from sqlalchemy.orm import Mapped, mapped_column

from sql_alchemy.DBBase import Base


class BookModel(Base):
    __tablename__ = "book"
    book_id: Mapped[str] = mapped_column(primary_key=True)
    book_name: Mapped[str]

    def __repr__(self) -> str:
        return f"BookModel(id={self.book_id!r}, name={self.book_name!r})"