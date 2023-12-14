from sqlalchemy.orm import Mapped, mapped_column

from temporarily_shared_files.sql_alchemy.models.DBBase import Base


class BookModel(Base):
    __tablename__ = "book"
    book_id: Mapped[str] = mapped_column(primary_key=True)
    book_name: Mapped[str]

    def __repr__(self) -> str:
        return f"BookModel(id={self.book_id!r}, name={self.book_name!r})"