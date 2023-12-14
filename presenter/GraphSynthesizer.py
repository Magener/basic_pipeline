def compute_book_name_column(book_dataframe):
    return book_dataframe.apply(
        lambda row: row["book_name"] if row["book_name"] else row["book_id"]
        , axis=1)
