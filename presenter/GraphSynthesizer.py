def get_book_identifier(row) -> str:
    if row["book_name"]:
        return row["book_name"]
    return row["book_id"]


def compute_presented_name(book_dataframe):
    return book_dataframe.apply(get_book_identifier, axis=1)
