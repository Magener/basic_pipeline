from temporarily_shared_files.sql_alchemy.CommandParser import CommandParser
from temporarily_shared_files.sql_alchemy.repositories.BookRepository import clear_processed_books, commit_raw_book, \
    organize_book_data
from temporarily_shared_files.sql_alchemy.repositories.RatingRepository import commit_review, find_top_rated_books


class DBEndpoint:
    __command_parser = None

    @classmethod
    def get_command_parser(cls) -> CommandParser:
        if cls.__command_parser is None:
            cls.__command_parser = CommandParser()
            cls.__initialize_command_parser()

        return cls.__command_parser

    @classmethod
    def __initialize_command_parser(cls) -> None:
        cls.__command_parser.add_command("commit_raw_book", commit_raw_book)
        cls.__command_parser.add_command("organize_book_data", organize_book_data)
        cls.__command_parser.add_command("clear_processed_books", clear_processed_books)
        cls.__command_parser.add_command("commit_review", commit_review)
        cls.__command_parser.add_command("find_top_rated_books", find_top_rated_books)
